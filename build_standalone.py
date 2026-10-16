"""Bundle the static planner as one HTML file; no third-party build tools."""
from pathlib import Path
import base64
root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text()
for name in ['leaflet.css', 'style.css']:
    content = (root / 'assets' / name).read_text()
    html = html.replace(f'<link rel="stylesheet" href="assets/{name}">', '<style>' + content + '</style>')
for name in ['leaflet.js', 'data.js', 'engine.js', 'app.js']:
    content = (root / 'assets' / name).read_text().replace('</script', '<\\/script')
    html = html.replace(f'<script src="assets/{name}"></script>', '<script>' + content + '</script>')
for name, mime in [('route.gpx', 'application/gpx+xml'), ('forecast-reference.png', 'image/png')]:
    url = 'data:' + mime + ';base64,' + base64.b64encode((root / 'assets' / name).read_bytes()).decode()
    html = html.replace('assets/' + name, url)
(root / 'soderasen-trip.html').write_text(html)
