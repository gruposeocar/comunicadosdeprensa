#!/usr/bin/env python3
"""Generador estatico de comunicadosdeprensa.es"""
import os, re, shutil, html, json

SITE = "https://comunicadosdeprensa.es"
BRAND = "Comunicados de Prensa"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")

NAV = [
    ("Servicios", "/publicar-nota-de-prensa/"),
    ("Enlaces en prensa", "/comprar-enlaces-prensa/"),
    ("Medios", "/medios/"),
    ("Guia", "/guia/"),
    ("Precios", "/precios/"),
]

CSS = """
:root{
  --tinta:#15181d; --tinta-2:#3f4651; --tinta-3:#6b7280;
  --linea:#e3e6ea; --fondo:#ffffff; --crema:#f7f6f3;
  --acento:#0b4f9e; --acento-2:#083a75; --destacado:#c8102e;
  --radio:10px; --ancho:1120px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--tinta);
  background:var(--fondo);line-height:1.65;font-size:18px;-webkit-font-smoothing:antialiased}
.sans{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
.wrap{max-width:var(--ancho);margin:0 auto;padding:0 24px}
a{color:var(--acento);text-decoration:none}
a:hover{text-decoration:underline}
img{max-width:100%;height:auto}

/* cabecera */
header.top{border-bottom:1px solid var(--linea);background:#fff;position:sticky;top:0;z-index:50}
.top .wrap{display:flex;align-items:center;justify-content:space-between;height:68px;gap:24px}
.logo{font-family:Georgia,serif;font-weight:700;font-size:20px;color:var(--tinta);letter-spacing:-.3px;white-space:nowrap}
.logo span{color:var(--acento)}
nav.main{display:flex;gap:22px;align-items:center}
nav.main a{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  font-size:15px;color:var(--tinta-2);font-weight:500}
.btn{display:inline-block;background:var(--acento);color:#fff!important;padding:11px 20px;
  border-radius:var(--radio);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  font-size:15px;font-weight:600;text-decoration:none!important;border:0;cursor:pointer;transition:background .15s}
.btn:hover{background:var(--acento-2)}
.btn.ghost{background:transparent;color:var(--acento)!important;border:1px solid var(--acento)}
.btn.ghost:hover{background:var(--crema)}
.btn.lg{padding:15px 30px;font-size:17px}
.menu-btn{display:none;background:none;border:0;font-size:24px;cursor:pointer;color:var(--tinta)}

/* hero */
.hero{padding:62px 0 48px;border-bottom:1px solid var(--linea)}
.hero h1{font-size:46px;line-height:1.15;margin:0 0 18px;letter-spacing:-.8px}
.hero .entradilla{font-size:21px;color:var(--tinta-2);max-width:700px;margin:0 0 30px}
.hero-cta{display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.hero-nota{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  font-size:14px;color:var(--tinta-3)}

/* contenido */
main{padding:0 0 60px}
article h1{font-size:40px;line-height:1.18;letter-spacing:-.6px;margin:0 0 16px}
article h2{font-size:28px;line-height:1.3;margin:46px 0 14px;letter-spacing:-.3px}
article h3{font-size:21px;line-height:1.35;margin:32px 0 10px}
article p{margin:0 0 18px}
article ul,article ol{margin:0 0 20px;padding-left:22px}
article li{margin-bottom:9px}
.entradilla{font-size:21px;color:var(--tinta-2);line-height:1.55}
.contenido{max-width:720px}
.cols{display:grid;grid-template-columns:1fr 320px;gap:56px;align-items:start;padding-top:40px}

/* caja lateral */
.aside{position:sticky;top:92px;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
.card{border:1px solid var(--linea);border-radius:var(--radio);padding:22px;background:var(--crema);margin-bottom:20px}
.card h3{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  font-size:17px;margin:0 0 10px;font-weight:700}
.card p{font-size:15px;color:var(--tinta-2);margin:0 0 14px;line-height:1.55}
.card .btn{width:100%;text-align:center}

/* bloques */
.bloque{padding:54px 0;border-top:1px solid var(--linea)}
.bloque.crema{background:var(--crema);border-top:0}
.bloque h2{font-size:31px;margin:0 0 10px;letter-spacing:-.4px}
.bloque .sub{font-size:19px;color:var(--tinta-2);max-width:640px;margin:0 0 34px}
.rejilla{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.rejilla.dos{grid-template-columns:repeat(2,1fr)}
.caja{border:1px solid var(--linea);border-radius:var(--radio);padding:26px;background:#fff}
.caja h3{font-size:20px;margin:0 0 9px}
.caja p{font-size:16px;color:var(--tinta-2);margin:0}
.num{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  font-size:13px;font-weight:700;color:var(--acento);letter-spacing:.8px;text-transform:uppercase;margin-bottom:8px}

/* precios */
.precios{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;align-items:start}
.plan{border:1px solid var(--linea);border-radius:var(--radio);padding:30px;background:#fff;position:relative}
.plan.destacado{border:2px solid var(--acento);box-shadow:0 8px 28px rgba(11,79,158,.1)}
.plan .etiqueta{position:absolute;top:-12px;left:30px;background:var(--acento);color:#fff;
  font-family:-apple-system,sans-serif;font-size:12px;font-weight:700;padding:5px 12px;border-radius:20px;letter-spacing:.4px}
.plan h3{font-size:22px;margin:0 0 6px}
.plan .precio{font-size:40px;font-weight:700;letter-spacing:-1px;margin:14px 0 4px}
.plan .precio small{font-size:16px;font-weight:400;color:var(--tinta-3)}
.plan ul{list-style:none;padding:0;margin:20px 0 24px;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:15px}
.plan ul li{padding-left:26px;position:relative;margin-bottom:11px;color:var(--tinta-2);line-height:1.5}
.plan ul li:before{content:"";position:absolute;left:0;top:7px;width:14px;height:8px;
  border-left:2px solid var(--acento);border-bottom:2px solid var(--acento);transform:rotate(-45deg)}
.plan .btn{width:100%;text-align:center}

/* tablas */
table{width:100%;border-collapse:collapse;margin:24px 0;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:15px}
th{text-align:left;padding:13px 14px;background:var(--crema);border-bottom:2px solid var(--linea);font-weight:700}
td{padding:13px 14px;border-bottom:1px solid var(--linea);vertical-align:top;color:var(--tinta-2)}
tr:hover td{background:#fbfbfa}

/* faq */
.faq{border-top:1px solid var(--linea);margin-top:16px}
.faq details{border-bottom:1px solid var(--linea);padding:18px 0}
.faq summary{font-weight:700;cursor:pointer;font-size:18px;list-style:none;position:relative;padding-right:32px}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";position:absolute;right:4px;top:-2px;font-size:24px;color:var(--acento);font-weight:400}
.faq details[open] summary:after{content:"\\2212"}
.faq p{margin:14px 0 0;color:var(--tinta-2)}

/* migas */
.migas{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  font-size:14px;color:var(--tinta-3);padding:18px 0 0}
.migas a{color:var(--tinta-3)}

/* formulario */
form.cot{display:grid;gap:14px;max-width:560px;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
form.cot label{font-size:14px;font-weight:600;margin-bottom:-8px}
form.cot input,form.cot select,form.cot textarea{padding:12px 14px;border:1px solid var(--linea);
  border-radius:var(--radio);font-size:16px;font-family:inherit;background:#fff}
form.cot textarea{min-height:110px;resize:vertical}
form.cot .legal{font-size:13px;color:var(--tinta-3);line-height:1.5}

/* directorio */
.filtros{display:flex;gap:10px;flex-wrap:wrap;margin:24px 0;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
.filtros select,.filtros input{padding:10px 13px;border:1px solid var(--linea);border-radius:var(--radio);font-size:15px;font-family:inherit}
.contador{font-family:-apple-system,sans-serif;font-size:14px;color:var(--tinta-3);margin-bottom:10px}

/* pie */
footer.pie{background:var(--tinta);color:#c9ced6;padding:52px 0 30px;
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-size:15px}
footer.pie a{color:#c9ced6}
.pie-rejilla{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:36px;margin-bottom:38px}
.pie-rejilla h4{color:#fff;font-size:15px;margin:0 0 14px;font-weight:700}
.pie-rejilla ul{list-style:none;padding:0;margin:0}
.pie-rejilla li{margin-bottom:9px}
.pie-logo{font-family:Georgia,serif;font-size:19px;color:#fff;font-weight:700;margin-bottom:10px}
.pie-abajo{border-top:1px solid #2b3139;padding-top:22px;font-size:13px;color:#8b94a0;
  display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}

@media(max-width:900px){
  .cols{grid-template-columns:1fr;gap:34px}
  .aside{position:static}
  .rejilla,.rejilla.dos,.precios{grid-template-columns:1fr}
  .pie-rejilla{grid-template-columns:1fr 1fr;gap:28px}
  nav.main{display:none}
  nav.main.abierto{display:flex;position:absolute;top:68px;left:0;right:0;background:#fff;
    flex-direction:column;align-items:flex-start;padding:18px 24px;gap:16px;border-bottom:1px solid var(--linea)}
  .menu-btn{display:block}
  .hero h1{font-size:33px}
  article h1{font-size:30px}
  article h2{font-size:24px}
  .hero .entradilla,.entradilla{font-size:19px}
  body{font-size:17px}
}
"""

