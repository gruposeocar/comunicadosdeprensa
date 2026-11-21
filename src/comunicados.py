# -*- coding: utf-8 -*-
"""Seccion de comunicados por categoria. Contenido propio en cada una."""
from build import escribir, migas, faq_html, FORMULARIO, CAJA_LATERAL, articulo_schema

# slug, nombre, titulo-h1, que es noticia, que no, consejo
CATS = [
    ("inmobiliario", "Inmobiliario",
     "Los medios locales publican datos de vivienda con mucha facilidad porque los piden sus lectores y "
     "casi nunca los tienen desagregados por ciudad.",
     ["Precio medio de compra o alquiler en tu zona, con tus propios contratos como fuente",
      "Apertura de oficina o entrada en una comarca nueva",
      "Operaciones singulares: un edificio rehabilitado, un pazo, suelo industrial",
      "Cambios normativos y como afectan al comprador de tu provincia"],
     "Que has vendido muchos pisos este mes o que tu equipo es el mejor de la zona.",
     "Si llevas una agencia, lo que mas rinde es publicar un informe trimestral con tus propios datos. "
     "Un medio local lo publica casi seguro y te convierte en la fuente a la que llaman la proxima vez."),

    ("tecnologia", "Tecnologia y software",
     "Es el sector con mas competencia por el espacio: todo el mundo lanza algo. Lo que separa una nota "
     "publicada de una descartada es que resuelva un problema reconocible.",
     ["Un producto que hace algo que antes no se podia hacer",
      "Una ronda de inversion, con cifra y nombres de los inversores",
      "Datos de uso propios: cuantos usuarios, que patron has detectado",
      "Alianzas con empresas que el lector reconozca"],
     "Una version nueva con mejoras menores, un rediseno o una integracion mas.",
     "Evita el vocabulario de inversor. Si un periodista generalista no entiende en una frase que hace tu "
     "producto, no va a escribir sobre el."),

    ("salud", "Salud y bienestar",
     "Es el sector con mas interes del lector y mas cuidado editorial. Los medios piden respaldo para "
     "cualquier afirmacion.",
     ["Apertura de clinica, nueva especialidad o equipamiento que no habia en la zona",
      "Resultados de un estudio propio o participacion en uno publicado",
      "Campanas de prevencion con datos locales",
      "Incorporacion de profesionales con trayectoria reconocible"],
     "Afirmaciones sobre resultados de tratamientos sin estudio detras. Es terreno regulado.",
     "Cuida mucho el lenguaje: no prometas curaciones ni resultados. Una nota de salud que exagera no solo "
     "no se publica, puede traerte un problema con Sanidad."),

    ("energia", "Energia y sostenibilidad",
     "Con los precios de la luz en la conversacion publica, cualquier dato concreto sobre consumo o ahorro "
     "tiene salida facil en prensa.",
     ["Instalaciones destacadas: autoconsumo en un poligono, una comunidad, una nave",
      "Datos propios de ahorro medio de tus clientes",
      "Analisis de como afecta un cambio regulatorio o tarifario a los hogares de tu zona",
      "Certificaciones y acuerdos con administraciones"],
     "Ofertas comerciales disfrazadas de noticia. Un titular con un precio es publicidad.",
     "Los datos comparativos funcionan muy bien: cuanto paga de media un hogar de tu provincia frente a la "
     "media nacional es el tipo de dato que un medio local busca activamente."),

    ("legal", "Legal y asesoria",
     "Los despachos tienen una ventaja enorme y la desaprovechan: pueden explicar sentencias y cambios "
     "normativos antes que nadie, y eso los medios lo necesitan cada semana.",
     ["Interpretacion de una sentencia relevante para el ciudadano de a pie",
      "Como afecta una reforma legal a un colectivo concreto",
      "Datos de tu despacho: cuantos casos de un tipo, que porcentaje prospera",
      "Incorporaciones, fusiones o apertura de sede"],
     "Publicidad de servicios juridicos encubierta, que ademas choca con el codigo deontologico.",
     "La clave es la rapidez. Una nota explicando una sentencia el mismo dia que se conoce entra en medios "
     "que no te cogerian el telefono en otro momento."),

    ("turismo", "Turismo y hosteleria",
     "Los medios de viajes y las secciones de ocio tienen un hueco permanente que llenar y agradecen el "
     "material bien preparado, sobre todo con fotos.",
     ["Apertura de alojamiento, restaurante o experiencia nueva",
      "Datos de ocupacion de tu zona en un puente o temporada",
      "Reconocimientos gastronomicos y guias",
      "Propuestas estacionales con enfoque local"],
     "Promociones y descuentos. Eso es publicidad y va a la seccion de pago.",
     "En este sector la foto vale tanto como el texto. Una imagen horizontal, en alta y bien iluminada "
     "multiplica las posibilidades, porque el medio necesita ilustrar."),

    ("formacion", "Formacion y empleo",
     "Las cifras de empleo y de matriculacion interesan siempre, y los centros de formacion suelen tener "
     "datos propios que nadie mas publica.",
     ["Datos de insercion laboral de tus alumnos",
      "Programas nuevos ligados a sectores con falta de personal",
      "Acuerdos con empresas para practicas o contratacion",
      "Becas y ayudas, con plazos concretos"],
     "El catalogo de cursos. Un listado de precios no es una noticia.",
     "Los datos de insercion son oro para la prensa local, sobre todo si los cruzas con los sectores que "
     "no encuentran trabajadores en tu comarca."),

    ("construccion", "Construccion y reformas",
     "Las ayudas a la rehabilitacion y la eficiencia energetica han puesto el sector en las paginas de "
     "economia local de forma permanente.",
     ["Obras singulares o rehabilitaciones con antes y despues",
      "Como solicitar una ayuda y que plazos hay, explicado en claro",
      "Datos de coste medio por tipo de reforma en tu provincia",
      "Incorporacion de tecnicas o materiales poco habituales en la zona"],
     "Presupuestos y ofertas. Tambien el autobombo sobre la calidad del trabajo.",
     "Explicar bien una ayuda publica es de lo que mas se publica y mas trafico te trae, porque la gente "
     "lo busca activamente cuando se abre el plazo."),

    ("alimentacion", "Alimentacion y agroalimentario",
     "El producto local tiene una puerta abierta en prensa regional, y mas si hay historia de familia, "
     "relevo generacional o denominacion de origen detras.",
     ["Premios y reconocimientos en catas o certamenes",
      "Entrada en una denominacion de origen o certificacion",
      "Datos de campana: produccion, precios, afectacion del clima",
      "Exportacion a un mercado nuevo"],
     "Lanzamientos de producto sin nada que los distinga de los que ya hay.",
     "La historia humana funciona aqui mejor que en ningun otro sector: quien lo hace, desde cuando y por "
     "que, es lo que convierte un producto en reportaje."),

    ("empresas", "Empresas y economia",
     "La categoria general para todo lo que no encaja en un sector concreto: resultados, cambios "
     "societarios, expansion y responsabilidad social.",
     ["Resultados anuales, facturacion o crecimiento, con cifras",
      "Apertura de sede, fusion o adquisicion",
      "Nombramientos en puestos de direccion",
      "Proyectos con impacto en el empleo local"],
     "Aniversarios sin nada que contar y notas sobre la cultura interna de la empresa.",
     "Si vas a dar cifras, dalas completas. Una nota que dice que creces mucho sin decir cuanto se "
     "interpreta como que el dato real no es bueno."),
]


