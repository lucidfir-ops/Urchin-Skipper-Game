#!/usr/bin/env python3
"""Author the original orthographic workboat SVG using only vector geometry.

Python standard library only. Run from any directory. Existing art is protected:
pass --replace-generated explicitly to rebuild the generated SVG after changes.
"""

from pathlib import Path
import argparse
import math
import random


DESTINATION = Path(__file__).resolve().parent.parent / 'generated-review/fleet-vector/urchin-workboat-top.svg'
RNG = random.Random(180926)
PARTS = []


def emit(markup):
    PARTS.append(markup)


def attrs(values):
    def value(v):
        return f'{v:.3f}'.rstrip('0').rstrip('.') if isinstance(v, float) else str(v)
    return ' '.join(f'{k.replace("_", "-")}="{value(v)}"' for k, v in values.items())


def path(d, **kwargs):
    emit(f'<path d="{d}" {attrs(kwargs)}/>')


def rect(x, y, width, height, **kwargs):
    emit(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" {attrs(kwargs)}/>')


def circle(x, y, r, **kwargs):
    emit(f'<circle cx="{x}" cy="{y}" r="{r}" {attrs(kwargs)}/>')


def ellipse(x, y, rx, ry, **kwargs):
    emit(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" {attrs(kwargs)}/>')


def use(name, x, y, rotate=0, scale=1):
    emit(f'<use href="#{name}" transform="translate({x} {y}) rotate({rotate}) scale({scale})"/>')


def layer(name, label):
    emit(f'<g id="{name}" inkscape:groupmode="layer" inkscape:label="{label}">')


def end():
    emit('</g>')


def weather_flecks(count, bounds, palette, opacity, size):
    """Small irregular material islands; no bitmap noise or filter primitives."""
    for _ in range(count):
        x, y = RNG.uniform(bounds[0], bounds[2]), RNG.uniform(bounds[1], bounds[3])
        rx, ry = RNG.uniform(.4, size), RNG.uniform(.25, size * .6)
        vertices = []
        for i in range(5):
            theta = math.tau * i / 5
            vertices.append(f'{x + math.cos(theta) * rx * RNG.uniform(.5,1.1):.2f} {y + math.sin(theta) * ry * RNG.uniform(.5,1.1):.2f}')
        path('M' + 'L'.join(vertices) + 'Z', fill=RNG.choice(palette), fill_opacity=RNG.uniform(opacity*.3,opacity))


HULL = 'M450 99 C398 121 311 216 259 311 C210 401 189 499 187 645 L199 1424 Q201 1480 230 1496 Q450 1528 670 1496 Q699 1480 701 1424 L713 645 C711 499 690 401 641 311 C589 216 502 121 450 99Z'
GUNWALE = 'M450 114 C399 140 323 223 273 316 C225 404 203 502 202 646 L214 1421 Q216 1468 240 1481 Q450 1510 660 1481 Q684 1468 686 1421 L698 646 C697 502 675 404 627 316 C577 223 501 140 450 114Z'
DECK = 'M450 144 C403 175 337 245 288 333 C242 418 222 516 220 648 L231 1415 Q232 1453 251 1463 Q450 1490 649 1463 Q668 1453 669 1415 L680 648 C678 516 658 418 612 333 C563 245 497 175 450 144Z'
ROOF = 'M316 438 Q450 415 584 438 Q608 442 612 467 L622 811 Q624 841 598 847 Q450 859 302 847 Q276 841 278 811 L288 467 Q292 442 316 438Z'


def definitions():
    emit('''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
     width="1800" height="3360" viewBox="0 0 900 1680" role="img" aria-labelledby="title description">
  <title id="title">Urchin workboat — orthographic overhead</title>
  <desc id="description">Original teal and ivory commercial dive workboat, seen vertically from above with the bow pointing up. Weathered nonslip deck, a forward pilothouse roof, stainless rails, anchor windlass, radar, liferaft, rope coils, fenders and a stern boarding platform. Transparent background. Entirely editable vector paths, shapes, gradients and patterns; no embedded bitmap, external resource, perspective projection or raster filter.</desc>
  <metadata>Created for Urchin Skipper on 2026-09-18. Original vector artwork. See create-workboat.py for the deterministic authoring recipe. Decorative asset only; not collision geometry.</metadata>
  <defs>
    <linearGradient id="hullPaint" x1="0" x2="1" y1="0" y2="0">
      <stop stop-color="#182f33"/><stop offset=".055" stop-color="#5b9291"/><stop offset=".13" stop-color="#377a7b"/>
      <stop offset=".43" stop-color="#428387"/><stop offset=".79" stop-color="#2f6267"/><stop offset=".94" stop-color="#21474d"/><stop offset="1" stop-color="#102a31"/>
    </linearGradient>
    <linearGradient id="capPaint" x1="0" x2="1" y1="0" y2=".3">
      <stop stop-color="#83afaa"/><stop offset=".15" stop-color="#629993"/><stop offset=".46" stop-color="#4b8682"/><stop offset=".81" stop-color="#39706e"/><stop offset="1" stop-color="#29514f"/>
    </linearGradient>
    <linearGradient id="deckBase" x1="0" x2=".8" y1="0" y2="1">
      <stop stop-color="#acae9e"/><stop offset=".34" stop-color="#919b91"/><stop offset=".7" stop-color="#878e81"/><stop offset="1" stop-color="#757f75"/>
    </linearGradient>
    <radialGradient id="deckLight" cx=".26" cy=".26" r=".85">
      <stop stop-color="#e3deba" stop-opacity=".21"/><stop offset=".64" stop-color="#bfc4a3" stop-opacity="0"/><stop offset="1" stop-color="#172c28" stop-opacity=".3"/>
    </radialGradient>
    <linearGradient id="ivory" x1="0" x2="1" y1="0" y2=".6">
      <stop stop-color="#d6d5c2"/><stop offset=".08" stop-color="#f2eee1"/><stop offset=".42" stop-color="#dedecf"/><stop offset=".88" stop-color="#cbcdbb"/><stop offset="1" stop-color="#909f94"/>
    </linearGradient>
    <radialGradient id="roofLight" cx=".3" cy=".21" r=".91">
      <stop stop-color="#fffcf0" stop-opacity=".76"/><stop offset=".49" stop-color="#e9e6d4" stop-opacity=".12"/><stop offset="1" stop-color="#647e70" stop-opacity=".29"/>
    </radialGradient>
    <linearGradient id="steel" x1="0" x2="1" y1="0" y2=".25">
      <stop stop-color="#45534f"/><stop offset=".12" stop-color="#aeb9ad"/><stop offset=".29" stop-color="#f1f1df"/><stop offset=".4" stop-color="#b8c5b9"/>
      <stop offset=".54" stop-color="#7b9088"/><stop offset=".78" stop-color="#d0d5c6"/><stop offset="1" stop-color="#4b625b"/>
    </linearGradient>
    <linearGradient id="steelHorizontal" x1="0" x2="0" y1="0" y2="1">
      <stop stop-color="#4c625c"/><stop offset=".22" stop-color="#e3e6d7"/><stop offset=".43" stop-color="#afbdb1"/><stop offset=".77" stop-color="#607b71"/><stop offset="1" stop-color="#314c45"/>
    </linearGradient>
    <radialGradient id="steelRound" cx=".29" cy=".23" r=".77">
      <stop stop-color="#f6f5e6"/><stop offset=".35" stop-color="#c9d1c3"/><stop offset=".68" stop-color="#95a89c"/><stop offset=".87" stop-color="#516c61"/><stop offset="1" stop-color="#304c43"/>
    </radialGradient>
    <linearGradient id="darkMetal" x1="0" x2="1" y1="0" y2=".25">
      <stop stop-color="#162b2b"/><stop offset=".3" stop-color="#4c6058"/><stop offset=".51" stop-color="#2a423b"/><stop offset="1" stop-color="#112726"/>
    </linearGradient>
    <linearGradient id="rubber" x1="0" x2="1" y1="0" y2=".08">
      <stop stop-color="#101e1d"/><stop offset=".18" stop-color="#394442"/><stop offset=".37" stop-color="#4c5550"/><stop offset=".61" stop-color="#2a3834"/><stop offset="1" stop-color="#112322"/>
    </linearGradient>
    <radialGradient id="rubberRound" cx=".3" cy=".27" r=".79">
      <stop stop-color="#555c51"/><stop offset=".48" stop-color="#303e36"/><stop offset=".8" stop-color="#172d27"/><stop offset="1" stop-color="#0d1c18"/>
    </radialGradient>
    <linearGradient id="glass" x1="0" x2=".9" y1="0" y2="1">
      <stop stop-color="#36585b"/><stop offset=".34" stop-color="#567b7a"/><stop offset=".36" stop-color="#3e6366"/><stop offset=".64" stop-color="#254747"/><stop offset="1" stop-color="#152c31"/>
    </linearGradient>
    <linearGradient id="orange" x1="0" x2="1" y1="0" y2=".8">
      <stop stop-color="#df9450"/><stop offset=".3" stop-color="#db7338"/><stop offset=".61" stop-color="#b8592b"/><stop offset="1" stop-color="#82482d"/>
    </linearGradient>
    <radialGradient id="orangeRound" cx=".3" cy=".22" r=".85">
      <stop stop-color="#f4ab64"/><stop offset=".43" stop-color="#dd7c38"/><stop offset=".78" stop-color="#b6582b"/><stop offset="1" stop-color="#753e25"/>
    </radialGradient>
    <linearGradient id="wood" x1="0" x2="1" y1="0" y2=".06">
      <stop stop-color="#575c43"/><stop offset=".12" stop-color="#ad9d6f"/><stop offset=".35" stop-color="#90835d"/><stop offset=".7" stop-color="#8e8560"/><stop offset="1" stop-color="#5e674f"/>
    </linearGradient>
    <radialGradient id="rust" cx=".5" cy=".35" r=".66">
      <stop stop-color="#79553b" stop-opacity=".61"/><stop offset=".36" stop-color="#a37c4e" stop-opacity=".27"/><stop offset="1" stop-color="#a99056" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="grime">
      <stop stop-color="#2a3d30" stop-opacity=".28"/><stop offset=".46" stop-color="#4b5b3e" stop-opacity=".13"/><stop offset="1" stop-color="#42583c" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="softShadow">
      <stop stop-color="#102a23" stop-opacity=".47"/><stop offset=".6" stop-color="#122e28" stop-opacity=".25"/><stop offset="1" stop-color="#122e28" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="rope" x1="0" x2="1" y1="0" y2="1">
      <stop stop-color="#d5c399"/><stop offset=".43" stop-color="#b7a475"/><stop offset="1" stop-color="#796d48"/>
    </linearGradient>
    <radialGradient id="whiteDome" cx=".32" cy=".22" r=".83">
      <stop stop-color="#ffffef"/><stop offset=".4" stop-color="#e4e5d7"/><stop offset=".75" stop-color="#b7c5b7"/><stop offset="1" stop-color="#6f897c"/>
    </radialGradient>
    <pattern id="tread" width="18" height="18" patternUnits="userSpaceOnUse">
      <path d="M2 7l4-4 M11 16l4-4" stroke="#dbe1c9" stroke-opacity=".2" stroke-width="1.7" stroke-linecap="round"/>
      <path d="M2 8l4-4 M11 17l4-4" stroke="#3a5347" stroke-opacity=".22" stroke-width="1.3" stroke-linecap="round"/>
    </pattern>
    <pattern id="grating" width="12" height="12" patternUnits="userSpaceOnUse">
      <rect width="12" height="12" fill="#233a32"/>
      <path d="M0 0H12V12" fill="none" stroke="#8c9e8b" stroke-width="3"/>
      <path d="M.5 1H10.5V11" fill="none" stroke="#c4cbb7" stroke-width=".8"/>
    </pattern>
    <g id="bolt">
      <circle cx=".8" cy="1" r="3.3" fill="#253c34" opacity=".45"/>
      <circle r="3.15" fill="#5e7465"/><circle cx="-.35" cy="-.4" r="2.5" fill="url(#steelRound)"/>
      <path d="M-1.15.6L1.15-.6" stroke="#394c40" stroke-width=".7"/>
    </g>
    <g id="cleat">
      <ellipse cx="3" cy="5" rx="12" ry="24" fill="url(#softShadow)"/>
      <rect x="-8" y="-14" width="16" height="28" rx="5" fill="url(#steel)" stroke="#53685a" stroke-width="1"/>
      <path d="M-4-21Q0-24 4-21L4-6Q8 0 4 6L4 21Q0 24-4 21L-4 6Q-8 0-4-6Z" fill="url(#steel)" stroke="#344e42"/>
      <path d="M-2-20V-7 M-2 8V20" stroke="#ecedda" stroke-width="1.7"/>
      <use href="#bolt" transform="translate(0 -9) scale(.6)"/><use href="#bolt" transform="translate(0 9) scale(.6)"/>
    </g>
    <g id="fairlead">
      <rect x="-7" y="-20" width="14" height="40" rx="5" fill="#344a3e"/>
      <rect x="-5.5" y="-19" width="11" height="38" rx="4" fill="url(#steel)"/>
      <rect x="-2.5" y="-12" width="5" height="24" rx="2.5" fill="#223d33"/>
      <path d="M-4-16V16" stroke="#e7e8d4" stroke-width="1"/>
    </g>
    <g id="fender">
      <rect x="-14" y="-41" width="28" height="82" rx="13" fill="url(#rubber)" stroke="#102622" stroke-width="1.5"/>
      <rect x="-5" y="-48" width="10" height="11" rx="3" fill="#283c32"/>
      <circle cy="-44" r="2" fill="#0b241e"/>
      <path d="M-7-27V26 M-3-31V31 M3-31V31 M8-24V23" stroke="#87907d" stroke-opacity=".21" fill="none"/>
      <path d="M-9-31Q0-38 9-31 M-9 31Q0 37 9 31" fill="none" stroke="#8e9380" stroke-opacity=".33"/>
      <path d="M-9-16l5 3 M0 20l5-1 M4-5l5-2" stroke="#c2bf9d" stroke-opacity=".24" stroke-width="1.1"/>
    </g>
    <g id="vent">
      <ellipse cx="3" cy="4" rx="22" ry="23" fill="url(#softShadow)"/>
      <circle r="17" fill="#667d6a"/><circle cy="-1" r="15" fill="url(#steelRound)"/>
      <circle cy="-1" r="10" fill="#425e4d"/>
      <path d="M-7-7H7 M-9-3H9 M-9 1H9 M-7 5H7" stroke="#c0cdbc" stroke-width="2"/>
      <path d="M-7-8H7 M-9-4H9 M-9 0H9 M-7 4H7" stroke="#e6e9d7" stroke-width=".7"/>
      <use href="#bolt" transform="translate(0 -13) scale(.55)"/><use href="#bolt" transform="translate(0 12) scale(.55)"/>
    </g>
    <g id="padeye">
      <ellipse rx="6" ry="9" fill="url(#steel)" stroke="#4a6050" stroke-width=".7"/>
      <ellipse rx="2.5" ry="4.5" fill="#293e30"/>
      <path d="M-3-5Q0-8 3-5" stroke="#eff0d8" fill="none"/>
    </g>
''')
    emit(f'<clipPath id="deckClip"><path d="{DECK}"/></clipPath>')
    emit(f'<clipPath id="hullClip"><path d="{HULL}"/></clipPath>')
    emit(f'<clipPath id="roofClip"><path d="{ROOF}"/></clipPath>')
    # Small, nonperiodic grain is still editable geometry, rather than a raster filter.
    emit('<pattern id="nonSlip" width="103" height="113" patternUnits="userSpaceOnUse">')
    for i in range(240):
        x, y = RNG.uniform(0, 103), RNG.uniform(0, 113)
        path(f'M{x:.2f} {y:.2f}l{RNG.uniform(.3,1.2):.2f} {RNG.uniform(-.4,.4):.2f}',
             stroke='#e1e1c8' if i % 3 else '#273d30', stroke_opacity=f'{RNG.uniform(.11,.28):.2f}',
             stroke_width=f'{RNG.uniform(.35,.9):.2f}', stroke_linecap='round')
    emit('</pattern></defs>')


def stern_platform():
    layer('boarding-platform', '01 · Stern boarding platform')
    path('M277 1468L276 1535Q280 1560 302 1568H598Q620 1560 624 1535L623 1468Z', fill='url(#darkMetal)', stroke='#20382f', stroke_width=3)
    path('M291 1479L289 1535Q292 1548 307 1554H593Q608 1548 611 1535L609 1479Z', fill='url(#steel)')
    rect(310, 1481, 280, 60, rx=4, fill='url(#grating)', stroke='#344d40', stroke_width=4)
    for x in (300, 450, 600):
        rect(x-5, 1480, 10, 67, rx=3, fill='url(#steel)')
        use('bolt', x, 1538)
    for x in (325, 575):
        path(f'M{x} 1499V1567', fill='none', stroke='#2a4437', stroke_width=7, stroke_linecap='round')
        path(f'M{x-1} 1499V1567', fill='none', stroke='url(#steel)', stroke_width=4, stroke_linecap='round')
    for y in (1518, 1544, 1566):
        path(f'M326 {y}H574', fill='none', stroke='url(#steelHorizontal)', stroke_width=5, stroke_linecap='round')
    end()


def hull_deck():
    layer('hull-and-gunwales', '02 · Teal hull and rubber rubbing strake')
    path(HULL, fill='url(#hullPaint)', stroke='#112b2d', stroke_width=5, stroke_linejoin='round')
    path(GUNWALE, fill='url(#capPaint)', stroke='#a1b6a1', stroke_width=1.5)
    path('M442 112C391 145 321 226 271 318C223 407 201 505 200 646L212 1423Q214 1468 238 1483',
         fill='none', stroke='#b9cabc', stroke_width=2.1, stroke_opacity=.7)
    path('M660 1488Q691 1473 692 1422L705 646C704 503 683 405 635 317C584 223 508 135 459 112',
         fill='none', stroke='#123b3d', stroke_width=4.5, stroke_opacity=.78)
    path(DECK, fill='url(#deckBase)', stroke='#304b3e', stroke_width=3)
    path(DECK, fill='url(#deckLight)')
    path(DECK, fill='url(#nonSlip)')
    emit('<g clip-path="url(#deckClip)">')
    path(DECK, fill='none', stroke='#2d493a', stroke_width=15, stroke_opacity=.17)
    path(DECK, fill='none', stroke='#2d493a', stroke_width=7, stroke_opacity=.31)
    for x,y,rx,ry in [(264,1050,45,230),(642,1066,51,300),(450,1450,260,55),(590,895,95,76),(450,438,189,75),(344,314,50,69),(270,685,38,189)]:
        ellipse(x,y,rx,ry,fill='url(#grime)')
    weather_flecks(1600, (220,160,680,1480), ['#d8d7b7','#c5c7a5','#3e5340','#65724f'], .19, 2.6)
    for i in range(160):
        x,y=RNG.uniform(237,663),RNG.uniform(175,1470)
        dx,dy=RNG.uniform(-5,7),RNG.uniform(3,24)
        path(f'M{x:.1f} {y:.1f}q{dx*.4:.1f} {dy*.48:.1f} {dx:.1f} {dy:.1f}',
             fill='none', stroke='#e0dcc0' if i%3 else '#435647', stroke_opacity=f'{RNG.uniform(.09,.27):.2f}', stroke_width=f'{RNG.uniform(.4,1.15):.2f}')
    end()
    end()


def deck_plates():
    layer('deck-plates', '03 · Nonslip working deck and flush access hatches')
    emit('<g clip-path="url(#deckClip)">')
    # Flush welded sheets: seams belong to the horizontal deck plane.
    for d in ['M230 877H670','M235 1150H665','M236 1401H664','M273 847L280 1466','M628 847L621 1466','M453 889V1050','M451 1269V1469','M281 393Q450 407 619 393']:
        path(d, fill='none', stroke='#d3d6bc', stroke_width=2, stroke_opacity=.41, transform='translate(-1 -1)')
        path(d, fill='none', stroke='#4b6050', stroke_width=1.35, stroke_opacity=.67)
    # Large engine hatch keeps the central aft deck visually open.
    rect(317,1064,266,260,rx=9,fill='#334d3d',fill_opacity=.14,stroke='#465c4a',stroke_width=4)
    rect(321,1067,258,252,rx=6,fill='url(#deckBase)',stroke='#c4c9ae',stroke_width=1.2)
    rect(321,1067,258,252,rx=6,fill='url(#nonSlip)')
    weather_flecks(410, (326,1073,574,1313), ['#dedabe','#3d513c','#b9bda2'], .19, 2.5)
    # Boot scuffs are incomplete, irregular strokes rather than stamped footprints.
    for x,y,angle in [(354,1202,27),(482,1254,-18),(486,1088,22),(539,1160,9)]:
        emit(f'<g transform="translate({x} {y}) rotate({angle})">')
        for off in range(7):
            path(f'M{-13+off*3} -18Q{-20+off*3} -2 {-12+off*3} 12',fill='none',stroke='#42523b',stroke_width=RNG.uniform(.4,1.3),stroke_opacity=RNG.uniform(.05,.14))
        end()
    path('M326 1313H574V1072',fill='none',stroke='#3b5140',stroke_width=1.3,stroke_opacity=.55)
    for x,y in [(331,1078),(569,1078),(331,1310),(569,1310),(331,1194),(569,1194)]:
        use('bolt',x,y,.0,.7)
    for x in (377,520):
        rect(x-15,1062,30,12,rx=2,fill='url(#steelHorizontal)',stroke='#465e4a',stroke_width=.8)
        path(f'M{x-9} 1067H{x+9}',stroke='#e3e5d0',stroke_width=1)
        use('bolt',x-10,1066,scale=.45)
        use('bolt',x+10,1066,scale=.45)
    rect(430,1284,40,17,rx=5,fill='#536452',stroke='#c4cab2',stroke_width=.8)
    rect(436,1289,28,6,rx=3,fill='#293f31')
    path('M436 1291H464',stroke='url(#steelHorizontal)',stroke_width=3)
    for x,y in [(242,966),(658,966),(247,1394),(652,1394)]:
        rect(x-7,y-15,14,30,rx=3,fill='#3e5947',stroke='#b0bba0',stroke_width=1)
        for yy in range(y-10,y+12,4):
            path(f'M{x-5} {yy}H{x+5}',stroke='#1c3627',stroke_width=1.8)
    end()
    end()


def paint_weathering():
    layer('hull-wear', '04 · Paint chips, salt marks and fasteners')
    emit('<g clip-path="url(#hullClip)">')
    for i in range(140):
        y=RNG.uniform(660,1440)
        left=i%2 == 0
        x=(204+(y-660)*.017) if left else (696-(y-660)*.017)
        x+=RNG.uniform(-5,7)
        path(f'M{x:.2f} {y:.2f}l{RNG.uniform(-1,1):.2f} {RNG.uniform(1,7):.2f}',
             stroke=RNG.choice(['#c2c5a9','#a7b49b','#224c46','#d3d2b4']),stroke_width=f'{RNG.uniform(.5,1.8):.2f}',stroke_opacity=f'{RNG.uniform(.23,.68):.2f}')
    for side in (-1,1):
        for y in range(690,1430,58):
            x=450+side*(236-(y-690)*.014)
            use('bolt',round(x,1),y,scale=.56)
        for x,y in [(298,291),(267,354),(243,424),(225,502),(216,579),(233,1451)]:
            use('bolt',x if side<0 else 900-x,y,scale=.56)
    for x in range(266,646,49):
        use('bolt',x,1491+7*(1-abs(x-450)/190),scale=.54)
    end()
    end()


def rope_coil(cx,cy,rx,ry,turns=6,angle=0):
    emit(f'<g transform="translate({cx} {cy}) rotate({angle})">')
    ellipse(3,5,rx+12,ry+10,fill='url(#softShadow)')
    for i in range(turns):
        a,b=rx-i*3.8,ry-i*3.8
        ellipse(1.2,1.7,a,b,fill='none',stroke='#3e452d',stroke_width=4.4,stroke_opacity=.48)
        ellipse(0,0,a,b,fill='none',stroke='url(#rope)',stroke_width=3.7)
        ellipse(-.5,-.65,a,b,fill='none',stroke='#efe0b1',stroke_width=.6,stroke_opacity=.65)
        ellipse(0,0,a,b,fill='none',stroke='#514e31',stroke_width=3.5,stroke_dasharray='.65 3.4',stroke_opacity=.34)
    path(f'M{-rx+2} 2C{-rx-17} 25 {-rx+13} {ry+26} {rx+8} {ry+29}',fill='none',stroke='#45513a',stroke_width=4.3,stroke_opacity=.7)
    path(f'M{-rx+1} 1C{-rx-16} 24 {-rx+14} {ry+25} {rx+9} {ry+28}',fill='none',stroke='url(#rope)',stroke_width=3)
    path(f'M{-rx+1} 1C{-rx-16} 24 {-rx+14} {ry+25} {rx+9} {ry+28}',fill='none',stroke='#504b2f',stroke_width=2.6,stroke_dasharray='.7 3',stroke_opacity=.45)
    end()


def bow_equipment():
    layer('foredeck', '05 · Anchor roller, chain, windlass and mooring line')
    # Bow fitting and short roller align exactly with the fore/aft centreline.
    path('M434 172L438 92Q450 77 462 92L466 172Z',fill='#243c32',stroke='#192e28',stroke_width=2)
    path('M439 167L442 96Q450 89 458 96L461 167Z',fill='url(#steel)',stroke='#c2cab3',stroke_width=1)
    rect(444,105,12,47,rx=3,fill='#243f36')
    rect(440,118,20,12,rx=3,fill='url(#steelHorizontal)')
    for x,y in [(443,153),(457,153),(443,168),(457,168)]:
        use('bolt',x,y,scale=.65)
    # Anchor shank and flukes viewed from above, with no projected side face.
    path('M447 150L447 206L432 226L425 218L432 199L435 203L444 190V150Z',fill='url(#steel)',stroke='#476052',stroke_width=1)
    path('M453 150L453 206L468 226L475 218L468 199L465 203L456 190V150Z',fill='url(#steel)',stroke='#476052',stroke_width=1)
    # Locker plate beneath windlass.
    path('M395 254Q450 238 505 254L529 388Q450 405 371 388Z',fill='#9ba18d',stroke='#465c47',stroke_width=2)
    path('M399 259Q450 245 501 259L524 383Q450 398 376 383Z',fill='url(#tread)',stroke='#c7ccb2',stroke_width=1)
    for x,y in [(400,265),(500,265),(383,380),(517,380)]:
        use('bolt',x,y,scale=.68)
    rect(427,365,46,13,rx=3,fill='url(#steelHorizontal)',stroke='#48604b',stroke_width=.8)
    rect(438,368,24,7,rx=2,fill='#3c503b')
    # Alternating flat/edge chain links.
    for i in range(18):
        y=174+i*7.1
        ellipse(450+(i%3-1)*.7,y,3 if i%2 else 4.5,5.2,fill='none',stroke='#3c4b35',stroke_width=2.6)
        ellipse(449.4+(i%3-1)*.7,y-.7,2.7 if i%2 else 4.2,4.7,fill='none',stroke='#bcc1a3',stroke_width=1.2)
    ellipse(460,323,53,33,fill='url(#softShadow)')
    rect(417,299,78,40,rx=10,fill='url(#steel)',stroke='#51644c',stroke_width=1.5)
    rect(471,299,24,40,rx=9,fill='url(#darkMetal)')
    for x in range(476,493,4):
        path(f'M{x} 305V332',stroke='#859381',stroke_width=1,stroke_opacity=.75)
    circle(444,315,25,fill='#3f5643',stroke='#b9c5aa',stroke_width=1.4)
    circle(444,313,21,fill='url(#steelRound)',stroke='#405842',stroke_width=1)
    circle(444,313,13,fill='#4a634a',stroke='#e1e4c7',stroke_width=1)
    circle(444,312,8,fill='url(#steelRound)')
    for i in range(8):
        a=i*math.tau/8
        use('bolt',round(444+17*math.cos(a),2),round(313+17*math.sin(a),2),scale=.55)
    use('cleat',350,337,rotate=25,scale=.9)
    use('cleat',550,337,rotate=-25,scale=.9)
    rope_coil(550,398,28,36,5,-22)
    end()


def cabin():
    layer('cabin-roof', '06 · Pilothouse roof — vertical overhead projection')
    # Tight contact shadows and directional cast shadows are separate vector shapes.
    emit('<g clip-path="url(#deckClip)">')
    for dx,dy,op in [(14,25,.08),(11,20,.1),(8,15,.13),(5,9,.19)]:
        path(ROOF,transform=f'translate({dx} {dy})',fill='#173d2f',fill_opacity=op)
    end()
    path(ROOF,fill='#233f34',stroke='#233c32',stroke_width=10)
    path(ROOF,fill='url(#ivory)',stroke='#879988',stroke_width=3)
    path(ROOF,fill='url(#roofLight)')
    emit('<g clip-path="url(#roofClip)">')
    path(ROOF,fill='none',stroke='#577968',stroke_width=13,stroke_opacity=.26)
    path(ROOF,fill='none',stroke='#eef0dc',stroke_width=5,stroke_opacity=.86,transform='translate(1 1)')
    for x in (316,583):
        path(f'M{x} 477L{x + (-8 if x<450 else 8)} 813',fill='none',stroke='#8d9e86',stroke_width=1,stroke_opacity=.5)
        path(f'M{x+2} 477L{x+2 + (-8 if x<450 else 8)} 813',fill='none',stroke='#f1f0d9',stroke_width=1.4,stroke_opacity=.66)
    for x,y,rx,ry in [(321,450,21,18),(600,811,30,41),(297,793,21,56),(576,448,44,24),(460,827,158,15),(390,552,47,28)]:
        ellipse(x,y,rx,ry,fill='url(#grime)')
    weather_flecks(1250, (283,432,618,850), ['#7c8265','#c1bc94','#ffffe8','#969b7b'], .16, 1.8)
    for i in range(160):
        x=RNG.uniform(293,610)
        y=RNG.choice([RNG.uniform(442,454),RNG.uniform(831,847)])
        path(f'M{x:.1f} {y:.1f}l{RNG.uniform(1,5):.1f} {RNG.uniform(-.5,.5):.1f}',stroke=RNG.choice(['#888d71','#f8f4da','#b0a383']),stroke_width=RNG.uniform(.35,1.3),stroke_opacity=RNG.uniform(.16,.42))
    for i in range(125):
        x,y=RNG.uniform(294,607),RNG.uniform(449,839)
        if i%4==0:
            ellipse(x,y,RNG.uniform(.4,1.5),RNG.uniform(.6,2.1),fill='#757d57',fill_opacity=RNG.uniform(.12,.27))
        else:
            path(f'M{x:.1f} {y:.1f}l{RNG.uniform(-1,1):.2f} {RNG.uniform(2,9):.2f}',stroke='#697e61' if i%3 else '#ffffe8',stroke_width=RNG.uniform(.3,.7),stroke_opacity=RNG.uniform(.06,.16))
    end()
    for x,y in [(304,467),(596,467),(299,536),(601,536),(295,639),(605,639),(293,742),(607,742),(302,829),(598,829),(400,840),(500,840)]:
        ellipse(x+1,y+5,5,12,fill='url(#rust)')
        use('bolt',x,y,scale=.63)
    # Hatch is horizontal roof glazing, not an exposed vertical windshield.
    rect(379,660,143,114,rx=9,fill='#1b392f',fill_opacity=.24,transform='translate(5 7)')
    rect(378,659,142,111,rx=9,fill='url(#steel)',stroke='#586e59',stroke_width=2)
    rect(386,667,126,95,rx=4,fill='#213a30')
    rect(391,672,116,85,rx=3,fill='url(#glass)',stroke='#8ea89a',stroke_width=.8)
    path('M396 676H491L396 739Z',fill='#c4d7c8',fill_opacity=.17)
    path('M398 676H500L398 697Z',fill='#ebf1db',fill_opacity=.15)
    path('M408 751L501 685 M417 751L501 694',stroke='#dae6ce',stroke_width=1,stroke_opacity=.14)
    rect(405,654,22,11,rx=2,fill='url(#steelHorizontal)',stroke='#58715b',stroke_width=.8)
    rect(472,654,22,11,rx=2,fill='url(#steelHorizontal)',stroke='#58715b',stroke_width=.8)
    rect(439,763,25,7,rx=2,fill='url(#steelHorizontal)',stroke='#3c5946',stroke_width=.7)
    for x,y in [(382,665),(516,665),(382,763),(516,763)]:
        use('bolt',x,y,scale=.5)
    use('vent',345,750,scale=.87)
    use('vent',555,784,scale=.82)
    # Horizontal grab rails on the roof, with all mounting feet seen from above.
    for x in (325,575):
        for y in (609,794):
            ellipse(x+2,y+3,6,10,fill='url(#softShadow)')
            rect(x-4,y-7,8,14,rx=3,fill='url(#steel)')
            use('bolt',x,y,scale=.55)
        path(f'M{x+4} 610V793',stroke='#2d4a37',stroke_width=4,stroke_opacity=.22)
        path(f'M{x} 610V793',stroke='url(#steel)',stroke_width=4.5,stroke_linecap='round')
        path(f'M{x-1} 612V791',stroke='#f6f4da',stroke_width=1,stroke_opacity=.8)
    end()


def rooftop_equipment():
    layer('roof-equipment', '07 · Radar, antennas and secured liferaft')
    # A compact canister lives across the front of the wheelhouse roof.
    rect(365,557,183,59,rx=26,fill='#214332',fill_opacity=.11)
    rect(361,550,180,58,rx=26,fill='#1b392b',fill_opacity=.16)
    for x in (391,509):
        rect(x-13,543,26,64,rx=4,fill='url(#steel)',stroke='#71856c',stroke_width=1)
    rect(359,540,182,61,rx=28,fill='url(#ivory)',stroke='#8b9f86',stroke_width=1.5)
    path('M386 543H514Q535 547 537 567',fill='none',stroke='#fffde9',stroke_width=1.8,stroke_opacity=.88)
    path('M362 574H538',fill='none',stroke='#667f68',stroke_width=1,stroke_opacity=.55)
    path('M369 580Q376 596 391 597H510Q529 595 535 580',fill='none',stroke='#829680',stroke_width=1.4,stroke_opacity=.55)
    for x in (393,507):
        rect(x-4,540,8,61,rx=2,fill='#879985',fill_opacity=.77)
        path(f'M{x-2} 542V598',stroke='#e4e7ce',stroke_width=1.3)
        rect(x-6,567,12,12,rx=2,fill='url(#steel)',stroke='#687e63',stroke_width=.7)
        rect(x-2,570,4,6,rx=1,fill='#6b7e61')
    rect(433,553,37,12,rx=2,fill='#668476',fill_opacity=.5)
    path('M440 559H464 M445 562H459',stroke='#dde2c9',stroke_width=1,stroke_opacity=.9)
    # Radar pedestal and top of a scanner bar. No perspective tilt.
    ellipse(457,503,41,24,fill='url(#softShadow)')
    circle(450,493,22,fill='url(#steelRound)',stroke='#637c64',stroke_width=1)
    circle(450,490,17,fill='url(#whiteDome)')
    rect(344,477,220,24,rx=10,fill='#2e503d',fill_opacity=.18,transform='translate(8 10)')
    rect(339,473,222,22,rx=9,fill='url(#ivory)',stroke='#6f866d',stroke_width=1.2)
    path('M348 476H552',stroke='#fffdeb',stroke_width=2.3,stroke_linecap='round')
    path('M348 491H552',stroke='#758e73',stroke_width=1,stroke_opacity=.65)
    for x in (351,549):
        path(f'M{x} 475V492',stroke='#819780',stroke_width=1,stroke_opacity=.63)
    # Vertical antennas foreshorten to small circular bases; their cast shadows carry height.
    for x,y in [(319,511),(586,610)]:
        path(f'M{x} {y}l24 54',stroke='#244b35',stroke_width=2,stroke_opacity=.18)
        circle(x,y,7,fill='url(#steelRound)',stroke='#5d745d',stroke_width=.8)
        circle(x,y,3.5,fill='#e6e8d1')
        circle(x-1,y-1,1.2,fill='#fffde9')
    # Navigation-light housings are horizontal footprints on the roof edge.
    for x,color in [(291,'#b94f39'),(609,'#507e59')]:
        rect(x-5,586,10,23,rx=4,fill='#2f4935',stroke='#8ba083',stroke_width=1)
        rect(x-3,589,6,17,rx=3,fill=color)
        path(f'M{x-2} 592V600',stroke='#fff0b0',stroke_width=1.3,stroke_opacity=.68)
    end()


def aft_equipment():
    layer('working-deck-equipment', '08 · Perimeter working gear and open cargo deck')
    # Low transverse storage bench behind the cabin.
    rect(320,868,273,72,rx=9,fill='#1d3f2c',fill_opacity=.14)
    rect(314,865,270,62,rx=7,fill='url(#hullPaint)',stroke='#2c5141',stroke_width=2)
    rect(314,859,270,61,rx=6,fill='url(#ivory)',stroke='#809680',stroke_width=1.4)
    path('M319 864H578 M319 914H578',stroke='#eff0d4',stroke_width=1.2,stroke_opacity=.8)
    path('M450 862V917',stroke='#778e75',stroke_width=1)
    for x in (349,547):
        rect(x-8,911,16,8,rx=2,fill='url(#steelHorizontal)',stroke='#607b60',stroke_width=.7)
        use('bolt',x,914,scale=.42)
    for x,y in [(324,870),(574,870),(324,909),(574,909)]:
        use('bolt',x,y,scale=.52)
    # Small stern-side winch: round drum, flanges, gearbox and deck socket.
    ellipse(300,995,47,57,fill='url(#softShadow)')
    rect(258,957,66,63,rx=7,fill='url(#steel)',stroke='#465f44',stroke_width=1.4)
    for x,y in [(265,964),(317,964),(265,1013),(317,1013)]:
        use('bolt',x,y,scale=.75)
    circle(288,985,31,fill='url(#darkMetal)',stroke='#b8c6a7',stroke_width=1.4)
    circle(288,983,26,fill='url(#steelRound)',stroke='#364f37',stroke_width=1)
    for r in range(11,25,3):
        circle(288,983,r,fill='none',stroke='#47533a',stroke_width=1.5)
        path(f'M{288-r} 983A{r} {r} 0 0 1 {288+r} 983',fill='none',stroke='#ccd1aa',stroke_width=.7)
    circle(288,983,8,fill='url(#steelRound)',stroke='#506649',stroke_width=1)
    rect(312,971,22,25,rx=5,fill='url(#darkMetal)',stroke='#526847',stroke_width=1)
    for yy in range(975,993,4):
        path(f'M318 {yy}H330',stroke='#95a388',stroke_width=.9)
    # A neatly stowed mooring line, away from the central hatch.
    rope_coil(613,995,24,38,5,9)
    # Wooden working strips protect the port walkway.
    for x in (251,265,279):
        rect(x+3,1112,12,186,rx=2,fill='#24432d',fill_opacity=.2)
        rect(x,1108,12,185,rx=2,fill='url(#wood)',stroke='#687452',stroke_width=.7)
        for i in range(6):
            xx=x+RNG.uniform(1,11)
            path(f'M{xx:.1f} 1114q{RNG.uniform(-2,2):.1f} 81 0 172',fill='none',stroke='#d5c99a' if i%2 else '#3e523b',stroke_width=.55,stroke_opacity=.35)
        for yy in (1118,1199,1281):
            use('bolt',x+6,yy,scale=.45)
    # Closed utility case, starboard. Horizontal lid only.
    rect(605,1147,49,112,rx=6,fill='#1e3d2d',fill_opacity=.25)
    rect(597,1139,49,111,rx=5,fill='url(#orange)',stroke='#775a37',stroke_width=1.3)
    rect(602,1144,39,101,rx=3,fill='none',stroke='#f0b46d',stroke_width=1.2,stroke_opacity=.61)
    for y in range(1157,1235,12):
        path(f'M606 {y}H637',stroke='#90512e',stroke_width=2.3,stroke_opacity=.45)
        path(f'M606 {y-1}H637',stroke='#ffc683',stroke_width=.65,stroke_opacity=.48)
    for yy in (1154,1232):
        rect(595,yy,6,12,rx=2,fill='url(#steel)',stroke='#657355',stroke_width=.5)
    rect(640,1180,8,29,rx=3,fill='#4e5739')
    rect(642,1186,3,17,rx=1,fill='#d2b57b')
    # Stern rope coil and hose mounted in discrete groups, all editable.
    rope_coil(297,1375,27,33,5,-12)
    for r in range(17,35,4):
        ellipse(614,1365,r,r*1.3,fill='none',stroke='#173b2c',stroke_width=4.3)
        ellipse(613.4,1364.3,r,r*1.3,fill='none',stroke='#55796a',stroke_width=1.2,stroke_opacity=.8)
    path('M643 1380C665 1409 638 1431 609 1430',fill='none',stroke='#1e4332',stroke_width=5,stroke_linecap='round')
    path('M643 1379C665 1408 638 1430 609 1429',fill='none',stroke='#7c9780',stroke_width=1.1,stroke_opacity=.6)
    rect(603,1425,13,8,rx=2,fill='url(#steel)',stroke='#455e3b',stroke_width=.7)
    # Flush stern access hatch with quiet fine tread, leaving the deck unoccupied.
    rect(380,1373,140,67,rx=5,fill='#82917a',stroke='#405b42',stroke_width=1.4)
    rect(384,1377,132,59,rx=3,fill='url(#tread)',stroke='#c6cbb0',stroke_width=.8)
    rect(432,1418,36,11,rx=4,fill='url(#steelHorizontal)',stroke='#536d4e',stroke_width=.7)
    rect(439,1421,22,5,rx=2,fill='#405539')
    for x,y in [(388,1382),(512,1382),(388,1431),(512,1431)]:
        use('bolt',x,y,scale=.55)
    end()


def life_ring():
    layer('lifebuoy', '09 · Lifebuoy secured beside the wheelhouse')
    cx,cy=651,781
    ellipse(cx+4,cy+5,30,48,fill='url(#softShadow)')
    # A circular ring really is circular in plan: no perspective squashing.
    circle(cx,cy,28,fill='none',stroke='#49503a',stroke_width=14)
    circle(cx,cy-1,28,fill='none',stroke='url(#orangeRound)',stroke_width=12)
    circle(cx-1,cy-2,28,fill='none',stroke='#efb270',stroke_width=1.1,stroke_opacity=.67)
    for a in range(0,360,90):
        emit(f'<g transform="translate({cx} {cy-1}) rotate({a})">')
        path('M-5-22L-6-34Q0-35 6-34L5-22Q0-21-5-22Z',fill='url(#ivory)',stroke='#af9c74',stroke_width=.6)
        path('M-3-23L-4-33',stroke='#fff0c4',stroke_width=1)
        end()
    circle(cx,cy-1,37,fill='none',stroke='#b6ab7e',stroke_width=2)
    for a in range(0,360,90):
        rad=a*math.pi/180
        x,y=cx+37*math.sin(rad),cy-1+37*math.cos(rad)
        path(f'M{x:.1f} {y:.1f}L{cx+32*math.sin(rad):.1f} {cy-1+32*math.cos(rad):.1f}',stroke='#d5c397',stroke_width=2)
    path(f'M{cx-23} {cy-28}L{cx+23} {cy+28}',stroke='#4c6550',stroke_width=3)
    path(f'M{cx-22} {cy-28}L{cx+24} {cy+28}',stroke='#8b9b79',stroke_width=1)
    end()


def deck_rails():
    layer('rails-and-cleats', '10 · Stainless rails, cleats and boarding gate')
    rail_paths=[
        'M438 154C380 199 322 278 280 363C240 447 224 526 224 616',
        'M462 154C520 199 578 278 620 363C660 447 676 526 676 616',
        'M220 661L226 982',
        'M228 1082L234 1429Q234 1452 253 1463H341',
        'M680 661L666 1429Q666 1452 647 1463H559',
    ]
    for d in rail_paths:
        path(d,fill='none',stroke='#244633',stroke_width=5,stroke_opacity=.23,transform='translate(7 10)',stroke_linecap='round')
    posts=[(403,188),(350,247),(297,330),(257,419),(234,516),(224,606),(220,673),(222,807),(225,949),(229,1093),(231,1256),(234,1415),(262,1463),(328,1463)]
    posts+= [(900-x,y) for x,y in posts if y<1050 or y>1400]
    posts += [(673,1074),(670,1232)]
    for x,y in posts:
        ellipse(x+2,y+3,7,8,fill='url(#softShadow)')
        circle(x,y,5,fill='url(#steelRound)',stroke='#577355',stroke_width=.7)
    for d in rail_paths:
        path(d,fill='none',stroke='#465f4e',stroke_width=5.2,stroke_linecap='round')
        path(d,fill='none',stroke='url(#steel)',stroke_width=3.6,stroke_linecap='round')
        path(d,fill='none',stroke='#f0efda',stroke_width=.85,stroke_opacity=.72,stroke_linecap='round',transform='translate(-.8 -.8)')
    # The port diver entry has a chain instead of a rigid rail.
    path('M226 984Q249 1033 228 1080',fill='none',stroke='#334e38',stroke_width=2.5)
    path('M226 984Q249 1033 228 1080',fill='none',stroke='#bfccb1',stroke_width=1.7,stroke_dasharray='3 3')
    for x,y,rot in [(244,707,0),(656,707,0),(249,1297,0),(650,1297,0),(285,1477,90),(615,1477,90)]:
        ellipse(x+2,y+5,12,31,fill='url(#rust)')
        use('cleat',x,y,rotate=rot,scale=.86)
    for x,y in [(207,828),(693,828),(212,1190),(688,1190)]:
        use('fairlead',x,y,scale=.85)
    # Stern rail surrounds the open centre boarding gate.
    for x in (352,548):
        rect(x-5,1454,10,28,rx=3,fill='url(#steel)',stroke='#627754',stroke_width=.8)
        use('bolt',x,1459,scale=.63)
    path('M357 1465Q450 1480 543 1465',fill='none',stroke='#4e6344',stroke_width=2.5)
    path('M357 1464Q450 1479 543 1464',fill='none',stroke='#ccd0ad',stroke_width=1.4,stroke_dasharray='4 3')
    end()


def outer_fenders():
    layer('hanging-fenders', '11 · Rubber fenders and attachment lines')
    for x,y,rot in [(185,694,1),(190,882,1),(200,1285,-1),(715,691,-1),(710,936,-1),(700,1325,1)]:
        use('fender',x,y,rotate=rot,scale=.86)
        inside=x+25 if x<450 else x-25
        path(f'M{x} {y-38}Q{inside} {y-63} {inside} {y-76}',fill='none',stroke='#374d33',stroke_width=3)
        path(f'M{x-.6} {y-38}Q{inside-.6} {y-63} {inside-.6} {y-76}',fill='none',stroke='#b7b285',stroke_width=1.6)
        use('padeye',inside,y-76,scale=.65)
    end()


def write_art():
    definitions()
    stern_platform()
    hull_deck()
    deck_plates()
    paint_weathering()
    bow_equipment()
    cabin()
    rooftop_equipment()
    aft_equipment()
    life_ring()
    deck_rails()
    outer_fenders()
    emit('</svg>')
    return '\n'.join(PARTS) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replace-generated', action='store_true', help='Replace only the review SVG, never canonical game artwork.')
    args = parser.parse_args()
    mode = 'w' if args.replace_generated else 'x'
    svg = write_art()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with DESTINATION.open(mode, encoding='utf-8') as handle:
        handle.write(svg)
    print(f'{DESTINATION.name}: {len(svg.encode("utf-8")):,} bytes; vector-only; 1800 × 3360 default size.')
