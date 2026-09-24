#!/usr/bin/env python3
"""Create the Reef Runner vector study from its designer-supplied fleet reference.

Uses the first boat's vector material/fitting helpers without changing that art.
Python standard library only. Existing output is preserved unless the explicit
--replace-generated flag is supplied. No image tracing or embedded bitmap.
"""

from pathlib import Path
import argparse
import importlib.util
import math
import sys


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('boat_vector_materials', ROOT / 'create-workboat.py')
art = importlib.util.module_from_spec(spec)
spec.loader.exec_module(art)
emit, path, rect = art.emit, art.path, art.rect
circle, ellipse, use = art.circle, art.ellipse, art.use
layer, end, flecks = art.layer, art.end, art.weather_flecks
rng = art.RNG

HULL = 'M264 112Q450 95 636 112Q678 116 686 153Q701 247 700 419L696 1321Q696 1382 674 1409Q450 1437 226 1409Q204 1382 204 1321L200 419Q199 247 214 153Q222 116 264 112Z'
CAP = 'M264 127Q450 111 636 127Q666 130 672 159Q686 250 685 419L682 1320Q682 1373 664 1396Q450 1422 236 1396Q218 1373 218 1320L215 419Q214 250 228 159Q234 130 264 127Z'
DECK = 'M267 153Q450 140 633 153Q644 155 647 172Q660 260 659 420L656 1318Q656 1359 644 1373Q450 1397 256 1373Q244 1359 244 1318L241 420Q240 260 253 172Q256 155 267 153Z'
ROOF = 'M291 1164Q450 1156 609 1164Q628 1166 630 1183L639 1410Q639 1429 620 1434Q450 1448 280 1434Q261 1429 261 1410L270 1183Q272 1166 291 1164Z'


