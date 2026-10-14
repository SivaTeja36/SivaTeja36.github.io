"""Render index.html from the data below.  `python build.py`

All content lives here (hero, about, experience, projects, skills, contact).
Edit the data, re-run, commit index.html. No dependencies beyond Python 3.
"""
import html
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://sivateja36.github.io"

# ---------------------------------------------------------------- data
NAME = "V. Siva Teja"
TAGLINE = "Full Stack · Azure Cloud · AI/ML Engineer"
ROLES = ["Full Stack Software Engineer", "Cloud Engineer", "AI / ML Engineer",
         "Python | FastAPI | PostgreSQL", "HTML | CSS | JavaScript | TypeScript | React",
         "AI / ML | RAG | LangChain | LangGraph", "Building Reliable AI-Powered Engineering Systems"]
SUMMARY = ("Software Engineer with 3+ years of experience across full stack development, cloud "
           "engineering and AI/ML. I build responsive React frontends and scalable Python/FastAPI "
           "backends, provision Azure infrastructure with Terraform, and ship AI-enabled systems: "
           "computer-vision pipelines, RAG chatbots and Text-to-SQL agents.")
EMAIL = "vantasivateja@gmail.com"
GITHUB = "https://github.com/SivaTeja36"
LINKEDIN = "https://www.linkedin.com/in/siva-teja-vanta-99213b257/"
LOCATION = "India"

STATS = [("3+", "Years of experience"), ("9", "Production projects"), ("3", "Domains: Cloud · Backend · AI/ML")]

FACTS = [
    ("Role", "Software Engineer @ NSP Product Engineering Services"),
    ("Since", "2022 — Present"),
    ("Education", "B.Tech, Mechanical Engineering (2018 — 2022)"),
    ("Origin", "India · open to remote"),
    ("Focus", "FastAPI · PostgreSQL · Azure IaC · LangChain"),
    ("Status", "Building + Learning + Shipping"),
]

EXPERIENCE = [dict(
    role="Software Engineer", org="NSP Product Engineering Services", where="India", when="2022 — Present",
    bullets=[
        "Designed and delivered end-to-end backend systems with Python and FastAPI across HR-tech, notification, AI/ML and cloud infrastructure projects.",
        "Built and deployed cloud-native applications on Azure: Container Apps, API Management, Front Door, Static Web Apps, Functions and Storage Accounts, secured with Private Endpoints.",
        "Authored Terraform modules to provision and manage Azure infrastructure across dev, QA and production as version-controlled Infrastructure as Code.",
        "Designed PostgreSQL schemas and data-access layers for multi-tenant, high-throughput backend services.",
        "Developed AI features: computer-vision pipelines, RAG chatbots and Text-to-SQL agents integrating LLMs, vector databases and embedding models.",
        "Partnered with analytics, engineering and business stakeholders to turn requirements into production-ready systems.",
    ],
)]

AWARDS = [("Performance Excellence Award", "NSP Product Engineering Services — consistent high-quality delivery"),
          ("Collaboration Award", "NSP Product Engineering Services — effective cross-functional teamwork")]

