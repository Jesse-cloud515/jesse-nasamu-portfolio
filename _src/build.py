"""
Static site generator for jesse-nasamu portfolio. No dependencies beyond Python 3.8+.
Usage (from the project root):  python3 _src/build.py
Writes index.html, work/<slug>/index.html, 404.html, sitemap.xml and robots.txt.
"""
import os, re, json, html, datetime, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content import SITE, HERO, ABOUT, SKILLS, EXPERIENCE, EDUCATION, SERVICES, TESTIMONIALS, PROJECTS, GALLERY, CASE  # noqa

e = html.escape
VERSION = datetime.date.today().strftime("%Y%m%d")


def img_exists(stem, folder="work"):
    return os.path.exists(os.path.join(ROOT, "assets/img", folder, f"{stem}-800.webp"))


def picture(rel, stem, alt, folder="work", sizes="(min-width: 900px) 60vw, 100vw", eager=False, cls=""):
    src = f"{rel}assets/img/{folder}/{stem}"
    w, h = SIZES.get(f"{folder}/{stem}", (1600, 1000))
    ratio_h = round(1600 * h / w) if w > 1600 else h
    ww = min(w, 1600)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{src}-1600.webp" srcset="{src}-800.webp 800w, {src}-1600.webp 1600w" sizes="{sizes}" '
            f'width="{ww}" height="{ratio_h}" alt="{e(alt)}" {load}>')


SIZES = {}
try:
    SIZES = json.load(open(os.path.join(HERE, "image-sizes.json")))
except FileNotFoundError:
    pass


