#!/usr/bin/env python3
"""
Script to update hreflang tags in all index.html files to use root URLs instead of /index.html.
This fixes the Google Search Console duplicate content issue.
"""

import os
import re
from pathlib import Path

# Files to update
INDEX_FILES = [
    "de/index.html",
    "jp/index.html", 
    "zh/index.html",
    "zh-cn/index.html"
]

# Replacements to make
REPLACEMENTS = [
    ('https://yehsheng.com/index.html', 'https://yehsheng.com/'),
    ('https://yehsheng.com/de/index.html', 'https://yehsheng.com/de/'),
    ('https://yehsheng.com/jp/index.html', 'https://yehsheng.com/jp/'),
    ('https://yehsheng.com/zh/index.html', 'https://yehsheng.com/zh/'),
    ('https://yehsheng.com/zh-cn/index.html', 'https://yehsheng.com/zh-cn/'),
]

def update_file(file_path):
    """Update hreflang URLs in a single file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old, new in REPLACEMENTS:
        if old in content:
            content = content.replace(old, new)
            modified = True
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {file_path}")
        return True
    else:
        print(f"⏭️  No changes needed: {file_path}")
        return False

def main():
    """Main function."""
    base_dir = Path(__file__).parent
    
    total_modified = 0
    
    for file_rel in INDEX_FILES:
        file_path = base_dir / file_rel
        if file_path.exists():
            if update_file(file_path):
                total_modified += 1
        else:
            print(f"❌ File not found: {file_path}")
    
    print(f"\n{'='*50}")
    print(f"✅ Total files modified: {total_modified}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