# (title, kicker, description, tech chips, link or None, accent)
PROJECTS = [
    ("AI Robot Trainer", "Vision model training & deployment platform",
     "End-to-end platform for configuring, training and deploying computer-vision models onto physical robots. "
     "Designed the Azure architecture (Front Door, Static Web App, APIM, Container Apps, Functions), Private "
     "Endpoints for PostgreSQL and Storage, the versioned training/deployment schema, Terraform IaC, and a "
     "LangChain RAG agent for querying jobs and deployment history.",
     ["Azure", "Terraform", "FastAPI", "PostgreSQL", "LangChain", "RAG"], None, "cyan"),
    ("Predictive Maintenance", "ML system for industrial machines",
     "Failure prediction from sensor data: cleaning, EDA, feature engineering, Random Forest and Logistic "
     "Regression models evaluated with confusion matrix and ROC, served real-time through a containerised "
     "FastAPI API with a Streamlit dashboard.",
     ["Python", "Scikit-learn", "Pandas", "FastAPI", "Docker", "Streamlit"], None, "purple"),
    ("Assisto", "Text-to-SQL agentic assistant",
     "Chatbot inside an HRMS product that turns natural-language questions into SQL and summarised answers. "
     "Multi-agent framework (schema, SQL, data-fetch, validation, orchestrator) coordinated by a ReAct loop.",
     ["Python", "FastAPI", "LangChain", "LLMs", "Agents"], None, "pink"),
    ("RAG Bots", "Domain chatbots on vector retrieval",
     "Sales and HR-policy bots answering questions over documentation and policies. Designed the RAG "
     "architecture, ingestion and retrieval pipelines on PgVector with tuned embeddings.",
     ["n8n", "RAG", "PgVector", "Embeddings", "LLMs"], None, "emerald"),
    ("Notify", "Multi-channel campaign platform",
     "Email and WhatsApp campaigns with bulk contact import, role-based access and two-way messaging. "
     "Backend architecture, schema and APIs, with memory-efficient bulk import via decorators and generators.",
     ["Python", "FastAPI", "PostgreSQL", "React", "Azure DevOps", "Docker"], None, "amber"),
    ("AI Attendance System", "Real-time face recognition",
     "Live-camera attendance with DeepFace (VGG-Face) over RTSP streams processed by OpenCV, logging "
     "in-time and out-time automatically.",
     ["Python", "FastAPI", "OpenCV", "DeepFace", "PostgreSQL", "React"], None, "cyan"),
    ("Saba", "Geolocation branch registration & reporting",
     "Cargo-tank and oil-testing operations: lab test reports, multi-client sharing, automated PDF "
     "generation, role-based UI and claim support.",
     ["Python", "FastAPI", "PostgreSQL", "React", "Docker"], None, "purple"),
    ("Notification Service & HireAssisto", "Shared microservice + AI recruitment",
     "Centralised Email/WhatsApp/SMS notification service with Meta Cloud API and delivery reporting, "
     "plus a multi-tenant recruitment platform with AI resume parsing and Foundit/Naukri integrations.",
     ["FastAPI", "RabbitMQ", "FastMail", "PostgreSQL", "Pytest", "Docker"], None, "pink"),
    ("FastAPI Multitenant Framework", "Reusable schema-based multi-tenant backend",
     "Open-source starter for rapid FastAPI projects: tenant-based database isolation, JWT auth, Alembic "
     "migrations, Dramatiq + RabbitMQ workers, APScheduler and Dockerised environments.",
     ["FastAPI", "SQLAlchemy", "Alembic", "Dramatiq", "RabbitMQ", "Docker"],
     "https://github.com/SivaTeja36/FastAPI-Multitenant-Dramatiq", "emerald"),
]

# (group, accent, [(label, icon-slug)])
SKILLS = [
    ("Languages & Frontend", "cyan", [("Python", "python"), ("TypeScript", "typescript"), ("JavaScript", "javascript"),
                                      ("SQL", "sql"), ("HTML5", "html5"), ("CSS", "css"), ("React", "react"),
                                      ("Streamlit", "streamlit")]),
    ("Backend", "purple", [("FastAPI", "fastapi"), ("Django", "django"), ("Flask", "flask"), ("SQLAlchemy", "sqlalchemy"),
                           ("Pytest", "pytest"), ("RabbitMQ", "rabbitmq"), ("Swagger", "swagger"), ("Postman", "postman")]),
    ("Cloud & DevOps", "amber", [("Azure", "azure"), ("Terraform", "terraform"), ("Docker", "docker"),
                                 ("Azure DevOps", "azure"), ("Linux", "linux"), ("Git", "git"), ("GitHub", "github")]),
    ("AI / ML", "pink", [("Scikit-learn", "scikitlearn"), ("OpenCV", "opencv"), ("LangChain", "langchain"),
                         ("LangGraph", "langgraph"), ("Ollama", "ollama"), ("n8n", "n8n"), ("NumPy", "numpy"),
                         ("Pandas", "pandas"), ("Jupyter", "jupyter")]),
    ("Data", "blue", [("PostgreSQL", "postgresql"), ("PgVector", "postgresql"), ("Redis", "redis"), ("SQLite", "sqlite")]),
]