def definitions():
    art.HULL, art.DECK, art.ROOF = HULL, DECK, ROOF
    art.definitions()
    emit('''<defs>
  <linearGradient id="reefBlue" x1="0" x2="1" y1="0" y2=".12">
    <stop stop-color="#17344c"/><stop offset=".07" stop-color="#517e9b"/>
    <stop offset=".17" stop-color="#3a7096"/><stop offset=".45" stop-color="#3d7196"/>
    <stop offset=".79" stop-color="#2a5679"/><stop offset=".96" stop-color="#214661"/><stop offset="1" stop-color="#152e42"/>
  </linearGradient>
  <linearGradient id="blueCap" x1="0" x2="1" y1="0" y2=".24">
    <stop stop-color="#90a8b2"/><stop offset=".08" stop-color="#7da0b3"/>
    <stop offset=".34" stop-color="#5686a3"/><stop offset=".72" stop-color="#4f7896"/><stop offset="1" stop-color="#305875"/>
  </linearGradient>
  <linearGradient id="aluminium" x1="0" x2=".83" y1="0" y2="1">
    <stop stop-color="#bbc0bb"/><stop offset=".3" stop-color="#a5ada9"/><stop offset=".66" stop-color="#999f9c"/><stop offset="1" stop-color="#737f7d"/>
  </linearGradient>
  <linearGradient id="steelCool" x1="0" x2="1" y1="0" y2=".15">
    <stop stop-color="#50636b"/><stop offset=".14" stop-color="#a6b7bd"/>
    <stop offset=".28" stop-color="#eff0e2"/><stop offset=".49" stop-color="#98a9b0"/>
    <stop offset=".73" stop-color="#c6d1cb"/><stop offset="1" stop-color="#526c76"/>
  </linearGradient>
  <linearGradient id="steelAcross" x1="0" x2="0" y1="0" y2="1">
    <stop stop-color="#4e656c"/><stop offset=".25" stop-color="#e3e6dc"/>
    <stop offset=".46" stop-color="#b8c4c1"/><stop offset=".8" stop-color="#71868a"/><stop offset="1" stop-color="#465d68"/>
  </linearGradient>
  <radialGradient id="deckIllumination" cx=".32" cy=".21" r=".87">
    <stop stop-color="#f5efdb" stop-opacity=".17"/><stop offset=".6" stop-color="#d2d6c9" stop-opacity="0"/><stop offset="1" stop-color="#34464a" stop-opacity=".19"/>
  </radialGradient>
  <linearGradient id="hatchMetal" x1="0" x2=".9" y1="0" y2="1">
    <stop stop-color="#a7b0b1"/><stop offset=".46" stop-color="#909b9e"/><stop offset="1" stop-color="#6f8083"/>
  </linearGradient>
  <linearGradient id="roofIvory" x1="0" x2=".72" y1="0" y2="1">
    <stop stop-color="#f0ecdf"/><stop offset=".39" stop-color="#e4e1d4"/><stop offset=".81" stop-color="#d4d6c9"/><stop offset="1" stop-color="#a8b6ae"/>
  </linearGradient>
  <linearGradient id="floatBlue" x1="0" x2="1" y1="0" y2=".15">
    <stop stop-color="#213f54"/><stop offset=".14" stop-color="#5689a7"/><stop offset=".38" stop-color="#95b5c4"/>
    <stop offset=".59" stop-color="#5a8cac"/><stop offset=".85" stop-color="#376482"/><stop offset="1" stop-color="#234760"/>
  </linearGradient>
  <linearGradient id="ochre" x1="0" x2=".78" y1="0" y2="1">
    <stop stop-color="#efcd74"/><stop offset=".4" stop-color="#d2aa4d"/><stop offset=".83" stop-color="#a07e37"/><stop offset="1" stop-color="#735e35"/>
  </linearGradient>
  <radialGradient id="rustCool">
    <stop stop-color="#816246" stop-opacity=".7"/><stop offset=".35" stop-color="#a68661" stop-opacity=".33"/><stop offset="1" stop-color="#aa8a64" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="saltBloom">
    <stop stop-color="#e4e4d3" stop-opacity=".2"/><stop offset=".53" stop-color="#cdd1c4" stop-opacity=".1"/><stop offset="1" stop-color="#cdd1c4" stop-opacity="0"/>
  </radialGradient>
  <pattern id="diamondPlate" width="13" height="13" patternUnits="userSpaceOnUse" patternTransform="rotate(5)">
    <path d="M2 4L5 1 M8 11L11 8" stroke="#435e63" stroke-opacity=".3" stroke-width="2.1" stroke-linecap="round"/>
    <path d="M1.5 3.5L4.5 .5 M7.5 10.5L10.5 7.5" stroke="#dbe1d9" stroke-opacity=".54" stroke-width="1.2" stroke-linecap="round"/>
  </pattern>
  <pattern id="catchNet" width="11" height="11" patternUnits="userSpaceOnUse">
    <rect width="11" height="11" fill="#2d4141"/>
    <path d="M-5.5 5.5L5.5-5.5 M0 11L11 0 M5.5 16.5L16.5 5.5 M-5.5 5.5L5.5 16.5 M0 0L11 11 M5.5-5.5L16.5 5.5" stroke="#738578" stroke-width="1" stroke-opacity=".7"/>
    <path d="M0 0L11 11" stroke="#a9ad85" stroke-width=".5" stroke-opacity=".44"/>
  </pattern>
  <clipPath id="frontHatchClip"><rect x="311" y="305" width="278" height="193" rx="6"/></clipPath>
  <clipPath id="rearHatchClip"><rect x="311" y="751" width="278" height="199" rx="6"/></clipPath>
  <clipPath id="netClip"><rect x="351" y="1049" width="198" height="99" rx="3"/></clipPath>
</defs>''')


