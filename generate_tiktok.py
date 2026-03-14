#!/usr/bin/env python3
"""
Generateur d'images TikTok
10 scripts x 5 slides = 50 images PNG (1080x1920)
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

FONT_IMPACT = "C:/Windows/Fonts/impact.ttf"
FONT_BOLD   = "C:/Windows/Fonts/arialbd.ttf"
FONT_REG    = "C:/Windows/Fonts/arial.ttf"

# ─── Data ─────────────────────────────────────────────────────────────────────

SCRIPTS = [
    {
        "num": 1,
        "folder": "script_01_faits_amour",
        "icon": "PSY",
        "colors": ("#FF1744", "#7B1FA2"),
        "title": "3 FAITS PSY\nSUR L'AMOUR",
        "hook": "Si tu te reconnais\ndans 1 seul point,\nt'es plus amoureux\nque tu le penses !",
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
        "cta": "Enregistre si t'es coupable !\nTag ton crush\npour le tester.",
        "hashtags": "#PsychoAmour  #FaitsAmour  #ReelsViral",
    },
    {
        "num": 2,
        "folder": "script_02_manipulation",
        "icon": "!",
        "colors": ("#B71C1C", "#0D0D1A"),
        "title": "3 SIGNES QUE\nQUELQU'UN\nTE MANIPULE",
        "hook": "Ca ressemble\na de l'amour...\nmais c'est du controle.\nVerifie vite !",
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
        "cta": "Envoie a une pote qui doute.\nSauvegarde pour\nne plus te faire avoir.",
        "hashtags": "#Manipulation  #RedFlags  #PsychologieRelation",
    },
    {
        "num": 3,
        "folder": "script_03_red_flags",
        "icon": ">>",
        "colors": ("#E65100", "#B71C1C"),
        "title": "3 RED FLAGS\nEMOTIONNELS\nQUE TU IGNORES",
        "hook": "Le vrai probleme ?\nTu excuseras\nces red flags\nau lieu de fuir.",
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
        "cta": "Like si t'as deja\ndit une de ces excuses.\nCommente ton pire red flag.",
        "hashtags": "#RedFlagsAmour  #Toxique  #CoupleGoals",
    },
    {
        "num": 4,
        "folder": "script_04_vrai_amour",
        "icon": "OK",
        "colors": ("#1B5E20", "#F9A825"),
        "title": "3 CHOSES QUE\nFAIT UNE PERSONNE\nVRAIMENT AMOUREUSE",
        "hook": "Vrai amour ou fake ?\nVoici les 3 preuves\nirrefutables.",
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
        "cta": "Tag celle / celui\nqui fait ca pour toi.\nEnregistre pour ton futur couple.",
        "hashtags": "#VraiAmour  #PsychoCouple  #RelationSaine",
    },
    {
        "num": 5,
        "folder": "script_05_pas_gueri_ex",
        "icon": "...",
        "colors": ("#4A148C", "#1A237E"),
        "title": "3 SIGNES QUE\nT'AS PAS GUERI\nDE TON EX",
        "hook": "Tu crois avoir\ntourne la page ?\nCes signes\ndisent NON.",
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
        "cta": "Sauvegarde et\nbloque ton ex aujourd'hui.\nCommente 'gueri' si t'es out.",
        "hashtags": "#ExToxique  #Guerir  #AmourPropre",
    },
    {
        "num": 6,
        "folder": "script_06_detruire_relation",
        "icon": "XX",
        "colors": ("#1A237E", "#311B92"),
        "title": "3 COMPORTEMENTS\nQUI DETRUISENT\nUNE RELATION",
        "hook": "Les couples meurent\npas d'un coup.\nC'est ca qui les\ntue lentement.",
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
        "cta": "Partage en story\npour sauver un couple.\nLike si t'as vecu ca.",
        "hashtags": "#CoupleFail  #RelationToxique  #ConseilsAmour",
    },
    {
        "num": 7,
        "folder": "script_07_amour_dependance",
        "icon": "?",
        "colors": ("#004D40", "#BF360C"),
        "title": "AMOUR OU\nDEPENDANCE ?\nTest en 15s.",
        "hook": "Amour ou besoin\nmaladif ?\nFais le test\nmaintenant.",
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
        "cta": "Enregistre pour\nton check-up perso.\nTag une amie dependante.",
        "hashtags": "#DependanceAffective  #SelfLove  #Psycho",
    },
    {
        "num": 8,
        "folder": "script_08_phrases_pieges",
        "icon": "!!",
        "colors": ("#0D47A1", "#6A1B9A"),
        "title": "3 PHRASES\nMANIPULATRICES\n'ROMANTIQUES'",
        "hook": "Ces mots ont\nl'air cute...\nmais c'est du piege.\nFais attention.",
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
        "cta": "Envoie a qui\ndit ca autour de toi.\nSauvegarde anti-gaslighting.",
        "hashtags": "#ManipulationAffective  #FakeAmour  #Alert",
    },
    {
        "num": 9,
        "folder": "script_09_toxique_deteste",
        "icon": ">>",
        "colors": ("#E65100", "#4A148C"),
        "title": "3 CHOSES QU'UN\nMANIPULATEUR\nDETESTE",
        "hook": "Pour enerver\nun toxique ?\nFais exactement ca.",
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
        "cta": "Like si tu\nvas tester ca.\nCommente ton power move.",
        "hashtags": "#AntiToxique  #Empowerment  #NoContact",
    },
    {
        "num": 10,
        "folder": "script_10_verites_2026",
        "icon": "26",
        "colors": ("#006064", "#4527A0"),
        "title": "3 VERITES\nINCONFORTABLES\nRELATIONS 2026",
        "hook": "Amour 2026 :\n3 verites que\npersonne n'ose dire.",
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
        "cta": "Like si t'es d'accord.\nPartage pour reveiller\nl'algorithme.",
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
    """Fast vertical gradient: create 1-pixel-wide column then resize."""
    pixels = [blend(c1, c2, y / max(h - 1, 1)) for y in range(h)]
    col = Image.new("RGB", (1, h))
    col.putdata(pixels)
    return col.resize((w, h), Image.NEAREST)


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        try:
            return ImageFont.truetype(FONT_BOLD, size)
        except Exception:
            return ImageFont.load_default()


def measure_text(draw, text, font):
    try:
        bb = draw.textbbox((0, 0), text, font=font)
        return bb[2] - bb[0], bb[3] - bb[1]
    except Exception:
        return len(text) * max(font.size // 2, 6), font.size


def draw_text_block(draw, lines_text, cx, y, font, color=(255, 255, 255),
                    max_w=940, line_gap=1.35, shadow=True):
    """Draw pre-split lines of text centered around cx, returns new y."""
    lines = []
    for raw in lines_text.split("\n"):
        lines.append(raw)

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
    """Draw a rounded-rectangle pill with text, returns bottom y."""
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


# ─── Slide 1: Hook ────────────────────────────────────────────────────────────

def slide_hook(s):
    c1 = rgb(s["colors"][0])
    c2 = rgb(s["colors"][1])
    img = gradient_img(c1, c2)
    draw = ImageDraw.Draw(img)

    # Decorative blobs
    dc = lighten(blend(c1, c2, 0.3), 0.18)
    draw.ellipse([(-120, -120), (380, 380)], fill=dc)
    draw.ellipse([(750, 1650), (1250, 2100)], fill=darken(c2, 0.2))
    draw.ellipse([(820, 80), (1150, 410)], fill=lighten(c2, 0.12))

    # Script tag pill
    f_tag = load_font(FONT_BOLD, 38)
    tag_text = f"SCRIPT {s['num']:02d} / 10"
    draw_pill(draw, tag_text, W // 2, 110,
              font=f_tag, bg=(255, 255, 255, 220) if False else (255, 255, 255),
              fg=darken(c1, 0.1))

    # Title
    f_title = load_font(FONT_IMPACT, 82)
    y = 230
    y = draw_text_block(draw, s["title"], W // 2, y, f_title, (255, 255, 255), shadow=True)

    # Divider
    y += 30
    draw_divider(draw, y, color=lighten(c2, 0.5), width=4)
    y += 50

    # Hook text
    f_hook = load_font(FONT_BOLD, 64)
    y = draw_text_block(draw, s["hook"], W // 2, y, f_hook, (255, 255, 255), shadow=True)

    # Big icon / label in lower area
    y = max(y + 60, H - 480)
    f_icon = load_font(FONT_IMPACT, 220)
    icon_color = lighten(blend(c1, (255, 255, 255), 0.1), 0.15)
    iw, ih = measure_text(draw, s["icon"], f_icon)
    draw.text((W // 2 - iw // 2 + 4, y + 4), s["icon"], font=f_icon, fill=(0, 0, 0))
    draw.text((W // 2 - iw // 2, y), s["icon"], font=f_icon, fill=icon_color)

    # Bottom bar
    bar_top = H - 120
    bar_col = darken(c2, 0.4)
    draw.rectangle([(0, bar_top), (W, H)], fill=bar_col)
    f_bar = load_font(FONT_BOLD, 40)
    bar_text = "Like  |  Commente  |  Sauvegarde"
    bw, bh = measure_text(draw, bar_text, f_bar)
    draw.text((W // 2 - bw // 2, bar_top + (120 - bh) // 2), bar_text,
              font=f_bar, fill=(255, 255, 255))

    return img


# ─── Slides 2-4: Points ───────────────────────────────────────────────────────

def slide_point(s, idx):
    c1 = rgb(s["colors"][0])
    c2 = rgb(s["colors"][1])
    # Alternate gradient direction for variety
    if idx % 2 == 0:
        img = gradient_img(darken(c2, 0.3), darken(c1, 0.2))
    else:
        img = gradient_img(darken(c1, 0.3), darken(c2, 0.2))
    draw = ImageDraw.Draw(img)

    num = idx + 1
    title, desc = s["points"][idx]

    # Huge background number (decorative)
    f_bg_num = load_font(FONT_IMPACT, 600)
    bg_num_str = str(num)
    bnw, bnh = measure_text(draw, bg_num_str, f_bg_num)
    bg_num_col = lighten(blend(c1, c2, 0.5), 0.12)
    draw.text((W // 2 - bnw // 2, H // 2 - bnh // 2 - 60),
              bg_num_str, font=f_bg_num, fill=bg_num_col)

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

    # Progress bar at bottom
    bar_top = H - 110
    draw.rectangle([(0, bar_top), (W, H)], fill=darken(c2, 0.5))
    f_prog = load_font(FONT_BOLD, 38)
    filled = chr(9679)  # ●
    empty  = chr(9675)  # ○
    prog_str = (filled * num) + (empty * (3 - num)) + f"   Slide {num + 1} / 5"
    pw, ph = measure_text(draw, prog_str, f_prog)
    draw.text((W // 2 - pw // 2, bar_top + (110 - ph) // 2),
              prog_str, font=f_prog, fill=(210, 210, 210))

    return img


# ─── Slide 5: CTA ─────────────────────────────────────────────────────────────

def slide_cta(s):
    c1 = rgb(s["colors"][1])   # reversed colors for CTA
    c2 = rgb(s["colors"][0])
    img = gradient_img(c1, c2)
    draw = ImageDraw.Draw(img)

    # Decorative shapes
    dc = lighten(blend(c1, c2, 0.4), 0.2)
    draw.ellipse([(-150, 200), (450, 800)], fill=dc)
    draw.ellipse([(700, 1200), (1350, 1850)], fill=darken(c2, 0.2))

    # "MAINTENANT" header
    f_head = load_font(FONT_IMPACT, 90)
    y = 140
    y = draw_text_block(draw, "FAIS-LE\nMAINTENANT !", W // 2, y, f_head,
                        (255, 255, 255), shadow=True)

    # Divider
    y += 35
    draw_divider(draw, y, color=lighten(c2, 0.5), width=4)
    y += 55

    # CTA text
    f_cta = load_font(FONT_BOLD, 58)
    y = draw_text_block(draw, s["cta"], W // 2, y, f_cta, (255, 255, 255), shadow=True)

    y += 70

    # Action buttons
    actions = ["LIKE", "COMMENTE", "SAUVEGARDE"]
    btn_w = 280
    btn_h = 110
    gap = 30
    total_w = len(actions) * btn_w + (len(actions) - 1) * gap
    bx = (W - total_w) // 2

    for action in actions:
        btn_bg = lighten(blend(c1, c2, 0.5), 0.25)
        draw.rounded_rectangle([(bx, y), (bx + btn_w, y + btn_h)],
                                radius=22, fill=btn_bg)
        f_btn = load_font(FONT_BOLD, 38)
        tw, th = measure_text(draw, action, f_btn)
        draw.text((bx + (btn_w - tw) // 2, y + (btn_h - th) // 2),
                  action, font=f_btn, fill=(255, 255, 255))
        bx += btn_w + gap

    y += btn_h + 60

    # Hashtags
    f_hash = load_font(FONT_REG, 38)
    hash_col = lighten(blend(c1, c2, 0.3), 0.45)
    y = draw_text_block(draw, s["hashtags"], W // 2, y, f_hash,
                        hash_col, shadow=False)

    # Follow CTA
    f_follow = load_font(FONT_BOLD, 36)
    follow_text = "Suis pour plus de contenu psy"
    fw, _ = measure_text(draw, follow_text, f_follow)
    draw.text((W // 2 - fw // 2, H - 100), follow_text,
              font=f_follow, fill=(210, 210, 210))

    return img


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total = 0

    for s in SCRIPTS:
        folder = os.path.join(OUTPUT_DIR, s["folder"])
        os.makedirs(folder, exist_ok=True)
        print(f"  [{s['num']:02d}/10] {s['folder']}")

        slide_hook(s).save(os.path.join(folder, "slide_01_hook.png"), "PNG")
        for i in range(3):
            slide_point(s, i).save(
                os.path.join(folder, f"slide_0{i + 2}_point{i + 1}.png"), "PNG"
            )
        slide_cta(s).save(os.path.join(folder, "slide_05_cta.png"), "PNG")

        total += 5
        print(f"         5 slides saved OK")

    print(f"\nDone! {total} images in '{OUTPUT_DIR}/'")


if __name__ == "__main__":
    main()