CUSTOM_ICONS = {
    "azure": ("M5.483 21.3H24L14.025 4.013l-3.038 8.347 5.836 6.938L5.483 21.3zM13.23 2.7L6.105 8.677 0 19.253h5.505v.014L13.23 2.7z", "#0078D4"),
    "sql": ("M12 2C7.03 2 3 3.57 3 5.5v13C3 20.43 7.03 22 12 22s9-1.57 9-3.5v-13C21 3.57 16.97 2 12 2zm0 2c4.42 0 7 1.35 7 1.5S16.42 7 12 7 5 5.65 5 5.5 7.58 4 12 4zm7 14.5c0 .15-2.58 1.5-7 1.5s-7-1.35-7-1.5v-3.1C6.6 18.3 9.2 19 12 19s5.4-.7 7-1.6v1.1zm0-4.5c0 .15-2.58 1.5-7 1.5S5 14.15 5 14v-3.1C6.6 11.8 9.2 12.5 12 12.5s5.4-.7 7-1.6V14zm0-4.5c0 .15-2.58 1.5-7 1.5S5 9.65 5 9.5V7.4C6.6 8.3 9.2 9 12 9s5.4-.7 7-1.6v2.1z", "#60A5FA"),
    "linkedin": ("M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.55V9h3.57v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z", "#0A66C2"),
}
# brand colours that vanish on one of the backgrounds
DARK_FIX = {"flask": "#E6E9F2", "github": "#E6E9F2", "ollama": "#E6E9F2", "django": "#44B78B", "pandas": "#A78BFA",
            "numpy": "#4DABCF", "sqlite": "#4DA8DA", "langchain": "#2DD4BF", "swagger": "#85EA2D"}
LIGHT_FIX = {"javascript": "#C9A800", "linux": "#B38600", "react": "#0E8FAF", "langgraph": "#1F7FD1",
             "sql": "#2563EB", "swagger": "#5BA800", "pytest": "#0A7CB3"}


# ---------------------------------------------------------------- helpers
def e(s): return html.escape(s, quote=True)


def icon(slug):
    if slug in CUSTOM_ICONS:
        d, col = CUSTOM_ICONS[slug]
    else:
        svg = open(os.path.join(HERE, "assets", "icons", f"{slug}.svg"), encoding="utf-8").read()
        d = re.search(r'<path d="([^"]+)"', svg).group(1)
        col = re.search(r'fill="(#[0-9A-Fa-f]{6})"', svg).group(1)
    dark, light = DARK_FIX.get(slug, col), LIGHT_FIX.get(slug, col)
    return (f'<svg class="ic" viewBox="0 0 24 24" style="--ic-dark:{dark};--ic-light:{light}" aria-hidden="true">'
            f'<path d="{d}"/></svg>')


def chip(label, slug):
    return f'<span class="chip">{icon(slug)}{e(label)}</span>'


def section_head(eyebrow, title, lead=""):
    lead_html = f'<p class="lead">{e(lead)}</p>' if lead else ""
    return f'<div class="sec-head reveal"><span class="eyebrow">// {e(eyebrow)}</span><h2>{e(title)}</h2>{lead_html}</div>'


# ---------------------------------------------------------------- blocks
def nav():
    return f'''<header class="nav" id="top">
  <a class="brand" href="#top"><span class="brand-dot"></span>siva<span class="brand-accent">.teja</span></a>
  <nav class="links" id="nav-links">
    <a href="#about">About</a><a href="#experience">Experience</a><a href="#projects">Projects</a>
    <a href="#skills">Skills</a><a href="#contact">Contact</a>
  </nav>
  <div class="nav-actions">
    <a class="btn btn-ghost btn-sm" href="{GITHUB}" target="_blank" rel="noopener">{icon("github")} GitHub</a>
    <button class="icon-btn" id="theme-toggle" aria-label="Toggle theme" title="Toggle theme">
      <svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.9 4.9l1.4 1.4m11.4 11.4 1.4 1.4M2 12h2m16 0h2M4.9 19.1l1.4-1.4m11.4-11.4 1.4-1.4"/></svg>
      <svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>
    </button>
    <button class="icon-btn burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>'''


