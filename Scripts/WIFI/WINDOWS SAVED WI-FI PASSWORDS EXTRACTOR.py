import subprocess
import re

def get_wifi_passwords():
    """Retrieve saved Wi-Fi SSIDs and their cleartext passwords on Windows."""
    print("=" * 60)
    print("          WINDOWS SAVED WI-FI PASSWORDS EXTRACTOR          ")
    print("=" * 60)
    
    try:
        # Get list of Wi-Fi profiles
        command_output = subprocess.check_output(
            ["netsh", "wlan", "show", "profiles"], 
            encoding="cp850", 
            errors="ignore"
        )
        
        # Extract profile names
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", command_output)
        
        if not profiles:
            print("No saved Wi-Fi profiles found.")
            return

        print(f"Found {len(profiles)} Wi-Fi profile(s):\n")
        print(f"{'Wi-Fi Name (SSID)':<35} | {'Password':<25}")
        print("-" * 65)

        for profile in profiles:
            profile_name = profile.strip("\r\n ")
            try:
                # Fetch security key for each profile
                profile_info = subprocess.check_output(
                    ["netsh", "wlan", "show", "profile", profile_name, "key=clear"],
                    encoding="cp850",
                    errors="ignore"
                )
                
                # Search for Key Content
                password_match = re.search(r"Key Content\s*:\s*(.*)", profile_info)
                
                if password_match:
                    password = password_match.group(1).strip("\r\n ")
                else:
                    password = "[Open Network / Not Stored]"
                
                print(f"{profile_name:<35} | {password:<25}")
            except Exception as e:
                print(f"{profile_name:<35} | [Error reading key]")
                
        print("\n" + "=" * 60)

    except Exception as err:
        print(f"Error executing netsh command: {err}")

if __name__ == "__main__":
    get_wifi_passwords()
