import os

BASE = r"C:\Users\USER\Documents\ANGELA"

BASE_CSS = """*{margin:0;padding:0;box-sizing:border-box}
:root{--orange:#ff6b35;--orange-light:#ff8c61;--orange-dark:#e85a2a;--yellow:#ffa500;--accent:#ffb347;--black:#0a0a0a;--dark:#1a1a1a;--white:#ffffff;--gray:#9ca3af;--gray-light:#d1d5db}
body{font-family:'Lora',Georgia,serif;background:var(--black);color:var(--white);overflow-x:hidden;line-height:1.8}
h1,h2,h3,h4,h5,h6{font-family:'Goudy Bookletter','Palatino Linotype',Palatino,Georgia,serif;font-weight:normal;letter-spacing:-.5px}
.hero h1{font-size:7rem!important;font-weight:normal}
.section-title{font-size:5rem!important;font-weight:normal}

@keyframes fadeInUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeInDown{from{opacity:0;transform:translateY(-40px)}to{opacity:1;transform:translateY(0)}}
@keyframes slideIn{from{opacity:0;transform:translateX(-60px)}to{opacity:1;transform:translateX(0)}}
@keyframes scaleIn{from{opacity:0;transform:scale(.9)}to{opacity:1;transform:scale(1)}}
@keyframes shimmer{0%{transform:translateX(-100%) translateY(-100%) rotate(45deg)}100%{transform:translateX(100%) translateY(100%) rotate(45deg)}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-15px)}}
@keyframes gradientMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}

.background-overlay{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0;background:radial-gradient(circle at 20% 30%,rgba(255,107,53,.1) 0%,transparent 50%),radial-gradient(circle at 80% 70%,rgba(255,140,97,.08) 0%,transparent 50%)}

.gradient-text{background:linear-gradient(135deg,var(--orange) 0%,var(--accent) 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}

.section-label{color:var(--orange-light);font-size:.85rem;font-weight:600;text-transform:uppercase;letter-spacing:3px;margin-bottom:20px;text-align:center}
.section-title{font-size:4.5rem;font-weight:800;margin-bottom:25px;letter-spacing:-2px;line-height:1.1;text-align:center}
.section-subtitle{font-size:1.3rem;color:var(--gray);max-width:750px;margin:0 auto;line-height:1.7;text-align:center}
.section-header{text-align:center;margin-bottom:90px}

.btn{padding:18px 40px;border-radius:12px;font-size:1rem;font-weight:600;text-decoration:none;display:inline-block;transition:all .4s cubic-bezier(.34,1.56,.64,1);position:relative;overflow:hidden}
.btn::before{content:'';position:absolute;top:50%;left:50%;width:0;height:0;border-radius:50%;background:rgba(255,255,255,.15);transform:translate(-50%,-50%);transition:width .5s,height .5s}
.btn:hover::before{width:400px;height:400px}
.btn span{position:relative;z-index:1}
.btn-primary{background:var(--orange);color:var(--white);box-shadow:0 10px 40px rgba(255,107,53,.3)}
.btn-primary:hover{background:var(--orange-dark);transform:translateY(-3px);box-shadow:0 15px 50px rgba(255,107,53,.5)}
.btn-secondary{background:var(--orange);color:var(--white);box-shadow:0 10px 40px rgba(255,107,53,.3)}
.btn-secondary:hover{background:var(--orange-dark);transform:translateY(-3px);box-shadow:0 15px 50px rgba(255,107,53,.5)}
.btn-outline{background:transparent;color:var(--white);border:2px solid rgba(255,107,53,.5)}
.btn-outline:hover{border-color:var(--orange);background:rgba(255,107,53,.1);transform:translateY(-3px)}

.reveal{opacity:0;transform:translateY(60px);transition:all 1s cubic-bezier(.34,1.56,.64,1)}
.reveal.active{opacity:1;transform:translateY(0)}
"""