def icon(name):
    paths = {
        "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "out": '<path d="M7 17 17 7M8 7h9v9"/>',
        "down": '<path d="M12 5v14M6 13l6 6 6-6"/>',
        "close": '<path d="M6 6l12 12M18 6 6 18"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    }
    return f'<svg class="i" width="18" height="18" aria-hidden="true"><use href="#i-{name}"/></svg>'


# All icons are drawn once here, then reused with <use href="#i-name">.
ICON_PATHS = {
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "out": '<path d="M7 17 17 7M8 7h9v9"/>',
    "down": '<path d="M12 5v14M6 13l6 6 6-6"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
}
SPRITE = ('<svg class="sprite" aria-hidden="true">'
          + "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICON_PATHS.items())
          + '</svg>')


def head(rel, title, desc, path, og_type="website", extra=""):
    url = SITE["base_url"] + path
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0e1b22">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE['base_url']}assets/img/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@JesseNasamu">
<link rel="icon" type="image/png" sizes="32x32" href="{rel}assets/img/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{rel}assets/img/favicon-16x16.png">
<link rel="apple-touch-icon" href="{rel}assets/img/apple-touch-icon.png">
<link rel="preload" href="{rel}assets/fonts/schibsted-grotesk-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{rel}assets/fonts/schibsted-grotesk-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{rel}assets/css/style.css?v={VERSION}">
{extra}
</head>
"""


def header(rel, home=False):
    h = "" if home else f"{rel}index.html"
    links = [("Work", "#work"), ("About", "#about"), ("Experience", "#experience"), ("Services", "#services"), ("Contact", "#contact")]
    items = "".join(f'<li><a href="{h}{a}">{t}</a></li>' for t, a in links)
    return SPRITE + f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header" data-header>
  <div class="wrap header-in">
    <a class="mark" href="{rel}index.html" aria-label="Jesse Nasamu, home"><span class="mark-nj" aria-hidden="true">NJ</span><span class="mark-name">Jesse Nasamu</span></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav" data-menu>{icon('menu')}<span class="sr">Menu</span></button>
    <nav id="nav" class="nav" aria-label="Main">
      <ul>{items}</ul>
      <a class="btn btn-small" href="{rel}{SITE['cv']}" download>Download CV</a>
    </nav>
  </div>
</header>
"""


def footer(rel):
    profiles = "".join(f'<li><a href="{u}" rel="me noopener" target="_blank">{n}</a></li>' for n, u in SITE["profiles"])
    year = datetime.date.today().year
    return f"""<footer class="site-footer">
  <div class="wrap footer-in">
    <p>&copy; {year} {e(SITE['full_name'])}. {e(SITE['location'])}.</p>
    <ul class="inline-links">{profiles}<li><a href="mailto:{SITE['email']}">Email</a></li></ul>
  </div>
</footer>
<script src="{rel}assets/js/main.js?v={VERSION}" defer></script>
</body>
</html>
"""


def pipeline_svg(compact=False):
    steps = [("Security events", "Raw network records"), ("Power Query", "Clean and transform"),
             ("Data model", "Structured for analysis"), ("DAX measures", "KPIs for attacks, severity, anomalies, response"),
             ("Reports", "Interactive visuals and filters"), ("Insight", "Monitoring and risk assessment")]
    items = "".join(
        f'<li><span class="pipe-n">{i + 1}</span><strong>{e(a)}</strong><span>{e(b)}</span></li>' for i, (a, b) in enumerate(steps))
    return f'<ol class="pipeline{" pipeline-compact" if compact else ""}" aria-label="How the dashboard was built, in six stages">{items}</ol>'


# ----------------------------------------------------------------------------------- HOME
def home():
    rel = ""
    parts = [head(rel, "Jesse Nasamu | UI/UX Designer, Data Analyst and Cybersecurity Analyst", SITE["description"], "",
                  extra=person_jsonld())]
    parts.append('<body class="home">' + header(rel, home=True))
    profiles = "".join(f'<li><a href="{u}" rel="me noopener" target="_blank">{n}</a></li>' for n, u in SITE["profiles"])
    parts.append(f"""<main id="main">
<section class="hero" aria-labelledby="hero-title">
  <div class="wrap hero-grid">
    <div class="hero-text">
      <h1 id="hero-title" class="hero-name"><span>Jesse</span> <span>Nasamu</span></h1>
      <p class="hero-statement">{e(HERO['statement'])}</p>
      <p class="hero-sub">{e(HERO['sub'])}</p>
      <div class="actions">
        <a class="btn" href="#work">See selected work</a>
        <a class="btn btn-ghost" href="{SITE['cv']}" download>Download CV {icon('down')}</a>
      </div>
      <ul class="inline-links hero-links" aria-label="Profiles">{profiles}</ul>
    </div>
  </div>
  <div class="wrap disciplines" aria-label="Disciplines">
    <span>UI/UX design</span><span>Graphic design</span><span>Data analysis</span><span>Cybersecurity</span><span>Web development</span>
  </div>
</section>
""")
    # ---------- Work
    case = CASE
    rows = []
    for p in PROJECTS:
        if p.get('listed') is False:
            continue
        thumb = p["images"][0][0] if p["images"] else ""
        t = picture(rel, thumb, "", sizes="120px", cls="row-thumb") if thumb else '<span class="row-thumb row-thumb-empty" aria-hidden="true"></span>'
        data_img = f' data-preview="assets/img/work/{thumb}-800.webp"' if thumb else ""
        tags = []
        d = p['discipline'].lower()
        if "ui/ux" in d or "web" in d: tags.append("design")
        if "data" in d: tags.append("data")
        if "cyber" in d: tags.append("security")
        if "graphic" in d: tags.append("graphic")
        rows.append(f"""<li data-tags="{' '.join(tags)}">
<a class="work-row" href="work/{p['slug']}/index.html"{data_img}>
{t}
<span class="row-title">{e(p['title'])}</span>
<span class="row-disc">{e(p['discipline'])}</span>
<span class="row-year">{e(p['year'])}</span>
{icon('arrow')}
</a>
</li>""")
    gallery = "".join(
        f'<li><button class="g-item" type="button" data-lightbox="assets/img/gallery/{s}-1600.webp" data-caption="{e(cap)}" data-link="{e(link)}">\n'
        f'{picture(rel, s, alt, folder="gallery", sizes="(min-width: 900px) 25vw, 70vw")}\n<span>{e(cap)}</span>\n</button></li>'
        for s, alt, cap, link in GALLERY)
    parts.append(f"""
<section id="work" class="section work" aria-labelledby="work-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="work-title">Selected work</h2>
      <p>Design, data and security projects, each with the problem, the process and what came out of it.</p>
    </div>
    <article class="featured">
      <div class="featured-text">
        <p class="kicker">Latest case study, {case['dates']}</p>
        <h3><a href="work/{case['slug']}/index.html">{e(case['title'])}</a></h3>
        <p class="featured-headline">{e(case['headline'])}</p>
        <p>{e(case['summary'])}</p>
        <ul class="tags">{''.join(f'<li>{e(t)}</li>' for t in case['tools'][:4])}</ul>
        <a class="btn" href="work/{case['slug']}/index.html">Read the case study</a>
      </div>
      <a class="featured-visual" href="work/{case['slug']}/index.html" tabindex="-1" aria-hidden="true">
        <span class="window">
          <span class="window-bar"><i></i><i></i><i></i></span>
          {picture(rel, case['screenshots'][0][0], case['screenshots'][0][1], sizes="(min-width: 900px) 55vw, 100vw")}
        </span>
      </a>
    </article>
    <div class="filters" role="group" aria-label="Filter projects" data-filters hidden>
      <button type="button" aria-pressed="true" data-filter="all">All</button>
      <button type="button" aria-pressed="false" data-filter="design">UI/UX and web</button>
      <button type="button" aria-pressed="false" data-filter="data">Data analysis</button>
      <button type="button" aria-pressed="false" data-filter="security">Cybersecurity</button>
    </div>
    <ul class="work-list" data-worklist>{''.join(rows)}</ul>
    <div class="gallery-head">
      <h3>Graphic design</h3>
      <p>Logos, posters and print pieces. Select an image to see it larger.</p>
    </div>
    <ul class="gallery">{gallery}</ul>
  </div>
  <img class="cursor-preview" alt="" aria-hidden="true" data-cursor-preview>
</section>
""")
    # ---------- About + skills
    qs = "".join(f"<li><strong>{e(q)}</strong><span>{e(a)}</span></li>" for q, a in ABOUT["questions"])
    paras = "".join(f"<p>{e(p)}</p>" for p in ABOUT["paragraphs"])
    aff = "".join(f"<li>{e(a)}</li>" for a in ABOUT["affiliations"])
    skills = "".join(
        f'<div class="skill-col"><h3>{e(cat)}</h3><ul>{"".join(f"<li>{e(s)}</li>" for s in items)}</ul></div>'
        for cat, items in SKILLS)
    parts.append(f"""
<section id="about" class="section about" aria-labelledby="about-title">
  <div class="wrap about-grid">
    <div class="about-side">
      <h2 id="about-title">About</h2>
      <picture class="about-photo"><source srcset="assets/img/jesse-nasamu.webp" type="image/webp"><img src="assets/img/jesse-nasamu.jpg" width="900" height="1125" alt="Jesse Nasamu standing against a warm wall" loading="lazy" decoding="async"></picture>
    </div>
    <div class="about-body">
      <p class="lead">{e(ABOUT['lead'])}</p>
      <ul class="questions">{qs}</ul>
      {paras}
      <h3 class="small-h">Memberships and credentials</h3>
      <ul class="plain cols">{aff}</ul>
      <p class="interests">Outside work: {e(", ".join(ABOUT["interests"]).lower().capitalize())}.</p>
    </div>
  </div>
  <div class="wrap skills" aria-labelledby="skills-title">
    <h2 id="skills-title" class="h-sub">Skills and tools</h2>
    <div class="skill-grid">{skills}</div>
  </div>
</section>
""")
    # ---------- Experience
    def tl(items, edu=False):
        out = []
        for it in items:
            pts = "" if edu else "<ul>" + "".join(f"<li>{e(x)}</li>" for x in it["points"]) + "</ul>"
            note = f"<p>{e(it['note'])}</p>" if edu else ""
            org = ", ".join(x for x in [it.get("org", ""), it.get("place", "")] if x)
            org_html = f'<p class="tl-org">{e(org)}</p>' if org else ""
            when = f'<p class="tl-when">{e(it["when"])}</p>' if it["when"] else ""
            out.append(f"""<li class="tl-item">{when}
<div><h4>{e(it['title'])}</h4>{org_html}{pts}{note}</div></li>""")
        return "".join(out)
    parts.append(f"""
<section id="experience" class="section experience" aria-labelledby="exp-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="exp-title">Experience and education</h2>
      <p><a class="text-link" href="{SITE['cv']}" download>Download the full CV (PDF)</a></p>
    </div>
    <div class="tl-grid">
      <div><h3 class="h-sub">Work</h3><ol class="timeline">{tl(EXPERIENCE)}</ol></div>
      <div><h3 class="h-sub">Education</h3><ol class="timeline">{tl(EDUCATION, edu=True)}</ol></div>
    </div>
  </div>
</section>
""")
    # ---------- Services
    sv = "".join(f"<li><h3>{e(t)}</h3><p>{e(d)}</p></li>" for t, d in SERVICES)
    parts.append(f"""
<section id="services" class="section services" aria-labelledby="svc-title">
  <div class="wrap">
    <div class="section-head">
      <h2 id="svc-title">Services</h2>
      <p>For startups, agencies and businesses that want design, data and security handled with the same care.</p>
    </div>
    <ul class="svc-list">{sv}</ul>
    <a class="btn" href="#contact">Start a project</a>
  </div>
</section>
""")
    # ---------- Testimonials
    tm = "".join(
        f'<li><figure><blockquote><p>{e(q)}</p></blockquote><figcaption><span class="initials" aria-hidden="true">'
        f'{"".join(w[0] for w in n.split()[:2])}</span><span><strong>{e(n)}</strong>{e(r)}</span></figcaption></figure></li>'
        for q, n, r in TESTIMONIALS)
    parts.append(f"""
<section id="testimonials" class="section quotes" aria-labelledby="q-title">
  <div class="wrap">
    <h2 id="q-title">What people say</h2>
    <ul class="quote-grid">{tm}</ul>
  </div>
</section>
""")
    # ---------- Contact
    parts.append(f"""
<section id="contact" class="section contact" aria-labelledby="contact-title">
  <div class="wrap contact-grid">
    <div class="contact-intro">
      <h2 id="contact-title">Have a role or a project in mind?</h2>
      <p>Tell me what you're working on and the best way to reach you.</p>
      <dl class="contact-list">
        <div><dt>Email</dt><dd><a href="mailto:{SITE['email']}">{SITE['email']}</a></dd></div>
        <div><dt>Phone</dt><dd><a href="tel:{SITE['phone_link']}">{SITE['phone_display']}</a></dd></div>
        <div><dt>Based in</dt><dd>{e(SITE['location'])}</dd></div>
        <div><dt>Elsewhere</dt><dd><ul class="inline-links">{profiles}</ul></dd></div>
      </dl>
    </div>
    <form class="contact-form" action="{SITE['form_endpoint']}" method="post" novalidate data-form>
      <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" type="text" autocomplete="name" required maxlength="120"></div>
      <div class="field"><label for="f-email">Email address</label><input id="f-email" name="email" type="email" autocomplete="email" required maxlength="200"></div>
      <fieldset class="field">
        <legend>What's it about?</legend>
        <div class="choice-row">
          <label><input type="radio" name="topic" value="Job opportunity" checked> Job opportunity</label>
          <label><input type="radio" name="topic" value="Freelance project"> Freelance project</label>
          <label><input type="radio" name="topic" value="Something else"> Something else</label>
        </div>
      </fieldset>
      <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" rows="6" required maxlength="5000"></textarea></div>
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn" type="submit" data-submit>Send message</button>
      <p class="form-status" role="status" aria-live="polite" data-status></p>
    </form>
  </div>
</section>
</main>
<div class="lightbox" hidden data-lb><button class="lb-close" type="button" aria-label="Close image">{icon('close')}</button><figure><img alt="" data-lb-img><figcaption><span data-lb-cap></span> <a data-lb-link hidden target="_blank" rel="noopener">Open in Figma</a></figcaption></figure></div>
""")
    parts.append(footer(rel))
    return "".join(parts)


def person_jsonld():
    data = {
        "@context": "https://schema.org", "@type": "Person", "name": SITE["full_name"], "alternateName": SITE["name"],
        "url": SITE["base_url"], "email": "mailto:" + SITE["email"], "image": SITE["base_url"] + "assets/img/jesse-nasamu.jpg",
        "jobTitle": "UI/UX Designer, Data Analyst and Cybersecurity Analyst",
        "address": {"@type": "PostalAddress", "addressLocality": "Abuja", "addressCountry": "NG"},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Bingham University"},
        "sameAs": [u for _, u in SITE["profiles"]],
    }
    return f'<script type="application/ld+json">{json.dumps(data)}</script>'


# ----------------------------------------------------------------------------------- PROJECT PAGE
def project_nav(rel, slug):
    order = [CASE["slug"]] + [p["slug"] for p in PROJECTS if p.get("listed") is not False]
    titles = {CASE["slug"]: CASE["title"], **{p["slug"]: p["title"] for p in PROJECTS}}
    i = order.index(slug) if slug in order else 0
    nxt = order[(i + 1) % len(order)]
    return f"""<nav class="next-project wrap" aria-label="Next project">
  <a href="{rel}index.html#work" class="text-link">All work</a>
  <a href="{rel}work/{nxt}/index.html" class="next-link"><span>Next project</span><strong>{e(titles[nxt])}</strong>{icon('arrow')}</a>
</nav>"""


def project_page(p):
    rel = "../../"
    path = f"work/{p['slug']}/"
    parts = [head(rel, f"{p['title']} | Jesse Nasamu", p["summary"], path, og_type="article")]
    parts.append('<body class="project">' + header(rel))
    meta = [("Discipline", p["discipline"])]
    if p.get("role"): meta.append(("My role", p["role"]))
    if p["dates"]: meta.append(("When", p["dates"]))
    if p["tools"]: meta.append(("Tools", ", ".join(p["tools"])))
    meta_html = "".join(f"<div><dt>{a}</dt><dd>{e(b)}</dd></div>" for a, b in meta)
    links = "".join(
        f'<a class="btn" href="{u}" target="_blank" rel="noopener">{e(t)} {icon("out")}</a>' if u.startswith("http")
        else f'<a class="btn btn-ghost" href="{rel}{u}" download>{e(t)} {icon("down")}</a>' for t, u in p["links"])
    lead_img = picture(rel, p["images"][0][0], p["images"][0][1], sizes="(min-width: 1200px) 1200px, 100vw", eager=True) if p["images"] else ""
    story = []
    labels = [("challenge", "The challenge"), ("approach", "My approach"), ("process", "Process"),
              ("solution", "The solution"), ("findings", "What I found"), ("recommendations", "Recommendations"),
              ("note", "About the data"), ("results", "Results and lessons")]
    for k, label in labels:
        v = p.get(k)
        if not v: continue
        if isinstance(v, list):
            cls = "findings-list" if k == "findings" else "steps"
            tag = "ul" if k in ("findings", "recommendations") else "ol"
            body = f"<{tag} class='{cls}'>" + "".join(f"<li>{e(x)}</li>" for x in v) + f"</{tag}>"
        else:
            body = f"<p>{e(v)}</p>"
        story.append(f'<section class="story-block"><h2>{label}</h2><div>{body}</div></section>')
    rest = "".join(
        f'<figure class="shot">{picture(rel, s, a, sizes="(min-width: 1200px) 1200px, 100vw")}</figure>'
        for s, a in p["images"][1:])
    parts.append(f"""<main id="main">
<article>
  <header class="p-head wrap">
    <a class="text-link back" href="{rel}index.html#work">All work</a>
    <h1>{e(p['title'])}</h1>
    <p class="p-summary">{e(p['summary'])}</p>
    <dl class="p-meta">{meta_html}</dl>
    <div class="actions">{links}</div>
  </header>
  {f'<figure class="p-lead wrap">{lead_img}</figure>' if lead_img else ''}
  <div class="wrap story">{''.join(story)}</div>
  {f'<div class="wrap shots">{rest}</div>' if rest else ''}
</article>
{project_nav(rel, p['slug'])}
</main>
""")
    parts.append(footer(rel))
    return "".join(parts)


# ----------------------------------------------------------------------------------- CASE STUDY
def case_page():
    c = CASE
    rel = "../../"
    path = f"work/{c['slug']}/"
    parts = [head(rel, f"{c['title']} | Case study by Jesse Nasamu", c["summary"], path, og_type="article")]
    parts.append('<body class="project case">' + header(rel))
    toc = [("overview", "Overview"), ("questions", "Questions"), ("data", "Dataset"), ("process", "Process"),
           ("dashboard", "Dashboard"), ("finding", "Key finding"), ("findings", "All findings"),
           ("recommendations", "Recommendations"), ("lessons", "Lessons"), ("limits", "Limitations")]
    toc_html = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in toc)
    links = "".join(
        f'<a class="btn btn-ghost" href="{u}" target="_blank" rel="noopener">{e(t)} {icon("out")}</a>' if u.startswith("http")
        else f'<a class="btn" href="{rel}{u}" download>{e(t)} {icon("down")}</a>' for t, u in c["links"])
    qs = "".join(f"<li>{e(q)}</li>" for q in c["questions"])
    ds = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in c["dataset"])
    proc = "".join(f"<li><h3>{e(a)}</h3><p>{e(b)}</p></li>" for a, b in c["process"])
    pages = "".join(f"<li><strong>{e(a)}</strong><span>{e(b)}</span></li>" for a, b in c["pages"])
    rows = []
    for sev, n, b, l, ig in c["response"]:
        rows.append(f"""<div class="rb-row" role="row">
  <span class="rb-label" role="rowheader">{sev}</span>
  <span class="rb-bar" role="cell" aria-label="Blocked {b}%, logged {l}%, ignored {ig}%">
    <span class="rb-seg rb-b" style="--w:{b}">{b}%</span><span class="rb-seg rb-l" style="--w:{l}">{l}%</span><span class="rb-seg rb-i" style="--w:{ig}">{ig}%</span>
  </span>
  <span class="rb-n" role="cell">{n:,} events</span>
</div>""")
    fnd = "".join(f"<tr><th scope='row'>{e(a)}</th><td>{e(b)}</td><td>{e(cc)}</td></tr>" for a, b, cc in c["findings"])
    recs = "".join(f"<li><h3>{e(a)}</h3><p>{e(b)}</p></li>" for a, b in c["recommendations"])
    les = "".join(f"<li><h3>{e(a)}</h3><p>{e(b)}</p></li>" for a, b in c["lessons"])
    lim = "".join(f"<li>{e(x)}</li>" for x in c["limitations"])
    s1, s2 = c["screenshots"]
    parts.append(f"""<main id="main">
<article>
  <header class="cs-hero" data-enter>
    <div class="wrap">
      <a class="text-link back" href="{rel}index.html#work">All work</a>
      <p class="kicker">Case study, {c['dates']}</p>
      <h1>{e(c['title'])}</h1>
      <p class="p-summary">{e(c['summary'])}</p>
      <dl class="p-meta"><div><dt>Category</dt><dd>{e(c['category'])}</dd></div><div><dt>Tools</dt><dd>{e(', '.join(c['tools']))}</dd></div></dl>
      <div class="actions">{links}</div>
      <figure class="cs-shot window">{picture(rel, s1[0], s1[1], sizes="(min-width: 1200px) 1200px, 100vw", eager=True)}</figure>
    </div>
  </header>
  <div class="wrap cs-layout">
    <nav class="cs-toc" aria-label="On this page"><ul>{toc_html}</ul></nav>
    <div class="cs-body">
      <section id="overview" class="cs-block"><h2>Overview</h2><div><p>{e(c['overview'])}</p><p>{e(c['problem'])}</p></div></section>
      <section id="questions" class="cs-block"><h2>The questions</h2><div><ol class="steps">{qs}</ol></div></section>
      <section id="data" class="cs-block"><h2>Dataset</h2><div><dl class="ds">{ds}</dl><p class="muted">{e(c['dataset_note'])}</p></div></section>
      <section id="process" class="cs-block"><h2>Process</h2><div><ol class="contrib">{proc}</ol></div></section>
      <section id="dashboard" class="cs-block cs-wide"><h2>The dashboard</h2>
        <p class="cs-intro">Seven pages share synced slicers for date, attack type, severity, protocol, traffic type and action, with a reset button, cross-filtering and tooltips. Severity and response always use the same colours.</p>
        <ul class="pages">{pages}</ul>
        <figure class="shot model">{picture(rel, s2[0], s2[1], sizes="(min-width: 1200px) 900px, 100vw")}</figure>
      </section>
    </div>
  </div>
  <section id="finding" class="cs-moment" aria-labelledby="finding-title">
    <div class="wrap">
      <h2 id="finding-title">Response did not follow risk</h2>
      <p class="moment-lede">{e(c['headline'])} Every severity level was blocked about a third of the time.</p>
      <div class="rb" role="table" aria-label="Share of events by recorded action, per severity level" data-bars>
        <div class="rb-key" aria-hidden="true"><span class="k-b">Blocked</span><span class="k-l">Logged</span><span class="k-i">Ignored</span></div>
        {''.join(rows)}
      </div>
      <p class="moment-foot">If response followed risk, the High row would be mostly blocked. Chi-square test of action against severity: p = 0.49. 4,460 High-severity events were ignored.</p>
    </div>
  </section>
  <div class="wrap cs-layout">
    <div class="cs-spacer" aria-hidden="true"></div>
    <div class="cs-body">
      <section id="findings" class="cs-block cs-wide"><h2>All findings</h2>
        <div class="table-wrap"><table class="ftable"><thead><tr><th scope="col">Area</th><th scope="col">Finding</th><th scope="col">Evidence</th></tr></thead><tbody>{fnd}</tbody></table></div>
        <p class="callout">{e(c['synthetic'])}</p>
      </section>
      <section id="recommendations" class="cs-block"><h2>Recommendations</h2><div><ol class="contrib">{recs}</ol></div></section>
      <section id="lessons" class="cs-block"><h2>Lessons learned</h2><div><ul class="impl">{les}</ul></div></section>
      <section id="limits" class="cs-block"><h2>Limitations</h2><div><ul class="findings-list">{lim}</ul><div class="actions">{links}</div></div></section>
    </div>
  </div>
</article>
{project_nav(rel, c['slug'])}
</main>
""")
    parts.append(footer(rel))
    return "".join(parts)


