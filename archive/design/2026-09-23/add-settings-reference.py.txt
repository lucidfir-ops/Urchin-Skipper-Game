"""Append the designer-approved Settings reference without rewriting existing DOCX parts."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
book = ROOT / 'Urchin_Skipper_Bible_Definitive_v2.docx'
photo = ROOT / 'feedback/9-20/doogee e3 tab max 14inch/another empty space to fill.jpg'
archive = ROOT / 'docs/history/2026-09-20-device-feedback'
archive.mkdir(parents=True, exist_ok=True)
backup = archive / 'Bible-before-settings-reference.docx'
marker = 'Settings menu reference — 20 September 2026'
with ZipFile(book) as source:
    parts = {name: source.read(name) for name in source.namelist()}
document = parts['word/document.xml'].decode('utf-8')
if marker in document:
    raise SystemExit('Reference already present; refusing a duplicate amendment.')
if backup.exists():
    raise SystemExit('Preserved original already exists; inspect before retrying.')
shutil.copy2(book, backup)
ns = {'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing'}
ids = [int(el.attrib['id']) for el in ET.fromstring(document).findall('.//wp:docPr', ns)]
drawing_id = max(ids, default=0) + 1
rid = 'rIdSettings20260920'
media = 'word/media/settings-reference-20260920.jpeg'
# Supplied JPEG is 1920 x 1280. Fit the original page's 6.9-inch text area.
cx, cy = 5943600, 3962400
caption = ('Designer-approved current Settings menu reference. Added at the designer’s request on '
           '20 September 2026. Preserve its organization while applying the explicitly requested '
           'responsive sizing, fullscreen and optional fit-to-screen controls. The existing '
           'harbour reference above remains unchanged. The weather screen is not an approved reference.')
addition = f'''<w:p><w:r><w:br w:type="page"/></w:r></w:p>
<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr><w:r><w:t>{escape(marker)}</w:t></w:r></w:p>
<w:p><w:r><w:t>{escape(caption)}</w:t></w:r></w:p>
<w:p><w:r><w:drawing><wp:inline xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" distT="0" distB="0" distL="0" distR="0">
<wp:extent cx="{cx}" cy="{cy}"/><wp:docPr id="{drawing_id}" name="Approved Settings screenshot" descr="Designer supplied tablet Settings menu reference, September 20"/>
<a:graphic xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">
<pic:nvPicPr><pic:cNvPr id="0" name="settings-reference-20260920.jpeg"/><pic:cNvPicPr/></pic:nvPicPr>
<pic:blipFill><a:blip xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>
<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm><a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>
</pic:pic></a:graphicData></a:graphic></wp:inline></w:drawing></w:r></w:p>'''
position = document.rfind('<w:sectPr')
assert position > 0
parts['word/document.xml'] = (document[:position] + addition + document[position:]).encode()
rels = parts['word/_rels/document.xml.rels'].decode()
parts['word/_rels/document.xml.rels'] = rels.replace('</Relationships>', f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="media/settings-reference-20260920.jpeg"/></Relationships>').encode()
parts[media] = photo.read_bytes()
for name in ['word/document.xml', 'word/_rels/document.xml.rels']:
    ET.fromstring(parts[name])
assert b'Extension="jpeg"' in parts['[Content_Types].xml']
temp = archive / 'Bible-amended.tmp.docx'
with ZipFile(temp, 'x', ZIP_DEFLATED) as output:
    for name, content in parts.items():
        output.writestr(name, content)
with ZipFile(backup) as before, ZipFile(temp) as after:
    assert after.testzip() is None
    for name in before.namelist():
        if name not in ['word/document.xml', 'word/_rels/document.xml.rels']:
            assert before.read(name) == after.read(name), name
    assert after.read(media) == photo.read_bytes()
    # Original text, drawing references and §23 content are literally unchanged.
    assert after.read('word/document.xml').decode().replace(addition, '') == document
temp.replace(book)
digest = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
record = {'original': digest(backup), 'amended': digest(book), 'settings_image': digest(photo),
          'preserved_parts': len(parts)-3, 'only_modified_parts': ['word/document.xml', 'word/_rels/document.xml.rels']}
(archive / 'bible-amendment-verification.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