REVEAL_JS = """<script>
function reveal(){
  document.querySelectorAll('.reveal').forEach(el=>{
    if(el.getBoundingClientRect().top < window.innerHeight-120) el.classList.add('active');
  });
}
window.addEventListener('scroll',reveal);
reveal();
function loadVideo(c){
  var f=document.createElement('iframe');
  f.src=c.dataset.src;f.title='Pitch';
  f.allow='accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture';
  f.allowFullscreen=true;c.innerHTML='';c.appendChild(f);
}
</script>"""

def wrap(title, bg, extra_css, body):
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>{BASE_CSS}{extra_css}</style></head>
<body style="background:{bg};color:#fff">{body}{REVEAL_JS}</body></html>"""


# ── HERO ──────────────────────────────────────────────────────────────────────
hero = wrap("Hero", "#0a0a0a", """
@keyframes stageEntry{from{opacity:0;transform:scale(.8)}to{opacity:1;transform:scale(1)}}
@keyframes platformFadeIn{from{opacity:0;transform:translateX(-50%) rotateX(60deg) translateY(20px)}to{opacity:1;transform:translateX(-50%) rotateX(60deg) translateY(0)}}
@keyframes spotlightFadeIn{from{opacity:0}to{opacity:.6}}
@keyframes spotlight-sweep{0%,100%{transform:rotate(-15deg);opacity:.6}50%{transform:rotate(15deg);opacity:1}}
@keyframes particle-float{0%{transform:translateY(0) scale(0);opacity:0}10%{opacity:1}90%{opacity:.8}100%{transform:translateY(-200px) scale(1.5);opacity:0}}
@keyframes glow-pulse{0%,100%{opacity:.5;transform:scale(1)}50%{opacity:1;transform:scale(1.1)}}

nav{position:fixed;top:0;left:0;right:0;padding:30px 60px;display:flex;justify-content:space-between;align-items:center;z-index:1000;background:rgba(10,10,10,.85);backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,107,53,.15);animation:fadeInDown .8s ease}
.logo{font-family:'Goudy Bookletter','Palatino Linotype',Georgia,serif;font-size:1.3rem;font-weight:700;letter-spacing:-.5px;color:var(--white)}
.nav-links{display:flex;gap:50px;list-style:none}
.nav-links a{color:var(--gray);text-decoration:none;font-weight:500;font-size:.95rem;position:relative;transition:color .3s}
.nav-links a::after{content:'';position:absolute;bottom:-6px;left:0;width:0;height:2px;background:var(--orange);transition:width .3s ease}
.nav-links a:hover{color:var(--white)}
.nav-links a:hover::after{width:100%}

.hero{min-height:100vh;display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:80px;padding:140px 60px 80px;position:relative;max-width:1400px;margin:0 auto}
.hero-content{position:relative;z-index:2}
.hero-label{display:inline-block;padding:10px 24px;background:rgba(255,107,53,.15);border:1px solid rgba(255,107,53,.3);border-radius:50px;font-size:.85rem;font-weight:600;text-transform:uppercase;letter-spacing:2px;margin-bottom:35px;color:var(--orange-light);animation:fadeInUp .8s ease .2s backwards}
.hero h1{font-size:6.5rem;font-weight:800;line-height:1.05;letter-spacing:-3px;margin-bottom:35px;animation:fadeInUp .8s ease .4s backwards}
.hero-description{font-size:1.4rem;color:var(--gray);max-width:700px;margin-bottom:50px;line-height:1.7;font-weight:400;animation:fadeInUp .8s ease .6s backwards}
.hero-buttons{display:flex;gap:20px;animation:fadeInUp .8s ease .8s backwards}