def not_found():
    from urllib.parse import urlparse
    rel = urlparse(SITE["base_url"]).path or "/"
    return (head(rel, "Page not found | Jesse Nasamu", "This page doesn't exist.", "404.html").replace("<head>", '<head>\n<meta name="robots" content="noindex">')
            + '<body class="project">' + header(rel) +
            f"""<main id="main" class="wrap nf"><h1>This page doesn't exist</h1><p>The link may be out of date. Everything is still on the home page.</p>
<a class="btn" href="{rel}index.html">Go to the home page</a></main>""" + footer(rel))


# ------------------------------------------------------------------ readable HTML output
# Puts every block-level element on its own line, indented two spaces per level.
# Inline content (text, links, spans inside a paragraph) is left exactly as written,
# so formatting never changes how the page looks.
BLOCK = set("""html head body header nav main section article aside footer div ul ol li dl dt dd
figure figcaption picture form fieldset legend table thead tbody tr p h1 h2 h3 h4 h5 h6
blockquote title meta link script noscript source textarea label button""".split())
VOID = {"meta", "link", "source", "br", "img", "input", "hr"}
TOKEN = re.compile(r"(<!--.*?-->|<!doctype[^>]*>|<script\b.*?</script>|<textarea\b.*?</textarea>|<[^>]+>)", re.S | re.I)


