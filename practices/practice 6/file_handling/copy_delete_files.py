from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
sample_file = BASE_DIR / "sample.txt"
backup_file = BASE_DIR / "sample_backup.txt"
temp_file = BASE_DIR / "temp_to_delete.txt"

if not sample_file.exists():
    with open(sample_file, "w", encoding="utf-8") as file:
        file.write("Alice, 85\nBob, 90\nCharlie, 78\n")

with open(sample_file, "a", encoding="utf-8") as file:
    file.write("Diana, 92\n")
    file.write("Erlan, 88\n")

print("New lines appended to sample.txt.")

with open(sample_file, "r", encoding="utf-8") as file:
    print("Updated content:")
    print(file.read())

shutil.copy(sample_file, backup_file)
print(f"Backup created: {backup_file}")

with open(temp_file, "w", encoding="utf-8") as file:
    file.write("This file will be deleted safely.")

if temp_file.exists():
    temp_file.unlink()
    print(f"Deleted: {temp_file}")
else:
    print("Temp file was not found.")