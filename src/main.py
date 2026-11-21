# -*- coding: utf-8 -*-
"""Genera el sitio completo en dist/"""
import os, shutil, datetime
import build
from build import OUT, SITE, CSS
import paginas, servicios, guias, guias2, medios, legal, comunicados

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

# Comunicados por categoria
rutas.extend(comunicados.todas())

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

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40">
<rect width="40" height="40" rx="8" fill="#0b4f9e"/>
<rect x="9" y="8" width="22" height="26" rx="3" fill="#fff"/>
<rect x="13" y="13" width="14" height="3.4" rx="1.2" fill="#0b4f9e"/>
<rect x="13" y="20" width="14" height="2" rx="1" fill="#9aa4b1"/>
<rect x="13" y="24.5" width="14" height="2" rx="1" fill="#9aa4b1"/>
<rect x="13" y="29" width="9" height="2" rx="1" fill="#9aa4b1"/>
<circle cx="31" cy="10" r="5.5" fill="#c8102e" stroke="#0b4f9e" stroke-width="1.6"/>
</svg>"""
with open(os.path.join(OUT, "favicon.svg"), "w", encoding="utf-8") as f:
    f.write(FAVICON)

hoy = datetime.date.today().isoformat()
PRIOR = {"/": "1.0", "/precios/": "0.9", "/nota-de-prensa/": "0.9",
         "/comprar-enlaces-prensa/": "0.9", "/medios/": "0.9", "/comunicados/": "0.9",
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

# Nada de codigo fuente ni metadatos del repositorio accesibles por web
RedirectMatch 404 ^/src/
RedirectMatch 404 ^/README\\.md$
RedirectMatch 404 ^/\\.git
RedirectMatch 404 ^/\\.gitignore$
<FilesMatch "\\.(py|md|yml|yaml|json|lock)$">
Require all denied
</FilesMatch>
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