def drive_and_stern():
    layer('stern-drive', '01 · Exposed sterndrive and stern hardware')
    path('M267 1390L266 1458Q270 1478 292 1480H608Q630 1478 634 1458L633 1390Z', fill='url(#reefBlue)', stroke='#283f4a', stroke_width=3)
    path('M283 1398V1452Q283 1464 299 1465H601Q617 1464 617 1452V1398Z', fill='url(#steelCool)', stroke='#6d8285', stroke_width=1.2)
    rect(303,1428,294,30,rx=3,fill='url(#grating)',stroke='#4c6870',stroke_width=2)
    for x in (293,606):
        rect(x-4,1407,8,61,rx=3,fill='url(#steelCool)',stroke='#4e6567',stroke_width=1)
        for y in (1414,1460):
            use('bolt',x,y,scale=.7)
    # Rubber bellows and transom plate of the steerable outdrive.
    rect(410,1449,80,35,rx=8,fill='url(#steelCool)',stroke='#385363',stroke_width=2)
    rect(422,1463,56,53,rx=17,fill='url(#rubber)',stroke='#20383d',stroke_width=2)
    for y in range(1472,1507,6):
        path(f'M426 {y}Q450 {y+6}474 {y}', fill='none',stroke='#60747b',stroke_width=2)
        path(f'M426 {y+1}Q450 {y+7}474 {y+1}',fill='none',stroke='#142b32',stroke_width=1)
    path('M432 1492Q450 1484 468 1492L474 1536L467 1560H433L426 1536Z',fill='url(#steelCool)',stroke='#3b5560',stroke_width=2)
    path('M440 1500H460L466 1536H434Z',fill='#7e979e',stroke='#cad4ce',stroke_width=.9)
    path('M403 1525L426 1518H474L497 1525L492 1544H408Z',fill='url(#steelCool)',stroke='#4f6c75',stroke_width=1.5)
    path('M407 1526H493',stroke='#e0e5d8',stroke_width=1.5,stroke_opacity=.82)
    path('M443 1538L438 1576Q450 1583 462 1576L457 1538Z',fill='url(#darkMetal)',stroke='#536c71',stroke_width=1.2)
    path('M446 1544V1572',stroke='#bac8c4',stroke_width=1.7)
    for x,y in [(416,1458),(484,1458),(438,1500),(462,1500)]:
        use('bolt',x,y,scale=.68)
    end()


def hull_and_deck():
    layer('blue-hull', '02 · Square bow, blue hull and gunwales')
    path(HULL,fill='url(#reefBlue)',stroke='#1e3546',stroke_width=5,stroke_linejoin='round')
    path(CAP,fill='url(#blueCap)',stroke='#a4b8be',stroke_width=1.2)
    path('M258 122Q450 107 638 122Q670 126 677 154',fill='none',stroke='#dae2d9',stroke_width=2.3,stroke_opacity=.68)
    path('M224 168Q207 294 209 443L212 1323Q213 1384 233 1401',fill='none',stroke='#aec2c7',stroke_width=2.2,stroke_opacity=.73)
    path('M676 166Q693 294 691 443L688 1323Q687 1384 667 1401',fill='none',stroke='#183a54',stroke_width=4,stroke_opacity=.7)
    path(DECK,fill='url(#aluminium)',stroke='#3f5660',stroke_width=3)
    path(DECK,fill='url(#deckIllumination)')
    path(DECK,fill='url(#nonSlip)')
    emit('<g clip-path="url(#deckClip)">')
    path(DECK,fill='none',stroke='#314953',stroke_width=16,stroke_opacity=.13)
    path(DECK,fill='none',stroke='#32454a',stroke_width=7,stroke_opacity=.31)
    for x,y,rx,ry in [(260,560,32,350),(638,680,46,393),(450,155,230,29),(450,1017,166,37),(289,221,41,51),(604,223,46,54)]:
        ellipse(x,y,rx,ry,fill='url(#grime)')
    for x,y,rx,ry in [(303,565,90,107),(514,656,140,90),(400,978,62,91)]:
        ellipse(x,y,rx,ry,fill='url(#saltBloom)')
    flecks(2000,(246,157,654,1368),['#e0e1d5','#56676a','#a49a83','#7d8580'],.21,2.7)
    for i in range(200):
        x,y=rng.uniform(251,649),rng.uniform(169,1330)
        path(f'M{x:.1f} {y:.1f}q{rng.uniform(-3,3):.1f} 6 {rng.uniform(-7,7):.1f} {rng.uniform(9,27):.1f}',fill='none',stroke='#e2e4d9' if i%3 else '#53686c',stroke_width=rng.uniform(.45,1.3),stroke_opacity=rng.uniform(.12,.34))
    end()
    end()


def weld(d):
    path(d,fill='none',stroke='#c8d0c6',stroke_width=3.2,stroke_opacity=.6,transform='translate(-.8 -.8)')
    path(d,fill='none',stroke='#606e6b',stroke_width=1.6,stroke_opacity=.77)
    path(d,fill='none',stroke='#dddcc9',stroke_width=2.2,stroke_dasharray='1 3.6',stroke_opacity=.29)