.hero-animation{position:relative;height:600px;display:flex;align-items:center;justify-content:center;perspective:1000px}
.stage-animation{position:relative;width:500px;height:400px;transform-style:preserve-3d;animation:stageEntry 1.5s ease-out}
.stage-glow{position:absolute;width:100%;height:100%;background:radial-gradient(circle at center,rgba(255,107,53,.2),transparent 60%);animation:glow-pulse 3s ease-in-out infinite}
.spotlight{position:absolute;width:3px;background:linear-gradient(180deg,rgba(255,140,97,.8),transparent);transform-origin:top center}
.spotlight-1{height:250px;left:20%;top:0;animation:spotlight-sweep 4s ease-in-out infinite,spotlightFadeIn 1s ease-out .5s backwards}
.spotlight-2{height:280px;left:40%;top:0;animation:spotlight-sweep 4s ease-in-out 1s infinite,spotlightFadeIn 1s ease-out .6s backwards}
.spotlight-3{height:300px;left:60%;top:0;animation:spotlight-sweep 4s ease-in-out 2s infinite,spotlightFadeIn 1s ease-out .7s backwards}
.spotlight-4{height:280px;left:80%;top:0;animation:spotlight-sweep 4s ease-in-out 3s infinite,spotlightFadeIn 1s ease-out .8s backwards}
.sound-particle{position:absolute;width:8px;height:8px;background:var(--orange-light);border-radius:50%;opacity:0;animation:particle-float 3s ease-in-out infinite}
.sound-particle:nth-child(6){left:30%;bottom:150px;animation-delay:1s}
.sound-particle:nth-child(7){left:50%;bottom:150px;animation-delay:1.5s}
.sound-particle:nth-child(8){left:70%;bottom:150px;animation-delay:2s}
.sound-particle:nth-child(9){left:40%;bottom:150px;animation-delay:2.5s}
.sound-particle:nth-child(10){left:60%;bottom:150px;animation-delay:3s}
.stage-platform{position:absolute;width:400px;height:40px;background:linear-gradient(180deg,rgba(255,107,53,.3),rgba(255,107,53,.1));bottom:100px;left:50%;transform:translateX(-50%) rotateX(60deg);border-radius:8px;box-shadow:0 20px 40px rgba(255,107,53,.4);animation:platformFadeIn 1s ease-out .3s backwards}
.animation-label{position:absolute;bottom:20px;left:50%;transform:translateX(-50%);font-size:.9rem;font-weight:600;color:var(--orange-light);text-transform:uppercase;letter-spacing:2px;animation:fadeInUp 1s ease-out 1s backwards}

@media(max-width:1200px){.hero{grid-template-columns:1fr;gap:60px}.hero h1{font-size:5rem}}
@media(max-width:768px){nav{padding:25px 30px}.nav-links{display:none}.hero{padding:120px 30px 60px}.hero h1{font-size:3.5rem}.hero-buttons{flex-direction:column}}
""", """
<div class="background-overlay"></div>
<nav>
  <div class="logo">Angela Parrado</div>
  <ul class="nav-links">
    <li><a href="#servicios">Servicios</a></li>
    <li><a href="#sobre-mi">Sobre mí</a></li>
    <li><a href="#galeria">Galería</a></li>
    <li><a href="#experiencia">Experiencia</a></li>
    <li><a href="#testimonios">Testimonios</a></li>
    <li><a href="#contacto">Contacto</a></li>
  </ul>