BASE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<meta property="og:type" content="{ogtype}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="{brand}">
<meta property="og:locale" content="es_ES">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/estilo.css">
{schema}
</head>
<body>
<header class="top">
  <div class="wrap">
    <a href="/" class="logo">Comunicados<span>dePrensa</span></a>
    <nav class="main" id="nav">{nav}</nav>
    <div style="display:flex;gap:10px;align-items:center">
      <a href="/precios/#cotizar" class="btn">Publicar mi nota</a>
      <button class="menu-btn" onclick="document.getElementById('nav').classList.toggle('abierto')" aria-label="Menu">&#9776;</button>
    </div>
  </div>
</header>
{body}
<footer class="pie">
  <div class="wrap">
    <div class="pie-rejilla">
      <div>
        <div class="pie-logo">ComunicadosdePrensa.es</div>
        <p style="color:#8b94a0;line-height:1.6;margin:0">Redaccion, publicacion y distribucion de notas de prensa para empresas y profesionales en Espana.</p>
      </div>
      <div>
        <h4>Servicios</h4>
        <ul>
          <li><a href="/publicar-nota-de-prensa/">Publicar nota de prensa</a></li>
          <li><a href="/enviar-nota-de-prensa/">Enviar a medios</a></li>
          <li><a href="/comprar-nota-de-prensa/">Comprar nota de prensa</a></li>
          <li><a href="/comprar-enlaces-prensa/">Enlaces en prensa</a></li>
          <li><a href="/precios/">Precios</a></li>
        </ul>
      </div>
      <div>
        <h4>Recursos</h4>
        <ul>
          <li><a href="/guia/">Guia completa</a></li>
          <li><a href="/guia/ejemplos-de-notas-de-prensa/">Ejemplos</a></li>
          <li><a href="/guia/plantilla-nota-de-prensa/">Plantillas</a></li>
          <li><a href="/medios/">Directorio de medios</a></li>
          <li><a href="/notas-de-prensa-gratis/">Publicar gratis</a></li>
        </ul>
      </div>
      <div>
        <h4>Legal</h4>
        <ul>
          <li><a href="/aviso-legal/">Aviso legal</a></li>
          <li><a href="/privacidad/">Privacidad</a></li>
          <li><a href="/cookies/">Cookies</a></li>
          <li><a href="/contacto/">Contacto</a></li>
        </ul>
      </div>
    </div>
    <div class="pie-abajo">
      <div>&copy; 2026 ComunicadosdePrensa.es &middot; Grupo Seocar S.L.</div>
      <div>Ferrol, Galicia &middot; Espana</div>
    </div>
  </div>