def hatches():
    layer('welded-deck', '03 · Welded aluminium deck and two large service hatches')
    emit('<g clip-path="url(#deckClip)">')
    for d in ['M246 269H654','M246 525H654','M246 638H654','M246 988H654','M253 1136H647','M338 151V269','M450 151V269','M562 151V269','M303 525V738','M593 525V738','M450 526V638']:
        weld(d)
    for x,y in [(254,269),(646,269),(301,526),(593,526),(304,638),(593,638),(251,988),(649,988),(450,269),(450,638)]:
        ellipse(x,y+7,13,27,fill='url(#rustCool)')
    end()
    for y,height,clip in [(298,208,'frontHatchClip'),(744,214,'rearHatchClip')]:
        rect(308,y+4,291,height+3,rx=11,fill='#2d4148',fill_opacity=.16)
        rect(301,y,298,height,rx=10,fill='url(#steelCool)',stroke='#495d60',stroke_width=3)
        rect(307,y+5,286,height-10,rx=7,fill='#465859')
        rect(311,y+7,278,height-14,rx=6,fill='url(#hatchMetal)',stroke='#c1cac3',stroke_width=1)
        rect(311,y+7,278,height-14,rx=6,fill='url(#diamondPlate)')
        emit(f'<g clip-path="url(#{clip})">')
        flecks(360,(311,y+7,589,y+height-7),['#d9ddd3','#526166','#acaf9f'],.19,2.3)
        for i in range(20):
            xx,yy=rng.uniform(320,580),rng.uniform(y+14,y+height-18)
            path(f'M{xx:.1f} {yy:.1f}l{rng.uniform(-12,12):.1f} {rng.uniform(3,12):.1f}',stroke='#d3d7cd',stroke_width=.7,stroke_opacity=.36)
        end()
        for x,yy in [(311,y+12),(589,y+12),(311,y+height-12),(589,y+height-12),(450,y+10),(450,y+height-10)]:
            ellipse(x+1,yy+4,9,11,fill='url(#rustCool)')
            use('bolt',x,yy,scale=.77)
        for x in (359,541):
            rect(x-13,y-3,26,12,rx=2,fill='url(#steelAcross)',stroke='#5d7375',stroke_width=.8)
            path(f'M{x-11} {y+1}H{x+11}',stroke='#e4e8db',stroke_width=1)
            for dx in (-8,8):
                use('bolt',x+dx,y+1,scale=.42)
        rect(432,y+height-21,36,13,rx=4,fill='#728185',stroke='#b7c3ba',stroke_width=.7)
        rect(438,y+height-17,24,5,rx=2,fill='#364a50')
        path(f'M439 {y+height-16}H461',stroke='#d1d6c8',stroke_width=1.6)
    end()


def paint_wear():
    layer('blue-paint-wear', '04 · Weathered blue paint and exposed metal')
    emit('<g clip-path="url(#hullClip)">')
    for i in range(290):
        y=rng.uniform(161,1388)
        is_left=i%2==0
        x=rng.uniform(217,234) if is_left else rng.uniform(666,683)
        if y<275:
            x+=4 if is_left else -4
        path(f'M{x:.2f} {y:.2f}l{rng.uniform(-2,2):.2f} {rng.uniform(1.4,8):.2f}',stroke=rng.choice(['#cbd1c4','#a8b8ba','#254c65','#d4d2bd','#8e8c75']),stroke_opacity=rng.uniform(.25,.71),stroke_width=rng.uniform(.65,2.5))
    for x in range(272,638,19):
        y=125+4*abs(x-450)/180
        path(f'M{x} {y:.1f}l{rng.uniform(2,6):.1f} {rng.uniform(-1,1):.1f}',stroke='#d6d6c3',stroke_width=rng.uniform(.6,1.6),stroke_opacity=rng.uniform(.3,.64))
    for x in (230,670):
        for y in range(292,1383,67):
            ellipse(x+1,y+4,4,9,fill='url(#rustCool)')
            use('bolt',x,y,scale=.55)
    for x in range(277,629,49):
        use('bolt',x,139,scale=.56)
    end()
    end()


