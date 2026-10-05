def defs():
    return '''<defs>
<radialGradient id="piel" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#ffe6cf"/><stop offset="1" stop-color="#f3b98f"/></radialGradient>
<radialGradient id="rubor" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ff7aa0" stop-opacity=".75"/><stop offset="1" stop-color="#ff7aa0" stop-opacity="0"/></radialGradient>
<linearGradient id="sombrero" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8a4bd6"/><stop offset="1" stop-color="#4a1f8f"/></linearGradient>
<linearGradient id="vestido" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffa13d"/><stop offset="1" stop-color="#f26a0c"/></linearGradient>
<radialGradient id="sabana" cx=".35" cy=".25" r=".9"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#d6d3ee"/></radialGradient>
<radialGradient id="calabaza" cx=".4" cy=".3" r=".8"><stop offset="0" stop-color="#ffb347"/><stop offset="1" stop-color="#e9590c"/></radialGradient>
<radialGradient id="pelo" cx=".4" cy=".3" r=".9"><stop offset="0" stop-color="#7a4a2b"/><stop offset="1" stop-color="#3a1f10"/></radialGradient>
</defs>'''

def ojos(cx, cy, sep=62, r=26):
    s=''
    for dx in (-sep/2, sep/2):
        x=cx+dx
        s+=f'<ellipse cx="{x}" cy="{cy}" rx="{r}" ry="{r*1.1}" fill="#fff"/><ellipse cx="{x+2}" cy="{cy+3}" rx="{r*.68}" ry="{r*.8}" fill="#3a2212"/><ellipse cx="{x+2}" cy="{cy+3}" rx="{r*.38}" ry="{r*.46}" fill="#120a05"/><circle cx="{x-4}" cy="{cy-6}" r="{r*.26}" fill="#fff"/><circle cx="{x+9}" cy="{cy+10}" r="{r*.12}" fill="#fff"/>'
    return s

def cara(cx, cy, R=140):
    s=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#piel)"/>'
    s+=f'<ellipse cx="{cx-R*.6}" cy="{cy+R*.3}" rx="{R*.2}" ry="{R*.14}" fill="url(#rubor)"/><ellipse cx="{cx+R*.6}" cy="{cy+R*.3}" rx="{R*.2}" ry="{R*.14}" fill="url(#rubor)"/>'
    s+=ojos(cx, cy-R*.05, sep=R*.46, r=R*.19)
    s+=f'<path d="M{cx-R*.3} {cy+R*.42} Q{cx} {cy+R*.78} {cx+R*.3} {cy+R*.42} Q{cx} {cy+R*.5} {cx-R*.3} {cy+R*.42}Z" fill="#b3202f"/><path d="M{cx-R*.17} {cy+R*.52} Q{cx} {cy+R*.66} {cx+R*.17} {cy+R*.52}Q{cx} {cy+R*.57} {cx-R*.17} {cy+R*.52}Z" fill="#ff7a8a"/>'
    s+=f'<ellipse cx="{cx}" cy="{cy+R*.22}" rx="{R*.06}" ry="{R*.045}" fill="#e39b78"/>'
    return s

