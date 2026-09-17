
# Pwntools — Python Exploitation Toolkit

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/CTF-Pwntools-red" alt="CTF">
  <img src="https://img.shields.io/badge/Cybersecurity-Exploit%20Development-black" alt="Cybersecurity">
  <img src="https://img.shields.io/badge/Focus-Binary%20Exploitation-orange" alt="Binary Exploitation">
</p>

A practical collection of **Python scripts, examples, and notes for learning Pwntools** and applying it to Capture The Flag (CTF) challenges, binary exploitation, and security research.

Pwntools is a Python-based CTF framework and exploit-development library designed to make exploit development and rapid prototyping easier.

---

## 📌 What is Pwntools?

**Pwntools** is a Python library commonly used in:

* Capture The Flag (CTF) competitions
* Binary exploitation
* Vulnerability research
* Reverse engineering workflows
* Exploit development
* Remote service interaction
* Shellcode development
* ELF analysis
* ROP-based exploitation
* Format-string exploitation

It provides a large collection of utilities that simplify common exploitation tasks such as:

* Starting local processes
* Connecting to remote services
* Sending and receiving data
* Packing and unpacking integers
* Generating cyclic patterns
* Working with ELF binaries
* Creating ROP chains
* Generating shellcode
* Assembling and disassembling instructions
* Interacting with GDB

---

## 🗂️ Repository Structure

```text
pwntools/
│
├── Readme.md
│
├── examples/
│   ├── process.py
│   ├── remote.py
│   ├── packing.py
│   ├── cyclic.py
│   ├── elf.py
│   ├── rop.py
│   └── shellcode.py
│
└── challenges/
    └── ...
```

> The exact structure may change as new Pwntools examples and CTF research are added.

---

# ⚙️ Installation

## Requirements

Recommended environment:

* Linux
* Python 3.10+
* pip
* Binutils
* Python development headers

Pwntools is best supported on 64-bit Ubuntu LTS systems, although much of the framework works on other POSIX-like systems.

### Ubuntu / Debian

```bash
sudo apt update

sudo apt install python3 python3-pip python3-dev \
git libssl-dev libffi-dev build-essential
```

### Install Pwntools

```bash
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pwntools
```

### Verify Installation

```bash
python3 -c "from pwn import *; print('Pwntools installed successfully!')"
```

---

# 🐍 Basic Usage

The most common way to use Pwntools is:

```python
from pwn import *
```

This provides access to many of the tools commonly required during CTF exploitation.

Example:

```python
from pwn import *

context.arch = "amd64"
context.os = "linux"

print("Pwntools is ready!")
```

---

# 🔌 Working With Processes

Pwntools can launch and communicate with local binaries.

```python
from pwn import *

p = process("./binary")

p.sendline(b"hello")
response = p.recvline()

print(response)

p.close()
```

This is useful when testing an exploit against a vulnerable binary locally.

---

# 🌐 Remote Connections

Pwntools also provides a simple interface for interacting with remote services.

```python
from pwn import *

HOST = "example.com"
PORT = 31337

r = remote(HOST, PORT)

r.sendline(b"hello")
print(r.recvline())

r.close()
```

The same exploit logic can often be adapted between a local process and a remote CTF service.

---

# 📦 Packing & Unpacking

Binary exploitation frequently requires converting integers into byte sequences.

Pwntools provides helpers such as:

```python
p32()
p64()
u32()
u64()
```

### Example

```python
from pwn import *

address = 0x401146

payload = p64(address)

print(payload)
```

For a 32-bit value:

```python
value = 0xdeadbeef

packed = p32(value)

print(packed)
```

Unpacking:

```python
data = b"ABCD"

value = u32(data)

print(hex(value))
```

Pwntools provides these helpers through its packing utilities, avoiding repetitive `struct` code.

---

# 🔢 Cyclic Patterns

Cyclic patterns are useful for determining the exact offset at which a buffer overflow overwrites a register or control-flow value.

Generate a pattern:

```python
from pwn import *

pattern = cyclic(200)

print(pattern)
```

After obtaining an overwritten value:

```python
offset = cyclic_find(0x6161616c)

print(offset)
```

Typical workflow:

```text
Generate cyclic pattern
        ↓
Send pattern to vulnerable program
        ↓
Program crashes
        ↓
Inspect overwritten register
        ↓
Find offset
        ↓
Build exploit payload
```

---

# 📄 ELF Analysis

Pwntools provides an `ELF` interface for inspecting ELF binaries.

```python
from pwn import *

elf = ELF("./binary")

print(elf.symbols)
print(elf.got)
print(elf.plt)
```

Individual symbols can also be accessed:

```python
print(hex(elf.symbols["main"]))
```

Useful information includes:

* Symbols
* GOT
* PLT
* Sections
* Addresses
* Architecture information
* Security-related properties

---

# 🧩 ROP

Pwntools provides utilities for building **Return-Oriented Programming (ROP)** chains.

```python
from pwn import *

elf = ELF("./binary")
rop = ROP(elf)

print(rop.rdi)
print(rop.rsi)
```

A basic ROP chain can be constructed using:

```python
rop = ROP(elf)

rop.call("puts", [elf.got["puts"]])

print(rop.dump())
```

ROP is commonly used when direct shellcode execution is prevented by protections such as NX.

---

# 💥 Buffer Overflow Workflow

A common basic exploitation workflow looks like:

```text
        Vulnerable Binary
               │
               ▼
        Analyze Binary
               │
               ▼
       Find Vulnerability
               │
               ▼
       Generate Cyclic Pattern
               │
               ▼
       Determine Offset
               │
               ▼
        Build Payload
               │
               ▼
       Control Execution
               │
               ▼
       ROP / Shellcode
               │
               ▼
        Test Locally
               │
               ▼
       Test CTF Service
```

Example payload structure:

```python
from pwn import *

offset = 72
target = 0x401146

payload = b"A" * offset
payload += p64(target)

p = process("./binary")

p.sendline(payload)
p.interactive()
```

> Only use exploitation techniques against systems and binaries you are authorized to test.

---

# 🐚 Shellcode

Pwntools includes `shellcraft`, which can generate assembly shellcode for supported architectures.

Example:

```python
from pwn import *

context.arch = "amd64"

shellcode = asm(shellcraft.sh())

print(shellcode)
```

The generated shellcode can then be used in appropriate controlled CTF or laboratory environments.

---

# 🛠️ Useful Pwntools Functions

| Function        | Purpose                        |
| --------------- | ------------------------------ |
| `process()`     | Start a local process          |
| `remote()`      | Connect to a remote service    |
| `send()`        | Send bytes                     |
| `sendline()`    | Send bytes followed by newline |
| `recv()`        | Receive data                   |
| `recvline()`    | Receive one line               |
| `recvuntil()`   | Receive until delimiter        |
| `interactive()` | Interactive terminal           |
| `p32()`         | Pack 32-bit integer            |
| `p64()`         | Pack 64-bit integer            |
| `u32()`         | Unpack 32-bit integer          |
| `u64()`         | Unpack 64-bit integer          |
| `cyclic()`      | Generate cyclic pattern        |
| `cyclic_find()` | Find pattern offset            |
| `ELF()`         | Load/analyze ELF               |
| `ROP()`         | Build ROP chains               |
| `asm()`         | Assemble instructions          |
| `disasm()`      | Disassemble instructions       |
| `shellcraft`    | Generate shellcode             |
| `gdb.debug()`   | Debug with GDB                 |

---

# 🧪 Local vs Remote Exploitation

A useful Pwntools pattern is to make the same script support both local and remote execution.

```python
from pwn import *

elf = ELF("./binary")

if args.REMOTE:
    p = remote("example.com", 31337)
else:
    p = process(elf.path)

p.interactive()
```

Run locally:

```bash
python3 exploit.py
```

Run remotely:

```bash
python3 exploit.py REMOTE
```

This makes CTF exploit scripts easier to maintain.

---

# 🐛 GDB Integration

Pwntools can also be used with GDB.

Example:

```python
from pwn import *

p = gdb.debug(
    "./binary",
    """
    break main
    continue
    """
)

p.interactive()
```

This is useful for debugging:

* Stack layout
* Register values
* Instruction flow
* Memory addresses
* Crashes
* Exploit offsets

---

# 🧠 Learning Path

Recommended order for learning Pwntools:

```text
1. Python Basics
       ↓
2. Linux Basics
       ↓
3. C Programming
       ↓
4. x86 / x86-64 Assembly
       ↓
5. GDB
       ↓
6. ELF Fundamentals
       ↓
7. Pwntools Basics
       ↓
8. Buffer Overflows
       ↓
9. ROP
       ↓
10. Format String Exploitation
       ↓
11. GOT / PLT
       ↓
12. Memory Leaks
       ↓
13. Advanced Binary Exploitation
```

---

# 🎯 CTF Use Cases

This directory is intended for practical learning and research around:

* **pwn / binary exploitation**
* Stack-based buffer overflows
* Integer packing
* Offset discovery
* ELF analysis
* GOT/PLT interaction
* ROP
* Shellcode
* Format strings
* Local process exploitation
* Remote service interaction
* CTF challenge automation

---

# 🔐 Ethical & Legal Use

Pwntools is a legitimate security research and CTF tool.

Use these scripts only against:

* CTF challenges
* Your own applications
* Local vulnerable binaries
* Intentionally vulnerable labs
* Systems where you have explicit authorization to test

Do **not** use these techniques against systems without permission.

---

# 📚 Resources

### Official Pwntools Documentation

https://docs.pwntools.com/

### Pwntools GitHub

https://github.com/Gallopsled/pwntools

### Pwntools Tutorials

https://github.com/Gallopsled/pwntools-tutorial

---

# 🚀 Quick Start

```bash
# Install dependencies
sudo apt update

sudo apt install python3 python3-pip python3-dev \
git libssl-dev libffi-dev build-essential

# Install Pwntools
python3 -m pip install --upgrade pwntools

# Create exploit
nano exploit.py
```

Example:

```python
from pwn import *

context.arch = "amd64"
context.os = "linux"

p = process("./binary")

p.sendline(b"Hello")

p.interactive()
```

Run:

```bash
python3 exploit.py
```

---

## 📌 About This Directory

This directory is part of my **Cybersecurity / Python research repository** and focuses on learning and documenting practical Pwntools usage.

The goal is to understand how Python can be used to automate common tasks in:

> **CTFs → Binary Analysis → Exploit Development → Security Research**

---

## ⭐ Related Repository

**HTB Writeups & Research**

https://github.com/ishan-walia/HTB-Writeups-and-Research

---

## ⚠️ Disclaimer

All examples are intended for **educational purposes, CTFs, authorized penetration testing, and security research**.

The author is not responsible for misuse of the information or code contained in this repository.

---

### Author

**Ishan Walia**

Cybersecurity Student | CTF Learner | Security Researcher
