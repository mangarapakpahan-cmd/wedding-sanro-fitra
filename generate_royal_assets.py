import os

img_dir = r"C:\Users\manga\.gemini\antigravity\scratch\wedding-sanro-fitra\assets\images"
os.makedirs(img_dir, exist_ok=True)

# 1. Royal Center Crest (S & F)
royal_crest_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <defs>
    <linearGradient id="goldLuxury" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff0c2"/>
      <stop offset="25%" stop-color="#e8c779"/>
      <stop offset="50%" stop-color="#d4af37"/>
      <stop offset="75%" stop-color="#aa8323"/>
      <stop offset="100%" stop-color="#6e5113"/>
    </linearGradient>
    <linearGradient id="goldRadial" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fdf4d8"/>
      <stop offset="50%" stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#916c17"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0a0c10" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="600" height="600" fill="#0c0e13"/>
  <circle cx="300" cy="300" r="280" fill="url(#glow)"/>

  <!-- Outer Intricate Rings -->
  <circle cx="300" cy="300" r="240" stroke="url(#goldLuxury)" stroke-width="1.5" fill="none" opacity="0.4"/>
  <circle cx="300" cy="300" r="230" stroke="url(#goldLuxury)" stroke-width="2" fill="none" stroke-dasharray="3,6"/>
  <circle cx="300" cy="300" r="218" stroke="url(#goldLuxury)" stroke-width="1" fill="none" opacity="0.6"/>
  <circle cx="300" cy="300" r="195" stroke="url(#goldLuxury)" stroke-width="2.5" fill="none"/>
  <circle cx="300" cy="300" r="185" stroke="url(#goldLuxury)" stroke-width="1" fill="none" opacity="0.5"/>

  <!-- Ornate Compass Flairs -->
  <g stroke="url(#goldLuxury)" stroke-width="2" fill="none">
    <path d="M 300 45 L 305 70 L 300 90 L 295 70 Z" fill="url(#goldLuxury)"/>
    <path d="M 300 555 L 305 530 L 300 510 L 295 530 Z" fill="url(#goldLuxury)"/>
    <path d="M 45 300 L 70 305 L 90 300 L 70 295 Z" fill="url(#goldLuxury)"/>
    <path d="M 555 300 L 530 305 L 510 300 L 530 295 Z" fill="url(#goldLuxury)"/>
  </g>

  <!-- Crown / Cross Emblem at Top -->
  <g transform="translate(300, 160)" stroke="url(#goldLuxury)" fill="none" stroke-width="2">
    <!-- Cross -->
    <line x1="0" y1="-30" x2="0" y2="10" stroke-width="3"/>
    <line x1="-14" y1="-18" x2="14" y2="-18" stroke-width="3"/>
    <!-- Crown filigree -->
    <path d="M -35 25 Q -20 5 0 25 Q 20 5 35 25 Q 45 40 0 45 Q -45 40 -35 25 Z" fill="url(#goldLuxury)" opacity="0.85"/>
    <circle cx="0" cy="-34" r="3" fill="url(#goldLuxury)"/>
  </g>

  <!-- Laurel Wreath Leaves -->
  <g stroke="url(#goldLuxury)" fill="url(#goldLuxury)" opacity="0.85">
    <!-- Left Wreath -->
    <path d="M 175 320 Q 155 260 190 210 Q 180 235 195 245 Q 170 270 185 300 Z" opacity="0.6"/>
    <path d="M 165 370 Q 150 320 175 280 Q 170 305 185 315 Q 165 345 175 370 Z" opacity="0.6"/>
    <path d="M 180 415 Q 170 375 195 340 Q 192 360 205 370 Q 188 395 195 420 Z" opacity="0.6"/>
    <path d="M 220 445 Q 200 420 230 385 Q 225 405 242 410 Q 225 430 235 448 Z" opacity="0.6"/>

    <!-- Right Wreath (Mirrored) -->
    <path d="M 425 320 Q 445 260 410 210 Q 420 235 405 245 Q 430 270 415 300 Z" opacity="0.6"/>
    <path d="M 435 370 Q 450 320 425 280 Q 430 305 415 315 Q 435 345 425 370 Z" opacity="0.6"/>
    <path d="M 420 415 Q 430 375 405 340 Q 408 360 395 370 Q 412 395 405 420 Z" opacity="0.6"/>
    <path d="M 380 445 Q 400 420 370 385 Q 375 405 358 410 Q 375 430 365 448 Z" opacity="0.6"/>
  </g>

  <!-- Central Intertwined Monogram: S & F -->
  <text x="245" y="345" font-family="'Cinzel', 'Playfair Display', Georgia, serif" font-size="120" font-weight="700" fill="url(#goldLuxury)" text-anchor="middle" letter-spacing="-5">S</text>
  <text x="300" y="335" font-family="'Alex Brush', cursive" font-size="70" font-style="italic" fill="url(#goldRadial)" text-anchor="middle">&amp;</text>
  <text x="355" y="345" font-family="'Cinzel', 'Playfair Display', Georgia, serif" font-size="120" font-weight="700" fill="url(#goldLuxury)" text-anchor="middle" letter-spacing="-5">F</text>

  <!-- Ribbon & Date Under Monogram -->
  <path d="M 200 410 Q 300 430 400 410 L 390 435 Q 300 455 210 435 Z" fill="url(#goldLuxury)" opacity="0.9"/>
  <text x="300" y="428" font-family="'Cinzel', serif" font-size="14" font-weight="600" fill="#0d0f14" text-anchor="middle" letter-spacing="4">21 . 10 . 2026</text>

  <!-- Bottom Filigree Flourish -->
  <path d="M 260 465 Q 300 480 340 465 Q 350 490 300 485 Q 250 490 260 465 Z" fill="url(#goldLuxury)" opacity="0.8"/>
  <circle cx="300" cy="495" r="4" fill="url(#goldLuxury)"/>