def categoria(slug, nombre, intro, si_noticia, no_noticia, consejo):
    bar, bar_ld = migas([("Inicio", "/"), ("Comunicados", "/comunicados/"), (nombre, None)])
    lis = "".join("<li>{}</li>".format(x) for x in si_noticia)
    otras = "".join(
        '<li><a href="/comunicados/{}/">{}</a></li>'.format(s, n)
        for s, n, _, _, _, _ in CATS if s != slug)
    preguntas = [
        ("Que medios publican notas de prensa de {}".format(nombre.lower()),
         "Medios sectoriales del ramo y prensa generalista y economica, tanto nacional como de tu "
         "provincia. Puedes filtrar unos y otros en nuestro directorio de medios."),
        ("Cuanto cuesta publicar una nota de prensa de {}".format(nombre.lower()),
         "Los planes empiezan en 179 euros al mes con publicacion garantizada en 50 medios digitales, "
         "redaccion incluida y sin permanencia."),
        ("Podeis escribirla vosotros",
         "Si. Nos cuentas que quieres anunciar en una conversacion de diez minutos y te devolvemos el "
         "texto para que lo apruebes antes de que salga."),
    ]
    faq, faq_ld = faq_html(preguntas)
    cuerpo = """
{bar}
<main><div class="wrap"><div class="cols">
<article class="contenido">
<h1>Notas de prensa de {nombre}</h1>
<p class="entradilla">{intro}</p>

<h2>Que se publica en este sector</h2>
<ul>{lis}</ul>

<h2>Que no va a publicarse</h2>
<p>{no}</p>

<h2>El consejo que damos a nuestros clientes</h2>
<p>{consejo}</p>

<h2>Publicaciones recientes</h2>
<p style="color:var(--tinta-3);border:1px dashed var(--linea);border-radius:var(--radio);
   padding:20px;background:var(--crema)">Aqui apareceran las notas de prensa de {nombre_min} que
publiquemos. Si quieres que la tuya sea de las primeras, el plan basico son 179&nbsp;&euro; al mes con
publicacion garantizada en 50 medios.</p>

<h2>Como enviamos tu nota</h2>
<p>La redactamos a partir de lo que nos cuentes, te la pasamos para que la apruebes y la publicamos con
enlace a tu web en los medios de tu plan. Despues recibes el informe con el enlace de cada publicacion.
Puedes ver el detalle en <a href="/precios/">precios</a>.</p>

<h2>Otras categorias</h2>
<ul>{otras}</ul>

{faq}
</article>
{caja}
</div></div></main>
""".format(bar=bar, nombre=nombre, nombre_min=nombre.lower(), intro=intro, lis=lis,
           no=no_noticia, consejo=consejo, otras=otras, faq=faq, caja=CAJA_LATERAL)
    ruta = "/comunicados/{}/".format(slug)
    titulo = "Notas de prensa de {}: que publicar y donde".format(nombre.lower())
    desc = ("Que se considera noticia en {} y que no, con los medios que lo publican y como enviar tu "
            "nota de prensa del sector.".format(nombre.lower()))
    return escribir(ruta, titulo, desc, cuerpo,
                    [bar_ld, faq_ld, articulo_schema(titulo, desc, ruta)], "/comunicados/", "article")


