from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
nested_dir = BASE_DIR / "demo_dir" / "course" / "week1"
empty_dir = BASE_DIR / "empty_folder"

# Create nested directories
os.makedirs(nested_dir, exist_ok=True)
print(f"Created nested directory: {nested_dir}")

# Create a sample text file inside nested directory
example_file = nested_dir / "notes.txt"
example_file.write_text("Directory management example", encoding="utf-8")

# Create an empty directory for os.rmdir() example
empty_dir.mkdir(exist_ok=True)
print(f"Created empty directory: {empty_dir}")

print("\nCurrent working directory before chdir:")
print(os.getcwd())

# Change current working directory
os.chdir(BASE_DIR)
print("\nCurrent working directory after chdir:")
print(os.getcwd())

print("\nItems inside directory_management folder:")
for item in os.listdir(BASE_DIR):
    item_path = BASE_DIR / item
    if item_path.is_dir():
        print(f"[DIR]  {item}")
    else:
        print(f"[FILE] {item}")

print("\nAll .txt files inside directory_management:")
for txt_file in BASE_DIR.rglob("*.txt"):
    print(txt_file)

# Remove empty directory safely
if empty_dir.exists() and empty_dir.is_dir():
    try:
        os.rmdir(empty_dir)
        print(f"\nRemoved empty directory: {empty_dir}")
    except OSError:
        print(f"\nCould not remove {empty_dir} because it is not empty.")