</nav>
<section class="hero">
  <div class="hero-content">
    <div class="hero-label">Stage &amp; Production Management</div>
    <h1>Eventos que <span class="gradient-text">transforman</span> experiencias</h1>
    <p class="hero-description">Producción integral, stage management y equipos profesionales. Creando momentos memorables con precisión y pasión.</p>
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
""")


# ── SERVICES ─────────────────────────────────────────────────────────────────
svc = wrap("Servicios", "#0a0a0a", """
.section{padding:120px 60px;position:relative}
.services-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:35px;max-width:1300px;margin:0 auto}
.service-card{background:rgba(255,107,53,.04);padding:50px 40px;border-radius:24px;border:1px solid rgba(255,107,53,.15);transition:all .5s cubic-bezier(.34,1.56,.64,1);position:relative;overflow:hidden}
.service-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:100%;background:linear-gradient(135deg,var(--orange),var(--accent));opacity:0;transition:opacity .5s}
.service-card:hover{transform:translateY(-12px) scale(1.02);border-color:var(--orange);box-shadow:0 25px 60px rgba(255,107,53,.35)}
.service-card:hover::before{opacity:.08}
.service-number{font-size:4rem;font-weight:800;color:rgba(255,107,53,.2);margin-bottom:20px;position:relative;z-index:1}
.service-card h3{font-size:1.8rem;margin-bottom:18px;font-weight:700;position:relative;z-index:1}
.service-card p{color:var(--gray);line-height:1.8;font-size:1.05rem;position:relative;z-index:1}
.btn-download{display:inline-flex;align-items:center;gap:10px;margin-top:25px;padding:12px 24px;background:transparent;border:1px solid rgba(255,107,53,.5);border-radius:10px;color:var(--orange-light);font-size:.9rem;font-weight:600;text-decoration:none;position:relative;z-index:1;transition:all .3s}
.btn-download:hover{background:rgba(255,107,53,.15);border-color:var(--orange);color:var(--white);transform:translateY(-2px)}
@media(max-width:1200px){.services-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:768px){.section{padding:80px 30px}.services-grid{grid-template-columns:1fr}}
""", """
<section class="section reveal" id="servicios">
  <div class="section-header">
    <div class="section-label">Servicios</div>
    <h2 class="section-title">Lo que hago</h2>
    <p class="section-subtitle">Soluciones completas para eventos inolvidables. De la conceptualización a la ejecución perfecta.</p>
  </div>
  <div class="services-grid">
    <div class="service-card">
      <div class="service-number">01</div>
      <h3>Stage Management</h3>
      <p>Coordinación completa del escenario. Timing perfecto, gestión de artistas y resolución instantánea de cualquier situación.</p>
    </div>
    <div class="service-card">
      <div class="service-number">02</div>
      <h3>Producción de Eventos</h3>
      <p>De la idea a la realidad. Logística integral, coordinación de equipos y gestión completa para eventos impecables.</p>
    </div>
    <div class="service-card">
      <div class="service-number">03</div>
      <h3>Alquiler de Equipos</h3>
      <p>Audio, infraestructura e iluminación profesional para eventos de alto impacto.</p>
      <a href="PABOLPRODUCCIONES.pdf" target="_blank" rel="noopener noreferrer" class="btn-download">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
          <polyline points="7 10 12 15 17 10"/>
          <line x1="12" y1="15" x2="12" y2="3"/>
        </svg>
        Catálogo PABOL PRODUCCIONES
      </a>
    </div>
  </div>
