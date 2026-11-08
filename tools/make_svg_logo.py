import matplotlib.textpath as tp
from matplotlib.font_manager import FontProperties

def path_to_svg_d(path, scale=1.0, offset=(0, 0)):
    codes = path.codes
    verts = path.vertices
    d = []
    i = 0
    while i < len(codes):
        code = codes[i]
        v = verts[i]
        x = v[0] * scale + offset[0]
        y = -v[1] * scale + offset[1]
        if code == 1:
            d.append(f'M {x:.2f} {y:.2f}')
        elif code == 2:
            d.append(f'L {x:.2f} {y:.2f}')
        elif code == 3:
            v1 = verts[i+1]
            x1 = v1[0] * scale + offset[0]
            y1 = -v1[1] * scale + offset[1]
            d.append(f'Q {x:.2f} {y:.2f} {x1:.2f} {y1:.2f}')
            i += 1
        elif code == 4:
            v1 = verts[i+1]
            v2 = verts[i+2]
            x1 = v1[0] * scale + offset[0]
            y1 = -v1[1] * scale + offset[1]
            x2 = v2[0] * scale + offset[0]
            y2 = -v2[1] * scale + offset[1]
            d.append(f'C {x:.2f} {y:.2f} {x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}')
            i += 2
        elif code == 79:
            d.append('Z')
        i += 1
    return ' '.join(d)

fp_bold = FontProperties(family='Segoe UI', weight='bold')

# Icon B
path_icon_b = tp.TextPath((0, 0), 'B', size=165, prop=fp_bold)
bbox_b = path_icon_b.get_extents()
w_b = bbox_b.width
h_b = bbox_b.height
ox_b = (240 - w_b) / 2 - bbox_b.x0
oy_b = 240 - (240 - h_b) / 2 + bbox_b.y0
d_icon_b = path_to_svg_d(path_icon_b, offset=(ox_b, oy_b))

# Brand text 'BKIT Office'
path_text = tp.TextPath((0, 0), 'BKIT Office', size=148, prop=fp_bold)
d_text = path_to_svg_d(path_text, offset=(310, 172))

svg_content = f'''<svg width="1091" height="240" viewBox="0 0 1091 240" fill="none" xmlns="http://www.w3.org/2000/svg">
<g id="bkit-icon">
  <rect x="4" y="4" width="232" height="232" rx="52" fill="#ffffff" stroke="#e5e7eb" stroke-width="8"/>
  <path d="{d_icon_b}" fill="#ff0000"/>
</g>
<g id="bkit-wordmark">
  <path class="brand-text" d="{d_text}" fill="#111827"/>
</g>
</svg>'''

with open('apps/shell/src/renderer/src/assets/genoffice-logo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

icon_svg = f'''<svg width="240" height="240" viewBox="0 0 240 240" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="4" y="4" width="232" height="232" rx="52" fill="#ffffff" stroke="#e5e7eb" stroke-width="8"/>
  <path d="{d_icon_b}" fill="#ff0000"/>
</svg>'''

with open('apps/shell/src/renderer/src/assets/bkit-icon.svg', 'w', encoding='utf-8') as f:
    f.write(icon_svg)

print('SVG files written successfully!')
