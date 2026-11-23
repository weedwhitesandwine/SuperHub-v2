"""Modern minimal icons for SuperHub-v2: the same shapes as sketch.py, drawn as
clean even-weight lines with flat fills (no hatching, no pencil wobble), plus
vector versions of the ten hand-supplied icons.

    python minimal.py OUTDIR [name ...]
"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sketch
from sketch import circ, line, path, rect

INK = '#111111'
FLAT = {'dark': INK, 'mid': '#d4d4d4', 'light': '#ffffff', 'white': '#ffffff'}
W = 30  # one stroke weight for everything


def part(shape, fill=None, w=16, line=False):
    if line:
        return f'<g fill="none" stroke="{INK}" stroke-width="{W}" stroke-linecap="round" stroke-linejoin="round">{shape}</g>'
    f = FLAT.get(fill, '#ffffff')
    return f'<g fill="{f}" stroke="{INK}" stroke-width="{W}" stroke-linecap="round" stroke-linejoin="round">{shape}</g>'


sketch.part = part  # sketch's icon functions look `part` up at call time
ICONS = dict(sketch.ICONS)


def icon(name):
    def deco(f):
        ICONS[name] = f
        return f
    return deco


@icon('calendar')
def calendar():
    p = [part(rect(170, 230, 684, 600, 60), 'light'), part(line(170, 380, 854, 380), line=True)]
    p += [part(line(x, 170, x, 290), line=True) for x in (360, 664)]
    for r in range(2):
        for c in range(4):
            p.append(part(circ(290 + c * 148, 500 + r * 160, 26), 'dark'))
    return p


@icon('notes')
def notes():
    p = [part(rect(190, 170, 520, 700, 50), 'light')]
    p.append(part(path('M270 330 L310 370 L390 280'), line=True))
    p += [part(circ(330, 520, 40), None), part(circ(330, 690, 40), None)]
    for y in (330, 520, 690):
        p.append(part(line(450, y, 620, y), line=True))
    p.append(part(path('M790 200 L870 200 L870 760 L830 840 L790 760 Z'), 'light'))
    return p


@icon('work')
def work():
    # a llama, side on
    body = 'M300 520 Q300 460 360 460 L640 460 Q700 460 700 520 L700 640 Q700 690 650 690 L350 690 Q300 690 300 640 Z'
    neck = 'M600 470 L600 250 Q600 200 650 200 L760 200 Q800 200 800 240 Q800 280 760 280 L700 280 L700 470'
    p = [part(path(body), 'light'), part(path(neck), 'light')]
    p += [part(path('M640 200 L655 130 L690 200'), line=True), part(path('M690 200 L705 140 L735 200'), line=True)]
    p += [part(line(x, 690, x, 850), line=True) for x in (350, 420, 580, 650)]
    p.append(part(circ(735, 235, 12), 'dark'))
    p.append(part(path('M300 540 Q240 560 250 620'), line=True))
    return p


@icon('lifter')
def lifter():
    p = [part(line(150, 300, 874, 300), line=True)]
    for x in (190, 834):
        p.append(part(rect(x - 30, 210, 60, 180, 16), 'dark'))
    p += [part(circ(512, 330, 60), 'light')]
    p.append(part(path('M440 420 Q512 400 584 420 L600 600 L424 600 Z'), 'light'))
    p += [part(path('M445 430 L380 300'), line=True), part(path('M579 430 L644 300'), line=True)]
    p += [part(path('M440 600 L360 690 L400 820'), line=True), part(path('M584 600 L664 690 L624 820'), line=True)]
    return p


@icon('star')
def star():
    p = [part(f'<path transform="translate(512,540) scale(2.1)" d="{sketch.STAR}"/>', 'light')]
    for a in (-90, -18, 54, 126, 198):
        r = math.radians(a + 36)
        p.append(part(line(round(512 + 330 * math.cos(r)), round(540 + 330 * math.sin(r)), round(512 + 400 * math.cos(r)), round(540 + 400 * math.sin(r))), line=True))
    return p


@icon('search')
def search():
    return [part(circ(440, 440, 230), 'light'), part(line(610, 610, 820, 820), line=True),
            '<g stroke="#111111" stroke-width="70" stroke-linecap="round"><path d="M640 640 L830 830"/></g>']


@icon('brain-bulb')
def brain_bulb():
    p = [part(path('M512 150 Q760 150 760 400 Q760 530 660 610 L640 700 L384 700 L364 610 Q264 530 264 400 Q264 150 512 150 Z'), 'light')]
    p += [part(line(400, 770, 624, 770), line=True), part(line(430, 840, 594, 840), line=True)]
    p.append(part(path('M512 220 L512 640'), line=True))
    p.append(part(path('M512 280 Q420 250 390 330 Q340 360 380 430 Q350 500 420 530 Q470 580 512 540'), line=True))
    p.append(part(path('M512 280 Q604 250 634 330 Q684 360 644 430 Q674 500 604 530 Q554 580 512 540'), line=True))
    return p


@icon('digest')
def digest():
    nodes = [(512, 512, 90), (300, 280, 60), (740, 260, 60), (820, 560, 60), (690, 800, 60), (280, 740, 60)]
    p = [part(line(512, 512, x, y), line=True) for x, y, _ in nodes[1:]]
    p += [part(circ(x, y, r), 'dark' if i == 0 else 'light') for i, (x, y, r) in enumerate(nodes)]
    return p


@icon('atelier')
def atelier():
    return [part(line(512, 130, 512, 230), line=True),
            part(line(420, 640, 320, 880), line=True), part(line(604, 640, 704, 880), line=True), part(line(512, 640, 512, 860), line=True),
            part(rect(230, 220, 564, 430, 30), 'light'),
            part(circ(640, 340, 46), None),
            part(path('M270 590 Q380 470 480 540 Q580 610 754 500'), line=True)]


@icon('keywords')
def keywords():
    tag = 'M180 300 Q180 220 260 220 L560 220 L860 520 L560 820 L180 440 Z'
    p = [part(path(tag), 'light'), part(circ(320, 360, 44), None)]
    p += [part(line(470, 420, 430, 640), line=True), part(line(560, 420, 520, 640), line=True),
          part(line(410, 490, 600, 490), line=True), part(line(400, 570, 590, 570), line=True)]
    return p


if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    for name in sys.argv[2:] or ICONS:
        open(os.path.join(out, name + '.svg'), 'w').write(sketch.svg(ICONS[name]()).replace('<rect width="1024" height="1024" fill="#fff"/>', ''))
        print(name)