def mimi(x, y, sc=1):
    cx,cy=0,0
    g=f'<g transform="translate({x},{y}) scale({sc})">'
    g+='<ellipse cx="0" cy="330" rx="170" ry="26" fill="#000" opacity=".28"/>'
    # piernas y zapatos
    g+='<rect x="-62" y="250" width="40" height="70" rx="18" fill="#f3b98f"/><rect x="22" y="250" width="40" height="70" rx="18" fill="#f3b98f"/>'
    g+='<ellipse cx="-44" cy="326" rx="48" ry="26" fill="#3b1a63"/><ellipse cx="44" cy="326" rx="48" ry="26" fill="#3b1a63"/>'
    # vestido
    g+='<path d="M-120 280 Q-130 120 -60 80 L60 80 Q130 120 120 280 Q0 310 -120 280Z" fill="url(#vestido)"/>'
    g+='<path d="M-120 280 Q0 310 120 280 L116 262 Q0 290 -116 262Z" fill="#ffd1a0" opacity=".55"/>'
    g+='<circle cx="-44" cy="190" r="12" fill="#fff3c4"/><circle cx="46" cy="214" r="12" fill="#fff3c4"/><circle cx="0" cy="160" r="10" fill="#fff3c4"/>'
    # brazos
    g+='<path d="M-100 110 Q-190 140 -176 210" stroke="#f3b98f" stroke-width="38" stroke-linecap="round" fill="none"/><path d="M100 110 Q190 70 196 -10" stroke="#f3b98f" stroke-width="38" stroke-linecap="round" fill="none"/>'
    g+='<circle cx="-176" cy="212" r="26" fill="#ffd7b8"/><circle cx="196" cy="-14" r="26" fill="#ffd7b8"/>'
    # pelo detrás + coletas
    g+='<circle cx="-150" cy="-30" r="52" fill="url(#pelo)"/><circle cx="150" cy="-30" r="52" fill="url(#pelo)"/>'
    g+='<circle cx="0" cy="-10" r="152" fill="url(#pelo)"/>'
    g+=cara(0,10,138)
    # flequillo
    g+='<path d="M-134 -26 Q-100 -118 0 -112 Q100 -118 134 -26 Q90 -70 30 -62 Q-20 -40 -80 -62 Q-120 -50 -134 -26Z" fill="url(#pelo)"/>'
    # sombrero
    g+='<ellipse cx="0" cy="-108" rx="190" ry="40" fill="#35176b"/>'
    g+='<path d="M-110 -112 Q-90 -260 -10 -372 Q40 -300 40 -320 Q96 -250 110 -112Z" fill="url(#sombrero)"/>'
    g+='<path d="M-10 -372 Q40 -392 74 -350 Q50 -352 40 -336Z" fill="#4a1f8f"/>'
    g+='<path d="M-112 -128 Q0 -96 112 -128 L110 -104 Q0 -72 -110 -104Z" fill="#ffc83d"/><rect x="-26" y="-134" width="52" height="40" rx="8" fill="none" stroke="#fff3c4" stroke-width="8" transform="translate(0,-6)"/>'
    g+='<path d="M-52 -230 l10 22 24 4 -18 16 4 24 -20 -12 -22 12 6 -24 -16 -18 24 -2z" fill="#ffd96a" transform="scale(.7) translate(-10,-60)"/>'
    g+='</g>'
    return g

def tito(x, y, sc=1):
    g=f'<g transform="translate({x},{y}) scale({sc})">'
    g+='<ellipse cx="0" cy="330" rx="170" ry="26" fill="#000" opacity=".28"/>'
    g+='<ellipse cx="-56" cy="322" rx="46" ry="24" fill="#2b2b3d"/><ellipse cx="56" cy="322" rx="46" ry="24" fill="#2b2b3d"/>'
    # sábana
    g+='<path d="M-150 300 Q-170 110 -70 60 L70 60 Q170 110 150 300 L120 280 L90 310 L55 282 L22 312 L-12 282 L-48 312 L-84 282 L-120 308Z" fill="url(#sabana)"/>'
    g+='<path d="M-130 250 Q-150 120 -78 74" stroke="#bdb9e3" stroke-width="6" fill="none" opacity=".6"/>'
    # brazos fuera de la sábana
    g+='<path d="M-110 120 Q-200 80 -196 -4" stroke="#f3b98f" stroke-width="36" stroke-linecap="round" fill="none"/><path d="M110 120 Q200 150 190 220" stroke="#f3b98f" stroke-width="36" stroke-linecap="round" fill="none"/>'
    g+='<circle cx="-196" cy="-8" r="25" fill="#ffd7b8"/><circle cx="190" cy="224" r="25" fill="#ffd7b8"/>'
    # capucha de sábana
    g+='<path d="M-170 10 Q-176 -170 0 -176 Q176 -170 170 10 Q160 100 90 100 L-90 100 Q-160 100 -170 10Z" fill="url(#sabana)"/>'
    g+='<path d="M-150 40 Q-150 -130 -10 -150" stroke="#bdb9e3" stroke-width="6" fill="none" opacity=".5"/>'
    # pelo y cara dentro de la capucha
    g+='<path d="M-30 -168 Q-10 -230 20 -190 Q10 -176 -10 -176Z" fill="url(#pelo)"/>'
    g+=cara(0,10,120)
    g+='<path d="M-118 -30 Q-80 -108 0 -102 Q80 -108 118 -30 Q80 -62 20 -56 Q-30 -40 -80 -56 Q-110 -48 -118 -30Z" fill="url(#pelo)"/>'
    g+='</g>'
    return g

