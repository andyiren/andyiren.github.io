"""Restore Design content from the user's saved Cargo exports. Run from repo root."""
from pathlib import Path
import re, shutil, html
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parent
source = root.parent
assets = root / 'assets' / 'design'
assets.mkdir(parents=True, exist_ok=True)
home = BeautifulSoup((source / 'Yi-dong.html').read_text(encoding='utf-8'), 'html.parser')
columns = []
for col in home.select('.thumbnails .column'):
    cards = []
    for item in col.select('.thumbnail'):
        image = item.select_one('img')
        title = item.select_one('.title').get_text(strip=True)
        filename = Path(image['src']).name
        shutil.copy2(source / 'Yi-dong_files' / filename, assets / filename)
        slug = {'Sequence House': 'sequence-house', 'Day-care': 'day-care'}.get(title)
        picture = f'<img src="/assets/design/{filename}" alt="{html.escape(title)}" loading="lazy" decoding="async">'
        cards.append((slug, title, picture))
    columns.append(cards)

for lang in ['en', 'zh', 'ja', 'de']:
    path = root / lang / 'index.html'
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    main = soup.main
    main.clear()
    main['class'] = 'design-index'
    main['id'] = 'main-content'
    grid = soup.new_tag('section', attrs={'class': 'design-columns', 'aria-label': 'Design projects'})
    for cards in columns:
        col = soup.new_tag('div', attrs={'class': 'design-column'})
        for slug, title, picture in cards:
            tag = f'<a href="/{lang}/projects/{slug}.html">' if slug else '<div class="project-preview">'
            end = '</a>' if slug else '</div>'
            card = f'<article class="design-project">{tag}{picture}<h2>{html.escape(title)}</h2>{end}</article>'
            col.append(BeautifulSoup(card, 'html.parser'))
        grid.append(col)
    main.append(grid)
    for icon in soup.select('link[rel="icon"]'):
        icon['href'] = '/assets/logo.png'
    soup.select_one('.nav-inline a')['aria-current'] = 'page'
    path.write_text(str(soup), encoding='utf-8')

for slug, filename in [('sequence-house', 'Sequence House - Yi-dong'), ('day-care', 'Day-care - Yi-dong')]:
    original = BeautifulSoup((source / f'{filename}.html').read_text(encoding='utf-8'), 'html.parser')
    # Content DOM preserves prose, captions, image sequence and original column proportions.
    content = original.select_one('.content_container .page_content')
    for image in content.select('img'):
        name = Path(image['src']).name
        shutil.copy2(source / f'{filename}_files' / name, assets / name)
        scale = image.get('data-scale')
        width = image.get('width')
        height = image.get('height')
        image.attrs = {'src': f'/assets/design/{name}', 'alt': f'{slug.replace("-", " ")} — {Path(name).stem}', 'loading': 'lazy', 'decoding': 'async'}
        if width and height:
            image['width'], image['height'] = width, height
        if scale:
            image['style'] = f'width:{scale}%;'
    for lang in ['en', 'zh', 'ja', 'de']:
        path = root / lang / 'projects' / f'{slug}.html'
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        gallery = soup.select_one('.gallery')
        # Original English is the explicit fallback until editorial translations exist.
        intro = soup.select_one('.project-intro')
        if intro:
            intro.decompose()
        if gallery is None:
            gallery = soup.select_one('.cargo-project')
        main = soup.new_tag('main', attrs={'class': f'cargo-project {slug}', 'id': 'main-content', 'lang': 'en'})
        main.append(BeautifulSoup(str(content), 'html.parser'))
        gallery.replace_with(main)
        soup.select_one('.nav-inline a')['aria-current'] = 'page'
        path.write_text(str(soup), encoding='utf-8')
print('Restored four Design indexes and two project sources; media stored locally.')
