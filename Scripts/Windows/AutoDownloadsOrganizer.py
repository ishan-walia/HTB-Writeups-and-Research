import os
import shutil
import logging
from datetime import datetime
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File extension mappings
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".epub"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
    "Executables": [".exe", ".msi", ".bat", ".cmd"],
    "Scripts_Code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".json", ".sh", ".ps1"],
}


def get_category(file_extension):
    """Return category folder name based on extension."""
    ext = file_extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def resolve_duplicate(target_path):
    """If target file exists, append timestamp to prevent overwriting."""
    if not target_path.exists():
        return target_path

    stem = target_path.stem
    suffix = target_path.suffix
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{stem}_{timestamp}{suffix}"
    return target_path.parent / new_filename


def organize_directory(source_dir):
    """Organize all files in the source directory into categorized folders."""
    source_path = Path(source_dir)

    if not source_path.exists():
        print(f"Error: Path '{source_dir}' does not exist.")
        return

    print(f"\n[+] Organizing files in: {source_path.resolve()}")
    moved_count = 0

    for item in source_path.iterdir():
        # Skip directories to prevent moving already organized folders
        if item.is_dir():
            continue

        # Skip hidden/system files
        if item.name.startswith("."):
            continue

        category = get_category(item.suffix)
        category_folder = source_path / category
        category_folder.mkdir(exist_ok=True)

        target_file_path = category_folder / item.name
        target_file_path = resolve_duplicate(target_file_path)

        try:
            shutil.move(str(item), str(target_file_path))
            logging.info(f"Moved: '{item.name}' -> '{category}/{target_file_path.name}'")
            moved_count += 1
        except Exception as e:
            logging.error(f"Failed to move '{item.name}': {e}")

    print(f"\n[✓] Done! Successfully organized {moved_count} file(s).\n")


def main():
    print("=" * 60)
    print("          WINDOWS FILE & DOWNLOADS ORGANIZER           ")
    print("=" * 60)
    
    # Default to User Downloads directory
    user_home = Path.home()
    default_downloads = user_home / "Downloads"

    print(f"1. Organize Downloads Folder ({default_downloads})")
    print("2. Organize Desktop Folder")
    print("3. Enter Custom Folder Path")
    
    choice = input("\nEnter choice (1/2/3) [Default: 1]: ").strip()

    if choice == "2":
        target_dir = user_home / "Desktop"
    elif choice == "3":
        custom_path = input("Enter full folder path: ").strip()
        target_dir = Path(custom_path)
    else:
        target_dir = default_downloads

    organize_directory(target_dir)


if __name__ == "__main__":
    main()
