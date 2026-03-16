from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sample_file = BASE_DIR / "sample.txt"

if sample_file.exists():
    with open(sample_file, "r", encoding="utf-8") as file:
        content = file.read()
    print("Full file content:")
    print(content)

    with open(sample_file, "r", encoding="utf-8") as file:
        first_line = file.readline()
    print("First line:")
    print(first_line)

    with open(sample_file, "r", encoding="utf-8") as file:
        all_lines = file.readlines()
    print("All lines as list:")
    print(all_lines)
else:
    print("sample.txt does not exist. Run write_files.py first.")