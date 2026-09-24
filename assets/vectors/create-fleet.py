#!/usr/bin/env python3
"""Draw one standalone fleet SVG per invocation, preserving existing artwork.

Original vector interpretations of the designer's selected boat reference files.
Uses only Python's standard library and the first approved boat's vector fittings.
No raster embedding, tracing, network access, game edits or test execution.
"""

from pathlib import Path
import argparse
import importlib.util
from html import escape
import math
import random
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('approved_vector_materials', ROOT/'create-workboat.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
emit, path, rect, circle, ellipse = b.emit, b.path, b.rect, b.circle, b.ellipse
use, layer, end, flecks = b.use, b.layer, b.end, b.weather_flecks
rng = b.RNG

# Each entry records a separately observed silhouette, layout and equipment.
BOATS = {
    'harbour-workhorse': dict(source='harbour workhorse', title='Harbour Workhorse', hull='point', paint='#829193', deck='alloy', roof=(284,388,332,419), roof_type='mast', gear=[('hatch',337,954,226,154),('hatch',337,1213,226,169),('grille',266,1120,24,102),('grille',610,1120,24,102),('hose',265,832,1)], stern='plain', finish=.85),
    'harbour-workhorse3': dict(source='harbour workhorse3',title='Harbour Workhorse · sister',hull='yacht',paint='#c9d1c6',deck='teak',roof=(290,478,320,462),roof_type='dome',gear=[('bench',293,986,106,76),('bench',500,986,106,76),('table',401,1120,98,91),('bench',294,1300,312,99)],stern='platform',finish=.45),
    'coastal-workhorse': dict(source='coastal workhorse',title='Coastal Workhorse',hull='point',paint='#8c8d66',deck='alloy',roof=(279,401,342,379),roof_type='dome',gear=[('crane',282,857,171,1125,'yellow'),('hatch',330,935,260,276),('case',256,1232,73,112),('crate',265,1352,79,91,'green'),('crate',548,1265,96,178,'green'),('crate',381,1360,94,73,'ochre'),('tanks',603,971,2)],stern='platform',finish=1),
    'coastal-workhorse2': dict(source='coastal workhorse2',title='Coastal Workhorse · sister',hull='tug',paint='#b8493c',deck='alloy',roof=(279,449,342,341),roof_type='dome',gear=[('tow',450,1055,1.15),('winch',290,1282,.83),('winch',610,1282,.83),('hazard',295,1417,310,34)],stern='plain',finish=.88),
    'reef-runner2': dict(source='reef runner2',title='Reef Runner · sister',hull='point',paint='#cbab39',deck='alloy',roof=(278,406,344,336),roof_type='dome',gear=[('crane',281,839,192,1017,'steel'),('crate',265,981,92,98,'green'),('crate',267,1124,57,65,'ivory'),('crate',338,1124,62,65,'red'),('tanks',604,919,1),('crate',573,1062,71,114,'blue'),('crate',267,1303,96,110,'ochre'),('crate',510,1282,130,137,'ochre'),('case',267,1431,100,51)],stern='platform',finish=1),
    'island-tender': dict(source='island tender',title='Island Tender',hull='rib',paint='#d77636',deck='dark',roof=(291,480,318,430),roof_type='dome',gear=[('hatch',399,323,102,105),('hatch',293,1002,143,153),('hatch',461,1002,143,153),('hatch',293,1174,143,175),('hatch',461,1174,143,175),('lifering',348,1070,1),('crate',286,1367,81,65,'ochre'),('crate',532,1367,81,65,'ochre')],stern='outboard2',finish=.55),
    'island-tender2': dict(source='island tender2',title='Island Tender · sister',hull='slender',paint='#aab6b5',deck='alloy',roof=(303,475,294,361),roof_type='dome',gear=[('hatch',409,275,82,90),('case',375,858,150,60),('hatch',389,1033,122,246),('case',279,1151,65,104),('case',556,1151,65,104),('crate',526,1360,102,85,'ochre')],stern='outboard1',finish=.74),
    'shoal-skipper': dict(source='shoal skipper',title='Shoal Skipper',hull='stub',paint='#b4b4a0',deck='dark',roof=(290,388,320,322),roof_type='utility',gear=[('case',359,811,181,130),('crane',572,1324,239,1225,'ivory'),('case',274,1347,80,66)],stern='jet1',finish=1),
    'shoal-skipper2': dict(source='shoal skipper2',title='Shoal Skipper · sister',hull='broad',paint='#c7a34c',deck='alloy',roof=(266,390,368,346),roof_type='dome',gear=[('crane',394,926,237,1223,'yellow'),('case',573,876,67,101),('case',569,1010,70,156),('hatch',274,1230,170,181),('hatch',460,1230,171,181)],stern='jet1',finish=1),
    'channel-master': dict(source='channel master',title='Channel Master',hull='cat',paint='#d2d6cb',deck='alloy',roof=(248,481,404,416),roof_type='plain',gear=[('hatch',237,1120,141,201),('hatch',392,1120,116,201),('hatch',522,1120,141,201),('bench',260,930,105,74),('bench',397,930,105,74),('bench',534,930,105,74)],stern='jet2',finish=.63),
    'channel-master2': dict(source='channel master2',title='Channel Master · sister',hull='cat',paint='#d6d9cd',deck='alloy',roof=(272,397,356,345),roof_type='instruments',gear=[('netbow',0,0,1),('deckcircle',450,1040,120),('case',602,943,65,80),('crate',234,1330,102,75,'red'),('crate',550,1268,105,134,'ochre'),('solar',342,1430,217,118),('buoy',225,1311,1)],stern='jet2',finish=.85),
    'rival1': dict(source='rival1',title='Rival 1 · working launch',hull='point',paint='#b6c0b3',deck='alloy',roof=(284,425,332,362),roof_type='dome',gear=[('case',374,829,152,75),('hatch',295,954,312,245),('case',557,1148,83,148),('crate',283,1310,123,126,'ochre'),('crate',525,1350,126,96,'ochre'),('tanks',263,1240,3),('crate',435,1306,66,132,'ivory')],stern='platform',finish=.94),
    'rival2': dict(source='rival2',title='Rival 2 · orange workboat',hull='point',paint='#c96934',deck='alloy',roof=(293,558,314,350),roof_type='dome',gear=[('case',371,381,157,103,'yellow'),('crate',370,1182,157,153,'red'),('hatch',266,1184,83,153),('crate',550,1171,86,163,'blue'),('buoy',619,1077,.7),('hazard',299,1431,302,22)],stern='platform',finish=.93),
    'rival3': dict(source='rival3',title='Rival 3 · narrow crane boat',hull='slender',paint='#9eaaa7',deck='alloy',roof=(308,502,284,388),roof_type='dome',gear=[('hatch',411,326,78,87),('crane',283,1041,161,1233,'ivory'),('case',473,1002,125,83),('hatch',284,1147,157,209),('hatch',455,1147,150,209),('crate',511,1380,91,73,'ochre'),('tanks',560,1445,1)],stern='platform',finish=.86),
    'rival4': dict(source='rival4',title='Rival 4 · teak cabin cruiser',hull='yacht',paint='#d1d6c6',deck='teak',roof=(300,518,300,514),roof_type='dome',gear=[('hatch',418,374,65,63),('case',353,1062,195,90),('bench',329,1370,244,84)],stern='platform',finish=.54),
    'rival5': dict(source='rival5',title='Rival 5 · blue double derrick',hull='slender',paint='#426f8a',deck='alloy',roof=(296,486,308,338),roof_type='dome',gear=[('hatch',423,330,54,63),('buoy',288,897,.6),('buoy',288,946,.6),('winch',603,932,.8),('hatch',360,1069,194,126),('hatch',360,1210,194,126),('case',575,1146,55,76),('crate',275,1363,105,101,'ochre'),('crate',539,1351,90,120,'green'),('crane',286,1170,174,1017,'steel'),('crane',602,1373,454,1485,'steel')],stern='platform',finish=.98),
    'rival6': dict(source='rival6',title='Rival 6 · blue twin outboard',hull='point',paint='#508bb1',deck='alloy',roof=(286,445,328,360),roof_type='dome',gear=[('crane',291,981,155,892,'ivory'),('case',564,1192,73,152),('case',602,946,41,72),('winch',612,875,.56)],stern='outboard2',finish=.83),
    'rival7': dict(source='rival7',title='Rival 7 · lived-in expedition workboat',hull='broad',paint='#797e67',deck='alloy',roof=(270,420,360,350),roof_type='utility',gear=[('table',353,273,193,82),('planter',220,536,42,173),('planter',639,521,42,179),('case',284,809,96,80),('case',523,809,96,80),('table',305,937,150,89),('table',305,1048,150,107),('winch',380,1103,.65),('dinghy',617,1112,102,270,'ivory'),('crate',254,1371,137,71,'green'),('crate',414,1371,111,71,'green'),('canopy',281,1160,270,146,'red'),('canopy',283,1286,245,117,'khaki'),('planter',633,1374,47,80)],stern='platform',finish=1.1),
    'rival8': dict(source='rival8',title='Rival 8 · green support vessel',hull='broad',paint='#527b6c',deck='paint',roof=(261,449,378,349),roof_type='dome',gear=[('winch',326,713,.65),('winch',570,713,.65),('dinghy',260,953,69,180,'orange'),('dinghy',640,953,69,180,'orange'),('case',317,936,59,61),('case',403,936,59,61),('case',489,936,59,61),('case',575,936,47,61),('helipad',285,1120,330,359)],stern='plain',finish=.85),
    'rival9': dict(source='rival9',title='Rival 9 · solar expedition catamaran',hull='cat',paint='#d5d9cc',deck='alloy',roof=(284,492,332,486),roof_type='solar',gear=[('netbow',0,0,1),('case',218,471,60,66),('case',622,471,60,66),('solar',319,810,110,94),('solar',472,810,110,94),('dinghy',650,1086,67,236,'orange'),('case',351,1294,75,75),('crane',239,1172,172,1375,'ivory'),('hatch',265,1276,66,80),('hatch',545,1276,66,80)],stern='outboard1',finish=.8),
    'rival11': dict(source='rival11',title='Rival 11 · teak twin outboard tender',hull='ribdark',paint='#3b4a4e',deck='teak',roof=(304,503,292,502),roof_type='dome',gear=[('table',414,235,71,95),('table',395,1206,110,86),('bench',302,1324,295,80),('bench',548,1131,58,177)],stern='outboard2',finish=.46),
    'rival12': dict(source='rival12',title='Rival 12 · green net tender',hull='point',paint='#648674',deck='paint',roof=(281,575,338,344),roof_type='utility',gear=[('planter',244,665,32,150),('planter',628,665,32,150),('case',277,951,61,58),('crate',558,951,61,59,'red'),('crate',337,1236,226,142,'ochre'),('case',339,1394,221,53,'yellow'),('crate',264,1240,61,98,'ivory'),('tanks',604,1291,2),('hose',442,1044,.76)],stern='platform',finish=1.05),
    'rival13': dict(source='rival13',title='Rival 13 · white passenger cruiser',hull='yacht',paint='#d8ddd0',deck='ivory',roof=(307,611,286,334),roof_type='dome',gear=[('hatch',421,325,58,72),('bench',347,1071,203,80),('case',570,1071,66,80),('bench',277,1212,166,84),('bench',457,1212,166,84),('bench',332,1390,237,69)],stern='outboard2',finish=.52),
    'rival14': dict(source='rival14',title='Rival 14 · aluminium twin outboard',hull='point',paint='#9eaaa4',deck='alloy',roof=(285,464,330,384),roof_type='utility',gear=[('case',275,957,73,94),('case',552,957,73,103),('hatch',382,968,133,89),('grille',268,1094,363,181),('case',349,1176,83,82)],stern='outboard2',finish=.88),
    'taxi1': dict(source='taxi1',title='Taxi 1 · orange twin outboard',hull='rib',paint='#de7b35',deck='alloy',roof=(296,489,308,510),roof_type='dome',gear=[('case',276,1071,68,88),('hatch',297,1283,82,115),('hatch',410,1283,80,115),('hatch',521,1283,82,115)],stern='outboard2',finish=.66),
    'taxi3': dict(source='taxi3',title='Taxi 3 · red passenger launch',hull='slender',paint='#b85445',deck='alloy',roof=(302,473,296,405),roof_type='dome',gear=[('hatch',354,487,65,49),('hatch',429,487,65,49),('hatch',272,1135,109,228),('hatch',397,1135,109,228),('hatch',522,1135,109,228),('case',362,1384,176,55),('winch',602,1468,.92)],stern='platform',finish=.85),
    'taxi4': dict(source='taxi4',title='Taxi 4 · charcoal harbour shuttle',hull='ribdark',paint='#424f53',deck='teak',roof=(303,548,294,377),roof_type='dome',gear=[('hatch',407,372,87,82),('bench',348,949,203,65),('case',401,1191,100,102),('case',288,1339,56,65),('case',557,1339,56,65)],stern='outboard2',finish=.71),
    'taxi5': dict(source='taxi5',title='Taxi 5 · teak passenger cruiser',hull='yacht',paint='#d7d9cb',deck='teak',roof=(297,547,306,448),roof_type='dome',gear=[('hatch',410,349,81,87),('bench',354,1169,192,88),('bench',361,1351,179,103),('bench',271,1351,73,106),('bench',557,1351,73,106)],stern='plain',finish=.54),
    'dfoboat1': dict(source='dfoboat1',title='DFO 1 · rigid inflatable patrol boat',hull='rib',paint='#394b55',deck='alloy',roof=(342,585,216,267),roof_type='plain',gear=[('case',422,322,56,117),('bench',344,941,212,87),('bench',337,1130,86,95),('bench',477,1130,86,95),('grille',337,1293,226,81)],stern='outboard2',finish=.58),
    'dfoboat2': dict(source='dfoboat2',title='DFO 2 · olive patrol launch',hull='slender',paint='#7e8774',deck='alloy',roof=(300,436,300,374),roof_type='dome',roof_paint='#a2a895',gear=[('hatch',358,1051,188,234),('case',270,1210,68,106),('winch',606,1209,.74),('case',565,1344,67,51,'yellow'),('case',362,1385,184,50),('case',269,1385,80,50)],stern='outboard2',finish=.82),
    'dfoboat3': dict(source='dfoboat3',title='DFO 3 · grey offshore patrol boat',hull='slender',paint='#838f91',deck='alloy',roof=(308,455,284,399),roof_type='instruments',roof_paint='#a3adab',gear=[('hatch',418,302,63,73),('case',277,916,54,80),('case',569,916,54,80),('hatch',287,1032,155,239),('hatch',456,1032,155,239),('case',283,1300,330,95)],stern='outboard2',finish=.87),
    'nine-ships-03-r1-c3': dict(source='nine-ships-03-r1-c3',title='Nine Ships 03 · futuristic hydrocraft',hull='future',paint='#a6b4b3',deck='dark',roof=(332,460,236,300),roof_type='utility',roof_paint='#c8d0c7',gear=[('sci-panels',0,0,1),('pod',237,1200,100,708,'blue'),('pod',663,1200,100,708,'blue'),('reactor',450,974,62,'blue'),('reactor',450,1455,39,'blue'),('grille',325,1033,31,222),('grille',544,1033,31,222),('case',414,1285,72,76),('lamp',354,1192,1),('lamp',546,1192,1)],stern='plain',bow_style='none',rail_style='none',finish=.8),
    'nine-ships-06-r2-c3': dict(source='nine-ships-06-r2-c3',title='Nine Ships 06 · double-crane vessel',hull='rib',paint='#a1b1b4',deck='red',roof=(286,404,328,325),roof_type='roundhatch',gear=[('case',343,755,214,70),('case',280,858,99,73,'yellow'),('case',520,858,99,73,'yellow'),('hatch',335,1033,230,136),('crate',400,1203,96,101,'ochre'),('case',397,1392,108,61),('crane',292,1335,182,983,'ivory'),('crane',608,1335,718,983,'ivory'),('rigging',182,983,224,1377,292,1335),('rigging',718,983,676,1377,608,1335),('lamp',302,883,1),('lamp',599,883,1)],stern='platform',finish=1),
    'nine-ships-07-r3-c1': dict(source='nine-ships-07-r3-c1',title='Nine Ships 07 · red-sailed galley',hull='galley',paint='#8b7750',deck='wood',roof=(360,440,180,140),no_cabin=True,bow_style='none',rail_style='historic',gear=[('oars',0,0,1),('grate',374,738,152,199),('table',382,969,136,83),('capstan',450,640,1),('historical-rig',0,0,1),('square-sail',181,364,538,252),('square-sail',231,1230,438,220),('carving',450,140,1)],stern='plain',finish=.95),
    'nine-ships-08-r3-c2': dict(source='nine-ships-08-r3-c2',title='Nine Ships 08 · blue sailing trimaran',hull='trimaran',paint='#668aa0',deck='teak',roof=(321,533,258,499),roof_type='plain',gear=[('trimaran-nets',0,0,1),('hatch',355,653,57,56),('hatch',487,653,57,56),('case',383,1154,134,130),('sailing-rig',0,0,1)],stern='plain',bow_style='none',rail_style='none',finish=.62),
    'nine-ships-09-r3-c3': dict(source='nine-ships-09-r3-c3',title='Nine Ships 09 · armoured utility craft',hull='armoured',paint='#737962',deck='paint',roof=(316,1290,268,173),roof_type='plain',roof_paint='#89947a',gear=[('armour',0,0,1),('reactor',450,396,110,'gold'),('crate',330,626,79,99,'ochre'),('crate',414,626,75,99,'ochre'),('crate',494,626,76,99,'blue'),('canopy',324,733,252,123,'khaki'),('case',337,973,66,79),('case',495,973,66,79),('hatch',409,1135,83,67),('pod',272,1544,82,164,'gold'),('pod',628,1544,82,164,'gold')],stern='plain',bow_style='none',rail_style='none',finish=1.1),
}


def blend(hexcolor, other, amount):
    c=[int(hexcolor[i:i+2],16) for i in (1,3,5)]
    d=[int(other[i:i+2],16) for i in (1,3,5)]
    return '#'+''.join(f'{round(a+(z-a)*amount):02x}' for a,z in zip(c,d))


def lin(name,stops,vertical=False):
    emit(f'<linearGradient id="{name}" x1="0" y1="0" x2="{0 if vertical else 1}" y2="{1 if vertical else .15}">')
    for pos,col in stops:
        emit(f'<stop offset="{pos}" stop-color="{col}"/>')
    emit('</linearGradient>')


def hull_path(kind,inset=0):
    i=inset
    if kind=='future':
        return f'M450 {97+i}C{522-i*.3} {120+i} {592-i} 324 {605-i} 540L{618-i} 1210Q{621-i} 1403 {521-i*.3} {1541-i}L484 {1447-i}H416L{379+i*.3} {1541-i}Q{279+i} 1403 {282+i} 1210L{295+i} 540C{308+i} 324 {378+i*.3} {120+i} 450 {97+i}Z'
    if kind=='galley':
        return f'M450 {108+i}C{368+i*.2} {139+i} {262+i} 329 {247+i} 538L{252+i} 1205Q{267+i} 1467 450 {1560-i}Q{633-i} 1467 {648-i} 1205L{653-i} 538C{638-i} 329 {532-i*.2} {139+i}450 {108+i}Z'
    if kind=='trimaran':
        main=f'M450 {129+i}C{516-i*.3} 262 {584-i} 420 {607-i} 706L{600-i} 1295Q{593-i} {1510-i}450 {1530-i}Q{307+i} {1510-i}{300+i} 1295L{293+i} 706C{316+i} 420 {384+i*.3} 262 450 {129+i}Z'
        s=i*.39
        for side in (-1,1):
            xx=lambda p:450+side*(450-p)
            main+=f'M{xx(201)} {115+i}Q{xx(169+s)} 335 {xx(165+s)} 600L{xx(174+s)} 1420Q{xx(180+s)} {1513-i} {xx(210)} {1540-i}Q{xx(239-s)} {1513-i} {xx(243-s)} 1420L{xx(245-s)} 600Q{xx(235-s)} 335 {xx(201)} {115+i}Z'
        return main
    if kind=='armoured':
        return f'M450 {111+i}C{331+i} {126+i} {247+i} 285 {232+i} 481L{207+i} 1094L{244+i} 1403Q{262+i} {1452-i}{302+i} {1469-i}H{598-i}Q{638-i} {1452-i}{656-i} 1403L{693-i} 1094L{668-i} 481C{653-i} 285 {569-i} {126+i}450 {111+i}Z'
    if kind=='cat':
        return f'M{195+i} 155Q202 {111+i} {235+i} {109+i}H{279-i}L{346-i} {393+i}H{554+i}L{621+i} {109+i}H{665-i}Q698 {111+i} {705-i} 155L{716-i} 1390Q714 {1496-i} {674-i} {1515-i}H{619+i}L{600+i} {1461-i}H{300-i}L{281-i} {1515-i}H{226+i}Q186 {1496-i} {184+i} 1390Z'
    if kind=='tug':
        return f'M450 {106+i}C{291+i} {108+i} {192+i} 292 {192+i} 495L{197+i} 1355Q{202+i} {1515-i} 450 {1515-i}Q{698-i} {1515-i} {703-i} 1355L{708-i} 495C{708-i} 292 {609-i} {108+i} 450 {106+i}Z'
    if kind=='rib':
        return f'M450 {105+i}Q{380+i} {102+i} {346+i} {166+i}C{266+i} 310 {206+i} 483 {202+i} 726L{213+i} {1431-i}Q{216+i} {1493-i} {248+i} {1493-i}H{652-i}Q{684-i} {1493-i} {687-i} {1431-i}L{698-i} 726C{694-i} 483 {634-i} 310 {554-i} {166+i}Q{520-i} {102+i} 450 {105+i}Z'
    if kind=='square':
        return f'M{260+i} {126+i}Q450 {110+i} {640-i} {126+i}Q{690-i} {130+i} {692-i} 212L{700-i} {1400-i}Q{700-i} {1490-i} {650-i} {1493-i}H{250+i}Q{200+i} {1490-i} {200+i} {1400-i}L{208+i} 212Q{210+i} {130+i} {260+i} {126+i}Z'
    w={'point':0,'slender':36,'yacht':24,'broad':-22,'stub':4,'wood':-8,'sail':37,'ribdark':25}.get(kind,0)
    left=198+w+i
    right=900-left
    top=106+i
    if kind=='stub':
        start=f'M{402+i*.4} {top}H{498-i*.4}L{588-i} 226'
    else:
        start=f'M450 {top}C502 {131+i} {587-i} 221 {623-i} 302'
    bottom=1497-i
    return start+f'C{right-9} 411 {right+3} 518 {right} 666L{right-12} 1405Q{right-13} {bottom} {right-49} {bottom}Q450 {bottom+21} {left+49} {bottom}Q{left+13} {bottom} {left+12} 1405L{left} 666C{left-3} 518 {left+9} 411 {277+i} 302C{313+i} 221 398 {131+i} 450 {top}Z'


def roof_path(x,y,w,h):
    return f'M{x+27} {y}Q{x+w/2} {y-14} {x+w-27} {y}Q{x+w-5} {y+1} {x+w-4} {y+25}L{x+w+5} {y+h-25}Q{x+w+7} {y+h-1} {x+w-16} {y+h}Q{x+w/2} {y+h+11} {x+16} {y+h}Q{x-7} {y+h-1} {x-5} {y+h-25}L{x+4} {y+25}Q{x+5} {y+1} {x+27} {y}Z'


def definitions(c):
    b.HULL=hull_path(c['hull'])
    b.DECK=hull_path(c['hull'],39 if c['hull']!='rib' else 52)
    b.ROOF=roof_path(*c['roof'])
    b.definitions()
    emit('<defs>')
    paint=c['paint']
    lin('fleetPaint',[(0,blend(paint,'#142c39',.58)),(.09,blend(paint,'#f4f0d4',.27)),(.22,paint),(.66,blend(paint,'#d8ddcc',.04)),(.93,blend(paint,'#192a34',.31)),(1,blend(paint,'#112533',.63))])
    lin('fleetCap',[(0,blend(paint,'#e9e5c7',.4)),(.2,blend(paint,'#d0dbd0',.26)),(.71,paint),(1,blend(paint,'#142d40',.3))])
    lin('alloy',[(0,'#b2b7ad'),(.27,'#a3aca6'),(.68,'#8f9995'),(1,'#778684')])
    lin('darkDeck',[(0,'#7d8886'),(.29,'#788583'),(.71,'#616f71'),(1,'#4c6064')])
    lin('teak',[(0,'#7f694b'),(.18,'#b39a6b'),(.48,'#bda77c'),(.84,'#95805b'),(1,'#746347')])
    if 'roof_paint' in c:
        rp=c['roof_paint']
        lin('roofIvory',[(0,blend(rp,'#eeebd9',.37)),(.23,rp),(.73,blend(rp,'#9ba99e',.16)),(1,blend(rp,'#354f53',.34))])
    else:
        lin('roofIvory',[(0,'#f4efe2'),(.23,'#eae6d7'),(.73,'#d8d9ca'),(1,'#a9b9ad')])
    lin('coolSteel',[(0,'#4c646d'),(.18,'#b3c0bd'),(.29,'#eeeede'),(.49,'#90a7ac'),(.76,'#c8d2c5'),(1,'#506b74')])
    lin('blueFloat',[(0,'#23445c'),(.17,'#5785a0'),(.39,'#a0bbc4'),(.71,'#467892'),(1,'#23465b')])
    lin('yellowPaint',[(0,'#8b713b'),(.21,'#e1be60'),(.47,'#d0a642'),(.81,'#b08c37'),(1,'#78653b')])
    lin('redPaint',[(0,'#703d37'),(.19,'#bb6b51'),(.44,'#b75b46'),(.85,'#934637'),(1,'#593a32')])
    lin('greenPaint',[(0,'#314c3e'),(.22,'#6f8871'),(.51,'#5c7a60'),(.8,'#3f6251'),(1,'#2b4338')])
    lin('motor',[(0,'#172b35'),(.18,'#40565e'),(.42,'#778789'),(.57,'#4b626c'),(.83,'#304650'),(1,'#142c38')])
    lin('canvas',[(0,'#8e7853'),(.24,'#c9b58a'),(.62,'#b29b70'),(1,'#756349')])
    lin('sailCloth',[(0,'#aea994'),(.22,'#e8e2c6'),(.54,'#f3edd8'),(.83,'#c1bea7'),(1,'#898f80')])
    lin('redSail',[(0,'#66372c'),(.17,'#a76049'),(.48,'#914935'),(.76,'#a1573e'),(1,'#5b392e')])
    lin('brass',[(0,'#5c5736'),(.19,'#c3a367'),(.35,'#ead39b'),(.58,'#af8f50'),(.88,'#7b693e'),(1,'#4c4d31')])
    emit('''<radialGradient id="cyanCore"><stop stop-color="#f4ffff"/><stop offset=".24" stop-color="#c9faff"/><stop offset=".52" stop-color="#77cede"/><stop offset=".78" stop-color="#2e879c"/><stop offset="1" stop-color="#1e4f64"/></radialGradient>
<radialGradient id="goldCore"><stop stop-color="#fffdea"/><stop offset=".24" stop-color="#ffedb4"/><stop offset=".55" stop-color="#e6ba69"/><stop offset="1" stop-color="#82623a"/></radialGradient>''')
    emit('''<pattern id="diamond" width="14" height="14" patternUnits="userSpaceOnUse"><path d="M2 5L6 1 M9 12L13 8" stroke="#3e5758" stroke-opacity=".25" stroke-width="2" stroke-linecap="round"/><path d="M1.5 4.5L5.5 .5 M8.5 11.5L12.5 7.5" stroke="#e2e4cf" stroke-opacity=".39" stroke-width="1" stroke-linecap="round"/></pattern>
<pattern id="net" width="12" height="12" patternUnits="userSpaceOnUse"><rect width="12" height="12" fill="#304c45"/><path d="M0 0L12 12M-6 6L6-6M0 12L12 0M6 18L18 6" fill="none" stroke="#9eac80" stroke-width="1" stroke-opacity=".55"/></pattern>
<pattern id="solarCells" width="18" height="26" patternUnits="userSpaceOnUse"><rect width="18" height="26" fill="#274454"/><rect x="1.5" y="1.5" width="15" height="23" rx="1" fill="#375970" stroke="#c6cfb9" stroke-width=".65"/><path d="M4 2V24M9 2V24M14 2V24" stroke="#9bb2bc" stroke-width=".45" stroke-opacity=".55"/></pattern>
<pattern id="hazardStripes" width="30" height="30" patternUnits="userSpaceOnUse" patternTransform="rotate(-42)"><rect width="30" height="30" fill="#29373b"/><rect width="14" height="30" fill="#d6b451"/></pattern>''')
    emit('</defs>')


def bolts_box(x,y,w,h):
    for px,py in [(x+7,y+7),(x+w-7,y+7),(x+7,y+h-7),(x+w-7,y+h-7)]:
        ellipse(px+1,py+4,5,9,fill='url(#rust)')
        use('bolt',px,py,scale=.65)


def hatch(x,y,w,h,glass=False):
    rect(x+3,y+4,w,h,rx=7,fill='#213b3c',fill_opacity=.17)
    rect(x,y,w,h,rx=7,fill='url(#coolSteel)',stroke='#4b625f',stroke_width=1.8)
    rect(x+6,y+6,w-12,h-12,rx=4,fill='url(#glass)' if glass else 'url(#darkDeck)',stroke='#adc2b2',stroke_width=.7)
    if glass:
        path(f'M{x+10} {y+10}H{x+w-15}L{x+10} {y+h*.72}Z',fill='#d1e4d8',fill_opacity=.13)
    else:
        rect(x+6,y+6,w-12,h-12,rx=4,fill='url(#diamond)')
        flecks(max(35,int(w*h/100)),(x+8,y+8,x+w-8,y+h-8),['#d6daca','#334e53','#a3a58a'],.16,1.9)
    bolts_box(x,y,w,h)
    for xx in (x+w*.26,x+w*.74):
        rect(xx-9,y-2,18,8,rx=2,fill='url(#steelHorizontal)',stroke='#637669',stroke_width=.6)
    rect(x+w/2-13,y+h-14,26,9,rx=3,fill='url(#steelHorizontal)',stroke='#465e4e',stroke_width=.6)
    rect(x+w/2-8,y+h-11,16,3,rx=1,fill='#344c40')


def case(x,y,w,h,color='ivory'):
    grad={'ivory':'roofIvory','yellow':'yellowPaint','red':'redPaint','green':'greenPaint','blue':'blueFloat'}.get(color,'roofIvory')
    rect(x+5,y+7,w,h,rx=7,fill='#173d34',fill_opacity=.18)
    rect(x,y,w,h,rx=6,fill=f'url(#{grad})',stroke='#5c7365',stroke_width=1.4)
    rect(x+5,y+5,w-10,h-10,rx=3,fill='none',stroke='#eeedd4',stroke_width=.9,stroke_opacity=.72)
    path(f'M{x+w*.5} {y+3}V{y+h-3}',stroke='#788879',stroke_width=1,stroke_opacity=.6)
    bolts_box(x,y,w,h)
    for xx in (x+w*.25,x+w*.75):
        rect(xx-5,y+h-7,10,7,rx=1.4,fill='url(#coolSteel)',stroke='#657669',stroke_width=.5)


def grille(x,y,w,h):
    rect(x,y,w,h,rx=3,fill='url(#coolSteel)',stroke='#546b63',stroke_width=1)
    rect(x+4,y+4,w-8,h-8,rx=1,fill='#243f3c')
    for yy in range(int(y+7),int(y+h-3),5):
        path(f'M{x+4} {yy}H{x+w-4}',stroke='#a0b19c',stroke_width=1.4)


def winch(cx,cy,s=1):
    emit(f'<g transform="translate({cx} {cy}) scale({s})">')
    ellipse(6,8,44,49,fill='url(#softShadow)')
    rect(-31,-32,62,64,rx=5,fill='url(#coolSteel)',stroke='#4e6458',stroke_width=1.6)
    bolts_box(-31,-32,62,64)
    circle(0,0,28,fill='url(#darkMetal)',stroke='#b9c7b0',stroke_width=1.2)
    for r in (24,20,16,12):
        circle(0,-1,r,fill='none',stroke='#98a98e',stroke_width=2)
        path(f'M{-r} -1A{r} {r} 0 0 1 {r} -1',fill='none',stroke='#d9ddc1',stroke_width=.8)
    circle(0,-1,8,fill='url(#steelRound)')
    rect(26,-13,20,27,rx=4,fill='url(#darkMetal)',stroke='#8ea084',stroke_width=.8)
    for yy in (-8,-3,2,7):
        path(f'M31 {yy}H42',stroke='#adba9c',stroke_width=.8)
    end()


def tow(cx,cy,s):
    emit(f'<g transform="translate({cx} {cy}) scale({s})">')
    rect(-56,-95,112,189,rx=12,fill='url(#coolSteel)',stroke='#3d514d',stroke_width=2)
    bolts_box(-56,-95,112,189)
    rect(-67,-43,134,76,rx=13,fill='url(#darkMetal)',stroke='#8ba18f',stroke_width=2)
    for x in range(-38,40,5):
        path(f'M{x} -39V28',stroke='#bac1a6',stroke_width=1.5,stroke_opacity=.6)
    for x in (-47,47):
        rect(x-8,-51,16,92,rx=5,fill='url(#steel)',stroke='#324d3e',stroke_width=1.5)
    circle(0,68,25,fill='url(#rubberRound)',stroke='#a2ad94',stroke_width=2)
    rect(-28,-110,56,37,rx=6,fill='url(#steelHorizontal)',stroke='#54705d',stroke_width=1)
    path('M0 0V164',stroke='#303b31',stroke_width=3)
    path('M-.8 0V164',stroke='#c6c5a0',stroke_width=1)
    end()


def crate(x,y,w,h,color='ochre'):
    grad={'ochre':'yellowPaint','green':'greenPaint','red':'redPaint','blue':'blueFloat','ivory':'roofIvory'}.get(color,'yellowPaint')
    rect(x+4,y+5,w,h,rx=5,fill='#24392f',fill_opacity=.24)
    rect(x,y,w,h,rx=5,fill='url(#darkMetal)',stroke='#293e35',stroke_width=2)
    rect(x+5,y+5,w-10,h-10,rx=2,fill='url(#net)')
    for i in range(max(8,int(w*h/500))):
        xx,yy=rng.uniform(x+8,x+w-8),rng.uniform(y+8,y+h-8)
        path(f'M{xx:.1f} {yy:.1f}q-7 -10 -11 0t12 5',fill='none',stroke='#b7ad7b',stroke_width=rng.uniform(.6,1.6),stroke_opacity=.26)
    rect(x+3,y+3,w-6,h-6,rx=3,fill='none',stroke=f'url(#{grad})',stroke_width=4.2)
    for d in [f'M{x+w/2} {y+5}V{y+h-5}',f'M{x+5} {y+h/2}H{x+w-5}']:
        path(d,stroke='#374636',stroke_width=4.5)
        path(d,stroke=f'url(#{grad})',stroke_width=2.8)
    path(f'M{x+7} {y+7}L{x+w-7} {y+h-7}M{x+w-7} {y+7}L{x+7} {y+h-7}',stroke='#c1b78c',stroke_width=1.5,stroke_opacity=.69)
    bolts_box(x,y,w,h)


def tanks(x,y,n=2):
    for i in range(n):
        yy=y+i*57
        rect(x-25+4,yy-23+5,50,47,rx=18,fill='#233c37',fill_opacity=.25)
        rect(x-25,yy-23,50,47,rx=18,fill='url(#blueFloat)',stroke='#2e5156',stroke_width=1.5)
        for xx in (x-14,x+14):
            path(f'M{xx} {yy-22}V{yy+22}',stroke='#354b43',stroke_width=4)
            path(f'M{xx-1} {yy-22}V{yy+22}',stroke='#b8c3b1',stroke_width=.85)
        path(f'M{x-16} {yy-15}Q{x} {yy-22} {x+16} {yy-15}',stroke='#d8e0cc',stroke_width=1.2,fill='none',stroke_opacity=.7)
        circle(x,yy-25,4,fill='url(#steelRound)')


def crane(x,y,tx,ty,color='yellow'):
    grad={'yellow':'yellowPaint','steel':'coolSteel','ivory':'roofIvory'}.get(color,'yellowPaint')
    rect(x-38,y-36,76,72,rx=8,fill=f'url(#{grad})',stroke='#435d4c',stroke_width=2)
    bolts_box(x-38,y-36,76,72)
    circle(x,y,31,fill='url(#darkMetal)',stroke='#a7b38c',stroke_width=2)
    circle(x,y,24,fill=f'url(#{grad})',stroke='#6f774d',stroke_width=1)
    dx,dy=tx-x,ty-y
    length=math.hypot(dx,dy)
    nx,ny=-dy/length*12,dx/length*12
    d=f'M{x+nx} {y+ny}L{tx+nx*.63} {ty+ny*.63}L{tx-nx*.63} {ty-ny*.63}L{x-nx} {y-ny}Z'
    path(d,transform='translate(8 12)',fill='#1b3a2d',fill_opacity=.2)
    path(d,fill=f'url(#{grad})',stroke='#566147',stroke_width=2)
    path(f'M{x+nx*.6} {y+ny*.6}L{tx+nx*.4} {ty+ny*.4}',stroke='#efdfa3',stroke_width=1.5,stroke_opacity=.77)
    path(f'M{x+nx*1.4} {y+ny*1.4}L{x+dx*.7+nx*1.4} {y+dy*.7+ny*1.4}',stroke='#263e34',stroke_width=7,stroke_linecap='round')
    path(f'M{x+nx*1.4} {y+ny*1.4}L{x+dx*.64+nx*1.4} {y+dy*.64+ny*1.4}',stroke='url(#coolSteel)',stroke_width=4,stroke_linecap='round')
    for xx,yy in [(x,y),(tx,ty)]:
        circle(xx,yy,12,fill='url(#steelRound)',stroke='#4c6149',stroke_width=1.4)
        use('bolt',xx,yy,scale=1.3)
    path(f'M{tx} {ty}Q{tx+17} {ty+23} {tx+35} {ty+18}',stroke='#354a39',stroke_width=2,fill='none')
    path(f'M{tx+34} {ty+17}q12 14 0 21q-9 1-5-7',stroke='url(#coolSteel)',stroke_width=4,fill='none')


def lifering(x,y,s=1):
    emit(f'<g transform="translate({x} {y}) scale({s})">')
    ellipse(4,6,43,44,fill='url(#softShadow)')
    circle(0,0,30,fill='none',stroke='#774f30',stroke_width=13)
    circle(0,-1,30,fill='none',stroke='url(#orangeRound)',stroke_width=11)
    for a in range(0,360,90):
        path('M-5-25L-6-37H6L5-25Z',transform=f'rotate({a})',fill='url(#roofIvory)',stroke='#ac9b73',stroke_width=.7)
    circle(0,-1,40,fill='none',stroke='#b5ad83',stroke_width=2)
    end()


def hose(x,y,s=1):
    emit(f'<g transform="translate({x} {y}) scale({s})">')
    for r in range(10,34,4):
        ellipse(2,3,r,r*1.7,fill='none',stroke='#172f2d',stroke_width=4.2)
        ellipse(1,2,r,r*1.7,fill='none',stroke='#748b7b',stroke_width=1,stroke_opacity=.65)
    path('M25 27C51 68 32 78 0 67',fill='none',stroke='#203e36',stroke_width=4)
    end()


def bench(x,y,w,h):
    rect(x+3,y+6,w,h,rx=9,fill='#244135',fill_opacity=.18)
    rect(x,y,w,h,rx=8,fill='url(#roofIvory)',stroke='#7d9380',stroke_width=1.7)
    for j in range(1,max(2,round(w/62))):
        xx=x+w*j/max(2,round(w/62))
        path(f'M{xx} {y+3}V{y+h-3}',stroke='#9aa792',stroke_width=1)
    rect(x+5,y+5,w-10,h-10,rx=6,fill='none',stroke='#fdf6de',stroke_width=.9,stroke_opacity=.84)


def table(x,y,w,h):
    rect(x+7,y+8,w,h,rx=6,fill='#183d2c',fill_opacity=.18)
    rect(x,y,w,h,rx=6,fill='url(#teak)',stroke='#5f6747',stroke_width=2)
    for xx in range(int(x+10),int(x+w),9):
        path(f'M{xx} {y+3}V{y+h-3}',stroke='#645636',stroke_width=.9)
        path(f'M{xx+1} {y+3}V{y+h-3}',stroke='#d5c494',stroke_width=.6,stroke_opacity=.7)
    bolts_box(x,y,w,h)


def solar(x,y,w,h):
    rect(x+4,y+6,w,h,rx=5,fill='#1c333d',fill_opacity=.25)
    rect(x,y,w,h,rx=4,fill='url(#roofIvory)',stroke='#668079',stroke_width=1.6)
    rect(x+7,y+7,w-14,h-14,rx=2,fill='url(#solarCells)')
    path(f'M{x+w/2} {y+5}V{y+h-5}M{x+5} {y+h/2}H{x+w-5}',stroke='#ccd4bc',stroke_width=3)
    bolts_box(x,y,w,h)


def hull(c):
    layer('hull-and-working-deck','02 · Reference hull, gunwales and working deck')
    path(b.HULL,fill='url(#fleetPaint)',stroke='#213a42',stroke_width=5,stroke_linejoin='round')
    path(hull_path(c['hull'],14),fill='url(#fleetCap)',stroke='#aebfae',stroke_width=1.3)
    path(b.DECK,fill='url(#'+{'alloy':'alloy','dark':'darkDeck','teak':'teak','wood':'teak','paint':'fleetCap','ivory':'roofIvory','red':'redPaint'}.get(c['deck'],'alloy')+')',stroke='#486053',stroke_width=2.4)
    path(b.DECK,fill='url(#nonSlip)')
    emit('<g clip-path="url(#deckClip)">')
    path(b.DECK,fill='none',stroke='#2a4840',stroke_width=12,stroke_opacity=.23)
    if c['deck'] in ('teak','wood'):
        for x in range(204,700,9):
            path(f'M{x} 114V1515',stroke='#4a4931',stroke_width=1.15,stroke_opacity=.75)
            path(f'M{x+1.1} 114V1515',stroke='#e5cc97',stroke_width=.65,stroke_opacity=.68)
            for k in range(4):
                yy=rng.uniform(120,1470)
                path(f'M{x+4} {yy:.1f}q2 31 0 74',fill='none',stroke='#655238',stroke_width=.55,stroke_opacity=.43)
        for y in range(241,1480,151):
            for x in range(213+(y%3)*9,687,45):
                path(f'M{x} {y}h8',stroke='#4e5034',stroke_width=.8,stroke_opacity=.7)
    else:
        for y in (393,901,1156,1391):
            path(f'M222 {y}H678',stroke='#c2cabb',stroke_width=2.4,stroke_opacity=.45,transform='translate(-.7 -.7)')
            path(f'M222 {y}H678',stroke='#53685e',stroke_width=1.2,stroke_opacity=.75)
        for x in (280,620):
            path(f'M{x} 784V1478',stroke='#51685a',stroke_width=1.2,stroke_opacity=.75)
    for x,y,rx,ry in [(267,1070,38,340),(635,1100,43,361),(450,1466,250,37),(452,418,173,42)]:
        ellipse(x,y,rx,ry,fill='url(#grime)')
    flecks(round(1800*c.get('finish',.7)),(215,155,690,1490),['#d7d6bc','#3b5550','#b0ab83','#6b7762'],.2,2.5)
    for _ in range(110):
        x,y=rng.uniform(229,671),rng.uniform(182,1481)
        path(f'M{x:.1f} {y:.1f}l{rng.uniform(-5,5):.1f} {rng.uniform(5,25):.1f}',stroke='#d5d5b9',stroke_width=rng.uniform(.5,1.1),stroke_opacity=.21)
    end()
    if c['hull']=='cat':
        for x in (214,612):
            path(f'M{x+19} 190H{x+46}L{x+72} 350H{x}Z',fill='url(#darkDeck)',stroke='#a5b5a3',stroke_width=1.3)
            path(f'M{x+19} 190H{x+46}L{x+72} 350H{x}Z',fill='url(#diamond)')
    # Paint chips occur on the narrow rail caps, not on an arbitrary silhouette.
    emit('<g clip-path="url(#hullClip)">')
    for j in range(round(150*c.get('finish',.7))):
        y=rng.uniform(684,1438)
        xx=(211 if j%2 else 689)+rng.uniform(-4,5)
        if c['hull'] in ('slender','yacht','sail','ribdark'):
            xx+=30 if j%2 else -30
        path(f'M{xx:.1f} {y:.1f}l{rng.uniform(-1,1):.1f} {rng.uniform(2,7):.1f}',stroke=rng.choice(['#c3c9ad','#1d4548','#bbb592']),stroke_width=rng.uniform(.6,1.8),stroke_opacity=.58)
    end()
    end()


def bow(c):
    layer('bow-fittings','03 · Bow hardware and mooring line')
    if c.get('bow_style')=='none':
        end();return
    if c['hull']=='cat':
        for x in (250,650):
            use('cleat',x,153,scale=.9)
        end();return
    top=132 if c['hull']!='tug' else 157
    rect(439,top-24,22,91,rx=5,fill='url(#coolSteel)',stroke='#557164',stroke_width=1.5)
    rect(445,top-18,10,66,rx=2,fill='#2d4945')
    rect(437,top-8,26,12,rx=3,fill='url(#steelHorizontal)')
    for i in range(14):
        yy=top+42+i*6.8
        ellipse(450,yy,3 if i%2 else 4.2,4.8,fill='none',stroke='#485443',stroke_width=2.3)
        ellipse(449.5,yy-.6,2.8 if i%2 else 4,4.4,fill='none',stroke='#c3c8a8',stroke_width=1)
    winch(450,top+164,.8)
    use('cleat',357,314,rotate=25,scale=.85)
    use('cleat',543,314,rotate=-25,scale=.85)
    if c['hull'] not in ('rib','ribdark'):
        b.rope_coil(361,358,23,28,5,-20)
    end()


def cabin(c):
    if c.get('no_cabin'):
        return
    x,y,w,h=c['roof']
    layer('pilothouse-roof','04 · Orthographic cabin roof and roof equipment')
    emit('<g clip-path="url(#deckClip)">')
    for dx,dy,op in [(11,18,.07),(7,12,.12),(4,7,.19)]:
        path(b.ROOF,transform=f'translate({dx} {dy})',fill='#1b3b34',fill_opacity=op)
    end()
    path(b.ROOF,fill='#334e43',stroke='#284738',stroke_width=8)
    path(b.ROOF,fill='url(#roofIvory)',stroke='#899e88',stroke_width=2)
    path(b.ROOF,fill='url(#roofLight)')
    emit('<g clip-path="url(#roofClip)">')
    path(b.ROOF,fill='none',stroke='#4c7460',stroke_width=11,stroke_opacity=.16)
    path(b.ROOF,fill='none',stroke='#ffffe4',stroke_width=3.8,stroke_opacity=.85,transform='translate(1 1)')
    flecks(round(900*c.get('finish',.7)),(x-3,y-9,x+w+3,y+h+9),['#899171','#beb68e','#fffce5','#788667'],.18,1.9)
    for xx,yy,rx,ry in [(x+11,y+18,23,30),(x+w-13,y+h-21,23,42),(x+w*.6,y+h-7,w*.36,13)]:
        ellipse(xx,yy,rx,ry,fill='url(#grime)')
    end()
    for xx in (x+14,x+w-14):
        for yy in (y+23,y+h*.4,y+h*.7,y+h-18):
            ellipse(xx,yy+4,4,9,fill='url(#rust)')
            use('bolt',xx,yy,scale=.62)
    for xx in (x+35,x+w-35):
        for yy in (y+61,y+h-45):
            rect(xx-4,yy-6,8,12,rx=3,fill='url(#coolSteel)')
            use('bolt',xx,yy,scale=.5)
        path(f'M{xx+4} {y+62}V{y+h-44}',stroke='#315340',stroke_width=4,stroke_opacity=.17)
        path(f'M{xx} {y+62}V{y+h-44}',stroke='url(#coolSteel)',stroke_width=4,stroke_linecap='round')
        path(f'M{xx-1} {y+62}V{y+h-44}',stroke='#fffbe2',stroke_width=.9,stroke_opacity=.88)
    typ=c.get('roof_type','dome')
    if typ=='dome':
        ellipse(456,y+h*.29+5,49,49,fill='url(#softShadow)')
        circle(450,y+h*.29,41,fill='#708b79',stroke='#9aaf99',stroke_width=1)
        circle(450,y+h*.29-2,38,fill='url(#whiteDome)',stroke='#d3deca',stroke_width=1)
        hatch(404,y+h*.61,92,h*.22,True)
        use('vent',x+63,y+h-35,scale=.74)
        use('vent',x+w-63,y+h-35,scale=.74)
    elif typ=='roundhatch':
        circle(454,y+119,66,fill='#204235',fill_opacity=.18)
        circle(450,y+112,63,fill='url(#darkMetal)',stroke='#586f60',stroke_width=3)
        circle(450,y+112,55,fill='url(#darkDeck)',stroke='#b1bfaa',stroke_width=1.5)
        for angle in range(0,360,45):
            rr=math.radians(angle)
            use('bolt',450+59*math.cos(rr),y+112+59*math.sin(rr),scale=.75)
        case(409,y+h-90,82,74)
    elif typ=='mast':
        circle(450,y+h*.35,25,fill='url(#whiteDome)',stroke='#6e8573',stroke_width=1)
        rect(366,y+57,168,17,rx=7,fill='url(#roofIvory)',stroke='#7c9480',stroke_width=1)
        path(f'M375 {y+59}H525',stroke='#fffce5',stroke_width=1.4)
        hatch(405,y+h*.69,90,83,True)
        case(x+55,y+h*.45,34,43)
        use('vent',x+w-67,y+h*.37,scale=.75)
        path(f'M450 {y+h*.35}L479 {y+h*.56}',stroke='#304e3e',stroke_width=2.5,stroke_opacity=.18)
    elif typ=='instruments':
        winch(450,y+h*.36,.9)
        hatch(x+w-114,y+h*.62,70,65,True)
        solar(x+35,y+h-51,w*.33,36)
        solar(x+w*.59,y+h-51,w*.31,36)
        use('vent',x+64,y+h*.3,scale=.8)
    elif typ=='utility':
        case(x+w*.5-27,y+58,54,59)
        case(x+49,y+h*.61,54,59)
        use('vent',450,y+h*.75,scale=.93)
    elif typ=='solar':
        solar(x+53,y+40,w-106,h*.48)
        hatch(416,y+h*.73,68,52,True)
        use('vent',x+61,y+h-46,scale=.8)
    else:
        path(f'M{x+18} {y+h*.55}H{x+w-18}',stroke='#839786',stroke_width=1,stroke_opacity=.7)
        use('vent',450,y+h*.77,scale=.88)
        hatch(x+69,y+37,w-138,48,True)
    # Lights and true vertical antenna footprints, without visible upright walls.
    for xx,col in [(x+1,'#bd6348'),(x+w-1,'#658268')]:
        rect(xx-4,y+95,8,20,rx=3,fill='#334e3e',stroke='#96ab94',stroke_width=.6)
        rect(xx-2,y+98,4,14,rx=2,fill=col)
    for xx,yy in [(x+29,y+32),(x+w-28,y+39)]:
        circle(xx,yy,5,fill='url(#steelRound)')
        circle(xx,yy-1,2,fill='#f5f0d6')
        path(f'M{xx} {yy}l19 41',stroke='#325941',stroke_width=1.4,stroke_opacity=.18)
    end()


def stern(c):
    layer('propulsion-and-platform','01 · Stern platform and visible propulsion fittings')
    typ=c.get('stern','platform')
    if typ=='plain':
        end();return
    if typ.startswith('outboard'):
        n=int(typ[-1]); xs=[450] if n==1 else [383,517]
        rect(287,1461,326,63,rx=9,fill='url(#coolSteel)',stroke='#36554f',stroke_width=2)
        rect(303,1472,294,39,rx=4,fill='url(#grating)')
        for x in xs:
            rect(x-23,1490,46,54,rx=8,fill='url(#coolSteel)',stroke='#314d50',stroke_width=2)
            path(f'M{x-44} 1539Q{x-51} 1507 {x} 1506Q{x+51} 1507 {x+44} 1539L{x+39} 1603Q{x+35} 1628 {x} 1629Q{x-35} 1628 {x-39} 1603Z',fill='url(#motor)',stroke='#243d48',stroke_width=3)
            path(f'M{x-29} 1535Q{x} 1517 {x+29} 1535L{x+27} 1597Q{x} 1611 {x-27} 1597Z',fill='none',stroke='#9aaba6',stroke_width=1.3,stroke_opacity=.57)
            rect(x-20,1541,40,11,rx=4,fill='#b4bfb2',fill_opacity=.6)
            for yy in range(1570,1596,5):
                path(f'M{x-23} {yy}H{x+23}',stroke='#1b3640',stroke_width=1.5,stroke_opacity=.58)
            path(f'M{x-24} 1529Q{x-32} 1574 {x-23} 1601',stroke='#d0d7c8',stroke_width=1.5,stroke_opacity=.35,fill='none')
    else:
        rect(298,1468,304,82,rx=11,fill='url(#coolSteel)',stroke='#3d5b51',stroke_width=2)
        rect(313,1481,274,51,rx=3,fill='url(#grating)',stroke='#4f6a58',stroke_width=2)
        for x in (305,450,595):
            rect(x-4,1474,8,68,rx=2,fill='url(#coolSteel)')
            use('bolt',x,1537,scale=.6)
        if typ.startswith('jet'):
            xs=[450] if typ=='jet1' else [261,639]
            for x in xs:
                rect(x-23,1490,46,56,rx=9,fill='url(#coolSteel)',stroke='#3b5950',stroke_width=2)
                rect(x-16,1504,32,34,rx=10,fill='url(#darkMetal)',stroke='#889f87',stroke_width=1.2)
                path(f'M{x-17} 1526Q{x} 1537 {x+17} 1526',fill='none',stroke='#c2cfb6',stroke_width=3)
    end()


def rails(c):
    layer('railings-and-fenders','07 · Rails, cleats, rubbing bands and fenders')
    if c.get('rail_style')=='none':
        end();return
    if c.get('rail_style')=='historic':
        for d in ['M438 153C326 249 271 387 270 600L275 1220Q291 1450 434 1521','M462 153C574 249 629 387 630 600L625 1220Q609 1450 466 1521']:
            path(d,fill='none',stroke='#3e4430',stroke_width=9)
            path(d,fill='none',stroke='url(#brass)',stroke_width=5.4)
            path(d,fill='none',stroke='#ebce8d',stroke_width=1,stroke_opacity=.68,transform='translate(-1 -1)')
        for x in (272,628):
            for y in range(641,1200,63):
                circle(x,y,5,fill='url(#brass)',stroke='#5d5834',stroke_width=1)
        end();return
    kind=c['hull']
    if kind=='cat':
        left,right=204,696
        railpaths=[f'M{left} 469V1414',f'M{right} 469V1414']
    else:
        narrow={'slender':36,'yacht':24,'sail':37,'ribdark':25}.get(kind,0)
        left,right=225+narrow,675-narrow
        railpaths=[f'M{left} 665L{left+12} 1423Q{left+12} 1459 {left+42} 1464H352',f'M{right} 665L{right-12} 1423Q{right-12} 1459 {right-42} 1464H548']
        if kind not in ('rib','ribdark','tug'):
            railpaths += [f'M438 154C{330+narrow} 269 {left} 427 {left} 608',f'M462 154C{570-narrow} 269 {right} 427 {right} 608']
    for d in railpaths:
        path(d,fill='none',stroke='#2a4a3d',stroke_width=4.5,stroke_opacity=.19,transform='translate(5 8)')
        path(d,fill='none',stroke='#4e6b5b',stroke_width=4.7,stroke_linecap='round')
        path(d,fill='none',stroke='url(#coolSteel)',stroke_width=3.3,stroke_linecap='round')
        path(d,fill='none',stroke='#f1eeda',stroke_width=.9,stroke_opacity=.75,transform='translate(-.6 -.6)')
    for side,x in [(-1,left),(1,right)]:
        for y in (684,853,1063,1277,1407):
            circle(x,y,4,fill='url(#steelRound)',stroke='#4c6a55',stroke_width=.5)
        for y in (732,1277):
            use('cleat',x-side*15,y,scale=.82)
        for y in (805,1371):
            use('fairlead',x+side*12,y,scale=.85)
        for y in (694,1129,1390):
            xx=x+side*31
            use('fender',xx,y,scale=.82)
            path(f'M{xx} {y-36}Q{x} {y-55} {x} {y-72}',fill='none',stroke='#bdba91',stroke_width=1.6)
    if kind in ('rib','ribdark'):
        # Stitched division seams run across the inflated perimeter tube.
        for side in (-1,1):
            for y in (411,585,809,1061,1270,1432):
                x=450+side*(226 if y>600 else (167 if y==411 else 215))
                path(f'M{x-side*14} {y}L{x+side*15} {y+3}',stroke='#354c4a',stroke_width=2.5,stroke_opacity=.7)
                path(f'M{x-side*14} {y-2}L{x+side*15} {y+1}',stroke='#e3c992',stroke_width=.8,stroke_opacity=.6)
    if kind=='tug':
        # Thick segmented bow and stern rubber give the tug its own silhouette.
        d='M201 495C202 290 295 109 450 106C605 109 698 290 699 495'
        path(d,fill='none',stroke='#213439',stroke_width=37,stroke_linecap='round')
        path(d,fill='none',stroke='#5a6360',stroke_width=30,stroke_dasharray='29 5',stroke_linecap='butt')
        path(d,fill='none',stroke='#bac0ac',stroke_width=30,stroke_dasharray='1 33',stroke_opacity=.55)
    end()


def gear(c):
    layer('deck-equipment','06 · Vessel-specific working equipment')
    for item in c.get('gear',[]):
        typ,*a=item
        if typ=='hatch': hatch(*a)
        elif typ=='case': case(*a)
        elif typ=='grille': grille(*a)
        elif typ=='crate': crate(*a)
        elif typ=='crane': crane(*a)
        elif typ=='tanks': tanks(*a)
        elif typ=='lifering': lifering(*a)
        elif typ=='tow': tow(*a)
        elif typ=='winch': winch(*a)
        elif typ=='hose': hose(*a)
        elif typ=='bench': bench(*a)
        elif typ=='table': table(*a)
        elif typ=='solar': solar(*a)
        elif typ=='hazard':
            x,y,w,h=a;rect(x,y,w,h,rx=3,fill='url(#hazardStripes)',stroke='#6f7853',stroke_width=1.5)
        elif typ=='deckcircle':
            x,y,r=a;circle(x,y,r,fill='none',stroke='#e0debb',stroke_width=4.4,stroke_opacity=.85);case(x-20,y-20,40,40)
        elif typ=='buoy':
            x,y,s=a;circle(x,y,25*s,fill='url(#yellowPaint)',stroke='#5d6542',stroke_width=2);path(f'M{x-24*s} {y}H{x+24*s}M{x} {y-24*s}V{y+24*s}',stroke='#465a3c',stroke_width=3)
        elif typ=='netbow':
            path('M287 175L333 378H567L613 175Z',fill='url(#net)',stroke='#9dad9b',stroke_width=3)
            path('M288 175L567 378M612 175L333 378',stroke='#a5b5a0',stroke_width=2)
            rect(444,159,12,205,rx=4,fill='url(#coolSteel)',stroke='#547367',stroke_width=1.3)
        else:
            draw_special(typ,a,c)
    end()


def draw_special(typ,a,c):
    if typ=='reactor':
        x,y,r,col=a
        glow='cyanCore' if col=='blue' else 'goldCore'
        metal='coolSteel' if col=='blue' else 'brass'
        ellipse(x+6,y+10,r+13,r+15,fill='url(#softShadow)')
        circle(x,y,r,fill='url(#darkMetal)',stroke=f'url(#{metal})',stroke_width=6)
        circle(x,y,r*.81,fill='url(#fleetPaint)',stroke='#829a88',stroke_width=1.4)
        circle(x,y,r*.55,fill='url(#darkMetal)',stroke=f'url(#{metal})',stroke_width=4.7)
        circle(x,y,r*.29,fill=f'url(#{glow})',stroke='#45616a',stroke_width=2)
        circle(x,y,r*.15,fill=f'url(#{glow})')
        for i in range(12):
            theta=math.tau*i/12
            dx,dy=math.cos(theta),math.sin(theta)
            path(f'M{x+dx*r*.56} {y+dy*r*.56}L{x+dx*r*.96} {y+dy*r*.96}',stroke='#253f42',stroke_width=3)
            path(f'M{x+dx*r*.57-1} {y+dy*r*.57-1}L{x+dx*r*.95-1} {y+dy*r*.95-1}',stroke='#b7c9b8',stroke_width=.85,stroke_opacity=.6)
            use('bolt',x+dx*r*.91,y+dy*r*.91,scale=.72)
            circle(x+dx*r*.4,y+dy*r*.4,2.4,fill=f'url(#{glow})')
    elif typ=='lamp':
        x,y,s=a
        rect(x-10*s,y-12*s,20*s,24*s,rx=4,fill='url(#coolSteel)',stroke='#506c61',stroke_width=1.2)
        rect(x-7*s,y-9*s,14*s,18*s,rx=4,fill='url(#goldCore)')
        path(f'M{x-4*s} {y-7*s}H{x+4*s}',stroke='#fff9db',stroke_width=1.6)
    elif typ=='pod':
        x,y,w,h,col=a
        glow='cyanCore' if col=='blue' else 'goldCore'
        emit(f'<g transform="translate({x} {y})">')
        d=f'M0 {-h*.5}Q{w*.48} {-h*.49} {w*.5} {-h*.37}L{w*.49} {h*.36}Q{w*.48} {h*.49}0 {h*.5}Q{-w*.48} {h*.49}{-w*.49} {h*.36}L{-w*.5} {-h*.37}Q{-w*.48} {-h*.49}0 {-h*.5}Z'
        path(d,fill='url(#motor)',stroke='#324d54',stroke_width=3)
        path(d,transform='scale(.86 .96)',fill='url(#coolSteel)',stroke='#859995',stroke_width=1.5)
        for yy in (-h*.26,0,h*.28):
            rect(-w*.48,yy-13,w*.96,26,rx=4,fill='url(#darkMetal)',stroke='#61796c',stroke_width=1.3)
            path(f'M{-w*.43} {yy-5}H{w*.43}',stroke='#ca985c',stroke_width=4)
            for xx in (-w*.35,w*.35):
                use('bolt',xx,yy+5,scale=.6)
        for yy in (-h*.38,h*.39):
            ellipse(0,yy,w*.25,h*.045,fill=f'url(#{glow})',stroke='#486d75',stroke_width=2)
        for yy in (-h*.16,h*.14):
            rect(-w*.3,yy-h*.07,w*.6,h*.12,rx=5,fill='url(#fleetPaint)',stroke='#435c61',stroke_width=1)
            for j in range(5):
                path(f'M{-w*.21} {yy-h*.05+j*h*.018}H{w*.21}',stroke='#526b70',stroke_width=1.5)
        path(f'M{-w*.28} {-h*.4}V{h*.41}',stroke='#e0e3cf',stroke_width=1.5,stroke_opacity=.6)
        end()
    elif typ=='sci-panels':
        # Orange inlays and longitudinal machinery channel preserve this reference's identity.
        rect(390,811,120,481,rx=26,fill='url(#darkMetal)',stroke='#9cac9d',stroke_width=3)
        for side in (-1,1):
            def pxx(p):return 450+side*(p-450)
            path(f'M{pxx(485)} 212L{pxx(536)} 333L{pxx(568)} 466L{pxx(529)} 397Z',fill='url(#orange)',stroke='#795e43',stroke_width=1.2)
            path(f'M{pxx(565)} 820L{pxx(602)} 919L{pxx(624)} 1245L{pxx(552)} 1339Z',fill='url(#coolSteel)',stroke='#516b70',stroke_width=2)
            path(f'M{pxx(535)} 838L{pxx(551)} 925L{pxx(559)} 1153L{pxx(534)} 1234Z',fill='url(#orange)',stroke='#93633e',stroke_width=1.4)
            rect(pxx(573)-10,602,20,169,rx=6,fill='url(#darkMetal)',stroke='#859995',stroke_width=1)
            circle(pxx(583),610,5,fill='url(#cyanCore)')
            path(f'M{pxx(469)} 774L{pxx(492)} 1200L{pxx(480)} 1350',fill='none',stroke='url(#coolSteel)',stroke_width=5,stroke_linecap='round')
            for yy in range(843,1250,79):
                use('bolt',pxx(504),yy,scale=.75)
        rect(428,183,44,211,rx=9,fill='url(#motor)',stroke='#8faaa3',stroke_width=1.3)
        grille(436,203,28,118)
        hatch(408,499,84,93,True)
    elif typ=='rigging':
        x1,y1,x2,y2,x3,y3=a
        path(f'M{x1} {y1}L{x2} {y2}L{x3} {y3}Z',fill='url(#sailCloth)',stroke='#8f9a83',stroke_width=1.1)
        path(f'M{x1+2} {y1+4}L{x2+3} {y2-8}',stroke='#faf7e0',stroke_width=1.2)
        for t in (.2,.4,.6,.8):
            path(f'M{x1+(x2-x1)*t} {y1+(y2-y1)*t}L{x1+(x3-x1)*t} {y1+(y3-y1)*t}',stroke='#969c84',stroke_width=.6,stroke_opacity=.58)
    elif typ=='grate':
        x,y,w,h=a
        rect(x,y,w,h,rx=4,fill='url(#brass)',stroke='#615738',stroke_width=3)
        rect(x+7,y+7,w-14,h-14,rx=1,fill='url(#grating)',stroke='#343f2e',stroke_width=2)
        bolts_box(x,y,w,h)
    elif typ=='capstan':
        x,y,s=a
        circle(x,y,36*s,fill='url(#teak)',stroke='#d2b273',stroke_width=4)
        for i in range(8):
            ang=math.tau*i/8
            path(f'M{x+math.cos(ang)*17*s} {y+math.sin(ang)*17*s}L{x+math.cos(ang)*51*s} {y+math.sin(ang)*51*s}',stroke='#4c4e32',stroke_width=6*s,stroke_linecap='round')
            path(f'M{x+math.cos(ang)*17*s-1} {y+math.sin(ang)*17*s-1}L{x+math.cos(ang)*51*s-1} {y+math.sin(ang)*51*s-1}',stroke='url(#brass)',stroke_width=3.4*s,stroke_linecap='round')
        circle(x,y,18*s,fill='url(#brass)',stroke='#665e3c',stroke_width=2)
    elif typ=='oars':
        for side in (-1,1):
            for j in range(9):
                yy=710+j*61
                inside=450+side*176
                outside=450+side*(332+(j%2)*8)
                ytip=yy-31
                path(f'M{inside} {yy}L{outside} {ytip}',stroke='#4d4b31',stroke_width=7,stroke_linecap='round')
                path(f'M{inside} {yy-1}L{outside} {ytip-1}',stroke='url(#teak)',stroke_width=4,stroke_linecap='round')
                path(f'M{outside-side*8} {ytip-6}L{outside+side*34} {ytip-11}L{outside+side*40} {ytip+3}L{outside-side*8} {ytip+7}Z',fill='url(#teak)',stroke='#6f6443',stroke_width=1.2)
                path(f'M{outside} {ytip-3}L{outside+side*31} {ytip-6}',stroke='#d7bf86',stroke_width=.9)
                ellipse(inside,yy,8,5,fill='url(#brass)',stroke='#625b3a',stroke_width=.8)
    elif typ=='historical-rig':
        for yy in (338,1211):
            rect(441,yy-61,18,305,rx=4,fill='url(#brass)',stroke='#655b38',stroke_width=1.3)
            circle(450,yy+260,22,fill='url(#brass)',stroke='#554e33',stroke_width=2)
            for dx in (-101,101):
                path(f'M450 {yy+270}L{450+dx} {yy+205}',stroke='#4f4e33',stroke_width=2)
                path(f'M450 {yy+269}L{450+dx} {yy+204}',stroke='#d9c38c',stroke_width=.7)
        path('M450 130V1490',stroke='#3f4530',stroke_width=3)
        path('M449 130V1490',stroke='#bfa469',stroke_width=1)
        for x in (303,597):
            for y in (623,1045):
                rect(x-28,y-12,56,24,rx=6,fill='url(#coolSteel)',stroke='#746a45',stroke_width=3)
                circle(x+(12 if x<450 else -12),y,14,fill='url(#darkMetal)',stroke='#b6995f',stroke_width=2)
        b.rope_coil(320,992,22,28,5,14)
        b.rope_coil(580,693,22,28,5,-13)
    elif typ=='square-sail':
        x,y,w,h=a
        d=f'M{x+42} {y+34}Q{x+w*.5} {y-23} {x+w-42} {y+34}L{x+w} {y+h}Q{x+w*.5} {y+h-73} {x} {y+h}Z'
        path(d,transform='translate(6 9)',fill='#25351f',fill_opacity=.22)
        path(d,fill='url(#redSail)',stroke='#796a43',stroke_width=3)
        path(f'M{x+44} {y+38}Q{x+w*.5} {y-16} {x+w-44} {y+38}',fill='none',stroke='url(#brass)',stroke_width=6)
        path(f'M{x+3} {y+h-2}Q{x+w*.5} {y+h-76} {x+w-3} {y+h-2}',fill='none',stroke='url(#brass)',stroke_width=6)
        for k in range(1,9):
            xx=x+w*k/9
            path(f'M{xx+17*(1-k/4.5)} {y+18+abs(k-4.5)*6}Q{xx+7} {y+h*.56} {xx} {y+h-8-32*(1-abs(k-4.5)/4.5)}',fill='none',stroke='#442f26',stroke_width=1.4,stroke_opacity=.58)
            path(f'M{xx+19*(1-k/4.5)} {y+20+abs(k-4.5)*6}Q{xx+9} {y+h*.56} {xx+2} {y+h-8-32*(1-abs(k-4.5)/4.5)}',fill='none',stroke='#d6a775',stroke_width=.7,stroke_opacity=.34)
        path(f'M450 {y-10}V{y+h-33}',stroke='url(#brass)',stroke_width=7)
        # Original heraldic sea-creature motifs, built from editable curves.
        for xx,scale in [(x+w*.31,1),(x+w*.69,-1)]:
            emit(f'<g transform="translate({xx} {y+h*.51}) scale({scale*.85} .85)">')
            path('M-8-30Q-28-55-38-32Q-18-32-23-15Q-43-11-35 10Q-22 5-11 16L-30 33L-42 24L-48 34L-30 47L-4 26L10 38L5 53L18 57L24 36L12 18Q37 22 34 5L48 4L49-7L26-4L20-22L32-35L21-42L7-31Q8-45-3-46Z',fill='url(#brass)',stroke='#b99658',stroke_width=.8)
            path('M-5 18Q-39 21-35-5Q-62-22-51 5Q-51 33-18 33',fill='none',stroke='#d9b777',stroke_width=5,stroke_linecap='round')
            circle(15,-29,2,fill='#705032')
            end()
        for xx,yy in [(x+42,y+34),(x+w-42,y+34),(x,y+h),(x+w,y+h)]:
            circle(xx,yy,5,fill='url(#brass)',stroke='#675a37',stroke_width=1)
    elif typ=='carving':
        x,y,s=a
        path(f'M{x} {y+74}Q{x-31} {y+20} {x-8} {y-33}Q{x+14} {y-52} {x+15} {y-26}Q{x-3} {y-22} {x+8} {y+5}L{x+27} {y+33}Z',fill='url(#brass)',stroke='#715e37',stroke_width=2)
        for yy in range(int(y-7),int(y+63),11):
            path(f'M{x-8} {yy}Q{x} {yy+7} {x+12} {yy+4}',fill='none',stroke='#ebca84',stroke_width=1.1)
    elif typ=='trimaran-nets':
        for flip in (False,True):
            emit('<g transform="translate(900 0) scale(-1 1)">' if flip else '<g>')
            path('M227 358L384 385L315 610L236 702Z',fill='url(#net)',stroke='#e1e2cb',stroke_width=3)
            path('M246 979L307 936L307 1308L235 1458Z',fill='url(#net)',stroke='#d8dfc7',stroke_width=3)
            path('M194 262L214 192L231 584L228 717L194 791Z',fill='url(#blueFloat)',stroke='#8ca9ac',stroke_width=1.3)
            path('M196 1052L224 1070L231 1422L201 1495Z',fill='url(#blueFloat)',stroke='#8ca9ac',stroke_width=1.3)
            path('M207 816L340 751M209 1486L369 1410',stroke='#546f72',stroke_width=10)
            path('M207 814L340 749M209 1484L369 1408',stroke='url(#coolSteel)',stroke_width=6)
            for yy in (518,848,1180,1451):
                use('bolt',208,yy,scale=.8)
            end()
    elif typ=='sailing-rig':
        path('M450 207V1527',stroke='#334946',stroke_width=3)
        path('M449 207V1527',stroke='#d0d9c4',stroke_width=1)
        rect(443,887,14,619,rx=5,fill='url(#coolSteel)',stroke='#3e5f5b',stroke_width=2)
        circle(450,880,18,fill='url(#darkMetal)',stroke='#c0c9af',stroke_width=3)
        for d in ['M450 880L217 690','M450 880L683 690','M450 880L205 1433','M450 880L695 1433','M450 207L217 690','M450 207L683 690']:
            path(d,fill='none',stroke='#425b4d',stroke_width=2)
            path(d,fill='none',stroke='#d5ddc4',stroke_width=.7,transform='translate(-.5 -.5)')
        path('M449 1378L178 1453M451 1378L722 1453',stroke='#415d56',stroke_width=10,stroke_linecap='round')
        path('M449 1376L178 1451M451 1376L722 1451',stroke='url(#coolSteel)',stroke_width=6,stroke_linecap='round')
        for x,y in [(399,1060),(501,1060),(372,1269),(528,1269)]:
            winch(x,y,.46)
        rect(437,250,26,111,rx=4,fill='url(#coolSteel)',stroke='#617d6c',stroke_width=1)
    elif typ=='armour':
        for flip in (False,True):
            emit('<g transform="translate(900 0) scale(-1 1)">' if flip else '<g>')
            path('M310 259L369 192L392 247L360 315Z',fill='url(#fleetPaint)',stroke='#acb59a',stroke_width=1.5)
            path('M255 520L312 502L300 866L239 887Z',fill='url(#fleetPaint)',stroke='#4c634f',stroke_width=3)
            path('M222 960L292 949L306 1370L249 1400L219 1293Z',fill='url(#fleetPaint)',stroke='#435c4d',stroke_width=3)
            case(219,957,71,113,'yellow')
            case(218,1084,74,129,'blue')
            grille(251,578,33,147)
            for yy in (615,810,964,1339):
                use('bolt',269,yy,scale=.8)
            path('M290 284L318 264M286 303L314 283M282 322L310 302',stroke='#d3b14f',stroke_width=6,stroke_opacity=.85)
            end()
        rect(423,158,54,163,rx=8,fill='url(#fleetPaint)',stroke='#b2b595',stroke_width=2)
        path('M430 238L450 217L470 238M430 267L450 246L470 267',fill='none',stroke='#d1ac4d',stroke_width=6)
        case(323,526,254,57,'yellow')
        for x in (323,577):
            path(f'M{x} 584V856',stroke='#51684f',stroke_width=8)
            path(f'M{x-1} 584V856',stroke='url(#coolSteel)',stroke_width=4)
    elif typ=='dinghy':
        x,y,w,h,col=a
        emit(f'<g transform="translate({x} {y})">')
        d=f'M0 {-h*.5}Q{w*.5} {-h*.4} {w*.49} {-h*.08}L{w*.44} {h*.36}Q{w*.41} {h*.5}0 {h*.5}Q{-w*.41} {h*.5}{-w*.44} {h*.36}L{-w*.49} {-h*.08}Q{-w*.5} {-h*.4}0 {-h*.5}Z'
        grad='orange' if col=='orange' else 'roofIvory'
        path(d,fill=f'url(#{grad})',stroke='#4a6262',stroke_width=3)
        path(d,transform='scale(.68 .81)',fill='url(#teak)',stroke='#63775f',stroke_width=2)
        for yy in (-h*.12,h*.17):
            rect(-w*.36,yy,w*.72,h*.07,rx=2,fill=f'url(#{grad})',stroke='#7a8f78',stroke_width=.9)
        for yy in (-h*.28,h*.29):
            path(f'M{-w*.44} {yy}H{w*.44}',stroke='#465f52',stroke_width=2)
            path(f'M{-w*.44} {yy-1}H{w*.44}',stroke='#c9ccb0',stroke_width=.7)
        path(f'M{-w*.3} {-h*.31}Q0 {-h*.47} {w*.3} {-h*.31}',fill='none',stroke='#f6ecd1',stroke_width=1.3,stroke_opacity=.8)
        rect(-w*.15,h*.38,w*.3,h*.13,rx=3,fill='url(#motor)',stroke='#87988b',stroke_width=.8)
        end()
    elif typ=='canopy':
        x,y,w,h,col=a
        grad='canvas' if col=='khaki' else 'redPaint'
        d=f'M{x} {y}Q{x+w*.5} {y+23} {x+w} {y}Q{x+w-20} {y+h*.5} {x+w+7} {y+h}Q{x+w*.55} {y+h-28} {x-8} {y+h}Q{x+20} {y+h*.5} {x} {y}Z'
        path(d,fill='#1a382b',fill_opacity=.23,transform='translate(8 12)')
        path(d,fill=f'url(#{grad})',stroke='#665b40',stroke_width=2)
        for xx,yy in [(x,y),(x+w,y),(x+w+7,y+h),(x-8,y+h)]:
            path(f'M{xx} {yy}Q{x+w*.49} {y+h*.53} {x+w*.5} {y+h*.5}',fill='none',stroke='#e0c8a0',stroke_width=1.3,stroke_opacity=.43)
            path(f'M{xx} {yy}l{(-18 if xx<x+w*.5 else 18)} {(-25 if yy<y+h*.5 else 25)}',stroke='#c8c09a',stroke_width=1.4)
            circle(xx,yy,2.5,fill='url(#steelRound)')
        for k in range(9):
            xx=x+w*(k+1)/10
            path(f'M{xx} {y+15}Q{xx+13} {y+h*.5} {xx+5} {y+h-15}',fill='none',stroke='#ddd2ad',stroke_width=.6,stroke_opacity=.13)
    elif typ=='planter':
        x,y,w,h=a
        rect(x,y,w,h,rx=3,fill='url(#teak)',stroke='#687453',stroke_width=2)
        rect(x+4,y+4,w-8,h-8,rx=2,fill='#354733')
        for _ in range(max(8,int(w*h/140))):
            xx,yy=rng.uniform(x+7,x+w-7),rng.uniform(y+7,y+h-7)
            d=f'M{xx:.1f} {yy:.1f}q-7 -8 -2 -13q11 4 2 13Z'
            path(d,fill=rng.choice(['#657b45','#8a9250','#a3a86d','#445d3e']),fill_opacity=.85)
    elif typ=='helipad':
        x,y,w,h=a
        rect(x+5,y+6,w,h,rx=15,fill='#263e35',fill_opacity=.25)
        rect(x,y,w,h,rx=13,fill='url(#greenPaint)',stroke='#b7bda5',stroke_width=3)
        rect(x+10,y+10,w-20,h-20,rx=9,fill='none',stroke='#dfddba',stroke_width=1.2,stroke_opacity=.7)
        circle(x+w/2,y+h/2,min(w,h)*.38,fill='none',stroke='#d4b356',stroke_width=6)
        cx,cy=x+w/2,y+h/2
        path(f'M{cx-29} {cy-42}V{cy+42}M{cx+29} {cy-42}V{cy+42}M{cx-29} {cy}H{cx+29}',stroke='#e7e8d3',stroke_width=10)
        flecks(240,(x+12,y+12,x+w-12,y+h-12),['#c6c9a2','#2f4f42','#9aa77c'],.24,2.6)
    else:
        raise ValueError(f'Unknown fitting: {typ}')


def make(name):
    c=BOATS[name]
    b.PARTS.clear()
    rng.seed(180930+sum((i+1)*ord(ch) for i,ch in enumerate(name)))
    definitions(c)
    stern(c)
    hull(c)
    bow(c)
    cabin(c)
    gear(c)
    rails(c)
    emit('</svg>')
    svg='\n'.join(b.PARTS)+'\n'
    start=svg.index('  <title')
    stop=svg.index('  <defs>',start)
    title=escape(c['title'])
    source=escape(c['source'])
    svg=svg[:start]+f'''  <title id="title">{title} — orthographic overhead</title>
  <desc id="description">Detailed editable vector interpretation of {title} from Urchin Skipper. True vertical top view, bow up, transparent background. Reference-specific hull, cabin, deck layout and equipment. Weathered paint, fine vector material grain, metal fittings, rails and ropes. All geometry, gradients and patterns are vector artwork; there is no embedded raster image.</desc>
  <metadata>Authored 2026-09-18. Reference: public/assets/fleet/{source}.png. Designer-supplied originals retained. Reproducible recipe: python3 assets/vectors/create-fleet.py {name}. Shared vector fittings: create-workboat.py. Standalone artwork; no changes to the live fleet, camera, collision geometry or game behavior. Browser and game checks omitted at the designer's request.</metadata>
'''+svg[stop:]
    out=ROOT.parent/f'generated-review/fleet-vector/{name}-top.svg'
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('x',encoding='utf-8') as f:
        f.write(svg)
    print(f'Created {out.name}')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('boat',choices=BOATS)
    make(parser.parse_args().boat)