</svg>'''

with open(os.path.join(img_dir, "royal-crest.svg"), "w", encoding="utf-8") as f:
    f.write(royal_crest_svg)

# 2. Monogram Groom (S)
groom_monogram_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="goldGroom" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff2cc"/>
      <stop offset="50%" stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#8a6714"/>
    </linearGradient>
    <radialGradient id="glowGroom" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#0a0c10" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="400" height="400" fill="#0d0f14"/>
  <circle cx="200" cy="200" r="180" fill="url(#glowGroom)"/>

  <!-- Ornate Octagon Shield -->
  <polygon points="200,30 320,80 370,200 320,320 200,370 80,320 30,200 80,80" 
           stroke="url(#goldGroom)" stroke-width="1.5" fill="none" opacity="0.5"/>
  <polygon points="200,45 305,90 350,200 305,310 200,355 95,310 50,200 95,90" 
           stroke="url(#goldGroom)" stroke-width="2" fill="rgba(18,21,28,0.7)"/>

  <!-- Laurel Wreath -->
  <circle cx="200" cy="200" r="115" stroke="url(#goldGroom)" stroke-width="1.5" stroke-dasharray="4,6" fill="none"/>
  
  <!-- Male Crown Emblem -->
  <path d="M 180 115 L 185 100 L 200 110 L 215 100 L 220 115 Z" fill="url(#goldGroom)"/>
  <circle cx="200" cy="95" r="3" fill="url(#goldGroom)"/>

  <!-- Center Letter S -->
  <text x="200" y="240" font-family="'Cinzel', Georgia, serif" font-size="115" font-weight="700" fill="url(#goldGroom)" text-anchor="middle">S</text>
  
  <text x="200" y="280" font-family="'Cinzel', sans-serif" font-size="12" font-weight="600" fill="#cbd5e1" text-anchor="middle" letter-spacing="5">THE GROOM</text>
  <text x="200" y="302" font-family="'Cormorant Garamond', Georgia, serif" font-size="14" font-style="italic" fill="#d4af37" text-anchor="middle">Sanro Andreas Sinurat</text>
</svg>'''

with open(os.path.join(img_dir, "monogram-groom.svg"), "w", encoding="utf-8") as f:
    f.write(groom_monogram_svg)

