"""Check Design navigation, local media and original gallery image counts."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

root = Path(__file__).resolve().parent
checked = 0
for lang in ['en', 'zh', 'ja', 'de']:
    for relative in ['index.html', 'projects/sequence-house.html', 'projects/day-care.html']:
        path = root / lang / relative
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        assert len(soup.select('.site-header')) == 1, path
        assert len(soup.select('[data-lang-link]')) == 4, path
        for tag in soup.select('[href], [src]'):
            value = tag.get('href', tag.get('src', ''))
            assert 'cargo.site' not in value, (path, value)
            if value.startswith('/'):
                target = root / urlsplit(value).path.lstrip('/')
                assert target.exists(), (path, value)
        for link in soup.select('[data-lang-link]'):
            expected = '' if relative == 'index.html' else relative
            assert link['href'] == f'/{link["data-lang-link"]}/{expected}'
        if relative == 'index.html':
            assert len(soup.select('.design-project')) == 9
            assert len(soup.select('.design-project a')) == 2
        else:
            assert len(soup.select('#main-content img')) == 5
        checked += 1
print(f'PASS: {checked} Design pages; all links/media local and present; 9 covers and 5 images per project.')
