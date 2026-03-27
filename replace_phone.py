import os

search_dir = r"c:\Users\USER\geinei_clean"
old_number_full = "2903-2176"
new_number_full = "2903-2176"

extensions_to_check = {'.html', '.py', '.txt', '.js', '.css', '.md', '.json'}
ignored_dirs = {'.git', 'node_modules', 'images', 'assets', '.gemini'}

modified_files = 0

for root, dirs, files in os.walk(search_dir):
    dirs[:] = [d for d in dirs if d not in ignored_dirs]
    for file in files:
        if any(file.endswith(ext) for ext in extensions_to_check):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if old_number_full in content:
                    content = content.replace(old_number_full, new_number_full)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {filepath}")
                    modified_files += 1
            except Exception as e:
                pass

print(f"Total files updated: {modified_files}")
