import os
from bs4 import BeautifulSoup
import re

def apply_ampersand_fix(root_dir):
    # Regex to find un-wrapped ampersands (escaping & to avoid BS4 auto-conversion issues)
    # We look for & or &amp; that is NOT inside our target span
    # Target span: <span style="font-family: 'Inter', 'Arial', sans-serif;">&amp;</span>
    
    # Actually, it's easier to use BeautifulSoup to manipulate the DOM
    
    files_modified = 0
    for root, dirs, files in os.walk(root_dir):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                modified = False
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    soup = BeautifulSoup(content, 'html.parser')
                    for tag_name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                        for tag in soup.find_all(tag_name):
                            # We need to preserve the inner HTML structure but replace ampersands in text nodes
                            # BS4 find_all(string=True) returns NavigableStrings
                            
                            # However, the requirement is to wrap the ampersand in a span.
                            # If we just replace text, it's hard to insert a span without it being escaped.
                            
                            # Let's try raw string replacement within the tag's inner HTML
                            inner_html = tag.decode_contents()
                            
                            # Use regex to find & or &amp; that isn't already wrapped.
                            # This is tricky with regex + HTML. 
                            # Let's use a simpler approach: replace & and &amp; then deduplicate/fix if it matches our pattern.
                            
                            # Pattern for already replaced:
                            pattern_wrapped = r'<span style="font-family: [\'"](?:Inter|Noto Sans JP|Noto Sans SC|Noto Sans TC|Arial)[\'"], sans-serif;">&amp;</span>'
                            
                            # If it's already there, we might want to skip or normalize.
                            # Let's find all ampersands and check their context.
                            
                            new_inner = inner_html
                            # This regex finds & or &amp; but skips them if they are part of our span
                            # We use a negative lookahead/lookbehind if possible, but let's just do a safer two-step:
                            # 1. Temporarily mark existing spans
                            # 2. Replace remaining &
                            # 3. Restore spans
                            
                            marker = "___AMP_SPAN_MARKER___"
                            temp_new_inner = re.sub(pattern_wrapped, marker, new_inner)
                            
                            if '&' in temp_new_inner:
                                # Replace any remaining & or &amp;
                                updated_inner = re.sub(r'&(amp;)?', '<span style="font-family: \'Inter\', \'Arial\', sans-serif;">&amp;</span>', temp_new_inner)
                                # Restore markers
                                updated_inner = updated_inner.replace(marker, '<span style="font-family: \'Inter\', \'Arial\', sans-serif;">&amp;</span>')
                                
                                if updated_inner != inner_html:
                                    # Use a fresh parser to set the new contents (to handle entity encoding correctly)
                                    tag.clear()
                                    tag.append(BeautifulSoup(updated_inner, 'html.parser'))
                                    modified = True
                    
                    if modified:
                        # Write back with original spacing if possible, but BS4 prettify might change things.
                        # Simple f.write(str(soup)) or soup.encode(formatter="html")
                        with open(path, 'w', encoding='utf-8') as f:
                            # Using 'html' formatter to keep entities like &amp; consistent
                            f.write(soup.decode(formatter="html"))
                        files_modified += 1
                        print(f"Updated: {path}")
                        
                except Exception as e:
                    print(f"Error processing {path}: {e}")
    
    print(f"Total files updated: {files_modified}")

if __name__ == "__main__":
    root = r"c:\Users\USER\geinei_clean"
    apply_ampersand_fix(root)