def foredeck():
    layer('foredeck-fittings', '05 · Bow mooring fittings and coiled lines')
    # The square bow is deliberately retained from the selected Reef Runner asset.
    for x in (280,620):
        ellipse(x,199,22,39,fill='url(#rustCool)')
        use('cleat',x,190,rotate=-18 if x<450 else 18,scale=1.04)
    art.rope_coil(297,225,23,28,5,-22)
    art.rope_coil(604,225,23,29,5,18)
    for x in (291,609):
        rect(x-11,140,22,37,rx=6,fill='url(#steelCool)',stroke='#4b6670',stroke_width=1)
        rect(x-5,147,10,23,rx=4,fill='#263f4f')
        path(f'M{x-8} 145V169',stroke='#e1e5d8',stroke_width=1.2)
    # Bow crossbar with short wear plates beneath its mountings.
    for x in (344,556):
        rect(x-10,120,20,28,rx=3,fill='url(#steelCool)',stroke='#4a6770',stroke_width=.8)
        use('bolt',x,125,scale=.59)
        use('bolt',x,143,scale=.59)
    path('M318 121H582',stroke='#2e4857',stroke_width=9,stroke_linecap='round')
    path('M318 119H582',stroke='url(#steelAcross)',stroke_width=7,stroke_linecap='round')
    path('M321 117H579',stroke='#e8e9d9',stroke_width=1.4,stroke_linecap='round')
    end()


def crate_and_floats():
    layer('cargo-rack', '06 · Yellow frame, netted rack and blue floats')
    # The reference's small yellow rack sits immediately ahead of the aft cabin.
    rect(335,1035,237,126,rx=6,fill='#324649',fill_opacity=.18)
    rect(330,1029,240,126,rx=5,fill='url(#steelCool)',stroke='#3a5358',stroke_width=2)
    rect(340,1039,220,116,rx=4,fill='#263b3e',stroke='#7c784c',stroke_width=2)
    rect(350,1048,200,101,rx=3,fill='url(#catchNet)')
    emit('<g clip-path="url(#netClip)">')
    # Irregular coils under the mesh convey a stowed net, all vector strokes.
    for i in range(36):
        x,y=rng.uniform(356,544),rng.uniform(1054,1145)
        path(f'M{x:.1f} {y:.1f}q{rng.uniform(-16,18):.1f} -17 {rng.uniform(-21,25):.1f} 2t{rng.uniform(-20,20):.1f} 15',fill='none',stroke=rng.choice(['#7b8764','#a0a177','#626f59','#d0be84']),stroke_width=rng.uniform(.7,2),stroke_opacity=rng.uniform(.18,.46))
    flecks(130,(351,1049,549,1148),['#b7aa77','#718270','#d4c493'],.3,2.4)
    end()
    rect(345,1043,210,111,rx=4,fill='none',stroke='#594f2f',stroke_width=8)
    rect(345,1042,210,111,rx=4,fill='none',stroke='url(#ochre)',stroke_width=5)
    for x in (415,485):
        path(f'M{x} 1045V1150',stroke='#695938',stroke_width=6)
        path(f'M{x-1} 1045V1150',stroke='url(#ochre)',stroke_width=3.7)
    path('M348 1097H552',stroke='#695938',stroke_width=6)
    path('M348 1096H552',stroke='url(#ochre)',stroke_width=3.7)
    for x,y in [(345,1043),(555,1043),(345,1153),(555,1153)]:
        use('bolt',x,y,scale=.6)
    path('M446 1034V1157',stroke='#222f31',stroke_width=4)
    path('M448 1034V1157',stroke='#9e9980',stroke_width=.85,stroke_opacity=.7)
    rect(442,1083,13,14,rx=2,fill='url(#steelCool)',stroke='#5b6b66',stroke_width=.8)
    # A pair of strapped blue barrel floats, kept tight to the sides of the rack.
    for x in (293,607):
        ellipse(x+4,1092,32,65,fill='url(#softShadow)')
        rect(x-26,1035,52,114,rx=24,fill='#233b4b',stroke='#8b9c9b',stroke_width=1.5)
        rect(x-24,1036,48,110,rx=23,fill='url(#floatBlue)',stroke='#4a6c80',stroke_width=1)
        path(f'M{x-17} 1050Q{x} 1040 {x+17} 1050 M{x-18} 1129Q{x} 1141 {x+18} 1129',fill='none',stroke='#b5cacf',stroke_width=2,stroke_opacity=.65)
        for yy in (1067,1118):
            path(f'M{x-24} {yy}Q{x} {yy+3} {x+24} {yy}',fill='none',stroke='#1d394a',stroke_width=7)
            path(f'M{x-24} {yy-1}Q{x} {yy+2} {x+24} {yy-1}',fill='none',stroke='#79939d',stroke_width=1.3)
        path(f'M{x} 1040V1143',stroke='#253c4b',stroke_width=4.5)
        path(f'M{x-1} 1041V1141',stroke='#b2bdb5',stroke_width=1)
        for i in range(24):
            xx,yy=x+rng.uniform(-18,18),rng.uniform(1047,1135)
            path(f'M{xx:.1f} {yy:.1f}l{rng.uniform(1,4):.1f} {rng.uniform(-1,2):.1f}',stroke='#dbe0ce',stroke_width=rng.uniform(.6,1.4),stroke_opacity=rng.uniform(.22,.51))
        use('padeye',x,1032,scale=.78)
    end()


