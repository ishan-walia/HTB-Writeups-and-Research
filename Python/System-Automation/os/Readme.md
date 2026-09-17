#  os Library

- Python ki os (Operating System) library Python program ko operating system ke saath interact karne deti hai.

# mein iska use mainly:

- 📁 Files aur directories handle karne ke liye
- 💻 System information lene ke liye
- 🔍 Files search/analyze karne ke liye
- ⚙️ Environment variables access karne ke liye
- 🖥️ System commands execute karne ke liye
- 🔐 Security scripts aur automation banane ke liye

# Current directory check karna

```py
import os

print(os.getcwd())
```

- Output:
```
C:\Users\Ishan\Desktop
```
# getcwd() = Get Current Working Directory

#  Directory ke files dekhna
```py
import os

files = os.listdir(".")

for file in files:
    print(file)
```
# . ka matlab current directory.

# Check karna file hai ya directory
```py
import os

path = "test.txt"

if os.path.isfile(path):
    print("File found")

elif os.path.isdir(path):
    print("Directory found")

else:
    print("Not found")
```

#  File existence check
```py
import os

if os.path.exists("passwords.txt"):
    print("File exists")
else:
    print("File does not exist")
```

# Environment variables
```py
import os

print(os.environ.get("PATH"))
```

# System information
```py
import os

print(os.name)
```
- Example:
```
nt

nt → Windows
posix → Linux/Unix-type systems
```

# Folder create karna
```py
import os

os.makedirs("security_logs", exist_ok=True)

print("Folder created")
```
# os.system() — important

Python se system command run kar sakte ho:
```
import os

os.system("whoami")
```
Windows par:
```
os.system("whoami")
```
Linux par bhi:
```
os.system("whoami")
```
Ye current user ka naam show karta hai.

# os mein ye functions  

- os.getcwd()	 --> Current directory
- os.listdir()	--> Files/folders list
- os.path.exists()	--> Path exist karta hai?
- os.path.isfile()	--> File check
- os.path.isdir() --> 	Directory check
- os.makedirs()	--> Directory create
- os.environ	--> Environment variables
- os.name	 --> OS type
- os.system()	 --> System command

Apne Kali Linux lab mein ek Python script :
```py
import os

print("Current Directory:", os.getcwd())
print("\nFiles and Directories:")

for item in os.listdir("."):
    print(item)

print("\nOperating System:", os.name)
print("User PATH available:", os.environ.get("PATH") is not None)
```
