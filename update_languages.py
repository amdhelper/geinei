import os
import re
from bs4 import BeautifulSoup

# Define base directory
BASE_DIR = '/home/ubuntu/pure_html'
LANGUAGES = ['zh', 'de', 'jp']

# Translation dictionary
TRANSLATIONS = {
    'zh': {
        # Navigation
        'Home': '首頁',
        'Solutions': '解決方案',
        'Applications': '應用領域',
        'Industries': '應用領域',
        'Emerging Tech': '新興技術',
        'Innovation': '創新技術',
        'Capabilities': '製程能力',
        'Products': '產品介紹',
        'About': '關於我們',
        'About Us': '關於我們',
        'Contact': '聯絡我們',
        'Contact Us': '聯絡我們',
        'Language': '語言',
        
        # Common
        'Yeh Sheng Powder Parts Ind. Co. Ltd.': 'Yeh Sheng Powder Parts Ind. Co. Ltd.',
        'Yeh Sheng': '治聖工業',
        'All rights reserved.': '版權所有',
        'No. 11, Ln. 721, Zhong Zheng Rd., Xin Zhuang Dist., New Taipei City, 24265, Taiwan': '24265 新北市新莊區中正路721巷11號',
        'No. 11, Ln. 721, Zhong Zheng Rd.': '新北市新莊區中正路721巷11號',
        'Xin Zhuang Dist., New Taipei City': '',
        'Taiwan 24265': '',
        'Phone': '電話',
        'Mobile': '手機',
        'Email': '電子郵件',
        'Company': '公司資訊',
        'Premier manufacturer of high-precision powder metallurgy components since 1980.': '自1980年以來的高精密粉末冶金組件領導製造商。',
        
        # Homepage Hero (New GKN Style)
        'ISO 9001:2015 Certified': 'ISO 9001:2015 認證',
        'Precision in': '精確至',
        'Every Particle': '每一微粒',
        'Precision in Every Particle': '精確至每一微粒',
        'Engineering high-performance sintered components with micron-level precision for the automotive and industrial future.': '為汽車與工業的未來，打造微米級精度的工程高性能燒結組件。',
        'Explore Products': '探索產品',
        'Contact Engineering': '聯絡工程團隊',
        
        # Homepage Stats
        'Years Experience': '年豐富經驗',
        'Tolerance': '精密公差',
        '9001 Certified': '9001 認證',
        'Export Reach': '出口範圍',
        
        # Key Industries Section
        'Our Expertise': '專業領域',
        'Key Industries': '關鍵產業',
        'View All Industries': '查看所有產業',
        'Automotive': '汽機車產業',
        'High-precision rotors and structural parts for next-gen mobility.': '用於下一代移動科技的高精密轉子與結構零件。',
        'Industrial': '工業機械',
        'Robust gears and transmission components for heavy-duty machinery.': '用於重型機械的堅固齒輪與傳動組件。',
        'Medical': '醫療器材',
        'Biocompatible stainless steel parts for surgical and diagnostic devices.': '用於手術與診斷設備的生物相容性不鏽鋼零件。',
        'Learn more': '了解更多',
        
        # Technology Section
        'Pioneering the Future of Metallurgy': '開創粉末冶金的未來',
        'From Soft Magnetic Composites (SMC) for EVs to high-precision micro-gears for robotics, we are pushing the boundaries of what\'s possible with sintered metal.': '從電動車用的軟磁複合材料 (SMC) 到機器人用的高精密微型齒輪，我們正在拓展燒結金屬的無限可能。',
        'Discover Technologies': '探索創新技術',
        
        # Other Pages (Keep existing translations)
        'Precision Powder Metallurgy Parts for Your Diverse Needs': '滿足您多樣化需求的精密粉末冶金零件',
        'Yesheng Powder Metallurgy has over 40 years of precision manufacturing experience...': '治聖工業擁有超過40年的精密製造經驗...',
        'All Products': '所有產品',
        'Precision Gears': '精密齒輪',
        'Automotive & Motorcycle': '汽機車零件',
        'Industrial Parts': '工業零件',
        'Industrial Components': '工業組件',
        'High Precision Applications': '高精密應用',
        'High-strength sintered gears for transmission systems': '用於傳動系統的高強度燒結齒輪',
        'Medical Components': '醫療器材零件',
        'Biocompatible stainless steel parts for medical devices': '用於醫療設備的生物相容性不鏽鋼零件',
        'Gear Assemblies': '齒輪組件',
        'Complex multi-part assemblies with precise fit': '精密配合的複雜多零件組件',
        'Oil Pump Rotors': '油泵轉子',
        'High-efficiency rotors for automotive oil pumps': '用於汽車油泵的高效率轉子',
        'Computer Parts': '電腦零件',
        'Small precision parts for computer and electronics': '用於電腦和電子產品的小型精密零件',
        'Complex Shapes': '複雜形狀零件',
        'Complex geometry parts with high structural integrity': '具有高結構完整性的複雜幾何形狀零件',
        'Surgical Components': '手術器械零件',
        'Precision stainless steel components for surgery': '用於手術的精密不鏽鋼組件',
        'Power Transmission': '動力傳輸零件',
        'Durable gears and sprockets for power transmission': '用於動力傳輸的耐用齒輪和鏈輪',
        'Engineering Solutions': '工程解決方案',
        'Solving complex challenges with powder metallurgy': '利用粉末冶金技術解決複雜挑戰',
        'Cost Reduction': '成本降低',
        'Complex Geometries': '複雜幾何形狀',
        'Material Versatility': '材料多樣性',
        'Industry Applications': '產業應用',
        'Serving diverse sectors with high-performance sintered components': '以高性能燒結組件服務多元產業',
        'Automotive & Motorcycle Parts': '汽機車零件',
        'Key Components': '關鍵組件',
        'Mechanical Parts': '機械零件',
        'Power Tool Parts': '電動工具零件',
        'Hardware & Electronics': '五金與電子',
        'Emerging Technologies': '新興技術',
        'Pioneering the future with advanced powder metallurgy solutions': '以先進粉末冶金解決方案開創未來',
        'Electric Vehicles (EV)': '電動車 (EV)',
        'Innovations': '創新技術',
        'Robotics & Automation': '機器人與自動化',
        'Green Energy': '綠色能源',
        'Manufacturing Capabilities': '製程能力',
        'State-of-the-art facilities ensuring precision and quality': '確保精密與品質的最先進設施',
        'Compacting': '成型',
        'Sintering': '燒結',
        'Secondary Operations': '二次加工',
        'Quality Control': '品質控制',
        'A Legacy of Precision and Innovation': '傳承精密與創新的卓越工藝',
        'Company Profile': '公司簡介',
        'Our Mission': '我們的使命',
        'Our Vision': '我們的願景',
        'Get in touch with our team for inquiries and support': '與我們的團隊聯繫以獲取諮詢和支援',
        'Send us a Message': '發送訊息',
        'Name': '姓名',
        'Email Address': '電子郵件地址',
        'Subject': '主旨',
        'Message': '訊息',
        'Send Message': '發送訊息',
        'Contact Information': '聯絡資訊',
        'Address': '地址',
        'Business Hours': '營業時間',
        'Monday - Friday: 8:00 AM - 5:00 PM': '週一至週五：上午 8:00 - 下午 5:00',
    },
    'de': {
        # Navigation
        'Home': 'Startseite',
        'Solutions': 'Lösungen',
        'Applications': 'Anwendungen',
        'Industries': 'Branchen',
        'Emerging Tech': 'Neue Technologien',
        'Innovation': 'Innovation',
        'Capabilities': 'Fertigung',
        'Products': 'Produkte',
        'About': 'Über uns',
        'About Us': 'Über uns',
        'Contact': 'Kontakt',
        'Contact Us': 'Kontakt',
        'Language': 'Sprache',
        
        # Common
        'Yeh Sheng Powder Parts Ind. Co. Ltd.': 'Yeh Sheng Powder Parts Ind. Co. Ltd.',
        'Yeh Sheng': 'Yeh Sheng',
        'All rights reserved.': 'Alle Rechte vorbehalten.',
        'No. 11, Ln. 721, Zhong Zheng Rd., Xin Zhuang Dist., New Taipei City, 24265, Taiwan': 'No. 11, Ln. 721, Zhong Zheng Rd., Xin Zhuang Dist., New Taipei City, 24265, Taiwan',
        'No. 11, Ln. 721, Zhong Zheng Rd.': 'No. 11, Ln. 721, Zhong Zheng Rd.',
        'Xin Zhuang Dist., New Taipei City': 'Xin Zhuang Dist., New Taipei City',
        'Taiwan 24265': 'Taiwan 24265',
        'Phone': 'Telefon',
        'Mobile': 'Mobil',
        'Email': 'E-Mail',
        'Company': 'Unternehmen',
        'Premier manufacturer of high-precision powder metallurgy components since 1980.': 'Führender Hersteller von hochpräzisen pulvermetallurgischen Komponenten seit 1980.',
        
        # Homepage Hero (New GKN Style)
        'ISO 9001:2015 Certified': 'ISO 9001:2015 Zertifiziert',
        'Precision in': 'Präzision in',
        'Every Particle': 'jedem Partikel',
        'Precision in Every Particle': 'Präzision in jedem Partikel',
        'Engineering high-performance sintered components with micron-level precision for the automotive and industrial future.': 'Entwicklung von Hochleistungs-Sinterkomponenten mit mikrometergenauer Präzision für die Zukunft der Automobil- und Industriebranche.',
        'Explore Products': 'Produkte entdecken',
        'Contact Engineering': 'Ingenieurteam kontaktieren',
        
        # Homepage Stats
        'Years Experience': 'Jahre Erfahrung',
        'Tolerance': 'Präzisionstoleranz',
        '9001 Certified': '9001 Zertifiziert',
        'Export Reach': 'Exportreichweite',
        
        # Key Industries Section
        'Our Expertise': 'Unsere Expertise',
        'Key Industries': 'Schlüsselbranchen',
        'View All Industries': 'Alle Branchen ansehen',
        'Automotive': 'Automobilindustrie',
        'High-precision rotors and structural parts for next-gen mobility.': 'Hochpräzise Rotoren und Strukturteile für die Mobilität der nächsten Generation.',
        'Industrial': 'Industrie',
        'Robust gears and transmission components for heavy-duty machinery.': 'Robuste Zahnräder und Getriebekomponenten für Schwermaschinen.',
        'Medical': 'Medizintechnik',
        'Biocompatible stainless steel parts for surgical and diagnostic devices.': 'Biokompatible Edelstahlteile für chirurgische und diagnostische Geräte.',
        'Learn more': 'Mehr erfahren',
        
        # Technology Section
        'Pioneering the Future of Metallurgy': 'Wegbereiter für die Zukunft der Metallurgie',
        'From Soft Magnetic Composites (SMC) for EVs to high-precision micro-gears for robotics, we are pushing the boundaries of what\'s possible with sintered metal.': 'Von weichmagnetischen Verbundwerkstoffen (SMC) für Elektrofahrzeuge bis hin zu hochpräzisen Mikrozahnrädern für die Robotik – wir erweitern die Grenzen des Machbaren mit Sintermetall.',
        'Discover Technologies': 'Technologien entdecken',
        
        # Other Pages
        'Precision Powder Metallurgy Parts for Your Diverse Needs': 'Präzisions-Pulvermetallurgieteile für Ihre vielfältigen Anforderungen',
        'All Products': 'Alle Produkte',
        'Precision Gears': 'Präzisionszahnräder',
        'Automotive & Motorcycle': 'Automobil & Motorrad',
        'Industrial Parts': 'Industrieteile',
        'Industrial Components': 'Industriekomponenten',
        'High Precision Applications': 'Hochpräzisionsanwendungen',
        'High-strength sintered gears for transmission systems': 'Hochfeste Sinterzahnräder für Getriebesysteme',
        'Medical Components': 'Medizinische Komponenten',
        'Biocompatible stainless steel parts for medical devices': 'Biokompatible Edelstahlteile für medizinische Geräte',
        'Gear Assemblies': 'Getriebebaugruppen',
        'Complex multi-part assemblies with precise fit': 'Komplexe mehrteilige Baugruppen mit präziser Passung',
        'Oil Pump Rotors': 'Ölpumpenrotoren',
        'High-efficiency rotors for automotive oil pumps': 'Hocheffiziente Rotoren für Automobil-Ölpumpen',
        'Computer Parts': 'Computerteile',
        'Small precision parts for computer and electronics': 'Kleine Präzisionsteile für Computer und Elektronik',
        'Complex Shapes': 'Komplexe Formen',
        'Complex geometry parts with high structural integrity': 'Teile mit komplexer Geometrie und hoher struktureller Integrität',
        'Surgical Components': 'Chirurgische Komponenten',
        'Precision stainless steel components for surgery': 'Präzisions-Edelstahlkomponenten für die Chirurgie',
        'Power Transmission': 'Kraftübertragung',
        'Durable gears and sprockets for power transmission': 'Langlebige Zahnräder und Kettenräder für die Kraftübertragung',
        'Engineering Solutions': 'Ingenieurlösungen',
        'Solving complex challenges with powder metallurgy': 'Lösung komplexer Herausforderungen mit Pulvermetallurgie',
        'Cost Reduction': 'Kostenreduzierung',
        'Complex Geometries': 'Komplexe Geometrien',
        'Material Versatility': 'Materialvielfalt',
        'Industry Applications': 'Branchenanwendungen',
        'Serving diverse sectors with high-performance sintered components': 'Bedienung verschiedener Sektoren mit leistungsstarken Sinterkomponenten',
        'Automotive & Motorcycle Parts': 'Automobil- & Motorradteile',
        'Key Components': 'Schlüsselkomponenten',
        'Mechanical Parts': 'Mechanische Teile',
        'Power Tool Parts': 'Elektrowerkzeugteile',
        'Hardware & Electronics': 'Hardware & Elektronik',
        'Emerging Technologies': 'Neue Technologien',
        'Pioneering the future with advanced powder metallurgy solutions': 'Wegweisend für die Zukunft mit fortschrittlichen pulvermetallurgischen Lösungen',
        'Electric Vehicles (EV)': 'Elektrofahrzeuge (EV)',
        'Innovations': 'Innovationen',
        'Robotics & Automation': 'Robotik & Automatisierung',
        'Green Energy': 'Grüne Energie',
        'Manufacturing Capabilities': 'Fertigungskapazitäten',
        'State-of-the-art facilities ensuring precision and quality': 'Modernste Anlagen für Präzision und Qualität',
        'Compacting': 'Pressen',
        'Sintering': 'Sintern',
        'Secondary Operations': 'Sekundärbearbeitung',
        'Quality Control': 'Qualitätskontrolle',
        'A Legacy of Precision and Innovation': 'Ein Erbe an Präzision und Innovation',
        'Company Profile': 'Unternehmensprofil',
        'Our Mission': 'Unsere Mission',
        'Our Vision': 'Unsere Vision',
        'Get in touch with our team for inquiries and support': 'Kontaktieren Sie unser Team für Anfragen und Unterstützung',
        'Send us a Message': 'Senden Sie uns eine Nachricht',
        'Name': 'Name',
        'Email Address': 'E-Mail-Adresse',
        'Subject': 'Betreff',
        'Message': 'Nachricht',
        'Send Message': 'Nachricht senden',
        'Contact Information': 'Kontaktinformationen',
        'Address': 'Adresse',
        'Business Hours': 'Geschäftszeiten',
        'Monday - Friday: 8:00 AM - 5:00 PM': 'Montag - Freitag: 8:00 - 17:00 Uhr',
    },
    'jp': {
        # Navigation
        'Home': 'ホーム',
        'Solutions': 'ソリューション',
        'Applications': '応用分野',
        'Industries': '産業分野',
        'Emerging Tech': '新技術',
        'Innovation': 'イノベーション',
        'Capabilities': '製造能力',
        'Products': '製品紹介',
        'About': '会社概要',
        'About Us': '会社概要',
        'Contact': 'お問い合わせ',
        'Contact Us': 'お問い合わせ',
        'Language': '言語',
        
        # Common
        'Yeh Sheng Powder Parts Ind. Co. Ltd.': 'Yeh Sheng Powder Parts Ind. Co. Ltd.',
        'Yeh Sheng': 'Yeh Sheng',
        'All rights reserved.': '無断転載を禁じます。',
        'No. 11, Ln. 721, Zhong Zheng Rd., Xin Zhuang Dist., New Taipei City, 24265, Taiwan': '24265 台湾新北市新荘区中正路721巷11号',
        'No. 11, Ln. 721, Zhong Zheng Rd.': '新北市新荘区中正路721巷11号',
        'Xin Zhuang Dist., New Taipei City': '',
        'Taiwan 24265': '',
        'Phone': '電話',
        'Mobile': '携帯',
        'Email': 'メール',
        'Company': '会社情報',
        'Premier manufacturer of high-precision powder metallurgy components since 1980.': '1980年創業、高精度粉末冶金部品の主要メーカー。',
        
        # Homepage Hero (New GKN Style)
        'ISO 9001:2015 Certified': 'ISO 9001:2015 認証',
        'Precision in': '一粒一粒に',
        'Every Particle': '宿る精密さ',
        'Precision in Every Particle': '一粒一粒に宿る精密さ',
        'Engineering high-performance sintered components with micron-level precision for the automotive and industrial future.': '自動車および産業の未来のために、ミクロンレベルの精度を持つ高性能焼結部品を設計・製造します。',
        'Explore Products': '製品を見る',
        'Contact Engineering': '技術チームに連絡',
        
        # Homepage Stats
        'Years Experience': '年の経験',
        'Tolerance': '精密公差',
        '9001 Certified': '9001 認証',
        'Export Reach': '輸出実績',
        
        # Key Industries Section
        'Our Expertise': '当社の専門分野',
        'Key Industries': '主要産業',
        'View All Industries': 'すべての産業を見る',
        'Automotive': '自動車産業',
        'High-precision rotors and structural parts for next-gen mobility.': '次世代モビリティ向けの高精度ローターおよび構造部品。',
        'Industrial': '産業機械',
        'Robust gears and transmission components for heavy-duty machinery.': '重機向けの堅牢なギアおよびトランスミッション部品。',
        'Medical': '医療機器',
        'Biocompatible stainless steel parts for surgical and diagnostic devices.': '手術および診断機器向けの生体適合性ステンレス鋼部品。',
        'Learn more': '詳細を見る',
        
        # Technology Section
        'Pioneering the Future of Metallurgy': '粉末冶金の未来を切り拓く',
        'From Soft Magnetic Composites (SMC) for EVs to high-precision micro-gears for robotics, we are pushing the boundaries of what\'s possible with sintered metal.': 'EV用軟磁性複合材料 (SMC) からロボット用高精度マイクロギアまで、焼結金属の可能性を広げています。',
        'Discover Technologies': '技術を見る',
        
        # Other Pages
        'Precision Powder Metallurgy Parts for Your Diverse Needs': '多様なニーズに応える精密粉末冶金部品',
        'All Products': 'すべての製品',
        'Precision Gears': '精密ギア',
        'Automotive & Motorcycle': '自動車・バイク',
        'Industrial Parts': '産業用部品',
        'Industrial Components': '産業用コンポーネント',
        'High Precision Applications': '高精度用途',
        'High-strength sintered gears for transmission systems': 'トランスミッションシステム用の高強度焼結ギア',
        'Medical Components': '医療用部品',
        'Biocompatible stainless steel parts for medical devices': '医療機器用の生体適合性ステンレス鋼部品',
        'Gear Assemblies': 'ギアアセンブリ',
        'Complex multi-part assemblies with precise fit': '精密な嵌合を持つ複雑な多部品アセンブリ',
        'Oil Pump Rotors': 'オイルポンプローター',
        'High-efficiency rotors for automotive oil pumps': '自動車用オイルポンプ用の高効率ローター',
        'Computer Parts': 'コンピュータ部品',
        'Small precision parts for computer and electronics': 'コンピュータおよび電子機器用の小型精密部品',
        'Complex Shapes': '複雑形状部品',
        'Complex geometry parts with high structural integrity': '高い構造的完全性を持つ複雑な幾何学的形状の部品',
        'Surgical Components': '手術用部品',
        'Precision stainless steel components for surgery': '手術用の精密ステンレス鋼コンポーネント',
        'Power Transmission': '動力伝達部品',
        'Durable gears and sprockets for power transmission': '動力伝達用の耐久性のあるギアとスプロケット',
        'Engineering Solutions': 'エンジニアリングソリューション',
        'Solving complex challenges with powder metallurgy': '粉末冶金で複雑な課題を解決',
        'Cost Reduction': 'コスト削減',
        'Complex Geometries': '複雑な幾何学形状',
        'Material Versatility': '材料の多様性',
        'Industry Applications': '産業用途',
        'Serving diverse sectors with high-performance sintered components': '高性能焼結部品で多様な分野に貢献',
        'Automotive & Motorcycle Parts': '自動車・バイク部品',
        'Key Components': '主要部品',
        'Mechanical Parts': '機械部品',
        'Power Tool Parts': '電動工具部品',
        'Hardware & Electronics': 'ハードウェア・電子機器',
        'Emerging Technologies': '新技術',
        'Pioneering the future with advanced powder metallurgy solutions': '先進的な粉末冶金ソリューションで未来を切り拓く',
        'Electric Vehicles (EV)': '電気自動車 (EV)',
        'Innovations': 'イノベーション',
        'Robotics & Automation': 'ロボット工学・自動化',
        'Green Energy': 'グリーンエネルギー',
        'Manufacturing Capabilities': '製造能力',
        'State-of-the-art facilities ensuring precision and quality': '精度と品質を保証する最先端の設備',
        'Compacting': '成形',
        'Sintering': '焼結',
        'Secondary Operations': '二次加工',
        'Quality Control': '品質管理',
        'A Legacy of Precision and Innovation': '精密さと革新の伝統',
        'Company Profile': '会社概要',
        'Our Mission': 'ミッション',
        'Our Vision': 'ビジョン',
        'Get in touch with our team for inquiries and support': 'お問い合わせやサポートについては、当社のチームにご連絡ください',
        'Send us a Message': 'メッセージを送信',
        'Name': 'お名前',
        'Email Address': 'メールアドレス',
        'Subject': '件名',
        'Message': 'メッセージ',
        'Send Message': 'メッセージを送信',
        'Contact Information': '連絡先情報',
        'Address': '住所',
        'Business Hours': '営業時間',
        'Monday - Friday: 8:00 AM - 5:00 PM': '月曜日 - 金曜日: 午前 8:00 - 午後 5:00',
    }
}

