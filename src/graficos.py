# -*- coding: utf-8 -*-
"""Ilustraciones SVG originales. Sin imagenes externas ni marcas de terceros."""

FIG = """
<figure class="fig">
{svg}
<figcaption>{pie}</figcaption>
</figure>
"""

CSS_FIG = """
.fig{margin:34px 0;padding:0}
.fig svg{width:100%;height:auto;display:block;border:1px solid var(--linea);
  border-radius:var(--radio);background:#fff}
.fig figcaption{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  font-size:14px;color:var(--tinta-3);margin-top:10px;line-height:1.5}
.svg-t{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
"""


def proceso():
    """Los cuatro pasos del servicio."""
    pasos = [("1", "Nos cuentas", "la noticia"), ("2", "La redactamos", "y la apruebas"),
             ("3", "Se publica", "en los medios"), ("4", "Recibes", "el informe")]
    cajas = ""
    x = 40
    for i, (n, l1, l2) in enumerate(pasos):
        cajas += """
  <g>
    <rect x="{x}" y="46" width="158" height="104" rx="10" fill="#fff" stroke="var(--linea)" stroke-width="1.5"/>
    <circle cx="{cx}" cy="76" r="16" fill="var(--acento)"/>
    <text class="svg-t" x="{cx}" y="82" text-anchor="middle" font-size="16" font-weight="700" fill="#fff">{n}</text>
    <text class="svg-t" x="{cx}" y="113" text-anchor="middle" font-size="15" font-weight="600" fill="var(--tinta)">{l1}</text>
    <text class="svg-t" x="{cx}" y="133" text-anchor="middle" font-size="14" fill="var(--tinta-3)">{l2}</text>
  </g>""".format(x=x, cx=x + 79, n=n, l1=l1, l2=l2)
        if i < 3:
            fx = x + 158
            cajas += """
  <path d="M{a} 98 L{b} 98" stroke="var(--acento)" stroke-width="2" stroke-linecap="round"/>
  <path d="M{c} 92 L{b} 98 L{c} 104" fill="none" stroke="var(--acento)" stroke-width="2"
        stroke-linecap="round" stroke-linejoin="round"/>""".format(a=fx + 9, b=fx + 31, c=fx + 25)
        x += 198
    svg = """<svg viewBox="0 0 860 190" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="Las cuatro fases del servicio: nos cuentas la noticia, la redactamos, se publica y recibes el informe">
  <text class="svg-t" x="40" y="28" font-size="13" font-weight="700" fill="var(--acento)"
        letter-spacing="1">DE LA IDEA AL MEDIO</text>
{cajas}
</svg>""".format(cajas=cajas)
    return FIG.format(svg=svg, pie="El proceso completo. Tu intervienes en el primer paso y en la aprobacion del texto.")


def tasa_publicacion():
    """100 cuadros: los que se publican frente a los que no."""
    cuadros = ""
    for i in range(100):
        fila, col = divmod(i, 20)
        x = 40 + col * 29
        y = 60 + fila * 29
        pub = i < 4
        cuadros += ('<rect x="{x}" y="{y}" width="22" height="22" rx="3" fill="{f}" '
                    'stroke="{s}" stroke-width="1"/>').format(
            x=x, y=y, f="var(--acento)" if pub else "#eef0f3",
            s="var(--acento)" if pub else "#dfe3e8")
    svg = """<svg viewBox="0 0 860 260" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="De cada cien notas de prensa enviadas a los medios, entre tres y cinco acaban publicadas">
  <text class="svg-t" x="40" y="30" font-size="13" font-weight="700" fill="var(--acento)"
        letter-spacing="1">DE CADA 100 NOTAS ENVIADAS</text>
  <text class="svg-t" x="40" y="50" font-size="14" fill="var(--tinta-3)">Cada cuadro es una nota de prensa</text>
{cuadros}
  <g transform="translate(660, 95)">
    <text class="svg-t" x="0" y="0" font-size="52" font-weight="700" fill="var(--acento)">3-5</text>
    <text class="svg-t" x="0" y="24" font-size="15" font-weight="600" fill="var(--tinta)">se publican</text>
    <text class="svg-t" x="0" y="52" font-size="30" font-weight="700" fill="var(--tinta-3)">95-97</text>
    <text class="svg-t" x="0" y="74" font-size="15" fill="var(--tinta-3)">no llegan a salir</text>
  </g>
</svg>""".format(cuadros=cuadros)
    return FIG.format(
        svg=svg,
        pie="Solo entre el 3% y el 5% de las notas enviadas a redacciones acaban publicadas. "
            "Por eso un plan con publicacion garantizada cambia tanto el resultado.")


