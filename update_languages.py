import os
import shutil
import re
from bs4 import BeautifulSoup

# Configuration
LANGUAGES = {
    'zh': {
        'name': '中文',
        'nav': {
            'Home': '首頁', 'Solutions': '解決方案', 'Applications': '應用領域',
            'Emerging Tech': '新興技術', 'Capabilities': '製程能力',
            'Products': '產品介紹', 'About': '關於我們', 'Contact': '聯絡我們'
        },
        'hero': {
            'Precision in <br>Every Particle': '精確至<br>每一微粒',
            'Over 40 years of excellence': '超過40年的粉末冶金卓越經驗',
            'Explore Products': '產品介紹', 'Discuss Your Design': '討論您的設計',
            '40+': '40+', 'Years Experience': '年豐富經驗',
            '±0.01mm': '±0.01mm', 'Precision Tolerance': '精密公差',
            'ISO 9001': 'ISO 9001', 'Quality Certified': '品質認證',
            'Global': '全球', 'Export Reach': '出口範圍',
            '100%': '100%', 'Customization': '客製化服務',
            'Cost': '成本', 'Effective': '效益最佳化',
            'Automotive Excellence': '汽機車卓越工藝',
            'Driving Future <br>Mobility': '驅動未來 <br>移動科技',
            'High-precision rotors, gears, and structural parts for next-generation automotive and motorcycle applications.': '為下一代汽機車應用提供高精密轉子、齒輪與結構件。',
            'View Automotive Parts': '查看汽機車零件',
            'Industrial Strength': '工業級強度',
            'Powering <br>Performance': '動力 <br>效能核心',
            'Robust gears and transmission components designed for high-torque power tools and industrial machinery.': '專為高扭力電動工具與工業機械設計的堅固齒輪與傳動組件。',
            'View Power Tool Parts': '查看電動工具零件'
        },
        'products': {
            'Our Products': '產品介紹',
            'Precision Powder Metallurgy Parts': '滿足您多樣需求的精密粉末冶金零件',
            'All Products': '所有產品', 'Precision Gears': '精密齒輪',
            'Automotive & Motorcycle': '汽機車零件', 'Industrial Parts': '工業零件',
            'High Precision Applications': '高精密應用',
            'High-strength sintered gears': '用於傳動系統的高強度燒結齒輪',
            'Biocompatible stainless steel parts': '用於醫療設備的生物相容性不鏽鋼零件',
            'Complex multi-part assemblies': '具有精密配合的複雜多部件組件',
            'High-efficiency rotors': '用於汽車油泵的高效率轉子',
            'Small precision parts': '用於電腦和電子產品的小型精密零件',
            'Complex geometry parts': '具有高結構完整性的複雜幾何形狀零件',
            'Precision stainless steel components': '用於手術的精密不鏽鋼組件',
            'Durable gears and sprockets': '用於動力傳輸的耐用齒輪和鏈輪'
        },
        'applications': {
            'Industry Applications': '產業應用',
            'Serving diverse sectors': '以高性能燒結組件服務多元產業',
            'Automotive & Motorcycle': '汽機車零件', 'Mechanical Parts': '機械零件',
            'Power Tool Parts': '電動工具零件', 'Hardware & Electronics': '五金與電子零件',
            'Engine, transmission, and oil pump components.': '引擎、變速箱與油泵組件。',
            'Industrial gears and hydraulic rotors.': '工業齒輪與液壓轉子。',
            'High-torque gears for professional tools.': '專業工具用高扭力齒輪。',
            'Precision lock parts and office machine components.': '精密鎖具零件與事務機組件。',
            'Key Components': '關鍵組件'
        },
        'capabilities': {
            'Manufacturing Capabilities': '製程能力',
            'Advanced Powder Metallurgy Process': '從設計到量產的先進粉末冶金製程',
            'Our Production Process': '我們的生產流程',
            'Powder': '粉末混合', 'Press': '成型', 'Sintered': '燒結',
            'Sizing': '整形', 'Secondary Machining': '二次加工',
            'Precise blending': '金屬粉末與潤滑劑的精確混合。',
            'Pressing powder': '以高噸位將粉末壓製成生胚。',
            'Bonding particles': '在控制氣氛爐中結合顆粒。',
            'Re-pressing': '重新壓製以獲得緊密公差和表面光潔度。',
            'Machining, heat treatment': '機械加工、熱處理和表面電鍍。'
        },
        'emerging': {
            'Emerging Technologies': '新興技術',
            'Pioneering the future': '以先進粉末冶金解決方案開拓未來',
            'Electric Vehicles (EV)': '電動車 (EV)', 'Robotics & Automation': '機器人與自動化', 'Green Energy': '綠色能源',
            'Developing soft magnetic composites': '開發軟磁複合材料 (SMC) 用於高效率馬達。',
            'Precision micro-gears': '用於機器人關節和工業手臂的精密微型齒輪。',
            'Supporting the renewable energy': '以耐用組件支持再生能源產業。',
            'Innovations': '創新技術'
        },
        'contact': {
            'Contact Us': '聯絡我們',
            'Get in touch': '與我們的工程團隊聯繫您的下一個專案',
            'Headquarters & Factory': '總部與工廠', 'Phone': '電話', 'Email': '電子郵件',
            'Send us a Message': '發送訊息給我們', 'Name': '姓名', 'Subject': '主旨', 'Message': '訊息',
            'Send Message': '發送訊息',
            'No. 11, Ln. 721, Zhong Zheng Rd., Xin Zhuang Dist., New Taipei City, 24265, Taiwan': '新北市新莊區中正路721巷11號',
            'View on Google Maps': '在 Google 地圖上查看'
        },
        'about': {
            'About Us': '關於我們',
            'A Legacy of Precision': '精密與創新的傳承',
            'Company Profile': '公司簡介', 'Our Mission': '我們的使命', 'Our Vision': '我們的願景'
        },
        'solutions': {
            'Engineering Solutions': '工程解決方案',
            'Solving complex challenges': '以粉末冶金解決複雜挑戰',
            'Cost Reduction': '成本降低', 'Complex Geometries': '複雜幾何', 'Material Versatility': '材料多樣性'
        }
    },
    'de': {
        'name': 'Deutsch',
        'nav': {
            'Home': 'Startseite', 'Solutions': 'Lösungen', 'Applications': 'Anwendungen',
            'Emerging Tech': 'Neue Technologien', 'Capabilities': 'Fähigkeiten',
            'Products': 'Produkte', 'About': 'Über uns', 'Contact': 'Kontakt'
        },
        'hero': {
            'Precision in <br>Every Particle': 'Präzision in <br>jedem Partikel',
            'Over 40 years of excellence': 'Über 40 Jahre Exzellenz in der Pulvermetallurgie',
            'Explore Products': 'Produkte erkunden', 'Discuss Your Design': 'Design besprechen',
            '40+': '40+', 'Years Experience': 'Jahre Erfahrung',
            '±0.01mm': '±0.01mm', 'Precision Tolerance': 'Präzisionstoleranz',
            'ISO 9001': 'ISO 9001', 'Quality Certified': 'Qualitätszertifiziert',
            'Global': 'Global', 'Export Reach': 'Exportreichweite',
            '100%': '100%', 'Customization': 'Maßanfertigung',
            'Cost': 'Kosten', 'Effective': 'Effizient',
            'Automotive Excellence': 'Automobile Exzellenz',
            'Driving Future <br>Mobility': 'Antrieb der Zukunft <br>Mobilität',
            'High-precision rotors, gears, and structural parts for next-generation automotive and motorcycle applications.': 'Hochpräzise Rotoren, Zahnräder und Strukturteile für Automobil- und Motorradanwendungen der nächsten Generation.',
            'View Automotive Parts': 'Automobilteile ansehen',
            'Industrial Strength': 'Industrielle Stärke',
            'Powering <br>Performance': 'Leistung <br>Antreiben',
            'Robust gears and transmission components designed for high-torque power tools and industrial machinery.': 'Robuste Zahnräder und Getriebekomponenten für drehmomentstarke Elektrowerkzeuge und Industriemaschinen.',
            'View Power Tool Parts': 'Elektrowerkzeugteile ansehen'
        },
        'products': {
            'Our Products': 'Unsere Produkte',
            'Precision Powder Metallurgy Parts': 'Präzisions-Pulvermetallurgieteile für Ihre Bedürfnisse',
            'All Products': 'Alle Produkte', 'Precision Gears': 'Präzisionszahnräder',
            'Automotive & Motorcycle': 'Automobil & Motorrad', 'Industrial Parts': 'Industrieteile',
            'High Precision Applications': 'Hochpräzisionsanwendungen',
            'High-strength sintered gears': 'Hochfeste Sinterzahnräder für Getriebesysteme',
            'Biocompatible stainless steel parts': 'Biokompatible Edelstahlteile für medizinische Geräte',
            'Complex multi-part assemblies': 'Komplexe mehrteilige Baugruppen mit präziser Passung',
            'High-efficiency rotors': 'Hocheffiziente Rotoren für Automobil-Ölpumpen',
            'Small precision parts': 'Kleine Präzisionsteile für Computer und Elektronik',
            'Complex geometry parts': 'Teile mit komplexer Geometrie und hoher struktureller Integrität',
            'Precision stainless steel components': 'Präzisionskomponenten aus Edelstahl für die Chirurgie',
            'Durable gears and sprockets': 'Langlebige Zahnräder und Kettenräder für die Kraftübertragung'
        },
        'applications': {
            'Industry Applications': 'Industrieanwendungen',
            'Serving diverse sectors': 'Bedienung verschiedener Sektoren mit Hochleistungskomponenten',
            'Automotive & Motorcycle': 'Automobil & Motorrad', 'Mechanical Parts': 'Mechanische Teile',
            'Power Tool Parts': 'Elektrowerkzeugteile', 'Hardware & Electronics': 'Hardware & Elektronik',
            'Engine, transmission, and oil pump components.': 'Motor-, Getriebe- und Ölpumpenkomponenten.',
            'Industrial gears and hydraulic rotors.': 'Industriegetriebe und Hydraulikrotoren.',
            'High-torque gears for professional tools.': 'Hochdrehmomentgetriebe für Profiwerkzeuge.',
            'Precision lock parts and office machine components.': 'Präzisionsschlossteile und Büromaschinenkomponenten.',
            'Key Components': 'Schlüsselkomponenten'
        },
        'capabilities': {
            'Manufacturing Capabilities': 'Fertigungskapazitäten',
            'Advanced Powder Metallurgy Process': 'Fortschrittlicher PM-Prozess vom Design bis zur Serie',
            'Our Production Process': 'Unser Produktionsprozess',
            'Powder': 'Pulvermischen', 'Press': 'Pressen', 'Sintered': 'Sintern',
            'Sizing': 'Kalibrieren', 'Secondary Machining': 'Nachbearbeitung',
            'Precise blending': 'Präzises Mischen von Metallpulvern.',
            'Pressing powder': 'Pressen von Pulver zu Grünlingen.',
            'Bonding particles': 'Verbinden von Partikeln im Sinterofen.',
            'Re-pressing': 'Nachpressen für enge Toleranzen.',
            'Machining, heat treatment': 'Bearbeitung, Wärmebehandlung und Beschichtung.'
        },
        'emerging': {
            'Emerging Technologies': 'Neue Technologien',
            'Pioneering the future': 'Wegweisend für die Zukunft mit PM-Lösungen',
            'Electric Vehicles (EV)': 'Elektrofahrzeuge (EV)', 'Robotics & Automation': 'Robotik & Automation', 'Green Energy': 'Grüne Energie',
            'Developing soft magnetic composites': 'Entwicklung weichmagnetischer Verbundwerkstoffe (SMC).',
            'Precision micro-gears': 'Präzisions-Mikrozahnräder für Robotergelenke.',
            'Supporting the renewable energy': 'Unterstützung des Sektors für erneuerbare Energien.',
            'Innovations': 'Innovationen'
        },
        'contact': {
            'Contact Us': 'Kontaktieren Sie uns',
            'Get in touch': 'Kontaktieren Sie unser Ingenieurteam',
            'Headquarters & Factory': 'Hauptsitz & Fabrik', 'Phone': 'Telefon', 'Email': 'E-Mail',
            'Send us a Message': 'Senden Sie uns eine Nachricht', 'Name': 'Name', 'Subject': 'Betreff', 'Message': 'Nachricht',
            'Send Message': 'Nachricht senden',
            'View on Google Maps': 'Auf Google Maps ansehen'
        },
        'about': {
            'About Us': 'Über uns',
            'A Legacy of Precision': 'Ein Erbe der Präzision',
            'Company Profile': 'Firmenprofil', 'Our Mission': 'Unsere Mission', 'Our Vision': 'Unsere Vision'
        },
        'solutions': {
            'Engineering Solutions': 'Ingenieurlösungen',
            'Solving complex challenges': 'Lösung komplexer Herausforderungen',
            'Cost Reduction': 'Kostenreduzierung', 'Complex Geometries': 'Komplexe Geometrien', 'Material Versatility': 'Materialvielfalt'
        }
    },
    'jp': {
        'name': '日本語',
        'nav': {
            'Home': 'ホーム', 'Solutions': 'ソリューション', 'Applications': '応用分野',
            'Emerging Tech': '新技術', 'Capabilities': '製造能力',
            'Products': '製品紹介', 'About': '会社概要', 'Contact': 'お問い合わせ'
        },
        'hero': {
            'Precision in <br>Every Particle': '一粒一粒に<br>宿る精密さ',
            'Over 40 years of excellence': '粉末冶金における40年以上の卓越した経験',
            'Explore Products': '製品紹介', 'Discuss Your Design': '設計を相談する',
            '40+': '40+', 'Years Experience': '年の経験',
            '±0.01mm': '±0.01mm', 'Precision Tolerance': '精密公差',
            'ISO 9001': 'ISO 9001', 'Quality Certified': '品質認証',
            'Global': 'グローバル', 'Export Reach': '輸出範囲',
            '100%': '100%', 'Customization': 'カスタマイズ',
            'Cost': 'コスト', 'Effective': '効率的',
            'Automotive Excellence': '自動車部品の卓越性',
            'Driving Future <br>Mobility': '未来のモビリティを <br>駆動する',
            'High-precision rotors, gears, and structural parts for next-generation automotive and motorcycle applications.': '次世代の自動車およびオートバイ用途向けの超精密ローター、ギア、構造部品。',
            'View Automotive Parts': '自動車部品を見る',
            'Industrial Strength': '産業用強度',
            'Powering <br>Performance': 'パフォーマンスを <br>支える力',
            'Robust gears and transmission components designed for high-torque power tools and industrial machinery.': '高トルク電動工具および産業機械向けに設計された堅牢なギアとトランスミッション部品。',
            'View Power Tool Parts': '電動工具部品を見る'
        },
        'products': {
            'Our Products': '製品紹介',
            'Precision Powder Metallurgy Parts': '多様なニーズに応える精密粉末冶金部品',
            'All Products': '全製品', 'Precision Gears': '精密ギア',
            'Automotive & Motorcycle': '自動車・バイク', 'Industrial Parts': '工業用部品',
            'High Precision Applications': '高精密用途',
            'High-strength sintered gears': 'トランスミッションシステム用の高強度焼結ギア',
            'Biocompatible stainless steel parts': '医療機器用の生体適合性ステンレス鋼部品',
            'Complex multi-part assemblies': '精密な嵌合を持つ複雑な多部品アセンブリ',
            'High-efficiency rotors': '自動車用オイルポンプ用の高効率ローター',
            'Small precision parts': 'コンピュータおよび電子機器用の小型精密部品',
            'Complex geometry parts': '高い構造的完全性を持つ複雑な形状の部品',
            'Precision stainless steel components': '手術用の精密ステンレス鋼コンポーネント',
            'Durable gears and sprockets': '動力伝達用の耐久性のあるギアとスプロケット'
        },
        'applications': {
            'Industry Applications': '産業応用',
            'Serving diverse sectors': '高性能焼結部品で多様な分野に貢献',
            'Automotive & Motorcycle': '自動車・バイク', 'Mechanical Parts': '機械部品',
            'Power Tool Parts': '電動工具部品', 'Hardware & Electronics': 'ハードウェア・電子部品',
            'Engine, transmission, and oil pump components.': 'エンジン、トランスミッション、オイルポンプ部品。',
            'Industrial gears and hydraulic rotors.': '産業用ギアおよび油圧ローター。',
            'High-torque gears for professional tools.': 'プロ用工具向け高トルクギア。',
            'Precision lock parts and office machine components.': '精密ロック部品および事務機器部品。',
            'Key Components': '主要部品'
        },
        'capabilities': {
            'Manufacturing Capabilities': '製造能力',
            'Advanced Powder Metallurgy Process': '設計から量産までの先進的な粉末冶金プロセス',
            'Our Production Process': '生産プロセス',
            'Powder': '粉末混合', 'Press': '成形', 'Sintered': '焼結',
            'Sizing': 'サイジング', 'Secondary Machining': '二次加工',
            'Precise blending': '金属粉末と潤滑剤の精密な混合。',
            'Pressing powder': '高トン数プレスで粉末を圧粉体に成形。',
            'Bonding particles': '雰囲気制御炉での粒子結合。',
            'Re-pressing': '寸法公差と表面仕上げのための再圧縮。',
            'Machining, heat treatment': '機械加工、熱処理、表面メッキ。'
        },
        'emerging': {
            'Emerging Technologies': '新技術',
            'Pioneering the future': '先進的な粉末冶金ソリューションで未来を拓く',
            'Electric Vehicles (EV)': '電気自動車 (EV)', 'Robotics & Automation': 'ロボット工学', 'Green Energy': 'グリーンエネルギー',
            'Developing soft magnetic composites': '高効率モーター用の軟磁性複合材料 (SMC) の開発。',
            'Precision micro-gears': 'ロボット関節および産業用アーム用の精密マイクロギア。',
            'Supporting the renewable energy': '耐久性のある部品で再生可能エネルギー分野を支援。',
            'Innovations': '革新技術'
        },
        'contact': {
            'Contact Us': 'お問い合わせ',
            'Get in touch': '次のプロジェクトについて技術チームにご相談ください',
            'Headquarters & Factory': '本社・工場', 'Phone': '電話', 'Email': 'メール',
            'Send us a Message': 'メッセージを送信', 'Name': 'お名前', 'Subject': '件名', 'Message': 'メッセージ',
            'Send Message': '送信する',
            'View on Google Maps': 'Googleマップで見る'
        },
        'about': {
            'About Us': '会社概要',
            'A Legacy of Precision': '精密と革新の伝統',
            'Company Profile': '会社案内', 'Our Mission': 'ミッション', 'Our Vision': 'ビジョン'
        },
        'solutions': {
            'Engineering Solutions': 'ソリューション',
            'Solving complex challenges': '複雑な課題を解決する',
            'Cost Reduction': 'コスト削減', 'Complex Geometries': '複雑な形状', 'Material Versatility': '材料の多様性'
        }
    }
}