# 3. Monogram Bride (F)
bride_monogram_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="400" height="400">
  <defs>
    <linearGradient id="goldBride" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff2cc"/>
      <stop offset="50%" stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#8a6714"/>
    </linearGradient>
    <radialGradient id="glowBride" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#0a0c10" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="400" height="400" fill="#0d0f14"/>
  <circle cx="200" cy="200" r="180" fill="url(#glowBride)"/>

  <!-- Ornate Floral Circular Shield -->
  <circle cx="200" cy="200" r="155" stroke="url(#goldBride)" stroke-width="1.5" fill="none" opacity="0.4"/>
  <circle cx="200" cy="200" r="145" stroke="url(#goldBride)" stroke-width="2" fill="rgba(18,21,28,0.7)"/>
  <circle cx="200" cy="200" r="132" stroke="url(#goldBride)" stroke-width="1" stroke-dasharray="3,5" fill="none"/>

  <!-- Tiara / Floral Crown -->
  <path d="M 175 118 Q 190 98 200 112 Q 210 98 225 118 Q 200 110 175 118 Z" fill="url(#goldBride)"/>
  <circle cx="200" cy="98" r="3.5" fill="url(#goldBride)"/>
  <circle cx="188" cy="103" r="2.5" fill="url(#goldBride)"/>
  <circle cx="212" cy="103" r="2.5" fill="url(#goldBride)"/>

  <!-- Center Letter F -->
  <text x="202" y="240" font-family="'Cinzel', Georgia, serif" font-size="115" font-weight="700" fill="url(#goldBride)" text-anchor="middle">F</text>
  
  <text x="200" y="280" font-family="'Cinzel', sans-serif" font-size="12" font-weight="600" fill="#cbd5e1" text-anchor="middle" letter-spacing="5">THE BRIDE</text>
  <text x="200" y="302" font-family="'Cormorant Garamond', Georgia, serif" font-size="14" font-style="italic" fill="#d4af37" text-anchor="middle">Elfitra Sitanggang</text>
</svg>'''

with open(os.path.join(img_dir, "monogram-bride.svg"), "w", encoding="utf-8") as f:
    f.write(bride_monogram_svg)

# 4. Catholic Altar & Cross Illustration for Church Section
church_cross_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 300" width="500" height="300">
  <defs>
    <linearGradient id="goldHoly" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff5db"/>
      <stop offset="50%" stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#7a5a0d"/>
    </linearGradient>
    <radialGradient id="holyGlow" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0a0c10" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="500" height="300" fill="#0d0f14"/>
  <circle cx="250" cy="120" r="130" fill="url(#holyGlow)"/>

  <!-- Cathedral Arch -->
  <path d="M 120 280 L 120 150 Q 250 20 380 150 L 380 280" stroke="url(#goldHoly)" stroke-width="2" fill="none" opacity="0.6"/>
  <path d="M 140 280 L 140 160 Q 250 45 360 160 L 360 280" stroke="url(#goldHoly)" stroke-width="1" stroke-dasharray="4,6" fill="none" opacity="0.4"/>

  <!-- Golden Ray Burst -->
  <g stroke="url(#goldHoly)" stroke-width="1" opacity="0.4">
    <line x1="250" y1="110" x2="250" y2="40"/>
    <line x1="250" y1="110" x2="300" y2="55"/>
    <line x1="250" y1="110" x2="330" y2="85"/>
    <line x1="250" y1="110" x2="200" y2="55"/>
    <line x1="250" y1="110" x2="170" y2="85"/>
  </g>

  <!-- Ornate Latin Crucifix -->
  <g stroke="url(#goldHoly)" stroke-width="3" fill="none">
    <line x1="250" y1="65" x2="250" y2="185"/>
    <line x1="215" y1="100" x2="285" y2="100"/>
    <circle cx="250" cy="100" r="16" stroke="url(#goldHoly)" stroke-width="1.5" opacity="0.8"/>
  </g>

  <!-- Holy Dove / Spirit Symbol -->
  <path d="M 240 145 Q 250 135 260 145 Q 268 140 263 150 Q 250 158 240 145 Z" fill="url(#goldHoly)" opacity="0.9"/>

  <text x="250" y="235" font-family="'Cinzel', serif" font-size="16" font-weight="600" fill="url(#goldHoly)" text-anchor="middle" letter-spacing="4">SAKRAMEN PERKAWINAN</text>
  <text x="250" y="260" font-family="'Cormorant Garamond', Georgia, serif" font-size="14" font-style="italic" fill="#cbd5e1" text-anchor="middle">Gereja Katolik St. Yoseph Stasi Pispis</text>
</svg>'''

with open(os.path.join(img_dir, "church-altar.svg"), "w", encoding="utf-8") as f:
    f.write(church_cross_svg)

print("Generated royal monograms and church assets!")