def aft_cabin():
    layer('aft-cabin-roof', '07 · Compact aft cabin, roof ribs and weathering')
    for dx,dy,op in [(11,16,.07),(7,11,.1),(4,6,.19)]:
        path(ROOF,transform=f'translate({dx} {dy})',fill='#203a41',fill_opacity=op)
    path(ROOF,fill='#314850',stroke='#29424c',stroke_width=8)
    path(ROOF,fill='url(#roofIvory)',stroke='#a0afa6',stroke_width=2.3)
    emit('<g clip-path="url(#roofClip)">')
    path(ROOF,fill='none',stroke='#70897d',stroke_width=12,stroke_opacity=.19)
    path(ROOF,fill='none',stroke='#fffce7',stroke_width=4,stroke_opacity=.81,transform='translate(1 1)')
    for x,y,rx,ry in [(286,1198,20,49),(611,1399,31,36),(345,1424,85,18),(576,1173,56,19)]:
        ellipse(x,y,rx,ry,fill='url(#grime)')
    flecks(830,(269,1164,632,1437),['#8e8a6f','#b6aa88','#fffbed','#808977'],.2,2.1)
    for i in range(100):
        x=rng.uniform(276,625)
        y=rng.choice([rng.uniform(1170,1180),rng.uniform(1420,1437)])
        path(f'M{x:.1f} {y:.1f}l{rng.uniform(1,5):.1f} {rng.uniform(-.4,.4):.1f}',stroke=rng.choice(['#8f8870','#c0ac84','#fff5d8']),stroke_width=rng.uniform(.4,1.7),stroke_opacity=rng.uniform(.21,.56))
    end()
    # Low transverse stiffening ribs on a horizontal roof: no visible cabin walls.
    for y in (1195,1295,1409):
        x1,x2=(286,614) if y<1300 else (279,621)
        path(f'M{x1+3} {y+6}Q450 {y-5} {x2+3} {y+6}',fill='none',stroke='#3c5354',stroke_width=9,stroke_opacity=.17,stroke_linecap='round')
        path(f'M{x1} {y}Q450 {y-11} {x2} {y}',fill='none',stroke='#8e9e94',stroke_width=10,stroke_linecap='round')
        path(f'M{x1} {y-1}Q450 {y-12} {x2} {y-1}',fill='none',stroke='#e8e7d8',stroke_width=7,stroke_linecap='round')
        path(f'M{x1} {y-3}Q450 {y-14} {x2} {y-3}',fill='none',stroke='#fffbea',stroke_width=1.6,stroke_linecap='round',stroke_opacity=.88)
        for x in (x1+7,x2-7):
            ellipse(x,y+3,9,11,fill='url(#rustCool)')
            use('bolt',x,y-1,scale=.64)
    # A restrained recessed roof panel and welded seam follow the source cabin.
    path('M296 1319Q450 1309 604 1319L606 1380Q450 1388 294 1380Z',fill='#b9c1b8',fill_opacity=.26,stroke='#8d9c90',stroke_width=1.1)
    path('M298 1321Q450 1312 602 1321',fill='none',stroke='#faf6df',stroke_width=1.5,stroke_opacity=.73)
    for x,y in [(285,1181),(615,1181),(279,1249),(621,1249),(275,1356),(625,1356),(288,1424),(612,1424),(364,1431),(536,1431)]:
        ellipse(x+1,y+4,7,13,fill='url(#rustCool)')
        use('bolt',x,y,scale=.62)
    end()