</section>
""")


# ── ABOUT ─────────────────────────────────────────────────────────────────────
about = wrap("Sobre mí", "#1a1a1a", """
.about-section{background:var(--dark);padding:120px 60px}
.about-content{max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:start}
.about-text h3{font-size:3rem;font-weight:800;margin-bottom:30px;letter-spacing:-1px;line-height:1.1}
.about-text p{font-size:1.15rem;line-height:1.85;color:var(--gray);margin-bottom:25px}
.about-highlights{display:grid;grid-template-columns:repeat(2,1fr);gap:20px;margin-top:40px}
.highlight-item{background:rgba(255,107,53,.08);padding:25px;border-radius:16px;border:1px solid rgba(255,107,53,.2);transition:all .3s}
.highlight-item:hover{background:rgba(255,107,53,.15);transform:translateY(-3px)}
.highlight-item h4{font-size:1.2rem;margin-bottom:8px;font-weight:600;color:var(--orange-light)}
.highlight-item p{font-size:.95rem;color:var(--gray);margin:0}
.about-right-col{display:flex;flex-direction:column;gap:20px;min-width:0}
.about-image{height:750px;border-radius:24px;overflow:hidden;position:relative;flex-shrink:0}
.about-image img{width:100%;height:100%;object-fit:cover;object-position:center center;display:block}
.about-video-wrapper{width:100%;min-width:0}
.about-video-label{font-size:.78rem;font-weight:600;text-transform:uppercase;letter-spacing:3px;color:var(--orange-light);margin-bottom:12px}
.video-container{position:relative;width:100%;padding-bottom:56.25%;border-radius:16px;overflow:hidden;border:1px solid rgba(255,107,53,.2);box-shadow:0 15px 40px rgba(0,0,0,.5);cursor:pointer}
.video-container img.video-thumb{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;display:block;transition:transform .4s}
.video-container:hover img.video-thumb{transform:scale(1.03)}
.play-btn{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:72px;height:72px;background:rgba(255,107,53,.92);border:none;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;z-index:2;transition:all .3s;box-shadow:0 6px 30px rgba(255,107,53,.5)}
.video-container:hover .play-btn{background:var(--orange);transform:translate(-50%,-50%) scale(1.12)}
.play-btn svg{width:28px;height:28px;fill:white;margin-left:5px}
.video-container iframe{position:absolute;top:0;left:0;width:100%;height:100%;border:none;display:block}
@media(max-width:1200px){.about-section{padding:80px 30px}.about-content{grid-template-columns:1fr;gap:50px}.about-image{height:350px}}
@media(max-width:768px){.about-text h3{font-size:2.2rem}.about-highlights{grid-template-columns:1fr}}
""", """
<section class="about-section reveal" id="sobre-mi">
  <div class="section-header">
    <div class="section-label">Sobre mí</div>
    <h2 class="section-title">Quién soy</h2>
    <p class="section-subtitle">Pasión por los eventos y dedicación en cada proyecto.</p>
  </div>
  <div class="about-content">
    <div class="about-text">
      <h3>Productora de eventos con visión integral</h3>
      <p>Desde muy pequeña tuve un acercamiento a este entorno gracias a la empresa de producción de eventos de mis padres, lo que me permitió crecer viendo de cerca cómo se construyen las experiencias detrás de un evento. Poco a poco empecé a involucrarme en diferentes producciones, primero desde espacios pequeños y luego en escenarios más grandes, descubriendo todo lo que ocurre detrás de la tarima para que un evento funcione correctamente.</p>
      <p>Con el tiempo entendí que lo que más me apasiona es el stage management, la coordinación técnica y la dinámica de trabajo que ocurre en tiempo real durante un evento en vivo. Me gusta la precisión, el manejo de los tiempos, la comunicación entre equipos y la resolución de imprevistos bajo presión.</p>
      <p>Actualmente me encuentro enfocando mi proceso hacia los escenarios en vivo y la logística de eventos, mientras desarrollo Expreso Social, un proyecto enfocado en crear experiencias más cercanas y auténticas entre artistas emergentes y su público.</p>
      <div class="about-highlights">
        <div class="highlight-item"><h4>Velocidad</h4><p>Resolución instantánea bajo presión</p></div>
        <div class="highlight-item"><h4>Versatilidad</h4><p>Conciertos, corporativos, privados e iglesias</p></div>
        <div class="highlight-item"><h4>Organización</h4><p>Metodología rigurosa y detallada</p></div>
        <div class="highlight-item"><h4>Pasión</h4><p>Amo la adrenalina de eventos en vivo</p></div>
      </div>
    </div>
    <div class="about-right-col">
      <div class="about-image">
        <img src="https://im.vsco.co/aws-us-west-2/0a6aa5/136624836/6a0f9681029435f53f3ae4c4/vsco_052126.jpg?w=1600" alt="Sobre mí">
      </div>
      <div class="about-video-wrapper">
        <div class="about-video-label">Conóceme en 60 segundos</div>
        <div class="video-container" onclick="loadVideo(this)" data-src="https://www.youtube.com/embed/FZPmelh2-2o?autoplay=1">
          <img class="video-thumb" src="https://img.youtube.com/vi/FZPmelh2-2o/maxresdefault.jpg" alt="Ver pitch de presentación">
          <button class="play-btn" aria-label="Reproducir video">
            <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</section>
