# 🔴 TryHackMe (THM) Labs

<p align="center">
  <img src="https://img.shields.io/badge/Platform-TryHackMe-212C42?style=for-the-badge&logo=tryhackme&logoColor=FF4747" alt="THM Badge"/>
  <img src="https://img.shields.io/badge/Mode-Guided%20%26%20CTF-critical?style=for-the-badge" alt="Mode"/>
  <img src="https://img.shields.io/badge/Status-Actively%20Building-orange?style=for-the-badge" alt="Status"/>
</p>

---

## 📌 Directory Structure

```text
TryHackMe/
│
├── 📦 Rooms/               # Vulnerable machine rooms & topic-focused walk-throughs
│   ├── Easy/              # Fundamental concepts, basic privesc, simple CTFs
│   ├── Medium/            # Multi-vector attacks, AD fundamentals, custom web apps
│   └── Hard/              # Advanced exploitation, pivoting, complex misconfigurations
│
├── 🌐 Networks/            # Multi-machine realistic corporate network labs (e.g. Wreath, Holo)
├── 🏆 CTF-Challenges/      # Timed, jeopardy-style CTFs and competition challenges
└── 📝 Walkthroughs/        # High-yield cheat sheets, methodologies & notes
```

---

## 🗂️ Modules & Organization

### 1. 📦 Rooms
Categorized by difficulty to structure learning progression:
* **[Easy/](./Rooms/Easy/)**: Beginner-friendly rooms covering Nmap, Metasploit, basic Web vulnerabilities (OWASP Top 10), and Linux/Windows privilege escalation fundamentals.
* **[Medium/](./Rooms/Medium/)**: Intermediate challenges involving Active Directory, token impersonation, buffer overflows, and API testing.
* **[Hard/](./Rooms/Hard/)**: Hardened targets requiring multi-stage exploitation, custom scripting, and chain attacks.

### 2. 🌐 Networks
Dedicated folder for complex virtual networks simulating corporate infrastructure:
* Multi-host attack progression
* Internal subnet pivoting (SSH tunnels, Chisel, Ligolo-ng, Proxychains)
* Domain controller compromise and forest exploitation

### 3. 🏆 CTF-Challenges
Jeopardy and King of the Hill (KotH) style challenge write-ups, custom scripts, and flag capture strategies.

### 4. 📝 Walkthroughs
Detailed explanations and reproducible commands for completed rooms and paths.

---

## 📋 Progress Tracker

| Room / Lab Name | Category / Path | Difficulty | Status | Writeup / Notes |
| :--- | :--- | :--- | :--- | :--- |
| *Template Room* | Web / PrivEsc | Easy | 🟡 In Progress | [Notes](./Rooms/Easy/) |
