#!/usr/bin/env python3
"""
Generateur d'images TikTok - Version Virale
10 scripts x 6 slides = 60 images PNG (1080x1920)
+ exports 4:5 et 1:1 + format court 3 slides
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
OUTPUT_DIR       = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
OUTPUT_SHORT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output_short")

FONT_IMPACT = "C:/Windows/Fonts/impact.ttf"
FONT_BOLD   = "C:/Windows/Fonts/arialbd.ttf"
FONT_REG    = "C:/Windows/Fonts/arial.ttf"

# Linux fallback fonts
_FONT_IMPACT_LINUX = "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf"
_FONT_BOLD_LINUX   = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
_FONT_REG_LINUX    = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

# ─── Data ─────────────────────────────────────────────────────────────────────

SCRIPTS = [
    {
        "num": 1,
        "folder": "script_01_faits_amour",
        "icon": "PSY",
        "colors": ("#FF1744", "#7B1FA2"),
        "title": "3 FAITS PSY\nSUR L'AMOUR",
        "hook": "Tu CROIS etre amoureux...\nou tu as juste PEUR\nd'etre seul ?\nVoici la verite.",
        "stat_num": "60%",
        "stat": "des amoureux confondent\nattachement hormonal\net vrai amour.",
        "label": "FAIT",
        "points": [
            (
                "Tu verifies son online...",
                "Tu fais genre t'en fous.\nC'est l'attachement\nhormonal pur.",
            ),
            (
                "Tu t'enerves pour un rien ?",
                "En vrai, t'as juste peur\nqu'il / elle parte.\nC'est la peur de l'abandon.",
            ),
            (
                "Tu imagines deja un futur ?",
                "Ton cerveau est en mode\n'love bombing' sur\ntoi-meme.",
            ),
        ],
        "cta_header": "TU TE RECONNAIS ?",
        "cta": "Enregistre si t'es coupable !\nTag ton crush\npour le tester.",
        "hashtags": "#PsychoAmour  #FaitsAmour  #ReelsViral",
    },
    {
        "num": 2,
        "folder": "script_02_manipulation",
        "icon": "!",
        "colors": ("#B71C1C", "#0D0D1A"),
        "title": "3 SIGNES QUE\nQUELQU'UN\nTE MANIPULE",
        "hook": "Ca ressemble\na de l'amour.\nMais c'est du CONTROLE.\nVerifie vite.",
        "stat_num": "1/3",
        "stat": "des personnes en couple\nsubissent de la manipulation\nsans le realiser.",
        "label": "SIGNE",
        "points": [
            (
                "'T'es trop sensible'",
                "Il / elle dit ca quand\ntu exprimes un vrai ressenti.\nC'est du gaslighting.",
            ),
            (
                "Adorable seulement...",
                "...quand tu fais pile\nce qu'il / elle veut.\nSinon, froid polaire.",
            ),
            (
                "Tu te sens coupable...",
                "...meme quand c'est\n100% sa faute.\nC'est classique.",
            ),
        ],
        "cta_header": "TU VIS CA ?",
        "cta": "Envoie a une pote qui doute.\nPartage pour\nne plus te faire avoir.",
        "hashtags": "#Manipulation  #RedFlags  #PsychologieRelation",
    },
    {
        "num": 3,
        "folder": "script_03_red_flags",
        "icon": ">>",
        "colors": ("#E65100", "#B71C1C"),
        "title": "3 RED FLAGS\nEMOTIONNELS\nQUE TU IGNORES",
        "hook": "T'as deja excuse\nun comportement inacceptable ?\nVoici les 3 red flags\nque personne ne voit.",
        "stat_num": "82%",
        "stat": "des victimes de relation\ntoxique ont ignore\nau moins 1 red flag.",
        "label": "RED FLAG",
        "points": [
            (
                "'C'est du caractere'",
                "Non.\nC'est de la mechancete\ngratuite. Point.",
            ),
            (
                "'Jaloux mignon'",
                "C'est de la surveillance\ntoxique.\nPas cute du tout.",
            ),
            (
                "'Il / elle va changer'",
                "Si les actes\nne suivent pas,\nc'est non. Next.",
            ),
        ],
        "cta_header": "T'EN AS IGNORE COMBIEN ?",
        "cta": "Commente le nombre\nde red flags\nque t'as excuses.",
        "hashtags": "#RedFlagsAmour  #Toxique  #CoupleGoals",
    },
    {
        "num": 4,
        "folder": "script_04_vrai_amour",
        "icon": "OK",
        "colors": ("#1B5E20", "#F9A825"),
        "title": "3 CHOSES QUE\nFAIT UNE PERSONNE\nVRAIMENT AMOUREUSE",
        "hook": "Vrai amour ou\nsimple habitude ?\nVoici les 3 preuves\nirrefutables.",
        "stat_num": "3",
        "stat": "gestes suffisent a prouver\nun amour vraiment sincere.\nTu les fais ?",
        "label": "PREUVE",
        "points": [
            (
                "Il / elle se souvient...",
                "...de tes anecdotes random\nque t'avais\ntoi-meme oubliees.",
            ),
            (
                "Te rassure sans manipulation",
                "Direct, sans te faire douter\npour mieux\nte controler.",
            ),
            (
                "Petits gestes quotidiens",
                "Pas juste des grandes\ndeclas Instagram\nquand ca l'arrange.",
            ),
        ],
        "cta_header": "IL / ELLE FAIT CA ?",
        "cta": "Tag celle / celui\nqui fait ca pour toi.\nEnregistre pour ton futur couple.",
        "hashtags": "#VraiAmour  #PsychoCouple  #RelationSaine",
    },
    {
        "num": 5,
        "folder": "script_05_pas_gueri_ex",
        "icon": "...",
        "colors": ("#4A148C", "#1A237E"),
        "title": "3 SIGNES QUE\nT'AS PAS GUERI\nDE TON EX",
        "hook": "Tu crois avoir\ntourne la page ?\nCes 3 signes disent\nNON.",
        "stat_num": "68%",
        "stat": "des gens se remettent\nen couple trop tot.\nEt repayent les frais.",
        "label": "SIGNE",
        "points": [
            (
                "Tu compares tout le monde",
                "...a lui / elle\ninconsciemment.\nC'est automatique.",
            ),
            (
                "Un like suffit...",
                "...a te ruiner\nla journee entiere.\nUn seul like.",
            ),
            (
                "Tu reves du 'et si'",
                "Plus du passe que\nde ton present.\nC'est le piege.",
            ),
        ],
        "cta_header": "T'AS VRAIMENT TOURNE LA PAGE ?",
        "cta": "Commente 'gueri' si t'es out.\nPartage a quelqu'un\nqui en a besoin.",
        "hashtags": "#ExToxique  #Guerir  #AmourPropre",
    },
    {
        "num": 6,
        "folder": "script_06_detruire_relation",
        "icon": "XX",
        "colors": ("#1A237E", "#311B92"),
        "title": "3 COMPORTEMENTS\nQUI DETRUISENT\nUNE RELATION",
        "hook": "Les couples meurent\npas d'un coup.\nCe sont CES comportements\nqui les tuent lentement.",
        "stat_num": "90%",
        "stat": "des ruptures auraient\npu etre evitees.\nVoici exactement pourquoi.",
        "label": "ERREUR",
        "points": [
            (
                "Silence sur les problemes",
                "'Ca passera.'\nNon. Ca empire.\nToujours.",
            ),
            (
                "Comparer aux autres couples",
                "Les couples Insta\nsont une illusion.\nArrete de comparer.",
            ),
            (
                "Zero effort",
                "'Il / elle sait\nque je l'aime.'\nDis-le. Prouve-le.",
            ),
        ],
        "cta_header": "T'AS VECU CA ?",
        "cta": "Partage en story\npour sauver un couple.\nCommente ton erreur n°1.",
        "hashtags": "#CoupleFail  #RelationToxique  #ConseilsAmour",
    },
    {
        "num": 7,
        "folder": "script_07_amour_dependance",
        "icon": "?",
        "colors": ("#004D40", "#BF360C"),
        "title": "AMOUR OU\nDEPENDANCE ?\nTest en 15s.",
        "hook": "Tu l'aimes vraiment...\nou tu as PEUR\nd'etre seul ?\nFais le test en 15s.",
        "stat_num": "45%",
        "stat": "des adultes souffrent\nde dependance affective\nsans le reconnaitre.",
        "label": "TEST",
        "points": [
            (
                "Pas de message = journee foutue",
                "C'est de la dependance\naffective.\nPas de l'amour.",
            ),
            (
                "Oui a tout",
                "...meme contre\nton propre bien-etre.\nC'est pas sain.",
            ),
            (
                "Peur du solo > peur d'etre maltraite",
                "Rester par peur\nd'etre seul.\nC'est le vrai piege.",
            ),
        ],
        "cta_header": "AMOUR OU DEPENDANCE ?",
        "cta": "Enregistre pour\nton check-up perso.\nTag une amie dependante.",
        "hashtags": "#DependanceAffective  #SelfLove  #Psycho",
    },
    {
        "num": 8,
        "folder": "script_08_phrases_pieges",
        "icon": "!!",
        "colors": ("#0D47A1", "#6A1B9A"),
        "title": "3 PHRASES\nMANIPULATRICES\n'ROMANTIQUES'",
        "hook": "Ces phrases ont l'air\nd'amour...\nmais c'est du chantage\nemotionnel pur.",
        "stat_num": "3",
        "stat": "phrases 'romantiques'\ncachent en realite\nde la manipulation pure.",
        "label": "PIEGE",
        "points": [
            (
                "'Sans toi je suis rien'",
                "Culpabilite maximum.\nC'est du chantage\nemotionnel pur.",
            ),
            (
                "'T'es la seule qui me comprend'",
                "Isolement progressif.\nC'est calcule\net dangereux.",
            ),
            (
                "'Si tu m'aimes, fais ca'",
                "Chantage pur.\nL'amour ne se\nmarchande pas.",
            ),
        ],
        "cta_header": "ON T'A DIT CA ?",
        "cta": "Envoie a qui\ndit ca autour de toi.\nPartage pour proteger tes proches.",
        "hashtags": "#ManipulationAffective  #FakeAmour  #Alert",
    },
    {
        "num": 9,
        "folder": "script_09_toxique_deteste",
        "icon": ">>",
        "colors": ("#E65100", "#4A148C"),
        "title": "3 CHOSES QU'UN\nMANIPULATEUR\nDETESTE",
        "hook": "Pour faire fuir\nun manipulateur toxique,\nfais EXACTEMENT ca.\nIl deteste.",
        "stat_num": "100%",
        "stat": "des manipulateurs\ndetestent ces 3 comportements.\nUtilise-les maintenant.",
        "label": "POWER",
        "points": [
            (
                "Dire 'non' sans justification",
                "Juste non.\nSans explication.\nSans excuse. Point.",
            ),
            (
                "Poser tes limites et les tenir",
                "Et ne jamais\nnegocier tes limites.\nJamais.",
            ),
            (
                "Ignorer ses provocs, zen total",
                "Le silence est\nton super-pouvoir.\nUtilise-le.",
            ),
        ],
        "cta_header": "PRET(E) A LE TESTER ?",
        "cta": "Commente ton power move.\nPartage a quelqu'un\nqui en a besoin.",
        "hashtags": "#AntiToxique  #Empowerment  #NoContact",
    },
    {
        "num": 10,
        "folder": "script_10_verites_2026",
        "icon": "26",
        "colors": ("#006064", "#4527A0"),
        "title": "3 VERITES\nINCONFORTABLES\nRELATIONS 2026",
        "hook": "Amour en 2026 :\nles 3 verites que\ntout le monde evite.\nAlerte spoiler.",
        "stat_num": "2026",
        "stat": "Amour 2026 :\n3 verites que\npersonne n'ose dire.",
        "label": "VERITE",
        "points": [
            (
                "On prefere l'illusion Insta",
                "...a un vrai boulot\nde couple.\nCe n'est pas de l'amour.",
            ),
            (
                "Attention 24/7 = ennui",
                "Pas de l'amour.\nLa constance,\nc'est ca le vrai amour.",
            ),
            (
                "Micro-gestes > grandes declas",
                "Un cafe le matin >>\nun post Instagram.\nVoila la verite.",
            ),
        ],
        "cta_header": "T'ES D'ACCORD ?",
        "cta": "Commente OUI ou NON.\nPartage pour reveiller\nl'algorithme.",
        "hashtags": "#Amour2026  #TendancesCouple  #PsychoModerne",
    },
]

# ─── Helpers ───────────────────────────────────────────────────────────────────

def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def blend(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


def gradient_img(c1, c2, w=W, h=H):
    """Fast vertical gradient."""
    pixels = [blend(c1, c2, y / max(h - 1, 1)) for y in range(h)]
    col = Image.new("RGB", (1, h))
    col.putdata(pixels)
    return col.resize((w, h), Image.NEAREST)


def gradient_diagonal(c1, c2, w=W, h=H):
    """Diagonal gradient top-left(c1) -> bottom-right(c2), fast via 256px tile."""
    SIZE = 256
    img_s = Image.new("RGB", (SIZE, SIZE))
    pixels = []
    for y in range(SIZE):
        for x in range(SIZE):
            t = (x / (SIZE - 1) + y / (SIZE - 1)) / 2
            pixels.append(blend(c1, c2, t))
    img_s.putdata(pixels)
    return img_s.resize((w, h), Image.BILINEAR)


def load_font(path, size):
    linux_map = {
        FONT_IMPACT: _FONT_IMPACT_LINUX,
        FONT_BOLD:   _FONT_BOLD_LINUX,
        FONT_REG:    _FONT_REG_LINUX,
    }
    candidates = [path, linux_map.get(path), _FONT_BOLD_LINUX, _FONT_REG_LINUX]
    for p in candidates:
        if p:
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def measure_text(draw, text, font):
    try:
        bb = draw.textbbox((0, 0), text, font=font)
        return bb[2] - bb[0], bb[3] - bb[1]
    except Exception:
        return len(text) * max(font.size // 2, 6), font.size


def draw_text_block(draw, lines_text, cx, y, font, color=(255, 255, 255),
                    max_w=940, line_gap=1.35, shadow=True):
    """Draw centered multi-line text block, returns new y."""
    lines = lines_text.split("\n")
    _, lh = measure_text(draw, "Ay", font)
    lh = int(lh * line_gap)
    for line in lines:
        tw, _ = measure_text(draw, line, font)
        x = cx - tw // 2
        if shadow:
            draw.text((x + 3, y + 3), line, font=font, fill=(0, 0, 0))
        draw.text((x, y), line, font=font, fill=color)
        y += lh
    return y


def draw_pill(draw, text, cx, y, font, bg, fg=(255, 255, 255)):
    """Draw rounded-rectangle pill with text, returns bottom y."""
    tw, th = measure_text(draw, text, font)
    pad_x, pad_y = 28, 16
    x0 = cx - tw // 2 - pad_x
    x1 = cx + tw // 2 + pad_x
    y0 = y
    y1 = y + th + pad_y * 2
    draw.rounded_rectangle([(x0, y0), (x1, y1)], radius=min(30, (y1 - y0) // 2), fill=bg)
    draw.text((cx - tw // 2, y0 + pad_y), text, font=font, fill=fg)
    return y1


def draw_divider(draw, y, color=(255, 255, 255), width=3, margin=140):
    draw.line([(margin, y), (W - margin, y)], fill=color, width=width)


def darken(c, factor=0.35):
    return tuple(int(v * (1 - factor)) for v in c)


def lighten(c, factor=0.25):
    return tuple(min(255, int(v + (255 - v) * factor)) for v in c)


def draw_glow_border(draw, color, width=14):
    """Draw layered neon border on canvas edges for glow effect."""
    for i, factor in enumerate([0.75, 0.50, 0.30]):
        border_color = lighten(color, factor)
        off = i * 5
        w = width - i * 4
        if w <= 0:
            continue
        # Top
        draw.rectangle([(off, off), (W - off, off + w)], fill=border_color)
        # Bottom
        draw.rectangle([(off, H - off - w), (W - off, H - off)], fill=border_color)
        # Left
        draw.rectangle([(off, off), (off + w, H - off)], fill=border_color)
        # Right
        draw.rectangle([(W - off - w, off), (W - off, H - off)], fill=border_color)


def draw_circle_number(draw, num, cx, cy, radius=85, fill=(255, 255, 255),
                       text_color=(0, 0, 0)):
    """Draw a filled circle with a number centered inside."""
    draw.ellipse([(cx - radius, cy - radius), (cx + radius, cy + radius)], fill=fill)
    f = load_font(FONT_IMPACT, int(radius * 1.05))
    txt = str(num)
    tw, th = measure_text(draw, txt, f)
    draw.text((cx - tw // 2, cy - th // 2), txt, font=f, fill=text_color)


def export_ratios(img, base_path):
    """Export 4:5 (1080x1350) and 1:1 (1080x1080) crops alongside original."""
    # 4:5
    crop_h = 1350
    top = (H - crop_h) // 2
    img.crop((0, top, W, top + crop_h)).save(base_path.replace(".png", "_45.png"), "PNG")
    # 1:1
    top = (H - W) // 2
    img.crop((0, top, W, top + W)).save(base_path.replace(".png", "_11.png"), "PNG")


# ─── Slide 1: Hook ────────────────────────────────────────────────────────────

def slide_hook(s):
    c1 = rgb(s["colors"][0])
    c2 = rgb(s["colors"][1])
    img = gradient_diagonal(c1, c2)
    draw = ImageDraw.Draw(img)

    # Decorative blobs
    dc = lighten(blend(c1, c2, 0.3), 0.18)
    draw.ellipse([(-120, -120), (380, 380)], fill=dc)
    draw.ellipse([(750, 1650), (1250, 2100)], fill=darken(c2, 0.2))
    draw.ellipse([(820, 80), (1150, 410)], fill=lighten(c2, 0.12))

    # Glow border
    draw_glow_border(draw, lighten(c1, 0.2))

    # Title
    f_title = load_font(FONT_IMPACT, 88)
    y = 170
    y = draw_text_block(draw, s["title"], W // 2, y, f_title, (255, 255, 255), shadow=True)

    # Divider
    y += 30
    draw_divider(draw, y, color=lighten(c2, 0.5), width=4)
    y += 50

    # Hook text
    f_hook = load_font(FONT_BOLD, 64)
    y = draw_text_block(draw, s["hook"], W // 2, y, f_hook, (255, 255, 255), shadow=True)

    # Teaser line
    y = max(y + 40, H - 560)
    f_teaser = load_font(FONT_REG, 44)
    teaser_col = lighten(blend(c1, (255, 255, 255), 0.3), 0.4)
    draw_text_block(draw, "Lequel des 3 va te choquer ?", W // 2, y,
                    f_teaser, teaser_col, shadow=False)

    # Big icon in lower area
    y = max(y + 80, H - 380)
    f_icon = load_font(FONT_IMPACT, 220)
    icon_color = lighten(blend(c1, (255, 255, 255), 0.1), 0.15)
    iw, ih = measure_text(draw, s["icon"], f_icon)
    draw.text((W // 2 - iw // 2 + 4, y + 4), s["icon"], font=f_icon, fill=(0, 0, 0))
    draw.text((W // 2 - iw // 2, y), s["icon"], font=f_icon, fill=icon_color)

    return img


# ─── Slide 2: Stat choc ───────────────────────────────────────────────────────

def slide_stat(s):
    c1 = rgb(s["colors"][1])   # reversed for visual variety
    c2 = rgb(s["colors"][0])
    img = gradient_diagonal(c1, c2)
    draw = ImageDraw.Draw(img)

    # Decorative blobs
    dc = lighten(blend(c1, c2, 0.4), 0.2)
    draw.ellipse([(-200, 1300), (500, 2000)], fill=dc)
    draw.ellipse([(600, -100), (1200, 500)], fill=darken(c2, 0.25))

    # Glow border
    draw_glow_border(draw, lighten(c1, 0.2))

    # Big number centered (upper half)
    f_num = load_font(FONT_IMPACT, 200)
    num_str = s["stat_num"]
    nw, nh = measure_text(draw, num_str, f_num)
    num_y = H // 2 - nh - 80
    num_color = lighten(blend(c1, (255, 255, 255), 0.2), 0.55)
    draw.text((W // 2 - nw // 2 + 5, num_y + 5), num_str, font=f_num, fill=(0, 0, 0))
    draw.text((W // 2 - nw // 2, num_y), num_str, font=f_num, fill=num_color)

    # Divider
    div_y = H // 2
    draw_divider(draw, div_y, color=lighten(c2, 0.5), width=4)

    # Stat text
    f_stat = load_font(FONT_BOLD, 60)
    y = div_y + 55
    y = draw_text_block(draw, s["stat"], W // 2, y, f_stat, (255, 255, 255), shadow=True)

    # Progress bar
    bar_top = H - 110
    draw.rectangle([(0, bar_top), (W, H)], fill=darken(c2, 0.5))
    f_prog = load_font(FONT_BOLD, 38)
    prog_str = "Slide 2 / 6"
    pw, ph = measure_text(draw, prog_str, f_prog)
    draw.text((W // 2 - pw // 2, bar_top + (110 - ph) // 2),
              prog_str, font=f_prog, fill=(210, 210, 210))

    return img


# ─── Slides 3-5: Points ───────────────────────────────────────────────────────

def slide_point(s, idx):
    c1 = rgb(s["colors"][0])
    c2 = rgb(s["colors"][1])
    if idx % 2 == 0:
        img = gradient_img(darken(c2, 0.4), darken(c1, 0.25))
    else:
        img = gradient_img(darken(c1, 0.4), darken(c2, 0.25))
    draw = ImageDraw.Draw(img)

    num = idx + 1
    title, desc = s["points"][idx]

    # Circle number (centered, large)
    circle_col = lighten(c1 if idx % 2 == 0 else c2, 0.35)
    circle_text_col = darken(c1 if idx % 2 == 0 else c2, 0.5)
    draw_circle_number(draw, num, W // 2, H // 2, radius=90,
                       fill=circle_col, text_color=circle_text_col)

    # Label pill  (e.g. "FAIT 1")
    f_label = load_font(FONT_BOLD, 46)
    label_text = f"{s['label']}  {num}"
    pill_bg = lighten(c1 if idx % 2 == 0 else c2, 0.15)
    y_after_pill = draw_pill(draw, label_text, W // 2, 160, f_label,
                             bg=pill_bg, fg=(255, 255, 255))

    # Title
    f_title = load_font(FONT_IMPACT, 76)
    y = y_after_pill + 50
    y = draw_text_block(draw, title, W // 2, y, f_title, (255, 255, 255), shadow=True)

    # Divider
    y += 30
    draw_divider(draw, y, color=(255, 255, 255), width=3)
    y += 45

    # Description
    f_desc = load_font(FONT_BOLD, 56)
    y = draw_text_block(draw, desc, W // 2, y, f_desc, (235, 235, 235), shadow=True)

    # Progress bar (slides 3-5 of 6)
    bar_top = H - 110
    draw.rectangle([(0, bar_top), (W, H)], fill=darken(c2, 0.55))
    f_prog = load_font(FONT_BOLD, 38)
    filled = chr(9679)  # ●
    empty  = chr(9675)  # ○
    prog_str = (filled * num) + (empty * (3 - num)) + f"   Slide {num + 2} / 6"
    pw, ph = measure_text(draw, prog_str, f_prog)
    draw.text((W // 2 - pw // 2, bar_top + (110 - ph) // 2),
              prog_str, font=f_prog, fill=(210, 210, 210))

    return img


# ─── Slide 6: CTA ─────────────────────────────────────────────────────────────

def slide_cta(s):
    c1 = rgb(s["colors"][1])   # reversed colors for CTA
    c2 = rgb(s["colors"][0])
    img = gradient_diagonal(c1, c2)
    draw = ImageDraw.Draw(img)

    # Decorative shapes
    dc = lighten(blend(c1, c2, 0.4), 0.2)
    draw.ellipse([(-150, 200), (450, 800)], fill=dc)
    draw.ellipse([(700, 1200), (1350, 1850)], fill=darken(c2, 0.2))

    # Glow border
    draw_glow_border(draw, lighten(c1, 0.2))

    # Personalized header from data
    f_head = load_font(FONT_IMPACT, 90)
    y = 140
    y = draw_text_block(draw, s["cta_header"], W // 2, y, f_head,
                        (255, 255, 255), shadow=True)

    # Divider
    y += 35
    draw_divider(draw, y, color=lighten(c2, 0.5), width=4)
    y += 55

    # CTA text
    f_cta = load_font(FONT_BOLD, 58)
    y = draw_text_block(draw, s["cta"], W // 2, y, f_cta, (255, 255, 255), shadow=True)

    y += 60

    # Hashtags
    f_hash = load_font(FONT_REG, 42)
    hash_col = lighten(blend(c1, c2, 0.3), 0.45)
    y = draw_text_block(draw, s["hashtags"], W // 2, y, f_hash,
                        hash_col, shadow=False)

    # Series indicator
    f_serie = load_font(FONT_REG, 36)
    serie_text = f"Serie Psycho  •  Episode {s['num']}"
    serie_col = lighten(blend(c1, c2, 0.5), 0.35)
    sw, _ = measure_text(draw, serie_text, f_serie)
    draw.text((W // 2 - sw // 2, H - 170), serie_text,
              font=f_serie, fill=serie_col)

    # Subscribe CTA
    f_follow = load_font(FONT_BOLD, 46)
    follow_text = "si tu aimes ce contenu abonne toi :)"
    fw, _ = measure_text(draw, follow_text, f_follow)
    draw.text((W // 2 - fw // 2, H - 110), follow_text,
              font=f_follow, fill=(255, 255, 255))

    return img


# ─── Format court 3 slides ────────────────────────────────────────────────────

def generate_short(s, base_dir):
    """Generate 3-slide short format (hook + best point + CTA) for 15s Reels."""
    folder = os.path.join(base_dir, s["folder"])
    os.makedirs(folder, exist_ok=True)

    p = os.path.join(folder, "slide_01_hook.png")
    img = slide_hook(s)
    img.save(p, "PNG")
    export_ratios(img, p)

    p = os.path.join(folder, "slide_02_best_point.png")
    img = slide_point(s, 0)
    img.save(p, "PNG")
    export_ratios(img, p)

    p = os.path.join(folder, "slide_03_cta.png")
    img = slide_cta(s)
    img.save(p, "PNG")
    export_ratios(img, p)


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_SHORT_DIR, exist_ok=True)
    total = 0

    for s in SCRIPTS:
        folder = os.path.join(OUTPUT_DIR, s["folder"])
        os.makedirs(folder, exist_ok=True)
        print(f"  [{s['num']:02d}/10] {s['folder']}")

        def save(img, path):
            img.save(path, "PNG")
            export_ratios(img, path)

        save(slide_hook(s),    os.path.join(folder, "slide_01_hook.png"))
        save(slide_stat(s),    os.path.join(folder, "slide_02_stat.png"))
        for i in range(3):
            save(slide_point(s, i),
                 os.path.join(folder, f"slide_0{i + 3}_point{i + 1}.png"))
        save(slide_cta(s),     os.path.join(folder, "slide_06_cta.png"))

        generate_short(s, OUTPUT_SHORT_DIR)

        total += 6
        print(f"         6 slides + ratios + short OK")

    print(f"\nDone! {total} full slides in '{OUTPUT_DIR}/'")
    print(f"      Short versions in '{OUTPUT_SHORT_DIR}/'")


if __name__ == "__main__":
    main()
