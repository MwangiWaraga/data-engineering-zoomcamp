from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"Files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath.name == current_file or not filepath.is_file():
        continue

    print(f"  - {filepath.name}")

    try:
        content = filepath.read_text()
        print(f"    Content: {content.strip()}")
    except UnicodeDecodeError:
        print("    [Skipped: not a UTF-readable text file]")
