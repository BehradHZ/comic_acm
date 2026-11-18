from pathlib import Path
from html import escape
p=Path('comic-kit/balloons')
ink='#17202b'
defs='''<defs><pattern id="dots" width="9" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.6" fill="#17202b" opacity=".24"/></pattern></defs>'''
paths={
'speech':'M 98,65 C 178,15 482,15 555,78 C 613,130 585,216 490,240 C 424,258 315,260 252,249 L 153,303 L 179,244 C 70,226 35,177 53,124 C 61,98 76,80 98,65 Z',
'whisper':'M 98,65 C 178,15 482,15 555,78 C 613,130 585,216 490,240 C 424,258 315,260 252,249 L 153,303 L 179,244 C 70,226 35,177 53,124 C 61,98 76,80 98,65 Z',
'shout':'M 70,91 L 107,83 L 86,33 L 163,53 L 187,14 L 239,45 L 290,11 L 329,43 L 390,17 L 414,50 L 488,24 L 493,68 L 561,51 L 542,97 L 602,124 L 561,152 L 595,194 L 534,199 L 550,245 L 478,229 L 446,269 L 394,243 L 340,266 L 299,244 L 211,306 L 222,251 L 154,264 L 149,226 L 79,241 L 95,196 L 37,178 L 73,140 L 31,111 Z',
'narration':'M 65,60 H 575 V 245 H 65 Z'
}
labels=['دیالوگ عادی','زمزمه','فریاد','روایت / گذر زمان']
samples=[['شاید هیچ‌کدام از ما','به‌تنهایی از پسش برنیاییم.'],['متأسفم، دوست قدیمی.'],['دیگر کافی است!'],['قرن‌ها گذشت.','سپس هزاره‌ها.']]
colors=['#b8cbdc','#c9d8e5','#e7ac9c','#d9c8a2']
def shape(name,offset=False):
    dashed=' stroke-dasharray="10 8"' if name=='whisper' else ''
    if offset:
        return f'<path d="{paths[name]}" transform="translate(8 10)" fill="url(#dots)" stroke="none"/>'
    return f'<path d="{paths[name]}" fill="#fffdf5" stroke="{ink}" stroke-width="4" stroke-linejoin="round"{dashed}/>'
for name in paths:
    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="640" height="330" viewBox="0 0 640 330">{defs}{shape(name)}</svg>'
    (p/f'{name}.svg').write_text(svg)
board=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1160" viewBox="0 0 1600 1160">{defs}',f'<rect width="1600" height="1160" fill="#f2eddf"/>',f'<text x="60" y="74" font-family="sans-serif" font-size="38" font-weight="900" fill="{ink}">THE THREE STONES / LETTERING KIT</text>','<text x="1540" y="125" text-anchor="end" font-family="Vazirmatn" font-size="25" fill="#526171">خط جوهری + رنگ تخت + بافت نقطه‌ای</text>']
for i,name in enumerate(paths):
    x=60+(i%2)*760;y=170+(i//2)*450
    board += [f'<g transform="translate({x} {y})">',f'<rect width="720" height="410" rx="6" fill="{colors[i]}" stroke="{ink}" stroke-width="2"/>','<rect width="720" height="410" fill="url(#dots)" opacity=".35"/>',f'<path d="M 0 330 L 720 190 L 720 410 L 0 410 Z" fill="{ink}" opacity=".05"/>',f'<text x="28" y="40" font-family="sans-serif" font-size="17" font-weight="700" fill="{ink}">0{i+1} / {name.upper()}</text>',f'<text x="687" y="42" text-anchor="end" font-family="Vazirmatn" font-size="23" font-weight="700" fill="{ink}">{labels[i]}</text>','<g transform="translate(38 65)">',shape(name,True),shape(name)]
    lines=samples[i]; cy=147 if len(lines)==1 else 129
    for j,line in enumerate(lines):
        board += [f'<text x="320" y="{cy+j*43}" text-anchor="middle" direction="rtl" font-family="Vazirmatn" font-size="{32 if name=="shout" else 27}" font-weight="{900 if name=="shout" else 500}" fill="{ink}">{escape(line)}</text>']
    board += ['</g></g>']
board += [f'<line x1="60" y1="1085" x2="1540" y2="1085" stroke="{ink}" stroke-width="2"/>','<text x="60" y="1124" font-family="sans-serif" font-size="17" fill="#526171">INK + CEL / HALFTONE     •     EDITABLE SVG     •     v01</text>','<text x="1540" y="1124" text-anchor="end" font-family="Vazirmatn" font-size="20" fill="#526171">بافت بیرون حباب، فضای متن روشن و خوانا</text>','</svg>']
(p/'balloon-style-sheet.svg').write_text(''.join(board))
