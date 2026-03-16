from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sample_file = BASE_DIR / "sample.txt"
exclusive_file = BASE_DIR / "created_with_x.txt"

sample_data = [
    "Alice, 85\n",
    "Bob, 90\n",
    "Charlie, 78\n"
]

# w mode: creates file or overwrites existing one
with open(sample_file, "w", encoding="utf-8") as file:
    file.writelines(sample_data)

print("sample.txt created with mode 'w' and data written successfully.")
print(f"Path: {sample_file}")

# x mode: creates file only if it does not already exist
if not exclusive_file.exists():
    with open(exclusive_file, "x", encoding="utf-8") as file:
        file.write("This file was created using mode x.\n")
    print("created_with_x.txt created with mode 'x'.")
else:
    print("created_with_x.txt already exists, so mode 'x' was skipped safely.")