"""Build the short Information biography from verified CV facts."""
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parent
copy = {
    'en': [
        'Design & documentation · Melbourne',
        'Andrew is a Melbourne-based architectural designer focused on residential additions and renovations. He takes projects from early ideas through planning approvals and construction documentation, working through site levels, planning constraints and the details that connect design with construction.',
        'He previously led exhibition design and tender documentation for the Australian Opal Centre, whose building was designed by Glenn Murcutt and Wendy Lewin. He also contributed to interpretation and wayfinding master planning for the Twelve Apostles Visitor Centre.',
        'He holds a Master of Architecture from the University of Michigan. Alongside architecture, his photography explores people and places.',
    ],
    'zh': [
        '住宅设计 · 墨尔本',
        '我在墨尔本从事住宅设计，参与从最初的构想到规划报批与施工图的各个阶段。工作多围绕住宅改造与扩建展开，也常常需要梳理场地高差、规划限制，以及与顾问和施工方之间的细节。对我来说，好的设计既关乎空间，也藏在这些具体的推敲里。',
        '此前，我负责过 Australian Opal Centre 的展览设计与招标文件，项目所在建筑由 Glenn Murcutt 与 Wendy Lewin 设计；也参与过 Twelve Apostles Visitor Centre 的解说与导视总体规划。',
        '我毕业于密歇根大学建筑学硕士项目。建筑之外，也用摄影记录人和地方。',
    ],
    'ja': [
        '住宅デザイン · メルボルン',
        'メルボルンで住宅の設計に携わっています。改修や増築を中心に、最初のアイデアから都市計画申請、実施設計図書の作成まで。敷地の高低差や計画上の制約を読み解き、各分野の専門家や施工者と調整しながら、暮らしの場を少しずつ具体的にしていく仕事です。',
        'これまでに、Glenn Murcutt と Wendy Lewin が建築を手がけた Australian Opal Centre の展示デザインと入札図書の作成を担当しました。また、Twelve Apostles Visitor Centre では、展示解説とサイン計画のマスタープランに携わりました。',
        'ミシガン大学で建築学修士号を取得しました。建築の傍ら、写真を通して人や場所にも目を向けています。',
    ],
    'de': [
        'Entwurf & Ausführungsplanung · Melbourne',
        'Andrew ist Architectural Designer in Melbourne und beschäftigt sich vor allem mit dem Umbau und der Erweiterung von Wohnhäusern. Er begleitet Projekte von der ersten Idee über die Planung für Genehmigungsverfahren bis zur Ausführungsplanung. Dabei verbindet er räumliche Fragen mit Geländehöhen, Planungsvorgaben und der Abstimmung mit Fachplanern und Baufirmen.',
        'Zuvor leitete er den Ausstellungsentwurf und die Erstellung der Ausschreibungsunterlagen für das Australian Opal Centre, dessen Gebäude von Glenn Murcutt und Wendy Lewin entworfen wurde. Zudem wirkte er an der übergeordneten Planung der Besucherinformation und des Leitsystems für das Twelve Apostles Visitor Centre mit.',
        'Er hat einen Master of Architecture der University of Michigan. Neben der Architektur widmet er sich der Fotografie von Menschen und Orten.',
    ],
}
for lang, (subtitle, *paragraphs) in copy.items():
    path = root / lang / 'information.html'
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    wrapper = soup.select_one('.wrap')
    header = wrapper.select_one('.site-header').extract()
    wrapper.clear()
    wrapper.append(header)
    main = soup.new_tag('main', attrs={'class': 'information-page', 'id': 'main-content'})
    title = soup.new_tag('h1')
    title.string = {'zh': '关于我', 'ja': '私について'}.get(lang, 'Andrew Yang')
    main.append(title)
    label = soup.new_tag('p', attrs={'class': 'information-role'})
    label.string = subtitle
    main.append(label)
    for paragraph in paragraphs:
        p = soup.new_tag('p')
        p.string = paragraph
        main.append(p)
    wrapper.append(main)
    header.select_one('.right h2 a')['aria-current'] = 'page'
    soup.title.string = f'{title.string} — Yi-dong'
    meta = soup.new_tag('meta', attrs={'name': 'description', 'content': paragraphs[0]})
    previous = soup.select_one('meta[name="description"]')
    if previous:
        previous.decompose()
    soup.head.append(meta)
    path.write_text(str(soup), encoding='utf-8')
print('Updated all four Information pages.')