def calabaza(x,y,sc=1):
    g=f'<g transform="translate({x},{y}) scale({sc})">'
    g+='<ellipse cx="0" cy="116" rx="130" ry="20" fill="#000" opacity=".28"/>'
    g+='<path d="M0 -92 C-10 -118 -4 -136 4 -150 C16 -132 12 -112 8 -92Z" fill="#4c8a2b"/>'
    g+='<ellipse cx="-62" cy="12" rx="78" ry="104" fill="#e9590c"/><ellipse cx="62" cy="12" rx="78" ry="104" fill="#e9590c"/><ellipse cx="0" cy="10" rx="82" ry="108" fill="url(#calabaza)"/>'
    g+='<path d="M0 -96 C-30 -40 -30 70 0 112 M0 -96 C30 -40 30 70 0 112" stroke="#c94a06" stroke-width="5" fill="none" opacity=".7"/>'
    g+='<path d="M-62 -10 L-20 -2 L-48 30Z M62 -10 L20 -2 L48 30Z" fill="#2a1005"/><path d="M0 28 L-12 52 L12 52Z" fill="#2a1005"/>'
    g+='<path d="M-60 62 Q0 118 60 62 Q40 78 20 70 Q0 86 -20 70 Q-40 78 -60 62Z" fill="#2a1005"/>'
    g+='</g>'
    return g

def fondo(w,h):
    s=f'<rect width="{w}" height="{h}" fill="url(#cielo)"/>'
    return s

W,H=1920,1080
def hoja():
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'+defs()
    s=s.replace('</defs>','<linearGradient id="cielo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#150a33"/><stop offset=".6" stop-color="#4a1d7c"/><stop offset="1" stop-color="#e2579a"/></linearGradient><radialGradient id="luna" cx=".4" cy=".35" r=".8"><stop offset="0" stop-color="#fff6d6"/><stop offset="1" stop-color="#ffcf70"/></radialGradient><filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter></defs>')
    s+=f'<rect width="{W}" height="{H}" fill="url(#cielo)"/>'
    import random; random.seed(5)
    for i in range(80): s+=f'<circle cx="{random.random()*W:.0f}" cy="{random.random()*520:.0f}" r="{random.random()*2.4+.6:.1f}" fill="#fff" opacity="{random.random()*.7+.3:.2f}"/>'
    s+='<circle cx="1560" cy="230" r="170" fill="#ffb347" opacity=".45" filter="url(#b)"/><circle cx="1560" cy="230" r="120" fill="url(#luna)"/><circle cx="1520" cy="200" r="22" fill="#f3c26b" opacity=".6"/><circle cx="1600" cy="268" r="14" fill="#f3c26b" opacity=".6"/>'
    s+='<path d="M0 1080 L0 800 Q300 740 640 790 Q1000 840 1340 780 Q1660 730 1920 790 L1920 1080Z" fill="#2a0f4d"/><path d="M0 1080 L0 900 Q480 850 960 900 Q1440 950 1920 890 L1920 1080Z" fill="#1d0a38"/>'
    s+='<g fill="#08020f"><path d="M1700 790 L1700 640 L1730 640 L1730 600 L1760 540 L1790 600 L1790 640 L1860 640 L1860 790Z"/></g><rect x="1716" y="668" width="14" height="22" fill="#ffb347"/><rect x="1820" y="668" width="14" height="22" fill="#ffb347"/>'
    s+='<g fill="#08020f"><path d="M110 800 C112 700 100 640 80 590 M80 590 C60 570 40 560 20 540 M80 590 C96 566 118 556 140 540 M104 680 C84 670 64 668 44 652" stroke="#08020f" stroke-width="10" stroke-linecap="round" fill="none"/></g>'
    s+=mimi(620,640,1.05)+tito(1160,640,1.05)+calabaza(1500,760,.85)
    # murciélagos
    for (bx,by,sc) in ((300,200,1),(900,140,.7),(1250,300,.8)):
        s+=f'<g transform="translate({bx},{by}) scale({sc})" fill="#08020f"><path d="M0 0 C-10 -14 -34 -16 -56 -2 C-44 -4 -36 2 -34 10 C-26 4 -16 6 -10 14 C-6 22 6 22 10 14 C16 6 26 4 34 10 C36 2 44 -4 56 -2 C34 -16 10 -14 0 0Z"/></g>'
    s+='<text x="960" y="120" text-anchor="middle" font-family="Liberation Sans, Arial" font-weight="800" font-style="italic" font-size="92" fill="#fff3d6" stroke="#ff7a1a" stroke-width="3" paint-order="stroke" letter-spacing="4">MIMI Y TITO</text>'
    s+='<text x="960" y="175" text-anchor="middle" font-family="Liberation Sans, Arial" font-size="30" fill="#ffd6e8" letter-spacing="10">PERSONAJES ORIGINALES · HALLOWEEN</text>'
    return s+'</svg>'

open('hoja-personajes.svg','w').write(hoja())
def solo(fn, f, w, h, ox, oy):
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'+defs()+f(ox,oy,1)+'</svg>'
    open(fn,'w').write(s)
solo('mimi.svg',mimi,700,820,350,470)
solo('tito.svg',tito,700,720,350,360)
solo('calabaza.svg',calabaza,400,340,200,170)