def update_language_pages():
    # Get list of all HTML files in base directory
    html_files = [f for f in os.listdir(BASE_DIR) if f.endswith('.html')]
    
    for lang in LANGUAGES:
        lang_dir = os.path.join(BASE_DIR, lang)
        os.makedirs(lang_dir, exist_ok=True)
        
        for filename in html_files:
            file_path = os.path.join(BASE_DIR, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # 1. Update Language Attribute
            soup.html['lang'] = lang
            
            # 2. Fix Resource Paths (CSS, JS, Images)
            # Since we are moving files to a subdirectory (e.g., /zh/), we need to prepend '../' to assets
            # But NOT to links to other HTML files (which are also in /zh/)
            
            # Fix CSS links
            for link in soup.find_all('link'):
                href = link.get('href')
                if href and not href.startswith(('http', '//', 'mailto:', '#', '../')):
                    link['href'] = '../' + href
            
            # Fix JS scripts
            for script in soup.find_all('script'):
                src = script.get('src')
                if src and not src.startswith(('http', '//', 'mailto:', '#', '../')):
                    script['src'] = '../' + src
            
            # Fix Images
            for img in soup.find_all('img'):
                src = img.get('src')
                if src and not src.startswith(('http', '//', 'mailto:', '#', '../')):
                    img['src'] = '../' + src
            
            # Fix Inline Styles with background-image
            for tag in soup.find_all(True):
                if tag.has_attr('style'):
                    style = tag['style']
                    if 'url(' in style and 'http' not in style:
                        tag['style'] = re.sub(r"url\(['\"]?(?!http|//|data:|\.\.)([^'\")]+)['\"]?\)", r"url('../\1')", style)

            # Also fix <style> blocks in head
            for style_tag in soup.find_all('style'):
                if style_tag.string:
                    style_tag.string = re.sub(r"url\(['\"]?(?!http|//|data:|\.\.)([^'\")]+)['\"]?\)", r"url('../\1')", style_tag.string)

            # 3. Update Language Switcher
            dropdown_div = soup.find('div', class_=re.compile(r'absolute.*group-hover:visible'))
            
            if dropdown_div:
                dropdown_div.clear()
                all_langs = [
                    {'code': 'en', 'name': 'English', 'path': '../' + filename},
                    {'code': 'zh', 'name': '中文', 'path': filename},
                    {'code': 'de', 'name': 'Deutsch', 'path': filename},
                    {'code': 'jp', 'name': '日本語', 'path': filename}
                ]
                
                for l in all_langs:
                    if l['code'] != lang:
                        target_href = ''
                        if l['code'] == 'en':
                            target_href = '../' + filename
                        else:
                            target_href = '../' + l['code'] + '/' + filename
                            
                        new_link = soup.new_tag('a', href=target_href, class_='block px-4 py-2 hover:bg-gray-100')
                        new_link.string = l['name']
                        dropdown_div.append(new_link)
                
                button = dropdown_div.find_previous_sibling('button')
                if button:
                    for child in button.children:
                        if child.name is None and child.string.strip():
                            display_name = {'zh': '中文', 'de': 'Deutsch', 'jp': '日本語'}.get(lang, lang.upper())
                            child.replace_with(f' {display_name} ')
                            break

            # 4. Translate Content
            def normalize_text(text):
                return ' '.join(text.split())

            def translate_text(text):
                normalized = normalize_text(text)
                if normalized in TRANSLATIONS[lang]:
                    return TRANSLATIONS[lang][normalized]
                return text

            for text_node in soup.find_all(string=True):
                if text_node.parent.name in ['script', 'style']:
                    continue
                
                # Skip if empty
                if not text_node.strip():
                    continue
                    
                new_text = translate_text(text_node)
                if new_text != text_node:
                    text_node.replace_with(new_text)
            
            for tag in soup.find_all(True):
                if tag.has_attr('placeholder'):
                    tag['placeholder'] = translate_text(tag['placeholder'])
                if tag.has_attr('alt'):
                    if 'Logo' not in tag['alt']:
                        tag['alt'] = translate_text(tag['alt'])

            # 5. Fix Homepage Layout (Index only)
            if filename == 'index.html':
                pass
            else:
                header = soup.find('header')
                if header:
                    if 'bg-secondary' in header.get('class', []):
                        header['class'] = [c for c in header['class'] if c not in ['bg-secondary', 'text-white']]
                        header['class'].append('bg-white')
                        header['class'].append('text-gray-900')
                        
                        p_tag = header.find('p')
                        if p_tag and 'text-gray-300' in p_tag.get('class', []):
                            p_tag['class'] = [c for c in p_tag['class'] if c != 'text-gray-300']
                            p_tag['class'].append('text-gray-600')
                            
                        overlay = header.find('div', class_=re.compile('absolute inset-0 opacity-20'))
                        if overlay:
                            overlay.decompose()

            output_path = os.path.join(lang_dir, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            
            print(f'Updated {output_path}')

if __name__ == '__main__':
    update_language_pages()
