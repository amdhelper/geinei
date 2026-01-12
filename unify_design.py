import os
import re

# Configuration
ROOT_DIR = '/home/ubuntu/pure_html'
FILES_TO_PROCESS = ['products.html', 'solutions.html', 'applications.html', 'capabilities.html', 'emerging-tech.html', 'about.html', 'contact.html']

# The "Klein Blue & Gold" Standard Header & Footer
# Updated to match the new index.html design: Klein Blue (#002FA7), Gold (#C5A059), and correct company name.

GOLD_HEAD_STYLES = """
    <!-- Import Google Fonts: Playfair Display (Serif) for Headings, Inter (Sans) for Body -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
    
    <style>
        /* Global Reset */
        body { margin: 0; padding: 0; font-family: 'Inter', sans-serif; color: #333; background-color: #fcfcfc; overflow-x: hidden; }
        a { text-decoration: none; color: inherit; transition: all 0.3s ease; }
        * { box-sizing: border-box; }
        
        /* Utility Classes */
        .container { max-width: 1400px; margin: 0 auto; padding: 0 20px; }
        
        /* Premium Card Style */
        .premium-card {
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            padding: 40px 30px;
            text-align: center;
            border-bottom: 4px solid #C5A059; /* Gold Accent */
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%;
        }
        .premium-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(197, 160, 89, 0.15);
        }

        /* Gold Button Style */
        .btn-gold {
            background-color: #C5A059;
            color: white;
            padding: 16px 32px;
            border-radius: 6px;
            font-weight: 500;
            letter-spacing: 0.5px;
            display: inline-block;
            border: 1px solid #C5A059;
            text-align: center;
            cursor: pointer;
        }
        .btn-gold:hover {
            background-color: #b08d4d;
            border-color: #b08d4d;
        }

        .btn-outline-gold {
            background-color: transparent;
            color: #C5A059;
            padding: 16px 32px;
            border-radius: 6px;
            font-weight: 500;
            letter-spacing: 0.5px;
            display: inline-block;
            border: 1px solid #C5A059;
            text-align: center;
            cursor: pointer;
        }
        .btn-outline-gold:hover {
            background-color: #C5A059;
            color: white;
        }

        /* Mobile Menu Styles */
        .mobile-menu-btn { display: none; cursor: pointer; font-size: 24px; color: #333; }
        .mobile-menu { 
            display: none; 
            position: absolute; 
            top: 100%; 
            left: 0; 
            width: 100%; 
            background: white; 
            box-shadow: 0 10px 20px rgba(0,0,0,0.1); 
            padding: 20px; 
            flex-direction: column; 
            gap: 15px; 
            z-index: 99;
        }
        .mobile-menu.active { display: flex; }
        
        /* Responsive Styles */
        @media (max-width: 768px) {
            .hidden-mobile { display: none !important; }
            .mobile-menu-btn { display: block; }
            
            /* Layout Adjustments */
            .flex-col-mobile { flex-direction: column !important; gap: 40px !important; }
            .w-full-mobile { width: 100% !important; }
            .mt-mobile { margin-top: 20px !important; }
            
            /* Typography Adjustments */
            h1 { font-size: 42px !important; line-height: 1.2 !important; }
            h2 { font-size: 32px !important; }
            p { font-size: 16px !important; }
            
            /* Spacing Adjustments */
            section { padding: 60px 0 !important; }
            .container { padding: 0 20px; }
            
            /* Button Adjustments */
            .btn-gold, .btn-outline-gold { width: 100%; box-sizing: border-box; }
            
            /* Grid Adjustments */
            .grid-mobile { grid-template-columns: 1fr !important; }
        }
    </style>
"""

