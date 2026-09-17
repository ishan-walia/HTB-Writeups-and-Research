<div align="center">

# 🛡️ HTB Writeups, Research & Security Engineering

### 🚀 An Advanced Cybersecurity Knowledge Base | CTF Solutions | DFIR Sherlocks | Python Security Suite | Red Team Automation

<p align="center">
  <a href="https://github.com/ishan-walia/HTB-Writeups-and-Research/stargazers"><img src="https://img.shields.io/github/stars/ishan-walia/HTB-Writeups-and-Research?color=brightgreen&logo=star&style=for-the-badge" alt="Stars"></a>
  <a href="https://github.com/ishan-walia/HTB-Writeups-and-Research/network/members"><img src="https://img.shields.io/github/forks/ishan-walia/HTB-Writeups-and-Research?color=orange&logo=git-pull-request&style=for-the-badge" alt="Forks"></a>
  <a href="https://github.com/ishan-walia/HTB-Writeups-and-Research/commits/main"><img src="https://img.shields.io/github/last-commit/ishan-walia/HTB-Writeups-and-Research?color=blue&logo=git&style=for-the-badge" alt="Last Commit"></a>
  <a href="https://github.com/ishan-walia/HTB-Writeups-and-Research"><img src="https://img.shields.io/github/repo-size/ishan-walia/HTB-Writeups-and-Research?color=purple&logo=files&style=for-the-badge" alt="Repo Size"></a>
  <a href="#-disclaimer"><img src="https://img.shields.io/badge/License-Educational%20Only-red.svg?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Hack%20The%20Box-111927?style=flat-square&logo=hackthebox&logoColor=9FEF00" alt="Hack The Box"/>
  <img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=flat-square&logo=kalilinux&logoColor=white" alt="Kali Linux"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white" alt="Bash"/>
  <img src="https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white" alt="Wireshark"/>
  <img src="https://img.shields.io/badge/Metasploit-000000?style=flat-square&logo=rapid7&logoColor=white" alt="Metasploit"/>
  <img src="https://img.shields.io/badge/Active%20Directory-0078D4?style=flat-square&logo=windows&logoColor=white" alt="Active Directory"/>
  <img src="https://img.shields.io/badge/Incident%20Response-DFIR-critical?style=flat-square" alt="DFIR"/>
</p>

---