def hero():
    stats = "".join(f'<div class="stat"><strong>{e(n)}</strong><span>{e(l)}</span></div>' for n, l in STATS)
    rows = "".join(f'<div class="trow"><span class="tkey">{e(k)}</span><span class="tdots"></span><span class="tval">{e(v)}</span></div>'
                   for k, v in [("Subject", NAME), ("Role", "Full Stack · Azure · AI/ML"), ("Origin", LOCATION),
                                ("Status", "Building + Learning + Shipping"), ("Core", "Python · FastAPI · PostgreSQL · Azure")])
    return f'''<section class="hero">
  <div class="hero-grid">
    <div class="hero-copy">
      <span class="eyebrow reveal">// HELLO, I'M</span>
      <h1 class="reveal">{e(NAME)}</h1>
      <p class="typing reveal"><span id="typed"></span><span class="caret">|</span></p>
      <p class="hero-sum reveal">{e(SUMMARY)}</p>
      <div class="hero-cta reveal">
        <a class="btn btn-primary" href="#projects">View projects</a>
        <a class="btn btn-ghost" href="#contact">Get in touch</a>
        <a class="btn btn-ghost" href="{LINKEDIN}" target="_blank" rel="noopener">{icon("linkedin")} LinkedIn</a>
      </div>
      <div class="stats reveal">{stats}</div>
    </div>
    <div class="hero-visual reveal">
      <div class="portrait-wrap">
        <div class="portrait-ring"></div>
        <picture><source srcset="assets/img/siva.webp" type="image/webp"><img class="portrait" src="assets/img/siva.jpg" alt="Portrait of V. Siva Teja" width="900" height="900"></picture>
        <div class="float-badge fb-1">{icon("azure")} Azure · Terraform</div>
        <div class="float-badge fb-2">{icon("fastapi")} FastAPI · PostgreSQL</div>
        <div class="float-badge fb-3">{icon("langchain")} RAG · Agents</div>
      </div>
      <div class="terminal">
        <div class="tbar"><i></i><i></i><i></i><span>profile.sh --live</span><em class="live"><b></b>LIVE</em></div>
        <div class="tbody">{rows}</div>
      </div>
    </div>
  </div>
  <div class="scroll-hint"><span></span></div>
</section>'''


def about():
    facts = "".join(f'<div class="fact reveal"><span class="fk">{e(k)}</span><span class="fv">{e(v)}</span></div>' for k, v in FACTS)
    awards = "".join(f'<li class="reveal"><strong>{e(t)}</strong><span>{e(d)}</span></li>' for t, d in AWARDS)
    return f'''<section id="about" class="section">
  {section_head("ABOUT", "What I build", "End-to-end ownership from architecture through deployment across HR-tech, notification, computer-vision and robotics platforms.")}
  <div class="about-grid">
    <div class="about-cards">
      <article class="card accent-cyan reveal"><h3>Backends</h3><p>Python / FastAPI microservices on PostgreSQL, multi-tenant by design, with RabbitMQ workers, Alembic migrations and Pytest coverage.</p></article>
      <article class="card accent-purple reveal"><h3>Azure infrastructure as code</h3><p>Container Apps, API Management, Front Door, Static Web Apps, Functions and Private Endpoints, all provisioned with Terraform across dev, QA and prod.</p></article>
      <article class="card accent-pink reveal"><h3>AI-enabled systems</h3><p>Computer-vision training and deployment pipelines, RAG chatbots on PgVector, and Text-to-SQL agents built with LangChain.</p></article>
    </div>
    <aside class="facts-card reveal">
      <span class="eyebrow">// SYSTEM.INFO</span>
      <div class="facts">{facts}</div>
      <span class="eyebrow" style="margin-top:22px">// AWARDS</span>
      <ul class="awards">{awards}</ul>
    </aside>
  </div>
</section>'''


def experience():
    items = ""
    for x in EXPERIENCE:
        b = "".join(f"<li>{e(t)}</li>" for t in x["bullets"])
        items += f'''<article class="tl-item reveal">
      <div class="tl-dot"></div>
      <div class="tl-card card">
        <div class="tl-head"><div><h3>{e(x["role"])}</h3><p class="tl-org">{e(x["org"])} · {e(x["where"])}</p></div><span class="tl-when">{e(x["when"])}</span></div>
        <ul class="bullets">{b}</ul>
      </div></article>'''
    items += '''<article class="tl-item reveal"><div class="tl-dot alt"></div><div class="tl-card card">
      <div class="tl-head"><div><h3>B.Tech, Mechanical Engineering</h3><p class="tl-org">Bachelor of Technology</p></div><span class="tl-when">2018 — 2022</span></div>
      <p class="muted">Engineering fundamentals, then a deliberate move into software: Python first, then backend systems, cloud and AI/ML.</p>
    </div></article>'''
    return f'''<section id="experience" class="section">
  {section_head("EXPERIENCE", "Where I've worked")}
  <div class="timeline">{items}</div>
</section>'''


