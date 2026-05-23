import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(
    page_title="Angela Parrado - Stage & Production Management",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""<style>
#MainMenu,header[data-testid="stHeader"],footer,.stDeployButton,
[data-testid="stSidebar"],[data-testid="stToolbar"],
[data-testid="stDecoration"],[data-testid="stStatusWidget"]{display:none!important}
.stApp,.main,.block-container{padding:0!important;margin:0!important;max-width:100%!important;background:#0a0a0a!important}
.stVerticalBlock,.element-container,div[data-testid="stMarkdownContainer"]{padding:0!important;margin:0!important}
iframe{
    position:fixed!important;
    top:0!important;left:0!important;
    width:100vw!important;height:100vh!important;
    border:none!important;display:block!important;
    z-index:999999!important;
}
</style>""", unsafe_allow_html=True)


def _font_b64(filename):
    base = os.path.dirname(os.path.abspath(__file__))
    for p in [
        os.path.join(base, "fonts", filename),
        os.path.join(base, filename),
        os.path.join(r"C:\Users\USER\Downloads", filename),
    ]:
        if os.path.exists(p):
            with open(p, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
    return None


_lr  = _font_b64("Lora-Regular.ttf")
_lb  = _font_b64("Lora-Bold.ttf")
_li  = _font_b64("Lora-Italic.ttf")
_lbi = _font_b64("Lora-BoldItalic.ttf")

# Build only the font-face block as an f-string (isolated, safe)
_font_face = ""
if _lr:
    _font_face += f"@font-face{{font-family:'Lora';src:url('data:font/truetype;base64,{_lr}') format('truetype');font-weight:400;font-style:normal;font-display:swap}}\n"
if _lb:
    _font_face += f"@font-face{{font-family:'Lora';src:url('data:font/truetype;base64,{_lb}') format('truetype');font-weight:700;font-style:normal;font-display:swap}}\n"
if _li:
    _font_face += f"@font-face{{font-family:'Lora';src:url('data:font/truetype;base64,{_li}') format('truetype');font-weight:400;font-style:italic;font-display:swap}}\n"
if _lbi:
    _font_face += f"@font-face{{font-family:'Lora';src:url('data:font/truetype;base64,{_lbi}') format('truetype');font-weight:700;font-style:italic;font-display:swap}}\n"

# ── EXACT original HTML ── only changes:
#   1. Goudy @font-face (local OTF) → Google Fonts import + rename to 'Goudy Bookletter 1911'
#   2. Lora @font-face local URLs  → __LORA_FONTS__ placeholder (replaced below)
#   3. Every 'Goudy Bookletter' reference → 'Goudy Bookletter 1911'
HTML = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stage & Production Management</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Goudy+Bookletter+1911&display=swap" rel="stylesheet">
    <style>
        __LORA_FONTS__

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --orange: #ff6b35;
            --orange-light: #ff8c61;
            --orange-dark: #e85a2a;
            --yellow: #ffa500;
            --accent: #ffb347;
            --black: #0a0a0a;
            --dark: #1a1a1a;
            --white: #ffffff;
            --gray: #9ca3af;
            --gray-light: #d1d5db;
        }

        body {
            font-family: 'Lora', serif;
            background: var(--black);
            color: var(--white);
            overflow-x: hidden;
            line-height: 1.8;
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Goudy Bookletter 1911', serif;
            font-weight: normal;
            letter-spacing: -0.5px;
        }

        .section-title,
        .hero h1,
        .service-card h3,
        .about-text h3,
        .project-card h5,
        .cta-section h2,
        .logo {
            font-family: 'Goudy Bookletter 1911', serif;
            font-weight: normal;
            letter-spacing: -1px;
        }

        .hero h1 {
            font-size: 7rem !important;
            font-weight: normal;
        }

        .section-title {
            font-size: 5rem !important;
            font-weight: normal;
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(40px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-40px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-60px); }
            to   { opacity: 1; transform: translateX(0); }
        }

        @keyframes scaleIn {
            from { opacity: 0; transform: scale(0.9); }
            to   { opacity: 1; transform: scale(1); }
        }

        @keyframes shimmer {
            0%   { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50%       { transform: translateY(-15px); }
        }

        @keyframes gradientMove {
            0%   { background-position: 0% 50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .background-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 0;
            background:
                radial-gradient(circle at 20% 30%, rgba(255, 107, 53, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(255, 140, 97, 0.08) 0%, transparent 50%);
        }

        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            padding: 30px 60px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
            background: rgba(10, 10, 10, 0.85);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 107, 53, 0.15);
            animation: fadeInDown 0.8s ease;
        }

        .logo {
            font-size: 1.3rem;
            font-weight: 700;
            letter-spacing: -0.5px;
            color: var(--white);
        }

        .nav-links {
            display: flex;
            gap: 50px;
            list-style: none;
        }

        .nav-links a {
            color: var(--gray);
            text-decoration: none;
            font-weight: 500;
            font-size: 0.95rem;
            position: relative;
            transition: color 0.3s;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -6px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--orange);
            transition: width 0.3s ease;
        }

        .nav-links a:hover { color: var(--white); }
        .nav-links a:hover::after { width: 100%; }

        .hero {
            min-height: 100vh;
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            gap: 80px;
            padding: 140px 60px 80px;
            position: relative;
            max-width: 1400px;
            margin: 0 auto;
        }

        .hero-content {
            position: relative;
            z-index: 2;
        }

        .hero-animation {
            position: relative;
            height: 600px;
            display: flex;
            align-items: center;
            justify-content: center;
            perspective: 1000px;
        }

        .stage-animation {
            position: relative;
            width: 500px;
            height: 400px;
            transform-style: preserve-3d;
            animation: stageEntry 1.5s ease-out;
        }

        @keyframes stageEntry {
            from { opacity: 0; transform: scale(0.8); }
            to   { opacity: 1; transform: scale(1); }
        }

        .stage-platform {
            position: absolute;
            width: 400px;
            height: 40px;
            background: linear-gradient(180deg, rgba(255, 107, 53, 0.3), rgba(255, 107, 53, 0.1));
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%) rotateX(60deg);
            border-radius: 8px;
            box-shadow: 0 20px 40px rgba(255, 107, 53, 0.4);
            animation: platformFadeIn 1s ease-out 0.3s backwards;
        }

        @keyframes platformFadeIn {
            from { opacity: 0; transform: translateX(-50%) rotateX(60deg) translateY(20px); }
            to   { opacity: 1; transform: translateX(-50%) rotateX(60deg) translateY(0); }
        }

        .spotlight {
            position: absolute;
            width: 3px;
            background: linear-gradient(180deg, rgba(255, 140, 97, 0.8), transparent);
            transform-origin: top center;
            animation: spotlight-sweep 4s ease-in-out infinite, spotlightFadeIn 1s ease-out backwards;
        }

        .spotlight-1 { height: 250px; left: 20%; top: 0; animation-delay: 0s,  0.5s; }
        .spotlight-2 { height: 280px; left: 40%; top: 0; animation-delay: 1s,  0.6s; }
        .spotlight-3 { height: 300px; left: 60%; top: 0; animation-delay: 2s,  0.7s; }
        .spotlight-4 { height: 280px; left: 80%; top: 0; animation-delay: 3s,  0.8s; }

        @keyframes spotlightFadeIn {
            from { opacity: 0; }
            to   { opacity: 0.6; }
        }

        @keyframes spotlight-sweep {
            0%, 100% { transform: rotate(-15deg); opacity: 0.6; }
            50%       { transform: rotate(15deg);  opacity: 1;   }
        }

        .sound-particle {
            position: absolute;
            width: 8px;
            height: 8px;
            background: var(--orange-light);
            border-radius: 50%;
            opacity: 0;
            animation: particle-float 3s ease-in-out infinite;
        }

        .sound-particle:nth-child(6)  { left: 30%; bottom: 150px; animation-delay: 1s;   }
        .sound-particle:nth-child(7)  { left: 50%; bottom: 150px; animation-delay: 1.5s; }
        .sound-particle:nth-child(8)  { left: 70%; bottom: 150px; animation-delay: 2s;   }
        .sound-particle:nth-child(9)  { left: 40%; bottom: 150px; animation-delay: 2.5s; }
        .sound-particle:nth-child(10) { left: 60%; bottom: 150px; animation-delay: 3s;   }

        @keyframes particle-float {
            0%   { transform: translateY(0) scale(0);    opacity: 0;   }
            10%  { opacity: 1; }
            90%  { opacity: 0.8; }
            100% { transform: translateY(-200px) scale(1.5); opacity: 0; }
        }

        .stage-glow {
            position: absolute;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at center, rgba(255, 107, 53, 0.2), transparent 60%);
            animation: glow-pulse 3s ease-in-out infinite;
        }

        @keyframes glow-pulse {
            0%, 100% { opacity: 0.5; transform: scale(1);   }
            50%       { opacity: 1;   transform: scale(1.1); }
        }

        .animation-label {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--orange-light);
            text-transform: uppercase;
            letter-spacing: 2px;
            animation: fadeInUp 1s ease-out 1s backwards;
        }

        .hero-label {
            display: inline-block;
            padding: 10px 24px;
            background: rgba(255, 107, 53, 0.15);
            border: 1px solid rgba(255, 107, 53, 0.3);
            border-radius: 50px;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 35px;
            color: var(--orange-light);
            animation: fadeInUp 0.8s ease 0.2s backwards;
        }

        .hero h1 {
            font-size: 6.5rem;
            font-weight: 800;
            line-height: 1.05;
            letter-spacing: -3px;
            margin-bottom: 35px;
            animation: fadeInUp 0.8s ease 0.4s backwards;
        }

        .hero h1 .gradient-text {
            background: linear-gradient(135deg, var(--orange) 0%, var(--accent) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-description {
            font-size: 1.4rem;
            color: var(--gray);
            max-width: 700px;
            margin-bottom: 50px;
            line-height: 1.7;
            font-weight: 400;
            animation: fadeInUp 0.8s ease 0.6s backwards;
        }

        .hero-buttons {
            display: flex;
            gap: 20px;
            animation: fadeInUp 0.8s ease 0.8s backwards;
        }

        .btn {
            padding: 18px 40px;
            border-radius: 12px;
            font-size: 1rem;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.15);
            transform: translate(-50%, -50%);
            transition: width 0.5s, height 0.5s;
        }

        .btn:hover::before { width: 400px; height: 400px; }

        .btn span { position: relative; z-index: 1; }

        .btn-primary {
            background: var(--orange);
            color: var(--white);
            box-shadow: 0 10px 40px rgba(255, 107, 53, 0.3);
        }

        .btn-primary:hover {
            background: var(--orange-dark);
            transform: translateY(-3px);
            box-shadow: 0 15px 50px rgba(255, 107, 53, 0.5);
        }

        .btn-secondary {
            background: var(--orange);
            color: var(--white);
            box-shadow: 0 10px 40px rgba(255, 107, 53, 0.3);
        }

        .btn-secondary:hover {
            background: var(--orange-dark);
            transform: translateY(-3px);
            box-shadow: 0 15px 50px rgba(255, 107, 53, 0.5);
        }

        .btn-outline {
            background: transparent;
            color: var(--white);
            border: 2px solid rgba(255, 107, 53, 0.5);
        }

        .btn-outline:hover {
            border-color: var(--orange);
            background: rgba(255, 107, 53, 0.1);
            transform: translateY(-3px);
        }

        .section {
            padding: 120px 60px;
            position: relative;
        }

        .section-header {
            text-align: center;
            margin-bottom: 90px;
        }

        .section-label {
            color: var(--orange-light);
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 3px;
            margin-bottom: 20px;
        }

        .section-title {
            font-size: 4.5rem;
            font-weight: 800;
            margin-bottom: 25px;
            letter-spacing: -2px;
            line-height: 1.1;
        }

        .section-subtitle {
            font-size: 1.3rem;
            color: var(--gray);
            max-width: 750px;
            margin: 0 auto;
            line-height: 1.7;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 35px;
            max-width: 1300px;
            margin: 0 auto;
        }

        .service-card {
            background: rgba(255, 107, 53, 0.04);
            padding: 50px 40px;
            border-radius: 24px;
            border: 1px solid rgba(255, 107, 53, 0.15);
            transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
            position: relative;
            overflow: hidden;
        }

        .service-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: linear-gradient(135deg, var(--orange), var(--accent));
            opacity: 0;
            transition: opacity 0.5s;
        }

        .service-card:hover {
            transform: translateY(-12px) scale(1.02);
            border-color: var(--orange);
            box-shadow: 0 25px 60px rgba(255, 107, 53, 0.35);
        }

        .service-card:hover::before { opacity: 0.08; }

        .service-number {
            font-size: 4rem;
            font-weight: 800;
            color: rgba(255, 107, 53, 0.2);
            margin-bottom: 20px;
            position: relative;
            z-index: 1;
        }

        .service-card h3 {
            font-size: 1.8rem;
            margin-bottom: 18px;
            font-weight: 700;
            position: relative;
            z-index: 1;
        }

        .service-card p {
            color: var(--gray);
            line-height: 1.8;
            font-size: 1.05rem;
            position: relative;
            z-index: 1;
        }

        .btn-download {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin-top: 25px;
            padding: 12px 24px;
            background: transparent;
            border: 1px solid rgba(255, 107, 53, 0.5);
            border-radius: 10px;
            color: var(--orange-light);
            font-family: 'Lora', serif;
            font-size: 0.9rem;
            font-weight: 600;
            text-decoration: none;
            position: relative;
            z-index: 1;
            transition: all 0.3s;
        }

        .btn-download:hover {
            background: rgba(255, 107, 53, 0.15);
            border-color: var(--orange);
            color: var(--white);
            transform: translateY(-2px);
        }

        .btn-download svg {
            flex-shrink: 0;
        }

        .about-section {
            background: var(--dark);
            padding: 120px 60px;
        }

        .about-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 80px;
            align-items: start;
        }

        .about-text h3 {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 30px;
            letter-spacing: -1px;
            line-height: 1.1;
        }

        .about-text p {
            font-size: 1.15rem;
            line-height: 1.85;
            color: var(--gray);
            margin-bottom: 25px;
        }

        .about-highlights {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-top: 40px;
        }

        .highlight-item {
            background: rgba(255, 107, 53, 0.08);
            padding: 25px;
            border-radius: 16px;
            border: 1px solid rgba(255, 107, 53, 0.2);
            transition: all 0.3s;
        }

        .highlight-item:hover {
            background: rgba(255, 107, 53, 0.15);
            transform: translateY(-3px);
        }

        .highlight-item h4 {
            font-size: 1.2rem;
            margin-bottom: 8px;
            font-weight: 600;
            color: var(--orange-light);
        }

        .highlight-item p {
            font-size: 0.95rem;
            color: var(--gray);
            margin: 0;
        }

        .about-right-col {
            display: flex;
            flex-direction: column;
            gap: 20px;
            min-width: 0;
        }

        .about-image {
            height: 750px;
            border-radius: 24px;
            overflow: hidden;
            position: relative;
            flex-shrink: 0;
        }

        .about-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center center;
            display: block;
        }

        .about-video-wrapper {
            width: 100%;
            min-width: 0;
        }

        .about-video-label {
            font-size: 0.78rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--orange-light);
            margin-bottom: 12px;
        }

        .video-container {
            position: relative;
            width: 100%;
            max-width: 100%;
            padding-bottom: 56.25%;
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid rgba(255, 107, 53, 0.2);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5);
            cursor: pointer;
        }

        .video-container img.video-thumb {
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.4s;
        }

        .video-container:hover img.video-thumb {
            transform: scale(1.03);
        }

        .play-btn {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            width: 72px; height: 72px;
            background: rgba(255, 107, 53, 0.92);
            border: none;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 2;
            transition: all 0.3s;
            box-shadow: 0 6px 30px rgba(255, 107, 53, 0.5);
        }

        .video-container:hover .play-btn {
            background: var(--orange);
            transform: translate(-50%, -50%) scale(1.12);
        }

        .play-btn svg {
            width: 28px; height: 28px;
            fill: white;
            margin-left: 5px;
        }

        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
            display: block;
        }

        .gallery-section {
            background: var(--dark);
            padding: 120px 60px;
        }

        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-auto-rows: 280px;
            gap: 30px;
            max-width: 1300px;
            margin: 0 auto;
        }

        .gallery-item {
            position: relative;
            border-radius: 20px;
            overflow: hidden;
            cursor: pointer;
            background: linear-gradient(135deg, rgba(255, 107, 53, 0.2), rgba(255, 140, 97, 0.2));
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .gallery-item:nth-child(1) { grid-column: span 2; grid-row: span 2; }
        .gallery-item:nth-child(2) { grid-column: span 1; grid-row: span 1; }
        .gallery-item:nth-child(3) { grid-column: span 1; grid-row: span 1; }

        .gallery-item::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(180deg, transparent 30%, rgba(0, 0, 0, 0.9) 100%);
            opacity: 0;
            transition: opacity 0.4s;
            z-index: 1;
        }

        .gallery-item:hover {
            transform: scale(1.05);
            box-shadow: 0 30px 60px rgba(255, 107, 53, 0.5);
            z-index: 10;
        }

        .gallery-item:hover::before { opacity: 1; }

        .gallery-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 30px;
            transform: translateY(100%);
            transition: transform 0.4s;
            z-index: 2;
        }

        .gallery-item:hover .gallery-overlay { transform: translateY(0); }

        .gallery-overlay h4 {
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 8px;
        }

        .gallery-overlay p {
            font-size: 0.9rem;
            color: var(--gray-light);
        }

        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .experience-section {
            background: linear-gradient(180deg, var(--black) 0%, var(--dark) 50%, var(--black) 100%);
        }

        .project-cards {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .project-card {
            background: rgba(255, 107, 53, 0.05);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid rgba(255, 107, 53, 0.2);
            transition: all 0.4s;
            position: relative;
            overflow: hidden;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(90deg, var(--orange), var(--accent));
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.4s;
        }

        .project-card:hover {
            background: rgba(255, 107, 53, 0.12);
            border-color: var(--orange);
            transform: translateY(-10px);
            box-shadow: 0 20px 50px rgba(255, 107, 53, 0.3);
        }

        .project-card:hover::before { transform: scaleX(1); }

        .project-card h5 {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 15px;
        }

        .project-card p {
            color: var(--gray);
            line-height: 1.7;
            font-size: 1.05rem;
            margin-bottom: 20px;
        }

        .project-meta {
            display: flex;
            gap: 20px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 107, 53, 0.15);
        }

        .meta-item { display: flex; flex-direction: column; }

        .meta-label {
            font-size: 0.8rem;
            color: var(--gray);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 5px;
        }

        .meta-value {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--orange-light);
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 35px;
            max-width: 1300px;
            margin: 0 auto;
        }

        .testimonial-card {
            background: rgba(255, 107, 53, 0.04);
            backdrop-filter: blur(10px);
            padding: 45px;
            border-radius: 24px;
            border: 1px solid rgba(255, 107, 53, 0.15);
            transition: all 0.4s;
        }

        .testimonial-card:hover {
            transform: translateY(-10px);
            border-color: var(--orange);
            box-shadow: 0 20px 50px rgba(255, 107, 53, 0.25);
        }

        .quote-mark {
            font-size: 4rem;
            color: var(--orange);
            opacity: 0.25;
            line-height: 1;
            margin-bottom: 20px;
            font-family: Georgia, serif;
        }

        .testimonial-text {
            font-size: 1.15rem;
            line-height: 1.8;
            color: var(--gray);
            margin-bottom: 30px;
        }

        .testimonial-author {
            font-weight: 700;
            color: var(--orange-light);
            font-size: 0.95rem;
        }

        .cta-section {
            padding: 150px 60px;
            text-align: center;
            position: relative;
            background: linear-gradient(135deg, rgba(255, 107, 53, 0.08), rgba(255, 140, 97, 0.08));
        }

        .cta-section h2 {
            font-size: 5.5rem;
            font-weight: 800;
            margin-bottom: 30px;
            line-height: 1.15;
            letter-spacing: -2px;
        }

        .cta-section p {
            font-size: 1.5rem;
            color: var(--gray);
            margin-bottom: 55px;
        }

        .cta-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
        }

        footer {
            padding: 80px 60px 50px;
            text-align: center;
            border-top: 1px solid rgba(255, 107, 53, 0.15);
        }

        .footer-logo {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 30px;
            letter-spacing: -1px;
        }

        footer p {
            color: var(--gray);
            margin-bottom: 12px;
            font-size: 0.95rem;
        }

        .reveal {
            opacity: 0;
            transform: translateY(60px);
            transition: all 1s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }

        @media (max-width: 1200px) {
            .hero { grid-template-columns: 1fr; gap: 60px; }
            .hero h1 { font-size: 5rem; }

            .services-grid { grid-template-columns: repeat(2, 1fr); }

            .about-content { grid-template-columns: 1fr; gap: 50px; }
            .about-image { min-height: 350px; }

            .gallery-grid {
                grid-template-columns: repeat(2, 1fr);
                grid-auto-rows: 250px;
            }

            .gallery-item:nth-child(1),
            .gallery-item:nth-child(2),
            .gallery-item:nth-child(3) {
                grid-column: span 1;
                grid-row: span 1;
            }

            .project-cards { grid-template-columns: 1fr; }
        }

        @media (max-width: 768px) {
            nav { padding: 25px 30px; }
            .nav-links { display: none; }

            .hero { padding: 120px 30px 60px; }
            .hero h1 { font-size: 3.5rem; }

            .section { padding: 80px 30px; }
            .about-section { padding: 80px 30px; }
            .about-text h3 { font-size: 2.2rem; }
            .about-highlights { grid-template-columns: 1fr; }

            .section-title { font-size: 3rem; }

            .services-grid,
            .testimonials-grid,
            .gallery-grid { grid-template-columns: 1fr; }

            .gallery-grid { grid-auto-rows: 250px; }

            .cta-section h2 { font-size: 3rem; }

            .hero-buttons,
            .cta-buttons { flex-direction: column; }
        }
    </style>
</head>
<body>
    <div class="background-overlay"></div>

    <nav>
        <div class="logo">Angela Parrado</div>
        <ul class="nav-links">
            <li><a href="#servicios">Servicios</a></li>
            <li><a href="#sobre-mi">Sobre m&#237;</a></li>
            <li><a href="#galeria">Galer&#237;a</a></li>
            <li><a href="#experiencia">Experiencia</a></li>
            <li><a href="#testimonios">Testimonios</a></li>
            <li><a href="#contacto">Contacto</a></li>
        </ul>
    </nav>

    <section class="hero">
        <div class="hero-content">
            <div class="hero-label">Stage &amp; Production Management</div>
            <h1>Eventos que <span class="gradient-text">transforman</span> experiencias</h1>
            <p class="hero-description">Producci&#243;n integral, stage management y equipos profesionales. Creando momentos memorables con precisi&#243;n y pasi&#243;n.</p>
            <div class="hero-buttons">
                <a href="#contacto" class="btn btn-primary"><span>Comenzar proyecto</span></a>
                <a href="#servicios" class="btn btn-outline"><span>Explorar servicios</span></a>
            </div>
        </div>

        <div class="hero-animation">
            <div class="stage-animation">
                <div class="stage-glow"></div>
                <div class="spotlight spotlight-1"></div>
                <div class="spotlight spotlight-2"></div>
                <div class="spotlight spotlight-3"></div>
                <div class="spotlight spotlight-4"></div>
                <div class="sound-particle"></div>
                <div class="sound-particle"></div>
                <div class="sound-particle"></div>
                <div class="sound-particle"></div>
                <div class="sound-particle"></div>
                <div class="stage-platform"></div>
            </div>
            <div class="animation-label">Stage Production</div>
        </div>
    </section>

    <section class="section reveal" id="servicios">
        <div class="section-header">
            <div class="section-label">Servicios</div>
            <h2 class="section-title">Lo que hago</h2>
            <p class="section-subtitle">Soluciones completas para eventos inolvidables. De la conceptualizaci&#243;n a la ejecuci&#243;n perfecta.</p>
        </div>

        <div class="services-grid">
            <div class="service-card">
                <div class="service-number">01</div>
                <h3>Stage Management</h3>
                <p>Coordinaci&#243;n completa del escenario. Timing perfecto, gesti&#243;n de artistas y resoluci&#243;n instant&#225;nea de cualquier situaci&#243;n.</p>
            </div>

            <div class="service-card">
                <div class="service-number">02</div>
                <h3>Producci&#243;n de Eventos</h3>
                <p>De la idea a la realidad. Log&#237;stica integral, coordinaci&#243;n de equipos y gesti&#243;n completa para eventos impecables.</p>
            </div>

            <div class="service-card">
                <div class="service-number">03</div>
                <h3>Alquiler de Equipos</h3>
                <p>Audio, infraestructura e iluminaci&#243;n profesional para eventos de alto impacto.</p>
                <a href="PABOLPRODUCCIONES.pdf" target="_blank" rel="noopener noreferrer" class="btn-download">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                        <polyline points="7 10 12 15 17 10"/>
                        <line x1="12" y1="15" x2="12" y2="3"/>
                    </svg>
                    Cat&#225;logo PABOL PRODUCCIONES
                </a>
            </div>
        </div>
    </section>

    <section class="about-section reveal" id="sobre-mi">
        <div class="section-header">
            <div class="section-label">Sobre m&#237;</div>
            <h2 class="section-title">Qui&#233;n soy</h2>
            <p class="section-subtitle">Pasi&#243;n por los eventos y dedicaci&#243;n en cada proyecto.</p>
        </div>

        <div class="about-content">
            <div class="about-text">
                <h3>Productora de eventos con visi&#243;n integral</h3>
                <p>Desde muy peque&#241;a tuve un acercamiento a este entorno gracias a la empresa de producci&#243;n de eventos de mis padres, lo que me permiti&#243; crecer viendo de cerca c&#243;mo se construyen las experiencias detr&#225;s de un evento. Poco a poco empec&#233; a involucrarme en diferentes producciones, primero desde espacios peque&#241;os y luego en escenarios m&#225;s grandes, descubriendo todo lo que ocurre detr&#225;s de la tarima para que un evento funcione correctamente.</p>
                <p>Con el tiempo entend&#237; que lo que m&#225;s me apasiona es el stage management, la coordinaci&#243;n t&#233;cnica y la din&#225;mica de trabajo que ocurre en tiempo real durante un evento en vivo. Me gusta la precisi&#243;n, el manejo de los tiempos, la comunicaci&#243;n entre equipos y la resoluci&#243;n de imprevistos bajo presi&#243;n.</p>
                <p>Actualmente me encuentro enfocando mi proceso hacia los escenarios en vivo y la log&#237;stica de eventos, mientras desarrollo Expreso Social, un proyecto enfocado en crear experiencias m&#225;s cercanas y aut&#233;nticas entre artistas emergentes y su p&#250;blico.</p>

                <div class="about-highlights">
                    <div class="highlight-item">
                        <h4>Velocidad</h4>
                        <p>Resoluci&#243;n instant&#225;nea bajo presi&#243;n</p>
                    </div>
                    <div class="highlight-item">
                        <h4>Versatilidad</h4>
                        <p>Conciertos, corporativos, privados e iglesias</p>
                    </div>
                    <div class="highlight-item">
                        <h4>Organizaci&#243;n</h4>
                        <p>Metodolog&#237;a rigurosa y detallada</p>
                    </div>
                    <div class="highlight-item">
                        <h4>Pasi&#243;n</h4>
                        <p>Amo la adrenalina de eventos en vivo</p>
                    </div>
                </div>
            </div>

            <div class="about-right-col">
                <div class="about-image">
                    <img src="https://im.vsco.co/aws-us-west-2/0a6aa5/136624836/6a0f9681029435f53f3ae4c4/vsco_052126.jpg?w=1600" alt="Sobre m&#237;">
                </div>

                <div class="about-video-wrapper">
                    <div class="about-video-label">Con&#243;ceme en 60 segundos</div>
                    <div class="video-container" onclick="loadVideo(this)" data-src="https://www.youtube.com/embed/FZPmelh2-2o?autoplay=1">
                        <img class="video-thumb" src="https://img.youtube.com/vi/FZPmelh2-2o/maxresdefault.jpg" alt="Ver pitch de presentaci&#243;n">
                        <button class="play-btn" aria-label="Reproducir video">
                            <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="gallery-section reveal" id="galeria">
        <div class="section-header">
            <div class="section-label">Galer&#237;a</div>
            <h2 class="section-title">Momentos capturados</h2>
            <p class="section-subtitle">Un vistazo a algunos de los eventos que he producido.</p>
        </div>

        <div class="gallery-grid">
            <div class="gallery-item">
                <img src="https://im.vsco.co/aws-us-west-2/0a6aa5/136624836/6a0fc92772d377d0e5a8c23e/vsco_052126.jpg?w=1600" alt="Evento Nacional Principal">
                <div class="gallery-overlay">
                    <h4>Lanzamiento Expreso Social</h4>
                    <p>Producci&#243;n completa con artistas reconocidos</p>
                </div>
            </div>
            <div class="gallery-item">
                <img src="https://im.vsco.co/aws-us-west-2/0a6aa5/136624836/6a0fc7f90d87a9ea47de49ca/vsco_052126.jpg?w=1600" alt="Stage Setup">
                <div class="gallery-overlay">
                    <h4>Stage Setup</h4>
                    <p>Montaje t&#233;cnico profesional</p>
                </div>
            </div>
            <div class="gallery-item">
                <img src="https://im.vsco.co/aws-us-west-2/0a6aa5/136624836/6a10e0f3acf4897c57d5d875/vsco_052226.jpg?w=1600" alt="Control T&#233;cnico">
                <div class="gallery-overlay">
                    <h4>Control T&#233;cnico</h4>
                    <p>Coordinaci&#243;n en tiempo real</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section experience-section reveal" id="experiencia">
        <div class="section-header">
            <div class="section-label">Experiencia</div>
            <h2 class="section-title">Proyectos destacados</h2>
            <p class="section-subtitle">5 meses de experiencia produciendo eventos memorables con resultados excepcionales.</p>
        </div>
        <div class="project-cards">
            <div class="project-card">
                <h5>Expreso social</h5>
                <span class="meta-value">Co-creadora y Producci&#243;n de Eventos</span>
                <div class="project-meta">
                    <div class="meta-item">
                        <p>Expreso Social es una promotora de eventos creada junto a otras dos personas, enfocada en desarrollar experiencias m&#225;s cercanas y conscientes entre artistas emergentes y su p&#250;blico. Dentro del proyecto participo en la planeaci&#243;n y producci&#243;n de eventos, apoyando procesos log&#237;sticos, coordinaci&#243;n general y desarrollo creativo de la experiencia visual y conceptual de cada evento.</p>
                    </div>
                </div>
            </div>

            <div class="project-card">
                <h5>Pabol Producciones - SAS</h5>
                <span class="meta-value">Apoyo Log&#237;stico y Producci&#243;n de Eventos</span>
                <div class="project-meta">
                    <div class="meta-item">
                        <p>He participado en distintos eventos apoyando procesos t&#233;cnicos, log&#237;sticos y operativos. En eventos peque&#241;os he trabajado en montaje y operaci&#243;n b&#225;sica de audio para presentaciones en vivo, y en producciones de mayor escala he apoyado procesos de log&#237;stica, coordinaci&#243;n de equipos, montaje y necesidades generales tanto en escenario como en front of house.</p>
                    </div>
                </div>
            </div>

            <div class="project-card">
                <h5>Iglesia del Nazareno Cali</h5>
                <span class="meta-value">Apoyo Stage y Producci&#243;n en Escenario</span>
                <div class="project-meta">
                    <div class="meta-item">
                        <p>Hago parte de apoyo de stage durante servicios, apoyando procesos como line checks, revisi&#243;n de instrumentos e input lists, adem&#225;s de facilitar la comunicaci&#243;n entre escenario e ingenier&#237;a durante cada culto.</p>
                    </div>
                </div>
            </div>

            <div class="project-card">
                <h5>Universidad Icesi</h5>
                <span class="meta-value">Stage y Backline</span>
                <div class="project-meta">
                    <div class="meta-item">
                        <p>He participado en diferentes eventos musicales e institucionales dentro de la Universidad Icesi, desempe&#241;&#225;ndome en roles de stage y backline durante presentaciones de ensambles y eventos universitarios. Dentro de estos espacios apoyo la organizaci&#243;n de escenario, manejo de tiempos, gu&#237;a de artistas y log&#237;stica en vivo.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="section reveal" id="testimonios">
        <div class="section-header">
            <div class="section-label">Testimonios</div>
            <h2 class="section-title">Lo que dicen</h2>
            <p class="section-subtitle">Resultados que hablan por s&#237; mismos.</p>
        </div>

        <div class="testimonials-grid">
            <div class="testimonial-card">
                <div class="quote-mark">&#8220;</div>
                <p class="testimonial-text">Angela es una persona muy organizada, firmar y clara en sus ideas, adem&#225;s de contar con la capacidad para gestionar de forma r&#225;pida y eficiente y es un gran equipo.</p>
                <p class="testimonial-author">Valeria y Veca</p>
            </div>

            <div class="testimonial-card">
                <div class="quote-mark">&#8220;</div>
                <p class="testimonial-text">Comunicaci&#243;n clara y efectiva. Siempre sabe exactamente qu&#233; necesitamos en cada momento del evento.</p>
                <p class="testimonial-author">Alexis Play</p>
            </div>

            <div class="testimonial-card">
                <div class="quote-mark">&#8220;</div>
                <p class="testimonial-text">Es una persona con buena atenci&#243;n al cliente y buen manejo de personal. Es eficiente y tranquila bajo presi&#243;n.</p>
                <p class="testimonial-author">Pabol producciones</p>
            </div>
        </div>
    </section>

    <section class="cta-section reveal" id="contacto">
        <h2>&#191;Listo para crear algo<br>extraordinario?</h2>
        <p>Conversemos sobre tu pr&#243;ximo proyecto</p>
        <div class="cta-buttons">
            <a href="mailto:Parradorestrepo05@gmail.com" class="btn btn-primary"><span>Enviar email</span></a>
            <a href="https://wa.me/573184036146" class="btn btn-secondary" target="_blank" rel="noopener noreferrer"><span>WhatsApp</span></a>
            <a href="https://instagram.com/angelaparrado22" class="btn btn-secondary" target="_blank" rel="noopener noreferrer"><span>Instagram</span></a>
        </div>
    </section>

    <footer>
        <div class="footer-logo">Angela Parrado</div>
        <p>&copy; 2025 Stage &amp; Production Management</p>
        <p>Cali, Valle del Cauca, Colombia</p>
    </footer>

    <script>
        function reveal() {
            const reveals = document.querySelectorAll('.reveal');
            reveals.forEach(element => {
                const windowHeight = window.innerHeight;
                const elementTop = element.getBoundingClientRect().top;
                if (elementTop < windowHeight - 120) {
                    element.classList.add('active');
                }
            });
        }

        window.addEventListener('scroll', reveal);
        reveal();

        function loadVideo(container) {
            const iframe = document.createElement('iframe');
            iframe.src = container.dataset.src;
            iframe.title = 'Pitch de presentación';
            iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
            iframe.allowFullscreen = true;
            container.innerHTML = '';
            container.appendChild(iframe);
        }
    </script>
</body>
</html>"""

# Inject the base64 Lora fonts (plain string replace — no f-string escaping issues)
HTML = HTML.replace("__LORA_FONTS__", _font_face)

components.html(HTML, height=800, scrolling=True)
