"""Build the short Information biography from verified CV facts."""
from pathlib import Path
from bs4 import BeautifulSoup

root = Path(__file__).resolve().parent
copy = {
    'en': [
        'Design & documentation · Melbourne',
        'Andrew Yang is a Melbourne-based architectural designer working across residential architecture, exhibitions and cultural projects. His experience spans concept design, town planning, construction documentation and consultant coordination.',
        'He holds a Master of Architecture from the University of Michigan and a Bachelor of Science in Architecture from the University of Minnesota. His practice draws on experience in Australia, the United States, China and Japan, alongside architectural studies in Copenhagen.',
        'His work brings design intent together with the detail and coordination needed to realise a project. Alongside architecture, he works in event and portrait photography.',
    ],
    'zh': [
        '建筑设计与技术文档 · 墨尔本',
        'Andrew Yang 是常驻墨尔本的建筑设计师，实践涵盖住宅建筑、展览及文化项目，工作经验包括概念设计、规划报批、施工图编制与专业顾问协调。',
        '他拥有密歇根大学建筑学硕士及明尼苏达大学建筑学理学学士学位，曾在澳大利亚、美国、中国和日本参与建筑实践，并在哥本哈根学习建筑与城市设计。',
        '他的工作注重将设计意图与项目落地所需的细节和协调相结合。建筑之外，他也从事活动与人像摄影。',
    ],
    'ja': [
        '建築デザイン・設計図書 · メルボルン',
        'Andrew Yang はメルボルンを拠点に、住宅建築、展示空間、文化施設に携わる建築デザイナーです。コンセプトデザインから都市計画申請、実施設計図書の作成、各分野の専門家との調整まで経験を重ねてきました。',
        'ミシガン大学で建築学修士号、ミネソタ大学で建築学の理学士号を取得。オーストラリア、アメリカ、中国、日本での実務に加え、コペンハーゲンで建築と都市デザインを学びました。',
        '設計の意図を大切にしながら、実現に必要な細部と調整に取り組んでいます。建築と並行して、イベントやポートレートの撮影も行っています。',
    ],
    'de': [
        'Entwurf & Ausführungsplanung · Melbourne',
        'Andrew Yang arbeitet als Architectural Designer in Melbourne. Seine Erfahrung umfasst Wohnarchitektur, Ausstellungen und Kulturprojekte – vom Konzeptentwurf über die Planung für Genehmigungsverfahren bis zur Ausführungsplanung und Fachplanerkoordination.',
        'Er hat einen Master of Architecture der University of Michigan und einen Bachelor of Science in Architecture der University of Minnesota. Seine Arbeit ist geprägt von Praxiserfahrungen in Australien, den USA, China und Japan sowie einem Studienaufenthalt für Architektur und Städtebau in Kopenhagen.',
        'Er verbindet die gestalterische Idee mit den Details und der Abstimmung, die für ihre Umsetzung erforderlich sind. Neben der Architektur ist er in der Event- und Porträtfotografie tätig.',
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
    title.string = 'Andrew Yang'
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
    soup.title.string = 'Andrew Yang — Information — Yi-dong'
    meta = soup.new_tag('meta', attrs={'name': 'description', 'content': paragraphs[0]})
    previous = soup.select_one('meta[name="description"]')
    if previous:
        previous.decompose()
    soup.head.append(meta)
    path.write_text(str(soup), encoding='utf-8')
print('Updated all four Information pages.')