def projects():
    cards = ""
    for title, kicker, desc, tech, link, accent in PROJECTS:
        chips = "".join(f'<span class="tag">{e(t)}</span>' for t in tech)
        link_html = (f'<a class="plink" href="{link}" target="_blank" rel="noopener">{icon("github")} Source</a>'
                     if link else '<span class="plink muted">Client / internal</span>')
        cards += f'''<article class="pcard card accent-{accent} reveal">
      <div class="pcard-top"><span class="pkicker">{e(kicker)}</span>{link_html}</div>
      <h3>{e(title)}</h3><p>{e(desc)}</p><div class="tags">{chips}</div></article>'''
    return f'''<section id="projects" class="section">
  {section_head("PROJECTS", "Things I've shipped", "Selected work across backend, cloud and AI/ML. Most are production systems built for clients; the framework is open source.")}
  <div class="pgrid">{cards}</div>
</section>'''


def skills():
    groups = ""
    for name, accent, items in SKILLS:
        chips = "".join(chip(l, s) for l, s in items)
        groups += f'<div class="sgroup reveal"><div class="sg-head"><i class="dash {accent}"></i><span class="eyebrow">{e(name.upper())}</span></div><div class="chips">{chips}</div></div>'
    return f'''<section id="skills" class="section">
  {section_head("TECH STACK", "Tools I build with")}
  <div class="skills card">{groups}</div>
</section>'''


def contact():
    return f'''<section id="contact" class="section">
  {section_head("LET'S CONNECT", "Let's build something together", "Open to backend, Azure and AI/ML collaborations, side projects and good problems.")}
  <div class="cgrid">
    <a class="ccard card reveal" href="mailto:{EMAIL}"><span class="ctile" style="--c:#EA4335">{icon("gmail")}</span><div><strong>Email</strong><span>{EMAIL}</span></div></a>
    <a class="ccard card reveal" href="{LINKEDIN}" target="_blank" rel="noopener"><span class="ctile" style="--c:#0A66C2">{icon("linkedin")}</span><div><strong>LinkedIn</strong><span>in/siva-teja-vanta</span></div></a>
    <a class="ccard card reveal" href="{GITHUB}" target="_blank" rel="noopener"><span class="ctile" style="--c:#E6E9F2">{icon("github")}</span><div><strong>GitHub</strong><span>@SivaTeja36</span></div></a>
    <button class="ccard card reveal" id="copy-email" type="button"><span class="ctile" style="--c:#34D399"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg></span><div><strong>Copy email</strong><span id="copy-label">click to copy</span></div></button>
  </div>
  <p class="quote reveal">“Build it right, ship it, then make it faster.”</p>
</section>'''


def footer():
    return f'''<footer class="footer">
  <span>© <span id="year"></span> {e(NAME)} · Built with plain HTML, CSS and a little JS · Hosted on GitHub Pages</span>
  <a href="#top" class="totop">Back to top ↑</a>
</footer>'''


def page():
    roles_js = ", ".join(f'"{r}"' for r in ROLES)
    return f'''<!doctype html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(NAME)} — {e(TAGLINE)}</title>
<meta name="description" content="{e(SUMMARY)}">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{SITE}/">
<meta property="og:type" content="website"><meta property="og:title" content="{e(NAME)} — {e(TAGLINE)}">
<meta property="og:description" content="{e(SUMMARY)}"><meta property="og:image" content="{SITE}/assets/img/og.jpg"><meta property="og:url" content="{SITE}/">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0A101F">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>try{{var t=localStorage.getItem('theme');if(!t)t=matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';document.documentElement.dataset.theme=t;}}catch(_){{}}</script>
</head>
<body>
<div class="bg-dots" aria-hidden="true"></div>
<div class="bg-glow g1" aria-hidden="true"></div><div class="bg-glow g2" aria-hidden="true"></div>
{nav()}
<main>
{hero()}
{about()}
{experience()}
{projects()}
{skills()}
{contact()}
</main>
{footer()}
<script>window.ROLES=[{roles_js}];</script>
<script src="assets/js/main.js"></script>
</body>
</html>
'''


if __name__ == "__main__":
    out = os.path.join(HERE, "index.html")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(page())
    print("index.html written,", os.path.getsize(out) // 1024, "KB")