def piramide():
    """Piramide invertida con las partes de la nota."""
    partes = [
        ("Titular", "La noticia en una linea", 0),
        ("Entradilla", "Que, quien, cuando, donde y por que", 1),
        ("Cuerpo", "Datos concretos, de mas a menos", 2),
        ("Cita", "Una declaracion con nombre y cargo", 3),
        ("Contacto", "Telefono que alguien coja", 4),
    ]
    filas = ""
    y = 56
    ancho_max, ancho_min = 560, 200
    for i, (t, d, n) in enumerate(partes):
        w = ancho_max - (ancho_max - ancho_min) * i / 4.0
        x = 40 + (ancho_max - w) / 2.0
        op = 1 - i * 0.14
        filas += """
  <rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="46" rx="6" fill="var(--acento)" opacity="{op:.2f}"/>
  <text class="svg-t" x="{cx:.0f}" y="{ty}" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">{t}</text>
  <text class="svg-t" x="630" y="{ty}" font-size="14" fill="var(--tinta-3)">{d}</text>""".format(
            x=x, y=y, w=w, op=op, cx=x + w / 2.0, ty=y + 28, t=t, d=d)
        y += 54
    svg = """<svg viewBox="0 0 860 340" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="Piramide invertida: titular, entradilla, cuerpo, cita y contacto, de mayor a menor importancia">
  <text class="svg-t" x="40" y="30" font-size="13" font-weight="700" fill="var(--acento)"
        letter-spacing="1">PIRAMIDE INVERTIDA</text>
{filas}
  <path d="M20 60 L20 316" stroke="var(--linea)" stroke-width="1.5"/>
  <text class="svg-t" x="14" y="195" font-size="12" fill="var(--tinta-3)"
        transform="rotate(-90 14 195)" text-anchor="middle">Importancia</text>
</svg>""".format(filas=filas)
    return FIG.format(
        svg=svg,
        pie="Lo mas importante arriba. Un periodista corta por abajo cuando le falta espacio, "
            "asi que el texto tiene que seguir funcionando sin los ultimos parrafos.")


def linea_evento():
    """Las tres notas de un evento sobre una linea de tiempo."""
    hitos = [(150, "-15 dias", "Convocatoria", "Que vaya un periodista"),
             (430, "Dia 0", "Nota del dia", "Que lo publiquen hoy"),
             (710, "+5 dias", "Balance", "Datos para sectoriales")]
    marcas = ""
    for cx, fecha, titulo, sub in hitos:
        marcas += """
  <circle cx="{cx}" cy="120" r="13" fill="#fff" stroke="var(--acento)" stroke-width="3"/>
  <circle cx="{cx}" cy="120" r="5" fill="var(--acento)"/>
  <text class="svg-t" x="{cx}" y="92" text-anchor="middle" font-size="13" font-weight="700"
        fill="var(--acento)">{fecha}</text>
  <text class="svg-t" x="{cx}" y="163" text-anchor="middle" font-size="16" font-weight="700"
        fill="var(--tinta)">{titulo}</text>
  <text class="svg-t" x="{cx}" y="184" text-anchor="middle" font-size="14" fill="var(--tinta-3)">{sub}</text>""".format(
            cx=cx, fecha=fecha, titulo=titulo, sub=sub)
    svg = """<svg viewBox="0 0 860 215" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="Linea de tiempo con las tres notas de prensa de un evento: convocatoria, nota del dia y balance">
  <text class="svg-t" x="40" y="30" font-size="13" font-weight="700" fill="var(--acento)"
        letter-spacing="1">LAS TRES NOTAS DE UN EVENTO</text>
  <path d="M60 120 L800 120" stroke="var(--linea)" stroke-width="3" stroke-linecap="round"/>
{marcas}
</svg>""".format(marcas=marcas)
    return FIG.format(
        svg=svg,
        pie="Un evento lleva tres notas, no una. La tercera es la que casi nadie envia y la que "
            "mas entra en medios sectoriales.")