def update_language(lang_code, config):
    base_dir = '/home/ubuntu/pure_html'
    target_dir = os.path.join(base_dir, lang_code)
    
    # Create directory if not exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
    # Copy all HTML files
    for filename in os.listdir(base_dir):
        if filename.endswith('.html'):
            src_path = os.path.join(base_dir, filename)
            dest_path = os.path.join(target_dir, filename)
            
            with open(src_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            soup = BeautifulSoup(content, 'html.parser')
            
            # 1. Fix relative paths for assets
            for tag in soup.find_all(['link', 'script', 'img', 'a']):
                if tag.has_attr('href'):
                    if tag['href'].startswith('assets/'): tag['href'] = '../' + tag['href']
                    if tag['href'].startswith('zh/'): tag['href'] = '../' + tag['href']
                    if tag['href'].startswith('de/'): tag['href'] = '../' + tag['href']
                    if tag['href'].startswith('jp/'): tag['href'] = '../' + tag['href']
                    if tag['href'] == 'index.html': tag['href'] = 'index.html'
                if tag.has_attr('src'):
                    if tag['src'].startswith('images/'): tag['src'] = '../' + tag['src']
                    if tag['src'].startswith('assets/'): tag['src'] = '../' + tag['src']

            # Update Navbar for Mobile (Full Name) and Colors
            navbar_content = soup.find('nav')
            if navbar_content:
                # Force navbar background to white and text to dark
                navbar_content['class'] = 'bg-white text-gray-900 sticky top-0 z-50 shadow-md border-b border-gray-100'

                # Update mobile menu button color
                mobile_btn = navbar_content.find('button', id='mobile-menu-btn')
                if mobile_btn:
                    mobile_btn['class'] = 'md:hidden text-gray-900 focus:outline-none p-2'

                # Try to find the container with either the old or new class
                logo_container = navbar_content.find('div', class_='flex items-center space-x-4')
                if not logo_container:
                    logo_container = navbar_content.find('div', class_='flex items-center space-x-3 md:space-x-4')
                
                if logo_container:
                    # Update container classes
                    logo_container['class'] = 'flex items-center space-x-3 md:space-x-4'
                    
                    # Clear existing content
                    logo_container.clear()
                    
                    # Rebuild with new structure
                    img_tag = soup.new_tag('img', src='../images/logo.png', alt='Yeh Sheng Logo')
                    img_tag['class'] = 'h-8 md:h-10'
                    logo_container.append(img_tag)
                    
                    span_full = soup.new_tag('span', attrs={'class': 'text-sm md:text-xl font-serif font-bold tracking-wide leading-tight text-gray-900'})
                    span_full.string = 'Yeh Sheng Powder Parts Ind. Co. Ltd.'
                    logo_container.append(span_full)
                
                # Update desktop menu link colors
                desktop_menu = navbar_content.find('div', class_='hidden md:flex')
                if desktop_menu:
                    links = desktop_menu.find_all('a')
                    for link in links:
                        if 'bg-primary' not in link.get('class', []):
                            # Reset classes to ensure correct color
                            if link.get('href') == filename.split('/')[-1] or (filename.endswith('index.html') and link.get('href') == 'index.html'):
                                link['class'] = 'text-primary hover:text-yellow-600 transition'
                            else:
                                link['class'] = 'text-gray-700 hover:text-primary transition'

            # Update Page Headers to Light Theme
            header_tag = soup.find('header')
            if header_tag:
                # Force light theme for all headers
                header_tag['class'] = 'bg-white text-gray-900 py-20 relative overflow-hidden border-b border-gray-100'
                # Remove background image overlay if present
                overlay = header_tag.find('div', class_='absolute inset-0 opacity-20')
                if overlay:
                    overlay.decompose()
                # Update text colors in header
                h1_tag = header_tag.find('h1')
                if h1_tag:
                    h1_tag['class'] = [c for c in h1_tag.get('class', []) if c != 'text-white'] + ['text-gray-900']
                p_tag = header_tag.find('p')
                if p_tag:
                    p_tag['class'] = [c for c in p_tag.get('class', []) if c != 'text-gray-300'] + ['text-gray-600']

            # 2. Fix Language Switcher
            lang_btn = soup.find('button', string=re.compile('EN'))
            if lang_btn:
                lang_btn.string = config['name'][:2].upper()
            
            # 3. Translate Content
            # Convert soup back to string for text replacement (simpler for bulk text)
            html_str = str(soup)
            
            # Apply translations
            for section, translations in config.items():
                if isinstance(translations, dict):
                    for en_text, trans_text in translations.items():
                        html_str = html_str.replace(en_text, trans_text)
            
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(html_str)
            print(f"Updated {dest_path}")

# Run update
for lang, conf in LANGUAGES.items():
    update_language(lang, conf)
