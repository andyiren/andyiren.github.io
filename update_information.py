"""Build the short Information biography from verified CV facts."""
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parent
copy = {
    'en': [
        'Design & documentation · Melbourne',
        'I work in residential design in Melbourne, taking projects from early ideas through planning approvals and construction documentation. My experience centres on additions, renovations and the practical details of building: site levels, planning constraints and coordination with consultants and builders.',
        'Previously, at Arterial Design, I led exhibition design and tender documentation for the Australian Opal Centre, housed in a building designed by Glenn Murcutt and Wendy Lewin.',
        'I hold a Master of Architecture from the University of Michigan. Beyond architecture, photography offers another way of looking at people and places.',
    ],
    'zh': [
        '住宅设计 · 墨尔本',
        '我在墨尔本从事住宅设计，参与从最初的构想到规划报批与施工图的各个阶段。工作多围绕住宅改造与扩建展开，也常常需要梳理场地高差、规划限制，以及与顾问和施工方之间的细节。对我来说，好的设计既关乎空间，也藏在这些具体的推敲里。',
        '此前在 Arterial Design，我负责过 Australian Opal Centre 的展览设计与招标文件。项目所在建筑由 Glenn Murcutt 与 Wendy Lewin 设计。',
        '我毕业于密歇根大学建筑学硕士项目。建筑之外，也用摄影记录人和地方。',
    ],
    'ja': [
        '住宅デザイン · メルボルン',
        'メルボルンで住宅の設計に携わっています。改修や増築を中心に、最初のアイデアから都市計画申請、実施設計図書の作成まで。敷地の高低差や計画上の制約を読み解き、各分野の専門家や施工者と調整しながら、暮らしの場を少しずつ具体的にしていく仕事です。',
        '以前は Arterial Design で、Australian Opal Centre の展示デザインと入札図書の作成を担当しました。建築は Glenn Murcutt と Wendy Lewin によるものです。',
        'ミシガン大学で建築学修士号を取得しました。建築の傍ら、写真を通して人や場所にも目を向けています。',
    ],
    'de': [
        'Entwurf & Ausführungsplanung · Melbourne',
        'Ich arbeite in Melbourne im Wohnungsbau, vor allem an Umbauten und Erweiterungen. Ich begleite Projekte von der ersten Idee über die Planung für Genehmigungsverfahren bis zur Ausführungsplanung. Dabei geht es ebenso um Räume wie um Geländehöhen, Planungsvorgaben und die Abstimmung mit Fachplanern und Baufirmen.',
        'Zuvor leitete ich bei Arterial Design den Ausstellungsentwurf und die Erstellung der Ausschreibungsunterlagen für das Australian Opal Centre. Das Gebäude wurde von Glenn Murcutt und Wendy Lewin entworfen.',
        'Meinen Master of Architecture habe ich an der University of Michigan abgeschlossen. Neben der Architektur ist die Fotografie für mich eine weitere Möglichkeit, Menschen und Orte zu betrachten.',
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