GOLD_NAV = """
    <!-- Top Bar (Klein Blue) -->
    <div style="background-color: #002FA7; color: white; padding: 10px 0;" class="hidden-mobile">
        <div class="container" style="display: flex; justify-content: flex-end; gap: 25px; font-size: 13px; font-weight: 500; letter-spacing: 0.5px;">
            <a href="about.html" style="color: #ddd;">About Us</a>
            <a href="contact.html" style="color: #ddd;">Contact</a>
            <div style="position: relative; display: inline-block;">
                <span style="cursor: pointer; color: #C5A059;">English ▼</span>
            </div>
        </div>
    </div>

    <!-- Navigation -->
    <nav style="background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 100;">
        <div class="container" style="padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; position: relative;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <a href="index.html" style="display: flex; align-items: center; gap: 15px;">
                    <img src="images/logo.png" alt="Logo" style="height: 40px;">
                    <div style="display: flex; flex-direction: column;">
                        <span style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; color: #111; line-height: 1;">Yeh Sheng</span>
                        <span style="font-size: 9px; text-transform: uppercase; letter-spacing: 1px; color: #C5A059; font-weight: 600;">Powder Metallurgy</span>
                    </div>
                </a>
            </div>
            
            <!-- Desktop Menu -->
            <div class="hidden-mobile" style="display: flex; gap: 35px; align-items: center;">
                <a href="products.html" style="font-size: 15px; font-weight: 500; color: #333; text-transform: uppercase; letter-spacing: 0.5px;">Products</a>
                <a href="solutions.html" style="font-size: 15px; font-weight: 500; color: #333; text-transform: uppercase; letter-spacing: 0.5px;">Solutions</a>
                <a href="capabilities.html" style="font-size: 15px; font-weight: 500; color: #333; text-transform: uppercase; letter-spacing: 0.5px;">Capabilities</a>
                <a href="applications.html" style="font-size: 15px; font-weight: 500; color: #333; text-transform: uppercase; letter-spacing: 0.5px;">Industries</a>
                <a href="contact.html" style="background: #C5A059; color: white; padding: 8px 20px; border-radius: 4px; font-size: 14px; font-weight: 500;">Contact</a>
            </div>

            <!-- Mobile Menu Button -->
            <div class="mobile-menu-btn" onclick="toggleMenu()">
                ☰
            </div>

            <!-- Mobile Menu Dropdown -->
            <div class="mobile-menu" id="mobileMenu">
                <a href="products.html" style="font-size: 16px; font-weight: 500; color: #333; padding: 10px 0; border-bottom: 1px solid #eee;">Products</a>
                <a href="solutions.html" style="font-size: 16px; font-weight: 500; color: #333; padding: 10px 0; border-bottom: 1px solid #eee;">Solutions</a>
                <a href="capabilities.html" style="font-size: 16px; font-weight: 500; color: #333; padding: 10px 0; border-bottom: 1px solid #eee;">Capabilities</a>
                <a href="applications.html" style="font-size: 16px; font-weight: 500; color: #333; padding: 10px 0; border-bottom: 1px solid #eee;">Industries</a>
                <a href="about.html" style="font-size: 16px; font-weight: 500; color: #333; padding: 10px 0; border-bottom: 1px solid #eee;">About Us</a>
                <a href="contact.html" style="font-size: 16px; font-weight: 500; color: #C5A059; padding: 10px 0;">Contact Us</a>
            </div>
        </div>
    </nav>
"""