""")


# ── GALLERY ───────────────────────────────────────────────────────────────────
gallery = wrap("Galería", "#1a1a1a", """
.gallery-section{background:var(--dark);padding:120px 60px}
.gallery-grid{display:grid;grid-template-columns:repeat(3,1fr);grid-auto-rows:280px;gap:30px;max-width:1300px;margin:0 auto}
.gallery-item{position:relative;border-radius:20px;overflow:hidden;cursor:pointer;background:linear-gradient(135deg,rgba(255,107,53,.2),rgba(255,140,97,.2));transition:all .4s cubic-bezier(.34,1.56,.64,1)}
.gallery-item:nth-child(1){grid-column:span 2;grid-row:span 2}
.gallery-item::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(180deg,transparent 30%,rgba(0,0,0,.9) 100%);opacity:0;transition:opacity .4s;z-index:1}
.gallery-item:hover{transform:scale(1.05);box-shadow:0 30px 60px rgba(255,107,53,.5);z-index:10}
.gallery-item:hover::before{opacity:1}
.gallery-overlay{position:absolute;bottom:0;left:0;right:0;padding:30px;transform:translateY(100%);transition:transform .4s;z-index:2}
.gallery-item:hover .gallery-overlay{transform:translateY(0)}
.gallery-overlay h4{font-size:1.3rem;font-weight:700;margin-bottom:8px}
.gallery-overlay p{font-size:.9rem;color:var(--gray-light)}
.gallery-item img{width:100%;height:100%;object-fit:cover;display:block}
@media(max-width:1200px){.gallery-grid{grid-template-columns:repeat(2,1fr);grid-auto-rows:250px}.gallery-item:nth-child(1),.gallery-item:nth-child(2),.gallery-item:nth-child(3){grid-column:span 1;grid-row:span 1}}
@media(max-width:768px){.gallery-section{padding:80px 30px}.gallery-grid{grid-template-columns:1fr;grid-auto-rows:250px}}
""", """
<section class="gallery-section reveal" id="galeria">
  <div class="section-header">
    <div class="section-label">Galería</div>
    <h2 class="section-title">Momentos capturados</h2>
    <p class="section-subtitle">Un vistazo a algunos de los eventos que he producido.</p>
  </div>
  <div class="gallery-grid">
    <div class="gallery-item">
      <img src="https://im.vsco.co/aws-us-west-2/0a6aa5/136624836/6a0fc92772d377d0e5a8c23e/vsco_052126.jpg?w=1600" alt="Lanzamiento Expreso Social">
      <div class="gallery-overlay">
        <h4>Lanzamiento Expreso Social</h4>
        <p>Producción completa con artistas reconocidos</p>
      </div>
    </div>
    <div class="gallery-item">
      <img src="https://im.vsco.co/aws-us-west-2/0a6aa5/136624836/6a0fc7f90d87a9ea47de49ca/vsco_052126.jpg?w=1600" alt="Stage Setup">
      <div class="gallery-overlay">
        <h4>Stage Setup</h4>
        <p>Montaje técnico profesional</p>
      </div>
    </div>
    <div class="gallery-item">
      <img src="https://im.vsco.co/aws-us-west-2/0a6aa5/136624836/6a10e0f3acf4897c57d5d875/vsco_052226.jpg?w=1600" alt="Control Técnico">
      <div class="gallery-overlay">
        <h4>Control Técnico</h4>
        <p>Coordinación en tiempo real</p>
      </div>
    </div>
  </div>
