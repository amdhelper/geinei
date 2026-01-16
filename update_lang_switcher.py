import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Files to update (excluding index.html and products.html which are already updated)
files_to_update = [
    'about.html', 'capabilities.html', 'contact.html', 
    'applications.html', 'solutions.html', 'resources.html', 
    'emerging-tech.html'
]

# Old pattern to find
old_pattern = r'''    <!-- Top Bar \(Klein Blue[^\)]*\) -->
    <div class="hidden-mobile" style="background-color: #002FA7; color: white; padding: 10px 0;">
        <div class="container"
            style="display: flex; justify-content: flex-end; gap: 25px; font-size: 13px; font-weight: 500; letter-spacing: 0.5px;">
            <a href="about.html" style="color: #ddd;">About Us</a>
            <a href="contact.html" style="color: #ddd;">Contact</a>
            <a href="javascript:void\(0\)" id="reset-lang-btn" onclick="resetLanguage\(\)"
                style="color: #C5A059; margin-right: 15px; font-weight: 600; cursor: pointer; text-decoration: none;">English</a>
            <div id="google_translate_element" style="display: inline-block; vertical-align: middle;"></div>
        </div>
    </div>'''

def get_new_topbar(filename):
    page_name = filename.replace('.html', '')
    return f'''    <!-- Top Bar (Klein Blue #002FA7) -->
    <div class="hidden-mobile" style="background-color: #002FA7; color: white; padding: 10px 0;">
        <div class="container"
            style="display: flex; justify-content: flex-end; gap: 25px; font-size: 13px; font-weight: 500; letter-spacing: 0.5px; align-items: center;">
            <a href="about.html" style="color: #ddd;">About Us</a>
            <a href="contact.html" style="color: #ddd;">Contact</a>
            <!-- Language Dropdown -->
            <div style="position: relative; display: inline-block;">
                <button onclick="toggleLangDropdown()" 
                    style="background: transparent; border: 1px solid #C5A059; color: #C5A059; padding: 6px 15px; border-radius: 4px; cursor: pointer; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 8px;">
                    🌐 English ▼
                </button>
                <div id="langDropdown" style="display: none; position: absolute; right: 0; top: 100%; margin-top: 5px; background: white; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.15); min-width: 160px; z-index: 1000; overflow: hidden;">
                    <a href="{filename}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px; border-bottom: 1px solid #eee; font-weight: 600; background: #f8f9fa;">🇺🇸 English</a>
                    <a href="zh/{filename}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px; border-bottom: 1px solid #eee;">🇹🇼 繁體中文</a>
                    <a href="zh-cn/{filename}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px; border-bottom: 1px solid #eee;">🇨🇳 简体中文</a>
                    <a href="de/{filename}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px; border-bottom: 1px solid #eee;">🇩🇪 Deutsch</a>
                    <a href="jp/{filename}" style="display: block; padding: 12px 20px; color: #333; font-size: 14px;">🇯🇵 日本語</a>
                </div>
            </div>
        </div>
    </div>'''

# JavaScript to add before </body>
lang_script = '''
    <script>
        // Language Dropdown Toggle
        function toggleLangDropdown() {
            var dropdown = document.getElementById("langDropdown");
            dropdown.style.display = dropdown.style.display === "none" ? "block" : "none";
        }
        
        // Close dropdown when clicking outside
        document.addEventListener('click', function(e) {
            var dropdown = document.getElementById("langDropdown");
            var button = e.target.closest('button');
            if (dropdown && !e.target.closest('#langDropdown') && (!button || !button.onclick || button.onclick.toString().indexOf('toggleLangDropdown') === -1)) {
                dropdown.style.display = "none";
            }
        });
    </script>
</body>'''

for filename in files_to_update:
    filepath = os.path.join(BASE_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace old topbar with new dropdown
        new_topbar = get_new_topbar(filename)
        content = re.sub(old_pattern, new_topbar, content, flags=re.DOTALL)
        
        # Add language script before </body> if not already present
        if 'toggleLangDropdown' not in content:
            content = content.replace('</body>', lang_script)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated {filename}")

print("Done!")