**Crafted with dedication by [Ishan Walia](https://github.com/ishan-walia)**  
*Documenting practical offensive security, digital forensics, reverse engineering, and custom automation tools.*

</div>

---

## 📑 Table of Contents

- [Executive Overview](#-executive-overview)
- [Repository Architecture](#-repository-architecture)
- [Module Breakdown](#-module-breakdown)
  - [1. Python Security Suite](#1--python-security-suite)
  - [2. Labs: Challenges & Sherlocks](#2--labs-challenges--sherlocks)
  - [3. Scripts & Automation](#3--scripts--automation)
  - [4. Write-ups & Research](#4--write-ups--research)
- [Tech Stack & Security Toolkit](#-tech-stack--security-toolkit)
- [Methodology & Mindset](#-methodology--mindset)
- [Disclaimer](#-disclaimer)
- [Connect & Collaborate](#-connect--collaborate)

---

## 🧭 Executive Overview

Welcome to my central cybersecurity hub. This repository serves as an evolving, hands-on archive of technical knowledge across multiple domains of cybersecurity:

* **Offensive Security & Red Teaming:** Step-by-step penetration testing methodology, CTF challenge breakdowns, exploit development, and Active Directory exploration.
* **Defensive Security & DFIR (Sherlocks):** Memory dump analysis, log forensics, pcap inspection, threat hunting, and root-cause determination.
* **Custom Security Tooling:** In-depth Python scripts, automation engines, malware analysis helpers, and network reconnaissance tools built from scratch or using industry-standard libraries.

---

## 🗂️ Repository Architecture

```text
HTB-Writeups-and-Research/
│
├── 📂 Python/                      # Modular Python Security Suite
│   ├── 🌐 Networking-Recon/        # Scapy, Nmap, Shodan, Censys, Socket, Pyshark
│   ├── 🕸️ Web-Security/           # Requests, BeautifulSoup, HTTPX, Selenium, Flask
│   ├── 🔬 File-Malware-Analysis/   # Capstone, Unicorn, LIEF, PEfile, Yara, Magic
│   ├── 🔐 Cryptography-Data/       # Cryptography, Hashlib, HMAC, Secrets, Base64
│   ├── ⚙️ System-Automation/       # OS internals, Subprocess, Psutil, Click, Rich
│   └── ⚔️ Advanced-Security/       # Impacket, Paramiko, Pwntools, Mitmproxy, Pandas
│
├── 📂 Labs /                       # Hands-on CTFs and Defensive Operations
│   ├── 🎯 Challenges/              # Web, Crypto, Reverse, Misc CTF Challenges
│   └── 🔍 Sherlocks/               # Real-world Incident Response & DFIR Cases
│
├── 📂 Scripts/                     # Custom Standalone Scripts & Utilities
│   ├── 📡 WIFI/                    # Windows Wi-Fi password extraction
│   ├── 💥 AllWindows-DDoS/         # Network stress & triage testing
│   └── 🖥️ Windows/                 # OS automation & file organizers
│
├── 📂 Write-Ups/                   # Comprehensive HTB Machine & Challenge Reports
│   └── 🎲 Lucky Dice/              # Detailed vulnerability analysis & exploitation
│
├── 📂 Research/                    # Vulnerability deep-dives, cheatsheets & notes
└── 📂 Tools/                       # Standalone pentest helper utilities
```

---

## 🔍 Module Breakdown

### 1. 🐍 Python Security Suite

A structured, library-by-library breakdown designed to build weaponized tools, automation pipelines, and forensic scripts.

| Domain | Included Libraries & Modules | Focus & Use-Cases |
| :--- | :--- | :--- |
| **🌐 Networking & Recon** | `scapy`, `python-nmap`, `shodan`, `censys`, `netaddr`, `dnspython`, `socket`, `pyshark`, `python-whois` | Packet sniffing, protocol manipulation, port scanning, OSINT aggregation, DNS queries |
| **🕸️ Web Security** | `requests`, `BeautifulSoup`, `lxml`, `httpx`, `aiohttp`, `websocket-client`, `selenium`, `flask` | HTTP fuzzing, form extraction, asynchronous web crawlers, headless browser exploitation, mock honeypots |
| **🔬 Malware & Binaries** | `capstone`, `unicorn`, `lief`, `python-magic`, `pefile`, `yara-python`, `zipfile` | Disassembly, binary emulation, PE header parsing, file signatures, YARA rule detection |
| **🔐 Cryptography & Data** | `cryptography`, `hashlib`, `hmac`, `secrets`, `base64`, `binascii`, `struct` | Cipher decryption, hashing algorithms, token generation, binary data packing/unpacking |
| **⚙️ System & Automation** | `os`, `psutil`, `subprocess`, `click`, `rich`, `colorama` | Process inspection, privilege triage, CLI tools, formatted logging, terminal UI |
| **⚔️ Advanced Security** | `impacket`, `paramiko`, `pwntools`, `mitmproxy`, `pandas` | Active Directory attacks (Kerberos/SMB), SSH automation, binary exploitation/ROP, proxy interception |

---

### 2. 🧪 Labs: Challenges & Sherlocks

Hands-on exercises from **Hack The Box** and industry CTF platforms covering both Red and Blue operations.

#### 🔍 DFIR & Incident Response (Sherlocks)
Deep forensic investigations solving real-world attack scenarios:
- **Unit42** – Advanced persistent threat (APT) forensic analysis.
- **Reaper** – Incident timeline reconstruction and adversary tracing.
- **ShadowBait** – Deception technology and credential harvesting analysis.
- **CAMouflage** – Endpoint tampering and persistence mechanism detection.
- **BFT ($MFT)** – Windows Master File Table NTFS forensic triage.
- **Fruitzy** – Web application compromise and lateral movement investigation.

#### 🎯 CTF Challenges
- **Spookifier** – Template injection / Web exploitation challenge.
- **ReactOOPS** – Client-side and server-side state security bugs.
- **Lucky Dice** – PRNG exploitation and logic vulnerabilities.
- **OpenSecret** – Cryptographic key leakage and authentication bypass.
- **Ether Tag** – Blockchain and token manipulation challenge.
- **Espresso & Primed for Action** – Reverse engineering and binary logic analysis.

---

### 3. ⚡ Scripts & Automation

Quick execution scripts crafted for post-exploitation, triage, and administrative efficiency:

* 📡 **Wi-Fi Credential Harvester:** Python script that queries stored WLAN profiles and decrypts stored cleartext keys on Windows hosts.
* 💥 **Stress & DDoS Simulation:** Educational network stress-testing tools to measure firewall throughput and connection handling.
* 📂 **Downloads & System Organizer:** Autonomous script utilizing file system events to catalog files based on extensions and hashes.

---

## 🛠️ Tech Stack & Security Toolkit

<div align="center">

| Area | Tools & Technologies |
| :--- | :--- |
| **Operating Systems** | Kali Linux, Windows 10/11 Enterprise, Parrot Security OS |
| **Network & Packet Analysis** | Wireshark, Tshark, Scapy, TCPdump, Nmap, Masscan |
| **Web Pentesting** | Burp Suite Professional, OWASP ZAP, Postman, SQLmap, Gobuster, Ffuf |
| **Binary & Reverse Engineering** | Ghidra, GDB-PEDA/GEF, Radare2, Capstone, Pwntools |
| **Active Directory & Post-Ex** | Impacket, BloodHound, CrackMapExec, Evil-WinRM, Mimikatz |
| **DFIR & Forensics** | Volatility 3, Autopsy, Eric Zimmerman's Tools, FTK Imager, KAPE |
| **Programming & Scripting** | Python 3, Bash, PowerShell, JavaScript, C/C++ |

</div>

---

## 🧠 Methodology & Mindset

Every machine write-up and research paper in this repo adheres to the standard penetration testing lifecycle:

```mermaid
flowchart LR
    A[🔍 Reconnaissance] --> B[🔎 Enumeration & Scanning]
    B --> C[💥 Vulnerability Assessment]
    C --> D[🎯 Initial Exploitation]
    D --> E[🛡️ Privilege Escalation]
    E --> F[📝 Remediation & Reporting]
```

1. **Information Gathering:** Passive & active OSINT without alerting the target.
2. **Surface Enumeration:** Fingerprinting services, versions, and hidden endpoints.
3. **Exploit Execution:** Crafting deterministic and clean exploits (avoiding system instability).
4. **Privilege Escalation:** Exploiting misconfigurations, kernel bugs, sudo privileges, or active directory paths.
5. **Post-Mortem Documentation:** Documenting root causes, CVSS vectors, and defensive mitigation steps.

---

## ⚠️ Disclaimer

> [!CAUTION]
> **For Educational and Ethical Testing Purposes Only.**
> 
> The contents, writeups, scripts, and code provided in this repository are strictly intended for **educational purposes, defensive research, and authorized penetration testing**. All writeups of Hack The Box machines/challenges adhere to HTB's Terms of Service and Responsible Disclosure guidelines.
>
> The author does **not** take responsibility for any unauthorized misuse, damage, or illegal actions caused by the code or methodologies contained herein. **Never test systems without explicit prior written authorization.**

---

## 🤝 Connect & Collaborate

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-ishan--walia-181717?style=for-the-badge&logo=github)](https://github.com/ishan-walia)
[![Hack The Box](https://img.shields.io/badge/HackTheBox-Profile-111927?style=for-the-badge&logo=hackthebox&logoColor=9FEF00)](https://app.hackthebox.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com)

⭐ **If you find this repository insightful, consider giving it a star!** ⭐

</div>