def rooftop_details():
    layer('cabin-fittings', '08 · Vents, radar and cabin grab rails')
    use('vent',314,1252,scale=1.12)
    use('vent',586,1252,scale=1.12)
    for x in (301,599):
        for y in (1218,1377):
            rect(x-4,y-7,8,14,rx=3,fill='url(#steelCool)',stroke='#6f8177',stroke_width=.7)
            use('bolt',x,y,scale=.48)
        path(f'M{x+5} 1220V1378',stroke='#334c4b',stroke_width=4,stroke_opacity=.17)
        path(f'M{x} 1220V1377',stroke='url(#steelCool)',stroke_width=4,stroke_linecap='round')
        path(f'M{x-1} 1222V1375',stroke='#fffbe4',stroke_width=.9,stroke_opacity=.84)
    # Radar scanner footprint on a compact central pedestal.
    ellipse(456,1226,25,21,fill='url(#softShadow)')
    circle(450,1218,16,fill='url(#steelRound)',stroke='#607a77',stroke_width=1)
    circle(450,1216,10,fill='#3f5b64',stroke='#a4b6ad',stroke_width=1)
    rect(344,1208,218,15,rx=6,fill='#324f52',fill_opacity=.21,transform='translate(5 7)')
    rect(339,1205,222,14,rx=6,fill='url(#roofIvory)',stroke='#8c9f93',stroke_width=1)
    path('M346 1207H554',stroke='#fffbe7',stroke_width=1.8,stroke_linecap='round')
    path('M347 1217H553',stroke='#8f9e8f',stroke_width=.8,stroke_opacity=.77)
    for x in (352,548):
        path(f'M{x} 1206V1218',stroke='#839a91',stroke_width=.9)
    # Vertical mast cap and antenna: their shadows indicate height in plan view.
    path('M450 1280L472 1327',stroke='#405c58',stroke_width=3,stroke_opacity=.16)
    circle(450,1280,9,fill='url(#steelRound)',stroke='#748a7c',stroke_width=.9)
    circle(450,1279,4,fill='#eae9d5')
    path('M465 1179L483 1221',stroke='#365154',stroke_width=1.3,stroke_opacity=.16)
    circle(465,1179,5,fill='url(#steelRound)')
    circle(465,1178,2,fill='#f6f1d9')
    # Amber work-light lens on the fore edge of the roof.
    rect(441,1163,18,14,rx=4,fill='#586d69',stroke='#b2bbae',stroke_width=.8)
    rect(444,1164,12,10,rx=4,fill='url(#orangeRound)')
    path('M446 1166H451',stroke='#ffe4a7',stroke_width=1.2,stroke_linecap='round')
    end()