</section>
""")


# ── EXPERIENCE ────────────────────────────────────────────────────────────────
exp = wrap("Experiencia", "#0a0a0a", """
.experience-section{background:linear-gradient(180deg,var(--black) 0%,var(--dark) 50%,var(--black) 100%);padding:120px 60px}
.project-cards{display:grid;grid-template-columns:repeat(2,1fr);gap:30px;max-width:1200px;margin:0 auto}
.project-card{background:rgba(255,107,53,.05);padding:40px;border-radius:20px;border:1px solid rgba(255,107,53,.2);transition:all .4s;position:relative;overflow:hidden}
.project-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:4px;background:linear-gradient(90deg,var(--orange),var(--accent));transform:scaleX(0);transform-origin:left;transition:transform .4s}
.project-card:hover{background:rgba(255,107,53,.12);border-color:var(--orange);transform:translateY(-10px);box-shadow:0 20px 50px rgba(255,107,53,.3)}
.project-card:hover::before{transform:scaleX(1)}
.project-card h5{font-size:1.5rem;font-weight:700;margin-bottom:15px}
.project-card p{color:var(--gray);line-height:1.7;font-size:1.05rem;margin-bottom:20px}
.project-meta{display:flex;gap:20px;padding-top:20px;border-top:1px solid rgba(255,107,53,.15)}
.meta-item{display:flex;flex-direction:column}
.meta-label{font-size:.8rem;color:var(--gray);text-transform:uppercase;letter-spacing:1px;margin-bottom:5px}
.meta-value{font-size:1.2rem;font-weight:700;color:var(--orange-light)}
@media(max-width:1200px){.project-cards{grid-template-columns:1fr}}
@media(max-width:768px){.experience-section{padding:80px 30px}}
""", """
<section class="experience-section section reveal" id="experiencia">
  <div class="section-header">
    <div class="section-label">Experiencia</div>
    <h2 class="section-title">Proyectos destacados</h2>
    <p class="section-subtitle">5 meses de experiencia produciendo eventos memorables con resultados excepcionales.</p>
  </div>
  <div class="project-cards">
    <div class="project-card">
      <h5>Expreso social</h5>
      <span class="meta-value">Co-creadora y Producción de Eventos</span>
      <div class="project-meta">
        <div class="meta-item">
          <p>Expreso Social es una promotora de eventos creada junto a otras dos personas, enfocada en desarrollar experiencias más cercanas y conscientes entre artistas emergentes y su público. Dentro del proyecto participo en la planeación y producción de eventos, apoyando procesos logísticos, coordinación general y desarrollo creativo de la experiencia visual y conceptual de cada evento.</p>
        </div>
      </div>
    </div>
    <div class="project-card">
      <h5>Pabol Producciones - SAS</h5>
      <span class="meta-value">Apoyo Logístico y Producción de Eventos</span>
      <div class="project-meta">
        <div class="meta-item">
          <p>He participado en distintos eventos apoyando procesos técnicos, logísticos y operativos. En eventos pequeños he trabajado en montaje y operación básica de audio para presentaciones en vivo, y en producciones de mayor escala he apoyado procesos de logística, coordinación de equipos, montaje y necesidades generales tanto en escenario como en front of house.</p>
        </div>
      </div>
    </div>
    <div class="project-card">
      <h5>Iglesia del Nazareno Cali</h5>
      <span class="meta-value">Apoyo Stage y Producción en Escenario</span>
      <div class="project-meta">
        <div class="meta-item">
          <p>Hago parte de apoyo de stage durante servicios, apoyando procesos como line checks, revisión de instrumentos e input lists, además de facilitar la comunicación entre escenario e ingeniería durante cada culto.</p>
        </div>
      </div>
    </div>
    <div class="project-card">
      <h5>Universidad Icesi</h5>
      <span class="meta-value">Stage y Backline</span>
      <div class="project-meta">
        <div class="meta-item">
          <p>He participado en diferentes eventos musicales e institucionales dentro de la Universidad Icesi, desempeñándome en roles de stage y backline durante presentaciones de ensambles y eventos universitarios. Dentro de estos espacios apoyo la organización de escenario, manejo de tiempos, guía de artistas y logística en vivo.</p>
        </div>
      </div>
    </div>
  </div>
</section>
""")


# ── TESTIMONIALS + CTA + FOOTER ───────────────────────────────────────────────
test = wrap("Testimonios", "#0a0a0a", """
.section{padding:120px 60px;position:relative}
.testimonials-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:35px;max-width:1300px;margin:0 auto}
.testimonial-card{background:rgba(255,107,53,.04);backdrop-filter:blur(10px);padding:45px;border-radius:24px;border:1px solid rgba(255,107,53,.15);transition:all .4s}
.testimonial-card:hover{transform:translateY(-10px);border-color:var(--orange);box-shadow:0 20px 50px rgba(255,107,53,.25)}
.quote-mark{font-size:4rem;color:var(--orange);opacity:.25;line-height:1;margin-bottom:20px;font-family:Georgia,serif}
.testimonial-text{font-size:1.15rem;line-height:1.8;color:var(--gray);margin-bottom:30px}
.testimonial-author{font-weight:700;color:var(--orange-light);font-size:.95rem}

