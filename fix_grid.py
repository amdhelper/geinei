import os
import re

base_dir = r"c:\Users\USER\geinei_clean"
files_updated = 0

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f == "resources.html" or f == "case-studies.html":
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Change minmax(320px, 1fr) to minmax(380px, 1fr) for grid container
            # This ensures at 1400px width, max 3 cards can fit per row.
            new_content = content.replace("minmax(320px, 1fr)", "minmax(380px, 1fr)")
            
            if new_content != content:
                with open(path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Updated grid in {path}")
                files_updated += 1

print(f"Updated {files_updated} files.")
