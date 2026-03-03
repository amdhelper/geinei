"""Add Self-Lubricating Bearings and Sintering Process articles to English resources.html"""
import re

BEARINGS_HTML = '''
                    <!-- Self-Lubricating Bearings Guide -->
                    <div id="bearings-guide" style="margin-bottom: 80px;">
                        <h3 style="font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 700; color: #333; margin-bottom: 15px; border-bottom: 2px solid #eee; padding-bottom: 10px;">
                            🔩 Self-Lubricating Bearings Guide
                        </h3>
                        <p style="font-size: 16px; color: #555; line-height: 1.7; margin-bottom: 25px;">
                            Oil-impregnated bearings are one of the most successful applications of Powder Metallurgy. Their unique porous structure allows them to store and release lubricant automatically, making them ideal for maintenance-free applications.
                        </p>

                        <h4 style="font-size: 22px; font-weight: 600; color: #002FA7; margin-bottom: 15px; padding-left: 15px; border-left: 4px solid #C5A059;">
                            How Self-Lubricating Bearings Work
                        </h4>
                        <div style="background: linear-gradient(135deg, #f0f4ff 0%, #e8f4fd 100%); border: 2px solid #C5A059; border-radius: 12px; padding: 25px; margin-bottom: 25px;">
                            <p style="font-size: 15px; line-height: 1.8; color: #333; margin: 0 0 15px 0;">
                                PM bearings are manufactured with <strong>controlled porosity (15-25% by volume)</strong>. After sintering, they are vacuum-impregnated with lubricating oil. During operation:
                            </p>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
                                <div style="background: white; padding: 15px; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 32px; margin-bottom: 8px;">🔄</div>
                                    <strong style="font-size: 14px; color: #002FA7;">1. Heat Expansion</strong>
                                    <p style="font-size: 13px; color: #666; margin: 5px 0 0;">Friction heats the bearing → oil expands and seeps to the surface</p>
                                </div>
                                <div style="background: white; padding: 15px; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 32px; margin-bottom: 8px;">💧</div>
                                    <strong style="font-size: 14px; color: #002FA7;">2. Lubrication</strong>
                                    <p style="font-size: 13px; color: #666; margin: 5px 0 0;">Oil film forms between bearing and shaft → reduces friction</p>
                                </div>
                                <div style="background: white; padding: 15px; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 32px; margin-bottom: 8px;">🧲</div>
                                    <strong style="font-size: 14px; color: #002FA7;">3. Re-absorption</strong>
                                    <p style="font-size: 13px; color: #666; margin: 5px 0 0;">When stopped, capillary action draws oil back into the pores</p>
                                </div>
                            </div>
                        </div>

                        <h4 style="font-size: 22px; font-weight: 600; color: #002FA7; margin-bottom: 15px; padding-left: 15px; border-left: 4px solid #C5A059;">
                            Bearing Type Comparison
                        </h4>
                        <table class="process-table">
                            <thead>
                                <tr>
                                    <th>Factor</th>
                                    <th>PM Oil-Impregnated</th>
                                    <th>Ball Bearing</th>
                                    <th>Plain Sleeve</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><strong>Maintenance</strong></td>
                                    <td class="highlight-pm">Maintenance-free</td>
                                    <td>Periodic lubrication</td>
                                    <td>Requires lubrication</td>
                                </tr>
                                <tr>
                                    <td><strong>Noise Level</strong></td>
                                    <td class="highlight-pm">Very quiet</td>
                                    <td>Moderate (rolling)</td>
                                    <td>Quiet</td>
                                </tr>
                                <tr>
                                    <td><strong>Cost (High Vol)</strong></td>
                                    <td class="highlight-pm">⭐ Lowest</td>
                                    <td>High</td>
                                    <td>Medium</td>
                                </tr>
                                <tr>
                                    <td><strong>Speed Range</strong></td>
                                    <td>Low-Medium</td>
                                    <td>High</td>
                                    <td>Low</td>
                                </tr>
                                <tr>
                                    <td><strong>Load Capacity</strong></td>
                                    <td>Light-Medium</td>
                                    <td>High</td>
                                    <td>Medium</td>
                                </tr>
                                <tr>
                                    <td><strong>Lifespan</strong></td>
                                    <td class="highlight-pm">10,000+ hours</td>
                                    <td>20,000+ hours</td>
                                    <td>5,000+ hours</td>
                                </tr>
                            </tbody>
                        </table>

                        <h4 style="font-size: 22px; font-weight: 600; color: #002FA7; margin-bottom: 15px; margin-top: 30px; padding-left: 15px; border-left: 4px solid #C5A059;">
                            Common Materials for PM Bearings
                        </h4>
                        <table class="term-table">
                            <thead>
                                <tr>
                                    <th style="width: 180px;">Material</th>
                                    <th>MPIF Code</th>
                                    <th>PV Limit (MPa·m/s)</th>
                                    <th>Best For</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="term-name">Bronze (90Cu-10Sn)</td>
                                    <td>CT-1000</td>
                                    <td>1.8</td>
                                    <td>Low-speed, light-load. Household appliances, fans, toys</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Iron-Copper</td>
                                    <td>FC-0208</td>
                                    <td>3.5</td>
                                    <td>Medium loads. Automotive accessories, power tools</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Iron-Bronze Composite</td>
                                    <td>FC-0800</td>
                                    <td>2.5</td>
                                    <td>Balanced performance. Motors, pumps</td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="decision-box" style="background: linear-gradient(135deg, #f0f4ff 0%, #e8f4fd 100%);">
                            <h4>🏭 Common Applications</h4>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px;">
                                <div style="background: white; padding: 12px; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 28px;">🖥️</div>
                                    <strong style="font-size: 13px;">Computer Fans</strong>
                                </div>
                                <div style="background: white; padding: 12px; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 28px;">🚗</div>
                                    <strong style="font-size: 13px;">Automotive Motors</strong>
                                </div>
                                <div style="background: white; padding: 12px; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 28px;">🏠</div>
                                    <strong style="font-size: 13px;">Home Appliances</strong>
                                </div>
                                <div style="background: white; padding: 12px; border-radius: 8px; text-align: center;">
                                    <div style="font-size: 28px;">🔧</div>
                                    <strong style="font-size: 13px;">Power Tools</strong>
                                </div>
                            </div>
                            <p style="margin-top: 15px; font-size: 14px; color: #666;">
                                <strong>💡 Design Tip:</strong> For optimal performance, maintain a shaft-to-bearing clearance of 0.02-0.05mm. <a href="contact.html" style="color: #002FA7;">Contact us</a> for bearing design support!
                            </p>
                        </div>
                    </div>
'''