.cta-section{padding:150px 60px;text-align:center;position:relative;background:linear-gradient(135deg,rgba(255,107,53,.08),rgba(255,140,97,.08))}
.cta-section h2{font-size:5.5rem;font-weight:800;margin-bottom:30px;line-height:1.15;letter-spacing:-2px}
.cta-section p{font-size:1.5rem;color:var(--gray);margin-bottom:55px}
.cta-buttons{display:flex;gap:20px;justify-content:center;flex-wrap:wrap}

footer{padding:80px 60px 50px;text-align:center;border-top:1px solid rgba(255,107,53,.15)}
.footer-logo{font-family:'Goudy Bookletter','Palatino Linotype',Georgia,serif;font-size:2rem;font-weight:800;margin-bottom:30px;letter-spacing:-1px;display:block}
footer p{color:var(--gray);margin-bottom:12px;font-size:.95rem}

@media(max-width:1200px){.testimonials-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:768px){.section{padding:80px 30px}.testimonials-grid{grid-template-columns:1fr}.cta-section{padding:80px 30px}.cta-section h2{font-size:3rem}.cta-buttons{flex-direction:column}}
""", """
<section class="section reveal" id="testimonios">
  <div class="section-header">
    <div class="section-label">Testimonios</div>
    <h2 class="section-title">Lo que dicen</h2>
    <p class="section-subtitle">Resultados que hablan por sí mismos.</p>
  </div>
  <div class="testimonials-grid">
    <div class="testimonial-card">
      <div class="quote-mark">"</div>
      <p class="testimonial-text">Angela es una persona muy organizada, firme y clara en sus ideas, además de contar con la capacidad para gestionar de forma rápida y eficiente y es un gran equipo.</p>
      <p class="testimonial-author">Valeria y Veca</p>
    </div>
    <div class="testimonial-card">
      <div class="quote-mark">"</div>
      <p class="testimonial-text">Comunicación clara y efectiva. Siempre sabe exactamente qué necesitamos en cada momento del evento.</p>
      <p class="testimonial-author">Alexis Play</p>
    </div>
    <div class="testimonial-card">
      <div class="quote-mark">"</div>
      <p class="testimonial-text">Es una persona con buena atención al cliente y buen manejo de personal. Es eficiente y tranquila bajo presión.</p>
      <p class="testimonial-author">Pabol Producciones</p>
    </div>
  </div>
</section>
<section class="cta-section reveal" id="contacto">
  <h2>¿Listo para crear algo<br>extraordinario?</h2>
  <p>Conversemos sobre tu próximo proyecto</p>
  <div class="cta-buttons">
    <a href="mailto:Parradorestrepo05@gmail.com" class="btn btn-primary"><span>Enviar email</span></a>
    <a href="https://wa.me/573184036146" class="btn btn-secondary" target="_blank" rel="noopener noreferrer"><span>WhatsApp</span></a>
    <a href="https://instagram.com/angelaparrado22" class="btn btn-secondary" target="_blank" rel="noopener noreferrer"><span>Instagram</span></a>
  </div>
</section>
<footer>
  <span class="footer-logo">Angela Parrado</span>
  <p>&copy; 2025 Stage &amp; Production Management</p>
  <p>Cali, Valle del Cauca, Colombia</p>
</footer>
""")


files = {
    "s_hero.html": hero,
    "s_servicios.html": svc,
    "s_about.html": about,
    "s_gallery.html": gallery,
    "s_exp.html": exp,
    "s_test.html": test,
}

for name, content in files.items():
    path = os.path.join(BASE, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  wrote {name}")

print("done")
