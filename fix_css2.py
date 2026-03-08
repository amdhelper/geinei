import glob
import os

files = glob.glob("*/resource*.html") + ["resources.html", "resource-process.html", "resource-design.html", "resource-materials.html", "resource-quality.html", "resource-faq.html"]

old_css = """            .resource-sidebar {
                display: none !important;
            }

            .resource-content {
                margin-left: 0 !important;
            }"""

old_css2 = """            .resource-sidebar {
                display: none !important
            }

            .resource-content {
                margin-left: 0 !important
            }"""

new_css = """            .resource-layout {
                flex-direction: column !important;
                gap: 20px !important;
            }

            .resource-sidebar {
                width: 100% !important;
                position: relative !important;
                top: 0 !important;
                max-height: none !important;
                padding: 15px 15px 5px 15px !important;
                margin-bottom: 20px;
                display: flex !important;
                flex-direction: column;
            }

            .sidebar-title {
                margin-bottom: 10px !important;
                padding-bottom: 5px !important;
            }

            .sidebar-nav {
                display: flex !important;
                overflow-x: auto !important;
                padding-bottom: 10px !important;
                gap: 10px !important;
                margin: 0 -15px !important;
                padding: 0 15px 15px 15px !important;
                -webkit-overflow-scrolling: touch;
            }

            .sidebar-nav::-webkit-scrollbar {
                display: none;
            }
            .sidebar-nav {
                -ms-overflow-style: none;
                scrollbar-width: none;
            }

            .sidebar-nav li {
                margin-bottom: 0 !important;
            }

            .sidebar-nav a {
                white-space: nowrap !important;
                padding: 8px 16px !important;
                background: #f8f9fa !important;
                border: 1px solid #eee !important;
                border-radius: 20px !important;
                border-left: none !important;
            }

            .sidebar-nav a.active {
                background: #f0f4ff !important;
                border: 1px solid #C5A059 !important;
            }

            .sidebar-nav .sub-item {
                display: none !important;
            }
            
            .resource-content {
                margin-left: 0 !important;
            }"""

for f in files:
    try:
        if not os.path.exists(f):
            continue
        with open(f, "r", encoding="utf-8") as file:
            content = file.read()
            
        modified = False
        if old_css in content:
            content = content.replace(old_css, new_css)
            modified = True
        elif old_css2 in content:
            content = content.replace(old_css2, new_css)
            modified = True
            
        if modified:
            with open(f, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Updated {f}")
        else:
            if new_css in content:
                print(f"Already updated: {f}")
            else:
                print(f"CSS not found in {f}")
    except Exception as e:
        print(f"Error {f}: {e}")
