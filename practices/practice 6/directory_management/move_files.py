from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent
source_dir = BASE_DIR / "source_files"
target_dir = BASE_DIR / "target_files"

source_dir.mkdir(exist_ok=True)
target_dir.mkdir(exist_ok=True)

source_file = source_dir / "example.txt"
source_file.write_text("This file will be copied and moved.", encoding="utf-8")

copied_file = target_dir / "copied_example.txt"
shutil.copy(source_file, copied_file)
print(f"Copied file to: {copied_file}")

moved_file = target_dir / "moved_example.txt"
shutil.move(str(source_file), str(moved_file))
print(f"Moved file to: {moved_file}")