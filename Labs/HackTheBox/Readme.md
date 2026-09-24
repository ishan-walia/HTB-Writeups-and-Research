# 🟢 Hack The Box (HTB) Labs

<p align="center">
  <img src="https://img.shields.io/badge/Platform-HackTheBox-111927?style=for-the-badge&logo=hackthebox&logoColor=9FEF00" alt="HTB Badge"/>
  <img src="https://img.shields.io/badge/Focus-Offensive%20%26%20Defensive-brightgreen?style=for-the-badge" alt="Focus"/>
  <img src="https://img.shields.io/badge/Status-Actively%20Updated-success?style=for-the-badge" alt="Status"/>
</p>

---

## 📌 Directory Structure

```text
HackTheBox/
│
├── 🎯 Challenges/          # Standalone category-based CTF challenges
│   ├── Espresso/           # Reverse Engineering & Binary logic
│   ├── Ether Tag/          # Blockchain & Smart Contract security
│   ├── Lucky Dice/         # PRNG exploitation & logic flaws
│   ├── OpenSecret/         # Cryptographic key leaks & auth bypass
│   ├── Primed for Action/  # Binary reversing & memory analysis
│   ├── ReactOOPS/          # Client/Server-side state vulnerabilities
│   └── Spookifier/         # SSTI / Web exploitation
│
├── 🔍 Sherlocks/           # Blue Team & DFIR Investigations
│   ├── BFT/                # $MFT / NTFS filesystem forensics
│   ├── CAMouflage/         # Endpoint tampering & persistence detection
│   ├── Fruitzy/            # Web compromise & lateral movement analysis
│   ├── Reaper/             # Incident timeline & adversary attribution
│   ├── ShadowBait/         # Deception technology & credential harvesting
│   └── Unit42/             # Advanced persistent threat (APT) triage
│
└── 🖥️ Machines/            # Full-scale target boxes
    ├── Easy/               # Foundational CVEs & straightforward privesc
    ├── Medium/             # Complex chains & Active Directory pivots
    ├── Hard/               # Custom exploits & intricate internal networks
    └── Insane/             # Zero-days, kernel exploitation & custom defenses
```

---

## 🎯 Challenges Breakdown

| Challenge | Category | Description / Concepts | Link |
| :--- | :--- | :--- | :--- |
| **Spookifier** | Web | Server-Side Template Injection (SSTI) | [View](./Challenges/Spookifier/) |
| **ReactOOPS** | Web | State manipulation & client-side exposure | [View](./Challenges/ReactOOPS/) |
| **Lucky Dice** | Misc / Crypto | Pseudo-Random Number Generator (PRNG) analysis | [View](./Challenges/Lucky%20Dice/) |
| **OpenSecret** | Crypto | Sensitive token leakage & cryptographic bypass | [View](./Challenges/OpenSecret/) |
| **Ether Tag** | Blockchain | Smart contract manipulation | [View](./Challenges/Ether%20Tag/) |
| **Espresso** | Reverse Engineering | Decompilation & control-flow analysis | [View](./Challenges/Espresso/) |
| **Primed for Action** | Reverse Engineering | Binary disassembly & signature verification | [View](./Challenges/Primed%20for%20Action/) |

---

## 🔍 DFIR & Incident Response (Sherlocks)

| Case Name | Investigation Focus | Artifacts Analyzed | Link |
| :--- | :--- | :--- | :--- |
| **Unit42** | APT Attack Analysis | Memory dumps, event logs, command history | [View](./Sherlocks/Unit42/) |
| **Reaper** | Timeline Reconstruction | Sysmon, Prefetch, Shimcache, Amcache | [View](./Sherlocks/Reaper/) |
| **ShadowBait** | Deception & Honeytokens | Honey-credentials, network connection logs | [View](./Sherlocks/ShadowBait/) |
| **CAMouflage** | Endpoint Defense Tampering | Registry modification, AMSI bypass artifacts | [View](./Sherlocks/CAMouflage/) |
| **BFT** | NTFS $MFT Analysis | Master File Table records, timestamp tampering | [View](./Sherlocks/BFT/) |
| **Fruitzy** | Web Intrusion & Pivot | Access logs, webshell forensics, lateral movement | [View](./Sherlocks/Fruitzy/) |

---

## 🖥️ Target Machines

Track machine write-ups, initial foothold techniques, lateral movements, and root/system privilege escalations organized by difficulty tier in [Machines/](./Machines/).
