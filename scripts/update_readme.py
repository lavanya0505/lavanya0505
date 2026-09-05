from pathlib import Path
from urllib.request import Request,urlopen
import json,os
root=Path(__file__).resolve().parent.parent; readme=root/'README.md'
req=Request('https://api.github.com/users/lavanya0505/repos?sort=updated&direction=desc&per_page=8',headers={'Accept':'application/vnd.github+json','User-Agent':'lavanya-profile'})
if os.getenv('GITHUB_TOKEN'): req.add_header('Authorization','Bearer '+os.environ['GITHUB_TOKEN'])
with urlopen(req,timeout=20) as r: repos=json.load(r)
rows=['| Project | Description |','|---|---|']
for x in [r for r in repos if not r.get('fork')][:5]: rows.append(f"| [{x['name']}]({x['html_url']}) | {(x.get('description') or 'AI/ML project').replace('|','\\|')} |")
t=readme.read_text(); a=t.index('<!-- RECENTLY_PUSHED_START -->'); b=t.index('<!-- RECENTLY_PUSHED_END -->'); readme.write_text(t[:a]+'<!-- RECENTLY_PUSHED_START -->\n'+'\n'.join(rows)+'\n'+t[b:])
