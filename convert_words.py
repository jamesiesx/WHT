# convert_words.py
from pathlib import Path
import json

# Path to your words.txt (you can leave this path as-is)
src = Path(r"C:\Users\james\source\repos\WordleHelper\words.txt")
dst = src.with_name("words.json")  # output in same folder

# Read lines, strip whitespace, ignore empty lines
with src.open("r", encoding="utf-8-sig") as f:
    words = [line.strip() for line in f if line.strip()]

# Save as JSON array
with dst.open("w", encoding="utf-8") as f:
    json.dump(words, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(words)} entries to: {dst}")