def pretty(html_text):
    out, line, depth = [], "", 0
    container_stack = []

    def flush():
        nonlocal line
        if line.strip():
            out.append("  " * depth + line.strip())
        line = ""

    for part in TOKEN.split(html_text):
        if not part:
            continue
        m = re.match(r"<(/?)([a-zA-Z0-9]+)", part)
        name = m.group(2).lower() if m else ""
        if m and m.group(1) == "" and re.search(r'class="(work-row|featured-visual|window|next-link)\b', part):
            container_stack.append(name); name = "__container__"
        elif m and m.group(1) == "/" and container_stack and container_stack[-1] == name and name in ("a", "span"):
            container_stack.pop(); name = "__container__"
        if part.lower().startswith(("<script", "<textarea", "<!doctype", "<!--")):
            flush(); out.append("  " * depth + part.strip()); continue
        if m and (name in BLOCK or name == "__container__"):
            closing = m.group(1) == "/"
            flush()
            if closing:
                depth = max(depth - 1, 0)
                out.append("  " * depth + part)
            else:
                out.append("  " * depth + part)
                if name not in VOID and not part.endswith("/>"):
                    depth += 1
            continue
        if not m and not part.strip():
            if "\n" in part:          # a line break between inline items starts a new output line
                flush()
            elif line:
                line += " "
            continue
        line += part if line else part.lstrip()
    flush()
    # join a short element whose only content is inline text back onto one line: <p>\n  text\n</p> -> <p>text</p>
    text = "\n".join(out) + "\n"
    text = re.sub(r"(<(p|h[1-6]|li|dt|dd|title|figcaption|label|button|legend|a)\b[^>\n]*>)\n\s*([^<\n][^\n]*|<(?!/?(?:%s)\b)[^\n]*)\n\s*(</\2>)" % "|".join(BLOCK),
                  r"\1\3\4", text)
    # empty elements stay on one line: <p ...>\n</p> -> <p ...></p>
    text = re.sub(r"(<([a-z0-9]+)\b[^>\n]*>)\n\s*(</\2>)", r"\1\3", text)
    return polish(text)


