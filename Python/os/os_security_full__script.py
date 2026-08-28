import os
import platform

print("=" * 60)
print("        PYTHON OS LIBRARY - SECURITY LAB")
print("=" * 60)

# --------------------------------------------------
# 1. Operating System Information
# --------------------------------------------------

print("\n[+] SYSTEM INFORMATION")

print("OS Name       :", os.name)
print("Platform      :", platform.system())
print("OS Release    :", platform.release())
print("Architecture  :", platform.machine())


# --------------------------------------------------
# 2. Current User
# --------------------------------------------------

print("\n[+] CURRENT USER")

username = os.environ.get("USERNAME") or os.environ.get("USER")

print("Username      :", username)


# --------------------------------------------------
# 3. Current Working Directory
# --------------------------------------------------

print("\n[+] CURRENT DIRECTORY")

current_dir = os.getcwd()

print("Working Dir   :", current_dir)


# --------------------------------------------------
# 4. Directory Enumeration
# --------------------------------------------------

print("\n[+] DIRECTORY ENUMERATION")

items = os.listdir(current_dir)

for item in items:
    full_path = os.path.join(current_dir, item)

    if os.path.isdir(full_path):
        print("[DIR ]", item)

    elif os.path.isfile(full_path):
        print("[FILE]", item)


# --------------------------------------------------
# 5. File / Directory Check
# --------------------------------------------------

print("\n[+] PATH CHECK")

test_path = input("Enter a file/directory path: ")

if os.path.exists(test_path):

    print("Path exists!")

    if os.path.isfile(test_path):
        print("Type : File")

    elif os.path.isdir(test_path):
        print("Type : Directory")

else:
    print("Path does not exist.")


# --------------------------------------------------
# 6. Create Security Lab Directory
# --------------------------------------------------

print("\n[+] SECURITY LOG DIRECTORY")

log_directory = "security_logs"

os.makedirs(log_directory, exist_ok=True)

print("Log directory:", log_directory)
print("Status: Ready")


# --------------------------------------------------
# 7. Environment Variables
# --------------------------------------------------

print("\n[+] ENVIRONMENT INFORMATION")

path_variable = os.environ.get("PATH")

if path_variable:
    print("PATH variable is available.")
else:
    print("PATH variable not found.")


# --------------------------------------------------
# 8. Safe System Command
# --------------------------------------------------

print("\n[+] CURRENT USER VERIFICATION")

if os.name == "nt":
    os.system("whoami")
else:
    os.system("whoami")


# --------------------------------------------------
# 9. Security Summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("                 LAB SUMMARY")
print("=" * 60)

print("[+] OS Detection       : Completed")
print("[+] User Detection     : Completed")
print("[+] Directory Check    : Completed")
print("[+] File Enumeration   : Completed")
print("[+] Path Verification  : Completed")
print("[+] Log Directory      : Completed")
print("[+] Environment Check  : Completed")
print("[+] User Verification  : Completed")

print("\nLab completed successfully.")