GOLD_FOOTER = """
    <!-- Footer (Klein Blue) -->
    <footer style="background: #002FA7; color: white; padding: 80px 0 40px 0;">
        <div class="container">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 50px; margin-bottom: 60px;">
                
                <!-- Brand -->
                <div>
                    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 25px;">
                        <img src="images/logo.png" alt="Logo" style="height: 40px; filter: brightness(0) invert(1);">
                        <div style="display: flex; flex-direction: column;">
                            <span style="font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; color: white; line-height: 1;">Yeh Sheng</span>
                            <span style="font-size: 9px; text-transform: uppercase; letter-spacing: 1px; color: #C5A059; font-weight: 600;">Powder Metallurgy</span>
                        </div>
                    </div>
                    <p style="color: #e0e0e0; line-height: 1.6; font-size: 14px;">
                        Premier manufacturer of high-precision powder metallurgy components since 1980.
                    </p>
                </div>

                <!-- Links -->
                <div>
                    <h4 style="color: white; font-size: 16px; font-weight: 600; margin-bottom: 25px;">Company</h4>
                    <div style="display: flex; flex-direction: column; gap: 15px;">
                        <a href="about.html" style="color: #e0e0e0; font-size: 14px;">About Us</a>
                        <a href="products.html" style="color: #e0e0e0; font-size: 14px;">All Products</a>
                        <a href="capabilities.html" style="color: #e0e0e0; font-size: 14px;">Capabilities</a>
                        <a href="contact.html" style="color: #e0e0e0; font-size: 14px;">Contact</a>
                    </div>
                </div>

                <!-- Contact -->
                <div>
                    <h4 style="color: white; font-size: 16px; font-weight: 600; margin-bottom: 25px;">Contact Us</h4>
                    <div style="display: flex; flex-direction: column; gap: 15px; color: #e0e0e0; font-size: 14px;">
                        <span>No. 11, Ln. 721, Zhong Zheng Rd.</span>
                        <span>Xin Zhuang Dist., New Taipei City</span>
                        <a href="mailto:sales@yehsheng.com.tw" style="color: #C5A059;">sales@yehsheng.com.tw</a>
                        <a href="tel:+886229018266" style="color: white;">+886-2-2901-8266</a>
                    </div>
                </div>

            </div>

            <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; text-align: center; color: #e0e0e0; font-size: 13px;">
                &copy; 2025 Yeh Sheng Powder Parts Ind. Co. Ltd. All rights reserved.
            </div>
        </div>
    </footer>

    <script>
        function toggleMenu() {
            var menu = document.getElementById('mobileMenu');
            if (menu.style.display === 'flex') {
                menu.style.display = 'none';
            } else {
                menu.style.display = 'flex';
            }
        }
    </script>
</body>
</html>
"""

def process_file(filename):
    path = os.path.join(ROOT_DIR, filename)
    if not os.path.exists(path):
        print(f"Skipping {filename} (not found)")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Head Styles
    # Find everything between <head> and </head> and insert our GOLD_HEAD_STYLES
    # But we want to keep the title and meta tags if possible.
    # Simple approach: Replace <style>...</style> block and ensure fonts are there.
    # Better approach: Find </title> and replace everything after it until </head>
    
    if '</title>' in content:
        parts = content.split('</title>')
        head_start = parts[0] + '</title>'
        rest = parts[1]
        if '</head>' in rest:
            body_parts = rest.split('</head>')
            new_head = GOLD_HEAD_STYLES
            content = head_start + new_head + '</head>' + body_parts[1]
    
    # 2. Replace Navigation
    # Find <body> and replace everything until the first <section> or main content container
    # This is tricky because pages might have different structures.
    # Let's look for <nav>...</nav> and the Top Bar div before it.
    
    # Regex to find the existing nav and top bar area
    # Assuming they start after <body> and end before the first <section> or <div class="page-header">
    
    # A safer way: Look for specific markers we used before or just replace the top chunk of body
    if '<body>' in content:
        body_split = content.split('<body>')
        pre_body = body_split[0] + '<body>'
        post_body = body_split[1]
        
        # Find where the main content starts. Usually it's a <div class="page-header"> or <section>
        # We will replace everything from <body> start to that point with GOLD_NAV
        
        match = re.search(r'(<div class="page-header"|<section)', post_body)
        if match:
            start_idx = match.start()
            main_content = post_body[start_idx:]
            content = pre_body + GOLD_NAV + main_content
        else:
            print(f"Could not find main content start in {filename}")

    # 3. Replace Footer
    # Find <footer>...</footer> and replace it, along with closing body/html tags
    if '<footer' in content:
        footer_start = content.find('<footer')
        content = content[:footer_start] + GOLD_FOOTER
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

if __name__ == "__main__":
    for filename in FILES_TO_PROCESS:
        process_file(filename)