LANDMARK = re.compile(r'^(\s*)<(section|header|footer|main|nav|article)\b([^>]*)>')
ATTR = re.compile(r'\s+([a-zA-Z_:][-\w:.]*(?:="[^"]*")?)')


def label_for(attrs):
    m = re.search(r'\bid="([^"]+)"', attrs) or re.search(r'aria-label="([^"]+)"', attrs) \
        or re.search(r'\bclass="([^"\s]+)', attrs)
    return m.group(1).replace("-", " ").capitalize() if m else ""


def wrap_tag(line, limit=110):
    """Put each attribute of a long tag on its own line."""
    m = re.match(r'^(\s*)<([a-zA-Z0-9]+)((?:\s+[^\s=>]+(?:="[^"]*")?)+)\s*(/?)>(.*)$', line)
    if not m or len(line) <= limit or m.group(2) not in ("img", "source", "a", "form", "input", "textarea", "button"):
        return line
    ind, name, attrs, slash, rest = m.groups()
    if rest and not rest.startswith("</"):
        return line
    pad = ind + "    "
    parts = ATTR.findall(attrs)
    return f"{ind}<{name}\n" + "\n".join(pad + a for a in parts) + f"\n{ind}{slash}>{rest}"


def polish(text):
    out = []
    for line in text.split("\n"):
        m = LANDMARK.match(line)
        if m and m.group(2) in ("section", "header", "footer", "main"):
            label = label_for(m.group(3)) or m.group(2).capitalize()
            if out and out[-1].strip():
                out.append("")
            out.append(f"{m.group(1)}<!-- {label} -->")
        out.append(wrap_tag(line))
    return "\n".join(out)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    if path.endswith(".html"):
        text = pretty(text)
    open(full, "w", encoding="utf-8").write(text)


def main():
    write("index.html", home())
    write(f"work/{CASE['slug']}/index.html", case_page())
    for p in PROJECTS:
        write(f"work/{p['slug']}/index.html", project_page(p))
    write("404.html", not_found())
    today = datetime.date.today().isoformat()
    urls = [""] + [f"work/{CASE['slug']}/"] + [f"work/{p['slug']}/" for p in PROJECTS]
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join(f"  <url><loc>{SITE['base_url']}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE['base_url']}sitemap.xml\n")
    print(f"Built {len(urls)} pages + 404, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
