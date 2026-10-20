import os

img_dir = r"C:\Users\manga\.gemini\antigravity\scratch\wedding-sanro-fitra\assets\images"
os.makedirs(img_dir, exist_ok=True)

def create_svg(path, title, subtitle, icon="heart", ratio="portrait"):
    width = 600
    height = 800 if ratio == "portrait" else (600 if ratio == "square" else 400)
    
    icon_svg = ""
    if icon == "heart":
        icon_svg = '<path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" fill="url(#goldGrad)" opacity="0.8"/>'
    elif icon == "couple":
        icon_svg = '<circle cx="9" cy="8" r="4" fill="url(#goldGrad)" opacity="0.9"/><path d="M2 19c0-3.87 3.13-7 7-7s7 3.13 7 7" stroke="url(#goldGrad)" stroke-width="2" fill="none"/><circle cx="17" cy="8" r="3.5" fill="url(#goldGrad)" opacity="0.8"/><path d="M12 19c0-2.8 2.2-5 5-5s5 2.2 5 5" stroke="url(#goldGrad)" stroke-width="2" fill="none"/>'
    elif icon == "groom":
        icon_svg = '<circle cx="12" cy="7" r="4" fill="url(#goldGrad)"/><path d="M4 21v-2a4 4 0 0 1 4-4h8a4 4 0 0 1 4 4v2" stroke="url(#goldGrad)" stroke-width="2" fill="none"/><path d="M12 11v6M10 13l2 2 2-2" stroke="url(#goldGrad)" stroke-width="1.5" fill="none"/>'
    elif icon == "bride":
        icon_svg = '<circle cx="12" cy="7" r="4" fill="url(#goldGrad)"/><path d="M6 21v-2a6 6 0 0 1 12 0v2" stroke="url(#goldGrad)" stroke-width="2" fill="none"/><path d="M8 5c1-3 7-3 8 0" stroke="url(#goldGrad)" stroke-width="1.5" fill="none"/>'
    elif icon == "church":
        icon_svg = '<path d="M12 2v6M9 5h6M4 12l8-5 8 5v10H4V12zm6 10v-5h4v5" stroke="url(#goldGrad)" stroke-width="2" fill="none"/>'
    elif icon == "ring":
        icon_svg = '<circle cx="9" cy="12" r="6" stroke="url(#goldGrad)" stroke-width="2" fill="none"/><circle cx="15" cy="12" r="6" stroke="url(#goldGrad)" stroke-width="2" fill="none"/><path d="M12 6l1-2h-2l1 2" stroke="url(#goldGrad)" stroke-width="1.5" fill="none"/>'
    elif icon == "qris":
        icon_svg = '<rect x="3" y="3" width="7" height="7" stroke="url(#goldGrad)" stroke-width="1.5" fill="none"/><rect x="5" y="5" width="3" height="3" fill="url(#goldGrad)"/><rect x="14" y="3" width="7" height="7" stroke="url(#goldGrad)" stroke-width="1.5" fill="none"/><rect x="16" y="5" width="3" height="3" fill="url(#goldGrad)"/><rect x="3" y="14" width="7" height="7" stroke="url(#goldGrad)" stroke-width="1.5" fill="none"/><rect x="5" y="16" width="3" height="3" fill="url(#goldGrad)"/><path d="M14 14h2v2h-2zm3 0h3v3h-3zm0 4h3v3h-3zm-3 2h2v2h-2z" fill="url(#goldGrad)"/>'

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141720"/>
      <stop offset="50%" stop-color="#0a0c10"/>
      <stop offset="100%" stop-color="#181b24"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f5d78a"/>
      <stop offset="50%" stop-color="#d4af37"/>
      <stop offset="100%" stop-color="#9a7722"/>
    </linearGradient>
    <radialGradient id="goldGlow" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#0a0c10" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(212,175,55,0.04)" stroke-width="1"/>
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="url(#bgGrad)"/>
  <rect width="{width}" height="{height}" fill="url(#grid)"/>
  <circle cx="{width/2}" cy="{height/2 - 40}" r="220" fill="url(#goldGlow)"/>

  <!-- Ornate Corner Borders -->
  <g stroke="url(#goldGrad)" stroke-width="1.5" fill="none" opacity="0.6">
    <path d="M 30 50 L 30 30 L 50 30 M 35 35 L 45 35"/>
    <path d="M {width-30} 50 L {width-30} 30 L {width-50} 30 M {width-35} 35 L {width-45} 35"/>
    <path d="M 30 {height-50} L 30 {height-30} L 50 {height-30} M 35 {height-35} L 45 {height-35}"/>
    <path d="M {width-30} {height-50} L {width-30} {height-30} L {width-50} {height-30} M {width-35} {height-35} L {width-45} {height-35}"/>
  </g>

  <!-- Center Circle Frame -->
  <circle cx="{width/2}" cy="{height/2 - 40}" r="110" stroke="url(#goldGrad)" stroke-width="2" fill="rgba(18,21,28,0.7)" stroke-dasharray="6,4"/>
  <circle cx="{width/2}" cy="{height/2 - 40}" r="96" stroke="rgba(212,175,55,0.3)" stroke-width="1" fill="none"/>

  <!-- Icon inside circle -->
  <g transform="translate({width/2 - 36}, {height/2 - 76}) scale(3)">
    {icon_svg}
  </g>

  <!-- Text elements -->
  <text x="{width/2}" y="{height/2 + 110}" text-anchor="middle" fill="#d4af37" font-family="'Cinzel', serif" font-size="22" font-weight="600" letter-spacing="3">{title.upper()}</text>
  <text x="{width/2}" y="{height/2 + 140}" text-anchor="middle" fill="#cbd5e1" font-family="'Cormorant Garamond', Georgia, serif" font-size="16" font-style="italic" letter-spacing="1">{subtitle}</text>
  <text x="{width/2}" y="{height/2 + 165}" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11" letter-spacing="2">GANTI DENGAN FOTO ANDA</text>