def comparativa():
    """Nota de prensa frente a enlace en prensa."""
    filas = [("Objetivo", "Notoriedad y cobertura", "Autoridad SEO"),
             ("Publicacion", "Garantizada en el plan", "Garantizada por contrato"),
             ("Eleccion del medio", "Segun sector y provincia", "Lo eliges tu del catalogo"),
             ("Tipo de enlace", "Segun el medio", "Dofollow acordado"),
             ("Se paga", "Plan mensual", "Por medio")]
    y = 92
    cuerpo = ""
    for i, (et, a, b) in enumerate(filas):
        if i % 2 == 0:
            cuerpo += '<rect x="40" y="{y}" width="780" height="42" fill="#fafaf8"/>'.format(y=y - 26)
        cuerpo += """
  <text class="svg-t" x="54" y="{y}" font-size="14" font-weight="600" fill="var(--tinta)">{et}</text>
  <text class="svg-t" x="310" y="{y}" font-size="14" fill="var(--tinta-2)">{a}</text>
  <text class="svg-t" x="580" y="{y}" font-size="14" fill="var(--tinta-2)">{b}</text>""".format(
            y=y, et=et, a=a, b=b)
        y += 42
    svg = """<svg viewBox="0 0 860 315" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="Comparacion entre una nota de prensa y un enlace en prensa segun objetivo, publicacion, eleccion del medio, tipo de enlace y forma de pago">
  <text class="svg-t" x="40" y="30" font-size="13" font-weight="700" fill="var(--acento)"
        letter-spacing="1">DOS PRODUCTOS DISTINTOS</text>
  <rect x="300" y="44" width="260" height="248" rx="8" fill="#f3f7fc"/>
  <text class="svg-t" x="310" y="66" font-size="15" font-weight="700" fill="var(--acento)">Nota de prensa</text>
  <text class="svg-t" x="580" y="66" font-size="15" font-weight="700" fill="var(--tinta)">Enlace en prensa</text>
  <path d="M40 76 L820 76" stroke="var(--linea)" stroke-width="1.5"/>
{cuerpo}
</svg>""".format(cuerpo=cuerpo)
    return FIG.format(
        svg=svg,
        pie="La nota busca que hablen de ti; el enlace busca mover posiciones en Google. "
            "Se contratan por separado porque funcionan distinto.")


def cobertura(n_medios, etiqueta):
    """Puntos que representan la cobertura de un plan."""
    puntos = ""
    for i in range(n_medios):
        fila, col = divmod(i, 20)
        puntos += '<circle cx="{x}" cy="{y}" r="5.5" fill="var(--acento)" opacity="0.85"/>'.format(
            x=30 + col * 19, y=30 + fila * 19)
    alto = 30 + ((n_medios - 1) // 20 + 1) * 19
    svg = """<svg viewBox="0 0 420 {alto}" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="{et}">
  <text class="svg-t" x="30" y="16" font-size="12" font-weight="700" fill="var(--tinta-3)"
        letter-spacing=".5">{et}</text>
{puntos}
</svg>""".format(alto=alto, et=etiqueta, puntos=puntos)
    return svg