def indice():
    bar, bar_ld = migas([("Inicio", "/"), ("Comunicados", None)])
    tarjetas = ""
    for slug, nombre, intro, _, _, _ in CATS:
        tarjetas += """
  <div class="caja">
    <h3><a href="/comunicados/{s}/">{n}</a></h3>
    <p>{i}</p>
  </div>""".format(s=slug, n=nombre, i=intro.split(".")[0] + ".")
    cuerpo = """
{bar}
<main><div class="wrap">
<article style="max-width:760px;padding-top:26px">
<h1>Comunicados por categoria</h1>
<p class="entradilla">Que se considera noticia en cada sector, que se descarta siempre y como enfocar tu
nota para que un periodista la lea entera. Una guia por categoria, y debajo las notas que vamos publicando.</p>
<p>Si no sabes en cual encaja lo tuyo, empieza por <a href="/comunicados/empresas/">empresas y
economia</a>, que recoge todo lo que no es de un sector concreto.</p>
</article>

<div class="rejilla" style="margin-top:40px">
{tarjetas}
</div>

<div style="max-width:760px;margin-top:50px">
<h2>Por que publicamos esto</h2>
<p>Porque la pregunta que mas nos hacen no es cuanto cuesta, es si lo que tienen da para noticia. Estas
paginas responden a eso por sectores, con los criterios que aplicamos nosotros antes de aceptar un encargo.</p>
<p>Si despues de leerlo sigues con dudas, cuentanoslo y te decimos si lo tuyo tiene recorrido. Esa
consulta no se cobra.</p>
</div>
</div></main>
""".format(bar=bar, tarjetas=tarjetas)
    return escribir("/comunicados/", "Comunicados de prensa por categoria y sector",
                    "Que es noticia en cada sector y como enfocar tu nota de prensa: inmobiliario, "
                    "tecnologia, salud, energia, legal, turismo, formacion y mas.",
                    cuerpo, [bar_ld], "/comunicados/")


def todas():
    rutas = [indice()]
    for slug, nombre, intro, si, no, consejo in CATS:
        rutas.append(categoria(slug, nombre, intro, si, no, consejo))
    return rutas