</svg>'''
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content)

# Generate assets
create_svg(os.path.join(img_dir, "hero-cover.svg"), "Sanro & Fitra", "The Holy Matrimony • 21.10.2026", "couple", "portrait")
create_svg(os.path.join(img_dir, "groom.svg"), "Sanro Andreas Sinurat", "Putra Bpk M. Sinurat & Ibu R. Malau", "groom", "portrait")
create_svg(os.path.join(img_dir, "bride.svg"), "Elfitra Sitanggang", "Putri Bpk St. H. Sitanggang & Ibu S. Situngkir", "bride", "portrait")
create_svg(os.path.join(img_dir, "couple.svg"), "Sanro & Fitra", "Dua Hati Menjadi Satu", "heart", "portrait")
create_svg(os.path.join(img_dir, "story-1.svg"), "Awal Pertemuan", "Pertemuan yang Mengubahkan", "heart", "square")
create_svg(os.path.join(img_dir, "story-2.svg"), "Jatuh Cinta", "Menumbuhkan Komitmen Bersama", "ring", "square")
create_svg(os.path.join(img_dir, "story-3.svg"), "Lamaran", "Restu Kedua Keluarga Besar", "ring", "square")
create_svg(os.path.join(img_dir, "story-4.svg"), "Hari Bahagia", "Pemberkatan Kudus di Hadapan Allah", "church", "square")

create_svg(os.path.join(img_dir, "gallery-1.svg"), "Prewedding Portrait", "Sanro & Fitra", "couple", "portrait")
create_svg(os.path.join(img_dir, "gallery-2.svg"), "Sweet Moments", "Bahagia Bersama", "heart", "square")
create_svg(os.path.join(img_dir, "gallery-3.svg"), "Love & Laughter", "Kebersamaan Penuh Sukacita", "heart", "square")
create_svg(os.path.join(img_dir, "gallery-4.svg"), "The Vow", "Menuju Janji Suci", "church", "portrait")
create_svg(os.path.join(img_dir, "gallery-5.svg"), "Forever in Love", "Kasih yang Sempurna", "ring", "square")
create_svg(os.path.join(img_dir, "gallery-6.svg"), "Two Families United", "Sinurat & Sitanggang", "couple", "square")

create_svg(os.path.join(img_dir, "qris.svg"), "QRIS Pembayaran", "a.n. Elfitra Sitanggang", "qris", "square")

print("Generated all placeholder SVGs successfully!")