</footer>
</body>
</html>"""


def nav_html(activo=""):
    out = []
    for nombre, url in NAV:
        est = ' style="color:var(--acento);font-weight:600"' if url == activo else ""
        out.append('<a href="{}"{}>{}</a>'.format(url, est, nombre))
    return "".join(out)


def migas(items):
    """items: [(nombre, url|None)]"""
    trozos, ld = [], []
    for i, (nombre, url) in enumerate(items, 1):
        if url:
            trozos.append('<a href="{}">{}</a>'.format(url, nombre))
        else:
            trozos.append('<span>{}</span>'.format(nombre))
        ld.append({"@type": "ListItem", "position": i, "name": nombre,
                   "item": SITE + (url or "")})
    bar = '<div class="wrap"><div class="migas">' + ' &rsaquo; '.join(trozos) + '</div></div>'
    schema = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld}
    return bar, schema


def faq_html(pares):
    if not pares:
        return "", None
    filas = []
    ld = []
    for p, r in pares:
        filas.append("<details><summary>{}</summary><p>{}</p></details>".format(p, r))
        ld.append({"@type": "Question", "name": re.sub("<[^>]+>", "", p),
                   "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", r)}})
    bloque = ('<h2>Preguntas frecuentes</h2><div class="faq">' + "".join(filas) + '</div>')
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ld}
    return bloque, schema


def escribir(ruta, titulo, desc, cuerpo, schemas=None, activo="", ogtype="website"):
    canon = SITE + ruta
    bloques = ""
    for s in (schemas or []):
        if s:
            bloques += '<script type="application/ld+json">' + json.dumps(s, ensure_ascii=False) + '</script>\n'
    doc = BASE.format(title=titulo, desc=desc, canon=canon, brand=BRAND,
                      nav=nav_html(activo), body=cuerpo, schema=bloques, ogtype=ogtype)
    destino = os.path.join(OUT, ruta.strip("/"), "index.html") if ruta != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(doc)
    return ruta


ORG = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "ComunicadosdePrensa.es",
    "url": SITE,
    "description": "Servicio de redaccion, publicacion y distribucion de notas de prensa en Espana.",
    "address": {"@type": "PostalAddress", "addressLocality": "Ferrol",
                "addressRegion": "A Coruna", "addressCountry": "ES"},
    "areaServed": {"@type": "Country", "name": "Espana"},
}


def servicio_schema(nombre, desc, precio=None):
    s = {
        "@context": "https://schema.org", "@type": "Service",
        "serviceType": nombre, "name": nombre, "description": desc,
        "provider": {"@type": "Organization", "name": "ComunicadosdePrensa.es", "url": SITE},
        "areaServed": {"@type": "Country", "name": "Espana"},
    }
    if precio:
        s["offers"] = {"@type": "Offer", "price": str(precio), "priceCurrency": "EUR"}
    return s


def articulo_schema(titulo, desc, ruta):
    return {
        "@context": "https://schema.org", "@type": "Article",
        "headline": titulo, "description": desc,
        "mainEntityOfPage": {"@type": "WebPage", "@id": SITE + ruta},
        "author": {"@type": "Organization", "name": "ComunicadosdePrensa.es"},
        "publisher": {"@type": "Organization", "name": "ComunicadosdePrensa.es"},
        "inLanguage": "es-ES",
    }


FORMULARIO = """
<form class="cot" id="cotizar" action="https://formsubmit.co/hola@comunicadosdeprensa.es" method="POST">
  <input type="hidden" name="_subject" value="Nueva solicitud desde ComunicadosdePrensa.es">
  <input type="hidden" name="_captcha" value="true">
  <input type="hidden" name="_template" value="table">
  <label for="f-nombre">Nombre y empresa</label>
  <input id="f-nombre" type="text" name="nombre" required placeholder="Nombre y nombre de la empresa">
  <label for="f-email">Email</label>
  <input id="f-email" type="email" name="email" required placeholder="tucorreo@empresa.com">
  <label for="f-tel">Telefono</label>
  <input id="f-tel" type="tel" name="telefono" placeholder="Opcional, para llamarte">
  <label for="f-serv">Que necesitas</label>
  <select id="f-serv" name="servicio">
    <option>Redaccion y publicacion de una nota de prensa</option>
    <option>Solo distribucion (ya tengo la nota escrita)</option>
    <option>Enlaces en medios de prensa</option>
    <option>Plan mensual de notas de prensa</option>
    <option>No lo tengo claro, quiero que me asesoren</option>
  </select>
  <label for="f-msg">Cuentanos la noticia</label>
  <textarea id="f-msg" name="mensaje" placeholder="Que quieres anunciar, en que sector trabajas y si tienes fecha limite."></textarea>
  <button class="btn lg" type="submit">Pedir presupuesto sin compromiso</button>
  <p class="legal">Respondemos en menos de 24&nbsp;horas laborables. Sin compromiso y sin permanencia.
  Tus datos los trata Grupo Seocar S.L. para responderte. Mas informacion en la <a href="/privacidad/">politica de privacidad</a>.</p>
</form>
"""

CAJA_LATERAL = """
<aside class="aside">
  <div class="card">
    <h3>Publicamos tu nota de prensa</h3>
    <p>La redactamos, la publicamos y la enviamos a los medios que interesan a tu sector. Desde 95&nbsp;&euro;.</p>
    <a href="/precios/#cotizar" class="btn">Ver precios</a>
  </div>
  <div class="card">
    <h3>Directorio de medios</h3>
    <p>Consulta a que medios espanoles puedes enviar tu nota, por provincia y por sector.</p>
    <a href="/medios/" class="btn ghost">Abrir directorio</a>
  </div>
</aside>
"""
