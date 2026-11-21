# -*- coding: utf-8 -*-
"""Genera el sitio completo en dist/"""
import os, shutil, datetime
import build
from build import OUT, SITE, CSS
import paginas, servicios, guias, guias2, medios, legal

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)

rutas = []

# Comerciales
rutas.append(paginas.home())
rutas.append(servicios.nota_pilar())
rutas.append(servicios.publicar())
rutas.append(servicios.comprar())
rutas.append(servicios.enviar())
rutas.append(servicios.donde())
rutas.append(servicios.gratis())
rutas.append(servicios.enlaces())
rutas.append(servicios.precios())

# Guia
rutas.append(guias.indice())
rutas.append(guias.estructura())
rutas.append(guias.que_es())
rutas.append(guias.como_hacer())
rutas.append(guias.formato())
rutas.append(guias2.ejemplos())
rutas.append(guias2.plantilla())
rutas.append(guias2.evento())
rutas.append(guias2.diferencia())
rutas.append(guias2.ingles())

# Directorio
rutas.append(medios.directorio())

# Legal
rutas.append(legal.contacto())
rutas.append(legal.aviso_legal())
rutas.append(legal.privacidad())
rutas.append(legal.cookies())

# ---- recursos ----
with open(os.path.join(OUT, "estilo.css"), "w", encoding="utf-8") as f:
    f.write(CSS)

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="12" fill="#0b4f9e"/>
<path d="M18 20h28v5H18zM18 30h28v4H18zM18 39h19v4H18z" fill="#fff"/>
</svg>"""
with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(FAVICON)

hoy = datetime.date.today().isoformat()
PRIOR = {"/": "1.0", "/precios/": "0.9", "/nota-de-prensa/": "0.9",
         "/comprar-enlaces-prensa/": "0.9", "/medios/": "0.9",
         "/aviso-legal/": "0.3", "/privacidad/": "0.3", "/cookies/": "0.3"}
urls = []
for r in rutas:
    urls.append("  <url>\n    <loc>{}{}</loc>\n    <lastmod>{}</lastmod>\n"
                "    <priority>{}</priority>\n  </url>".format(
                    SITE, r, hoy, PRIOR.get(r, "0.8")))
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(urls) + "\n</urlset>\n")
with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)

with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
    f.write("User-agent: *\nAllow: /\n\nSitemap: {}/sitemap.xml\n".format(SITE))

HTACCESS = """# Compresion
<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css text/javascript application/javascript application/json image/svg+xml
</IfModule>

# Cache
<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 1 year"
ExpiresByType image/svg+xml "access plus 1 year"
ExpiresByType text/html "access plus 1 hour"
</IfModule>

# Seguridad
<IfModule mod_headers.c>
Header set X-Content-Type-Options "nosniff"
Header set X-Frame-Options "SAMEORIGIN"
Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>

# https y sin www, barra final
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
RewriteCond %{HTTP_HOST} ^www\\.(.*)$ [NC]
RewriteRule ^(.*)$ https://%1/$1 [L,R=301]

ErrorDocument 404 /404.html
"""
with open(os.path.join(OUT, ".htaccess"), "w", encoding="utf-8") as f:
    f.write(HTACCESS)

# 404
err = """<main><div class="wrap" style="padding:80px 0;text-align:center;max-width:600px;margin:0 auto">
<h1>Esta pagina no existe</h1>
<p class="entradilla">Puede que el enlace este mal o que hayamos movido el contenido.</p>
<p style="margin-top:30px"><a href="/" class="btn">Volver al inicio</a>
<a href="/guia/" class="btn ghost" style="margin-left:10px">Ir a la guia</a></p>
</div></main>"""
doc404 = build.BASE.format(title="Pagina no encontrada", desc="La pagina no existe.",
                           canon=SITE + "/404.html", brand=build.BRAND,
                           nav=build.nav_html(), body=err, schema="", ogtype="website")
with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
    f.write(doc404)

print("Paginas generadas: {}".format(len(rutas)))
for r in sorted(rutas):
    print("  " + r)

# ---- acentuacion final sobre el html generado ----
import acentos, io
tocados = 0
for raiz, _, ficheros in os.walk(OUT):
    for fich in ficheros:
        if fich.endswith((".html", ".xml")):
            p = os.path.join(raiz, fich)
            with io.open(p, encoding="utf-8") as f:
                antes = f.read()
            despues = acentos.acentua_html(antes)
            if antes != despues:
                with io.open(p, "w", encoding="utf-8") as f:
                    f.write(despues)
                tocados += 1
print("Ficheros acentuados: {}".format(tocados))
