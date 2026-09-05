from pathlib import Path
from urllib.request import Request, urlopen
import argparse
import json
import os


def fetch_repositories(username, count):
	request = Request(
		f'https://api.github.com/users/{username}/repos?sort=updated&direction=desc&per_page=100',
		headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'lavanya-profile'},
	)
	if os.getenv('GITHUB_TOKEN'):
		request.add_header('Authorization', 'Bearer ' + os.environ['GITHUB_TOKEN'])
	with urlopen(request, timeout=20) as response:
		repositories = json.load(response)
	return [repo for repo in repositories if not repo.get('fork')][:count]


def render_rows(repositories):
	rows = ['| Project | What it is | Stack | Updated |', '|---|---|---|---|']
	for repo in repositories:
		description = (repo.get('description') or 'AI/ML project').replace('|', '\\|')
		language = repo.get('language') or 'AI/ML'
		updated = repo['updated_at'][:10]
		rows.append(
			f"| [{repo['name']}]({repo['html_url']}) | {description} | `{language}` | {updated} |"
		)
	return '\n'.join(rows)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--count', type=int, default=6)
	args = parser.parse_args()

	root = Path(__file__).resolve().parent.parent
	readme = root / 'README.md'
	username = os.getenv('GH_USER', 'lavanya0505')
	repositories = fetch_repositories(username, args.count)
	text = readme.read_text()
	start = text.index('<!-- RECENTLY_PUSHED_START -->')
	end = text.index('<!-- RECENTLY_PUSHED_END -->')
	replacement = '<!-- RECENTLY_PUSHED_START -->\n' + render_rows(repositories) + '\n'
	readme.write_text(text[:start] + replacement + text[end:])


if __name__ == '__main__':
	main()