def rails():
    layer('rails-and-deck-fittings', '09 · Rails, cleats, fairleads and drains')
    rail_paths=[
        'M246 183Q234 264 234 413L237 974',
        'M654 183Q666 264 666 413L663 974',
        'M239 1047L241 1351Q242 1374 258 1381',
        'M661 1047L659 1351Q658 1374 642 1381',
        'M277 148Q450 134 623 148',
    ]
    posts=[(244,213),(234,358),(235,548),(236,758),(237,954),(239,1065),(240,1203),(242,1348),(290,147),(371,141)]
    posts += [(900-x,y) for x,y in posts]
    for d in rail_paths:
        path(d,fill='none',stroke='#314951',stroke_width=4.7,stroke_opacity=.21,stroke_linecap='round',transform='translate(6 8)')
    for x,y in posts:
        ellipse(x+2,y+3,8,10,fill='url(#rustCool)')
        circle(x,y,5,fill='url(#steelRound)',stroke='#5c7270',stroke_width=.6)
    for d in rail_paths:
        path(d,fill='none',stroke='#49626d',stroke_width=5,stroke_linecap='round')
        path(d,fill='none',stroke='url(#steelCool)',stroke_width=3.6,stroke_linecap='round')
        path(d,fill='none',stroke='#f0efdf',stroke_width=.85,stroke_opacity=.82,stroke_linecap='round',transform='translate(-.7 -.7)')
    for x,y in [(254,691),(646,691),(257,1019),(643,1019)]:
        use('cleat',x,y,scale=.79)
    for x,y in [(221,285),(679,285),(224,1287),(676,1287)]:
        use('fairlead',x,y,scale=.95)
    for x,y in [(257,582),(643,582),(257,1109),(643,1109)]:
        rect(x-6,y-15,12,30,rx=3,fill='#5b6e70',stroke='#c0cbc2',stroke_width=.8)
        for yy in range(y-10,y+12,4):
            path(f'M{x-4} {yy}H{x+4}',stroke='#263f4b',stroke_width=1.7)
    for x in (237,663):
        path(f'M{x} 977Q{x+(-8 if x<450 else 8)} 1008 {x+(-1 if x<450 else 1)} 1044',fill='none',stroke='#334c55',stroke_width=2.4)
        path(f'M{x} 977Q{x+(-8 if x<450 else 8)} 1008 {x+(-1 if x<450 else 1)} 1044',fill='none',stroke='#c1cabe',stroke_width=1.6,stroke_dasharray='3 3')
    end()


def fenders():
    layer('fenders-and-lines', '10 · Blue black rubber fenders and mooring ties')
    for x,y,rot in [(202,262,-3),(201,641,0),(204,1310,-1),(698,264,3),(699,699,0),(696,1312,1)]:
        use('fender',x,y,rotate=rot,scale=.83)
        # Narrow blue highlight picks up the hull color without a raster effect.
        path(f'M{x-4} {y-25}V{y+22}',stroke='#6c8b9a',stroke_width=2.1,stroke_opacity=.42,stroke_linecap='round')
        tie=x+24 if x<450 else x-24
        path(f'M{x} {y-37}Q{tie} {y-51} {tie} {y-69}',fill='none',stroke='#3b4e51',stroke_width=3.1)
        path(f'M{x-.4} {y-37}Q{tie-.4} {y-51} {tie-.4} {y-69}',fill='none',stroke='#c8c4a7',stroke_width=1.65)
        use('padeye',tie,y-69,scale=.6)
    end()


def create_svg():
    art.PARTS.clear()
    rng.seed(180927)
    definitions()
    drive_and_stern()
    hull_and_deck()
    hatches()
    paint_wear()
    foredeck()
    crate_and_floats()
    aft_cabin()
    rooftop_details()
    rails()
    fenders()
    emit('</svg>')
    result='\n'.join(art.PARTS)+'\n'
    result=result.replace('Urchin workboat — orthographic overhead','Reef Runner — orthographic overhead')
    begin=result.index('  <desc id="description">')
    finish=result.index('  <defs>',begin)
    result=result[:begin]+'''  <desc id="description">Reef Runner from Urchin Skipper, drawn in a true orthographic top view with bow up and transparent background. Square bow, weathered blue gunwales, an open aluminium deck, two large diamond-plate hatches, a small ivory aft cabin, yellow netted rack, paired blue floats and a stern drive. All visible surfaces are horizontal footprints; the cabin has no visible vertical walls. Editable vector paths, gradients and patterns only, with no embedded image or raster filters.</desc>
  <metadata>Created for Urchin Skipper on 2026-09-18. Reference: public/assets/fleet/reef runner.png, the designer-selected sterndrive family artwork. Newly authored vector interpretation; original reference preserved. Recipe: create-reef-runner.py, using vector material helpers from create-workboat.py. This is a standalone art study and is not wired into the game.</metadata>
'''+result[finish:]
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replace-generated',action='store_true')
    options=parser.parse_args()
    output=ROOT.parent/'generated-review/fleet-vector/reef-runner-top.svg'
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open('w' if options.replace_generated else 'x',encoding='utf-8') as handle:
        handle.write(create_svg())
    print(output)
