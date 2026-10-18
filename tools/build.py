#!/usr/bin/env python3
"""全ページのHTMLを生成するスクリプト。

ヘッダー・フッター・文言を変更するときはこのファイルを編集し、
`python3 tools/build.py` を実行すると5ページすべてに反映されます。
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIL = "info@kukuna-lino.com"
ADDR_HTML = "〒150-0043<br>東京都渋谷区道玄坂1丁目10番8号<br>渋谷道玄坂東急ビル2F−C"
ADDR_LINE = "〒150-0043 東京都渋谷区道玄坂1丁目10番8号 渋谷道玄坂東急ビル2F−C"
MAIL_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h12M9 3l5 5-5 5"/></svg>'
EXT = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3h8v8M13 3L3 13"/></svg>'

PAGES = [
    ("philosophy.html", "企業理念", "Philosophy"),
    ("business.html", "事業内容", "Business"),
    ("company.html", "会社概要", "Company"),
    ("contact.html", "お問い合わせ", "Contact"),
]

BIZ = [
    dict(id="ec", img="biz-ec", num="01", title="EC販売支援事業", en="E-commerce Support",
         alt="EC販売支援事業のイメージ：ノートパソコンでECサイトを運営する様子",
         short="商品の選定からECサイトでの販売、運用・改善までをサポートします。",
         text="商品の選定からECサイトでの販売、運用・改善までをサポート。オンラインでの販路づくりを通じて、商品とお客様との新しい出会いを生み出します。",
         case=True),
    dict(id="sales", img="biz-sales", num="02", title="営業支援事業", en="Sales Support",
         alt="営業支援事業のイメージ：商談成立の握手",
         short="新規顧客の開拓や商談の機会づくりなど、営業活動をサポートします。",
         text="新規顧客の開拓や商談の機会づくりなど、企業の営業活動をサポート。取引先の商品・サービスの魅力を、必要とするお客様へ的確に届けます。"),
    dict(id="bpo", img="biz-bpo", num="03", title="業務支援・受託事業", en="Business Process Outsourcing",
         alt="業務支援・受託事業のイメージ：パソコンで事務作業・データ管理を行う様子",
         short="事務作業や受発注管理など、バックオフィス業務を受託します。",
         text="事務作業や受発注管理、データ入力などのバックオフィス業務を受託。煩雑な業務を私たちが担うことで、お客様がコア業務に集中できる環境をつくります。"),
]


def head(title, desc, path):
    full = "株式会社ククナリノ | KUKUNALINO Inc." if not title else f"{title} | 株式会社ククナリノ"
    url = "https://kukuna-lino.com/" + ("" if path == "index.html" else path)
    return f'''<!DOCTYPE html>
<html lang="ja" class="no-js">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full}</title>
  <meta name="description" content="{desc}">
  <meta property="og:title" content="{full}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="https://kukuna-lino.com/assets/images/ogp.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="assets/images/favicon.png">
  <link rel="apple-touch-icon" href="assets/images/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Noto+Sans+JP:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
'''


def header(current):
    items = []
    for href, ja, _ in PAGES:
        cls = "nav__link nav__link--btn" if href == "contact.html" else "nav__link"
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'          <li><a href="{href}" class="{cls}"{cur}>{ja}</a></li>')
    items = "\n".join(items)
    return f'''
  <!-- ===== Header ===== -->
  <header class="header" id="header">
    <div class="header__inner">
      <a href="index.html" class="header__logo" aria-label="株式会社ククナリノ トップへ">
        <img src="assets/images/logo.png" alt="株式会社ククナリノ" class="header__logo-img" width="800" height="280">
      </a>
      <nav class="nav" id="nav" aria-label="メインメニュー">
        <ul class="nav__list">
{items}
        </ul>
      </nav>
      <button class="menu-btn" id="menuBtn" aria-label="メニューを開く" aria-expanded="false" aria-controls="nav">
        <span></span><span></span>
      </button>
    </div>
  </header>
'''


def footer():
    links = "\n".join(f'        <li><a href="{h}">{ja}</a></li>' for h, ja, _ in PAGES)
    return f'''
  <!-- ===== Footer ===== -->
  <footer class="footer">
    <div class="footer__inner">
      <div class="footer__brand">
        <p class="footer__logo"><img src="assets/images/logo-mark.png" alt="" width="83" height="32">KUKUNALINO</p>
        <p class="footer__name">株式会社ククナリノ</p>
        <p class="footer__addr">{ADDR_LINE}</p>
      </div>
      <ul class="footer__nav">
        <li><a href="index.html">トップ</a></li>
{links}
      </ul>
    </div>
    <p class="footer__copy"><small>&copy; <span id="year">2026</span> KUKUNALINO Inc.</small></p>
  </footer>

  <script src="assets/js/main.js"></script>
</body>
</html>
'''


def contact_band():
    return f'''
    <!-- ===== Contact ===== -->
    <section class="contact">
      <div class="container">
        <div class="contact__inner fade">
          <p class="section__en section__en--light">Contact</p>
          <h2 class="contact__title">お問い合わせ</h2>
          <p class="contact__text">
            ご相談・ご質問は、下記ボタンからメールにてお気軽にご連絡ください。
          </p>
          <a href="mailto:{MAIL}" class="contact__btn">
            {MAIL_ICON}
            <span>メールでお問い合わせ</span>
          </a>
        </div>
      </div>
    </section>
'''


def page_hero(ja, en):
    return f'''
    <!-- ===== Page header ===== -->
    <section class="page-hero">
      <div class="page-hero__bg" aria-hidden="true"></div>
      <div class="page-hero__inner">
        <p class="page-hero__en fade">{en}</p>
        <h1 class="page-hero__title fade">{ja}</h1>
        <ol class="breadcrumb fade" aria-label="パンくずリスト">
          <li><a href="index.html">トップ</a></li>
          <li aria-current="page">{ja}</li>
        </ol>
      </div>
    </section>
'''


def next_link(current):
    order = [p[0] for p in PAGES]
    i = order.index(current)
    href, ja, en = PAGES[(i + 1) % len(PAGES)]
    return f'''
    <!-- ===== Next ===== -->
    <nav class="next-page" aria-label="次のページ">
      <a href="{href}" class="next-page__link">
        <span class="next-page__label">Next</span>
        <span class="next-page__title">{ja}<span class="next-page__en">{en}</span></span>
        <span class="next-page__arrow">{ARROW}</span>
      </a>
    </nav>
'''


def more_btn(href, label):
    return f'<a href="{href}" class="btn-more">{label}<span class="btn-more__icon">{ARROW}</span></a>'


def section_head(num, en, ja, tag="h2"):
    return f'''        <div class="section__head fade">
          <p class="section__en"><span class="section__num">{num}</span>{en}</p>
          <{tag} class="section__ja">{ja}</{tag}>
        </div>'''


PHILOSOPHY_TEXT = '''良い商品やサービスが、必要としている人にきちんと届くこと。<br>
            そして、そのために働く人が本来の仕事に集中できること。<br>
            株式会社ククナリノは、販売・営業・業務の各領域で企業の活動を支え、<br class="sp-none">
            信頼できる「つなぎ手」として、社会にやさしい流れを生み出していきます。'''

VALUES = [
    ("Mission", "使命", "価値ある商品・サービスと、それを求める人とを確かにつなぎ、取引先の成長に貢献する。"),
    ("Vision", "目指す姿", "「ククナリノに任せれば安心」と言われる、信頼のビジネスパートナーであり続ける。"),
    ("Value", "大切にすること", "誠実さ・スピード・継続性。一つひとつの約束を守り、長く続く関係を築く。"),
]

PROFILE = [
    ("会社名", "株式会社ククナリノ"),
    ("代表者", "代表取締役　曲 智徳"),
    ("設立", "2021年9月16日"),
    ("所在地", ADDR_HTML),
    ("事業内容", '''
              <ul class="profile__list">
                <li>EC販売支援事業</li>
                <li>営業支援事業</li>
                <li>業務支援・受託事業</li>
              </ul>
            '''),
    ("お問い合わせ", f'''
              <a href="mailto:{MAIL}" class="mail-link">
                {MAIL_ICON}
                メールでお問い合わせ
              </a>
            '''),
]


def profile_dl(rows):
    out = ['        <dl class="profile fade">']
    for dt, dd in rows:
        out.append(f'''          <div class="profile__row">
            <dt>{dt}</dt>
            <dd>{dd}</dd>
          </div>''')
    out.append("        </dl>")
    return "\n".join(out)


# ---------------------------------------------------------------- index
def build_index():
    cards = []
    for b in BIZ:
        cards.append(f'''          <li class="biz-card fade">
            <a href="business.html#{b['id']}" class="biz-card__link">
              <div class="biz-card__figure">
                <img src="assets/images/{b['img']}.jpg" alt="{b['alt']}" width="1200" height="900" loading="lazy">
              </div>
              <div class="biz-card__body">
                <p class="biz-card__num">{b['num']}</p>
                <h3 class="biz-card__title">{b['title']}</h3>
                <p class="biz-card__en">{b['en']}</p>
                <p class="biz-card__text">{b['short']}</p>
                <span class="biz-card__more">詳しく見る{ARROW}</span>
              </div>
            </a>
          </li>''')
    cards = "\n".join(cards)
    short_profile = profile_dl([PROFILE[0], PROFILE[1], PROFILE[2], ("所在地", ADDR_HTML)])
    body = f'''
  <main id="top">

    <!-- ===== Hero ===== -->
    <section class="hero">
      <div class="hero__bg" aria-hidden="true"></div>
      <div class="hero__inner">
        <p class="hero__label fade">KUKUNALINO Inc.</p>
        <h1 class="hero__title fade">
          <span>つなぐ力で、</span><span>ビジネスに確かな流れを。</span>
        </h1>
        <p class="hero__lead fade">
          EC販売支援・営業支援・業務支援／受託。<br class="sp-none">
          私たちは、企業の「売る」「広げる」「支える」に寄り添うパートナーです。
        </p>
      </div>
      <a href="#philosophy" class="hero__scroll" aria-label="下へスクロール">
        <span>Scroll</span>
      </a>
    </section>

    <!-- ===== Philosophy ===== -->
    <section class="section philosophy" id="philosophy">
      <div class="container">
{section_head("01", "Philosophy", "企業理念")}
        <div class="philosophy__main philosophy__main--digest fade">
          <p class="philosophy__catch">人と企業を、<br>誠実につなぐ。</p>
          <div>
            <p class="philosophy__text">
            {PHILOSOPHY_TEXT}
            </p>
            <div class="more-wrap">{more_btn("philosophy.html", "企業理念を見る")}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== Business ===== -->
    <section class="section business" id="business">
      <div class="container">
{section_head("02", "Business", "事業内容")}
        <p class="business__intro fade">3つの事業を通じて、企業の「売る」「広げる」「支える」をトータルにサポートします。</p>
        <ul class="biz-cards">
{cards}
        </ul>
        <div class="more-wrap more-wrap--center fade">{more_btn("business.html", "事業内容を見る")}</div>
      </div>
    </section>

    <!-- ===== Company ===== -->
    <section class="section company" id="company">
      <div class="container">
        <div class="company-digest">
{section_head("03", "Company", "会社概要")}
{short_profile}
          <div class="company-digest__more more-wrap fade">{more_btn("company.html", "会社概要を見る")}</div>
        </div>
      </div>
    </section>
{contact_band()}
  </main>
'''
    return (head(None, "株式会社ククナリノは、EC販売支援事業・営業支援事業・業務支援・受託事業を通じて、企業の成長を支えるパートナーです。", "index.html")
            + header("index.html") + body + footer())


# ---------------------------------------------------------------- philosophy
def build_philosophy():
    vals = "\n".join(f'''          <li class="values__item fade">
            <p class="values__en">{en}</p>
            <h3 class="values__title">{ja}</h3>
            <p class="values__text">{t}</p>
          </li>''' for en, ja, t in VALUES)
    body = f'''
  <main>
{page_hero("企業理念", "Philosophy")}
    <section class="section philosophy">
      <div class="container">
        <div class="philosophy__main fade">
          <p class="philosophy__catch">人と企業を、<br>誠実につなぐ。</p>
          <p class="philosophy__text">
            {PHILOSOPHY_TEXT}
          </p>
        </div>

        <ul class="values">
{vals}
        </ul>
      </div>
    </section>
{next_link("philosophy.html")}{contact_band()}
  </main>
'''
    return (head("企業理念", "株式会社ククナリノの企業理念。人と企業を、誠実につなぐ。", "philosophy.html")
            + header("philosophy.html") + body + footer())


# ---------------------------------------------------------------- business
def build_business():
    arts = []
    for i, b in enumerate(BIZ):
        rev = " biz--reverse" if i % 2 else ""
        case = ""
        if b.get("case"):
            case = f'''
              <div class="biz__case">
                <p class="biz__case-label">取り扱い例</p>
                <p class="biz__case-text">ウォーターサーバーの販売（代理店）</p>
                <a href="https://mugensui.kukuna-lino.com/" class="biz__link" target="_blank" rel="noopener">
                  ECサイトを見る
                  {EXT}
                </a>
              </div>'''
        arts.append(f'''
          <article class="biz{rev} fade" id="{b['id']}">
            <div class="biz__figure">
              <img src="assets/images/{b['img']}.jpg" alt="{b['alt']}" width="1200" height="900" loading="lazy">
            </div>
            <div class="biz__body">
              <p class="biz__num">{b['num']}</p>
              <h2 class="biz__title">{b['title']}</h2>
              <p class="biz__en">{b['en']}</p>
              <p class="biz__text">
                {b['text']}
              </p>{case}
            </div>
          </article>''')
    arts = "\n".join(arts)
    body = f'''
  <main>
{page_hero("事業内容", "Business")}
    <section class="section business">
      <div class="container">
        <p class="business__lead fade">3つの事業を通じて、企業の「売る」「広げる」「支える」をトータルにサポートします。</p>
        <div class="business__list">
{arts}

        </div>
      </div>
    </section>
{next_link("business.html")}{contact_band()}
  </main>
'''
    return (head("事業内容", "株式会社ククナリノの事業内容。EC販売支援事業・営業支援事業・業務支援・受託事業。", "business.html")
            + header("business.html") + body + footer())


# ---------------------------------------------------------------- company
def build_company():
    body = f'''
  <main>
{page_hero("会社概要", "Company")}
    <section class="section company">
      <div class="container container--narrow">
{profile_dl(PROFILE)}

        <div class="map fade">
          <iframe
            src="https://www.google.com/maps?q=%E6%9D%B1%E4%BA%AC%E9%83%BD%E6%B8%8B%E8%B0%B7%E5%8C%BA%E9%81%93%E7%8E%84%E5%9D%821%E4%B8%81%E7%9B%AE10%E7%95%AA8%E5%8F%B7&output=embed"
            title="株式会社ククナリノ 所在地の地図"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"></iframe>
        </div>
      </div>
    </section>
{contact_band()}
  </main>
'''
    return (head("会社概要", "株式会社ククナリノの会社概要。所在地：東京都渋谷区道玄坂。", "company.html")
            + header("company.html") + body + footer())


# ---------------------------------------------------------------- contact
def build_contact():
    body = f'''
  <main>
{page_hero("お問い合わせ", "Contact")}
    <section class="section contact-page">
      <div class="container container--narrow">
        <p class="contact-page__lead fade">
          事業内容やお取引に関するご相談・ご質問は、<br class="sp-none">メールにてお気軽にお問い合わせください。<br>
          内容を確認のうえ、担当者よりご連絡いたします。
        </p>

        <div class="contact-card fade">
          <div class="contact-card__icon">{MAIL_ICON}</div>
          <h2 class="contact-card__title">メールでのお問い合わせ</h2>
          <p class="contact-card__text">下記ボタンをクリックすると、メールソフトが起動します。</p>
          <a href="mailto:{MAIL}" class="contact-card__btn">
            {MAIL_ICON}
            <span>メールでお問い合わせ</span>
          </a>
        </div>

        <ul class="contact-notes fade">
          <li>お問い合わせの際は、会社名・お名前・ご用件をご記入ください。</li>
          <li>内容によっては、ご返信までにお時間をいただく場合がございます。</li>
          <li>営業・勧誘を目的としたご連絡はご遠慮ください。</li>
        </ul>
      </div>
    </section>
{next_link("contact.html")}
  </main>
'''
    return (head("お問い合わせ", "株式会社ククナリノへのお問い合わせはメールにて承ります。", "contact.html")
            + header("contact.html") + body + footer())


for name, fn in [("index.html", build_index), ("philosophy.html", build_philosophy),
                 ("business.html", build_business), ("company.html", build_company),
                 ("contact.html", build_contact)]:
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(fn())
    print("wrote", name)