SINTERING_HTML = '''
                    <!-- Sintering Process Guide -->
                    <div id="sintering-guide" style="margin-bottom: 80px;">
                        <h3 style="font-family: 'Playfair Display', serif; font-size: 28px; font-weight: 700; color: #333; margin-bottom: 15px; border-bottom: 2px solid #eee; padding-bottom: 10px;">
                            🔥 Sintering Process Explained
                        </h3>
                        <p style="font-size: 16px; color: #555; line-height: 1.7; margin-bottom: 25px;">
                            Sintering is the critical heat treatment step that transforms compacted metal powder ("green parts") into strong, functional components. Understanding the sintering process helps engineers optimize part properties and quality.
                        </p>

                        <h4 style="font-size: 22px; font-weight: 600; color: #002FA7; margin-bottom: 15px; padding-left: 15px; border-left: 4px solid #C5A059;">
                            The PM Manufacturing Process
                        </h4>
                        <div style="display: flex; flex-wrap: wrap; gap: 0; margin-bottom: 30px; justify-content: center;">
                            <div style="background: #002FA7; color: white; padding: 20px 15px; text-align: center; min-width: 140px; flex: 1; border-radius: 8px 0 0 8px;">
                                <div style="font-size: 28px; margin-bottom: 8px;">⚗️</div>
                                <strong style="font-size: 14px;">1. Powder Mixing</strong>
                                <p style="font-size: 12px; opacity: 0.85; margin: 5px 0 0;">Metal powders + additives blended to spec</p>
                            </div>
                            <div style="background: #1a47b8; color: white; padding: 20px 15px; text-align: center; min-width: 140px; flex: 1;">
                                <div style="font-size: 28px; margin-bottom: 8px;">🔨</div>
                                <strong style="font-size: 14px;">2. Compaction</strong>
                                <p style="font-size: 12px; opacity: 0.85; margin: 5px 0 0;">400-700 MPa pressure in precision die</p>
                            </div>
                            <div style="background: #C5A059; color: white; padding: 20px 15px; text-align: center; min-width: 140px; flex: 1; border: 3px solid #8B6914;">
                                <div style="font-size: 28px; margin-bottom: 8px;">🔥</div>
                                <strong style="font-size: 14px;">3. SINTERING</strong>
                                <p style="font-size: 12px; opacity: 0.95; margin: 5px 0 0;">1100-1300°C controlled atmosphere furnace</p>
                            </div>
                            <div style="background: #1a47b8; color: white; padding: 20px 15px; text-align: center; min-width: 140px; flex: 1; border-radius: 0 8px 8px 0;">
                                <div style="font-size: 28px; margin-bottom: 8px;">✨</div>
                                <strong style="font-size: 14px;">4. Finishing</strong>
                                <p style="font-size: 12px; opacity: 0.85; margin: 5px 0 0;">Sizing, heat treat, plating as needed</p>
                            </div>
                        </div>

                        <h4 style="font-size: 22px; font-weight: 600; color: #002FA7; margin-bottom: 15px; padding-left: 15px; border-left: 4px solid #C5A059;">
                            Sintering Temperature &amp; Atmosphere Guide
                        </h4>
                        <table class="term-table">
                            <thead>
                                <tr>
                                    <th style="width: 180px;">Material</th>
                                    <th>Temperature (°C)</th>
                                    <th>Atmosphere</th>
                                    <th>Time (min)</th>
                                    <th>Key Notes</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="term-name">Iron-Carbon Steel<br>(FC-0208)</td>
                                    <td>1120 - 1150</td>
                                    <td>N₂/H₂ (90/10)</td>
                                    <td>20 - 30</td>
                                    <td>Most common. Carbon control is critical for hardness.</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Iron-Nickel Steel<br>(FN-0205)</td>
                                    <td>1120 - 1150</td>
                                    <td>N₂/H₂ (90/10)</td>
                                    <td>25 - 35</td>
                                    <td>Higher strength. Ni improves toughness and hardenability.</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Stainless Steel<br>(SS-316L)</td>
                                    <td>1250 - 1350</td>
                                    <td>Vacuum or H₂</td>
                                    <td>30 - 60</td>
                                    <td>High temp required. Must avoid Cr oxidation.</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Bronze<br>(CT-1000)</td>
                                    <td>800 - 850</td>
                                    <td>N₂/H₂ or Endothermic</td>
                                    <td>15 - 25</td>
                                    <td>Lower temp. Used for bearings and bushings.</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Soft Magnetic<br>(Iron Pure)</td>
                                    <td>1120 - 1150</td>
                                    <td>H₂ or Dissociated NH₃</td>
                                    <td>30 - 45</td>
                                    <td>High-purity atmosphere needed for magnetic properties.</td>
                                </tr>
                            </tbody>
                        </table>

                        <h4 style="font-size: 22px; font-weight: 600; color: #002FA7; margin-bottom: 15px; margin-top: 30px; padding-left: 15px; border-left: 4px solid #C5A059;">
                            What Happens During Sintering?
                        </h4>
                        <table class="term-table">
                            <thead>
                                <tr>
                                    <th style="width: 180px;">Stage</th>
                                    <th>Temperature Range</th>
                                    <th>What Happens</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td class="term-name">Burn-off</td>
                                    <td>150 - 600°C</td>
                                    <td>Lubricant (zinc stearate) evaporates. Critical to control ramp rate to avoid blistering.</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Oxide Reduction</td>
                                    <td>600 - 900°C</td>
                                    <td>Hydrogen reduces surface oxides on powder particles, enabling metallic bonding.</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Particle Bonding</td>
                                    <td>900 - 1150°C</td>
                                    <td>Atomic diffusion creates necks between particles. Strength increases dramatically.</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Densification</td>
                                    <td>Peak Temperature</td>
                                    <td>Pores shrink, grain growth occurs. Part reaches final density (6.4-7.2 g/cm³).</td>
                                </tr>
                                <tr>
                                    <td class="term-name">Cooling</td>
                                    <td>Peak → Room Temp</td>
                                    <td>Controlled cooling rate determines final microstructure and hardness.</td>
                                </tr>
                            </tbody>
                        </table>

                        <div class="decision-box" style="background: linear-gradient(135deg, #fff8e1 0%, #fff3e0 100%);">
                            <h4>🔬 Sintering Quality Control at Yeh Sheng</h4>
                            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
                                <div style="background: white; padding: 15px; border-radius: 8px; border-left: 3px solid #C5A059;">
                                    <strong style="color: #002FA7;">🌡️ Temperature Monitoring</strong>
                                    <p style="font-size: 13px; margin: 8px 0 0; color: #666;">±5°C accuracy across the furnace zone</p>
                                </div>
                                <div style="background: white; padding: 15px; border-radius: 8px; border-left: 3px solid #C5A059;">
                                    <strong style="color: #002FA7;">💨 Atmosphere Control</strong>
                                    <p style="font-size: 13px; margin: 8px 0 0; color: #666;">Dew point and gas composition continuously monitored</p>
                                </div>
                                <div style="background: white; padding: 15px; border-radius: 8px; border-left: 3px solid #C5A059;">
                                    <strong style="color: #002FA7;">📊 Density Testing</strong>
                                    <p style="font-size: 13px; margin: 8px 0 0; color: #666;">Every batch verified per MPIF Standard 42</p>
                                </div>
                            </div>
                            <p style="margin-top: 15px; font-size: 14px; color: #666;">
                                <strong>📧 Have questions about sintering?</strong> Our engineering team can help you select the right parameters. <a href="contact.html" style="color: #002FA7; font-weight: 600;">Contact us →</a>
                            </p>
                        </div>
                    </div>
'''

# Read file
with open('resources.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert before Legal Statement
marker = '                    <!-- Legal Statement -->'
if marker not in content:
    marker = '                        <!-- Legal Statement -->'
content = content.replace(marker, BEARINGS_HTML + SINTERING_HTML + '\n' + marker)

# Update JS sections array
old_sections = "const sections = ['process-guide', 'gear-types', 'forming-methods', 'pm-vs-cnc', 'surface-treatment', 'design-guide', 'faq', 'glossary', 'materials', 'iron-steel', 'stainless', 'magnetic', 'bronze-brass'];"
new_sections = "const sections = ['process-guide', 'gear-types', 'forming-methods', 'pm-vs-cnc', 'surface-treatment', 'design-guide', 'bearings-guide', 'sintering-guide', 'faq', 'glossary', 'materials', 'iron-steel', 'stainless', 'magnetic', 'bronze-brass'];"
content = content.replace(old_sections, new_sections)

with open('resources.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("English resources.html updated successfully!")
