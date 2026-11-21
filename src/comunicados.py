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

# slug -> (titular_malo, titular_bueno1, titular_bueno2, cuando, errores[3], medios_txt)
DETALLE = {
 "inmobiliario": (
  "Inmobiliaria X celebra su decimo aniversario con grandes resultados",
  "El alquiler en Ferrol sube un 11% y es el mayor aumento de la provincia",
  "Una agencia de Ferrolterra detecta que el 40% de los compradores ya son de fuera de Galicia",
  "Enero y septiembre concentran las decisiones de compra, asi que los informes de precios rinden mas "
  "si salen la primera semana de esos meses. El verano funciona para alquiler vacacional y el cierre de "
  "ano para balances.",
  ["Dar precios sin decir de donde salen. Si no explicas la muestra, el periodista no lo publica.",
   "Mezclar el informe con la promocion de tus inmuebles en la misma nota.",
   "Hablar de metro cuadrado sin concretar zona: el dato provincial no interesa en la prensa local."],
  "Prensa local y provincial, secciones de economia de los generalistas, y medios sectoriales como "
  "Idealista News, Brainsre o Metros2 para operaciones grandes."),
 "tecnologia": (
  "Nuestra startup lanza la version 3.0 de su plataforma",
  "Una empresa gallega desarrolla un sistema que detecta fugas de agua antes de que sean visibles",
  "El 62% de las pymes espanolas sigue sin copia de seguridad automatica, segun un analisis de 400 casos",
  "Evita las semanas del Mobile World Congress y de los grandes eventos del sector: compites con todo "
  "el mundo. Septiembre y enero son los mejores meses.",
  ["Explicar la tecnologia en vez del problema que resuelve.",
   "Usar vocabulario de ronda de inversion en una nota dirigida a prensa generalista.",
   "Anunciar funcionalidades menores como si fueran lanzamientos."],
  "Xataka, Hipertextual, Computer Hoy y ComputerWorld en lo sectorial; secciones de tecnologia de los "
  "generalistas y medios economicos si hay cifras de negocio."),
 "salud": (
  "La clinica X ofrece los mejores tratamientos de la ciudad",
  "Una clinica de Ferrol incorpora el primer equipo de diagnostico por imagen de la comarca",
  "El 30% de los pacientes de una consulta gallega llega con un diagnostico previo erroneo de internet",
  "Las campanas de prevencion funcionan ligadas a dias mundiales, pero hay mucha competencia: busca el "
  "angulo local con datos propios en vez de sumarte al dia sin mas.",
  ["Prometer resultados o curaciones. Ademas de no publicarse, puede acarrearte un expediente.",
   "Usar testimonios de pacientes sin consentimiento expreso por escrito.",
   "Dar cifras de eficacia sin estudio publicado detras."],
  "Redaccion Medica, ConSalud, El Medico Interactivo y Gaceta Medica en lo sectorial; prensa local para "
  "aperturas y equipamiento."),
 "energia": (
  "Instaladora X, lider en placas solares de Galicia",
  "Un poligono de Ferrolterra cubre ya el 40% de su consumo con autoconsumo compartido",
  "Las familias gallegas pagan 18 euros mas al mes que la media espanola, segun un analisis de 1.200 facturas",
  "Octubre y noviembre, cuando llega el frio y se habla de la factura, son los meses con mas hueco. "
  "Tambien cada revision tarifaria o cambio regulatorio.",
  ["Convertir la nota en una oferta comercial con precios.",
   "Dar ahorros medios sin explicar sobre que muestra se calculan.",
   "Prometer amortizaciones concretas sin matizar que dependen del consumo."],
  "El Periodico de la Energia, Energias Renovables, PV Magazine y Energy News; prensa local y economica "
  "para instalaciones concretas."),
 "legal": (
  "El despacho X, referente en derecho laboral",
  "Una sentencia obliga a las companias a devolver los gastos de hipoteca tambien en subrogaciones",
  "El 70% de las reclamaciones por clausulas abusivas prospera, segun los datos de un despacho gallego",
  "La rapidez lo es todo: el mismo dia que se conoce una sentencia o entra en vigor una reforma. "
  "Pasadas 48 horas, el tema ya no es noticia.",
  ["Escribir en jerga juridica. Si hay que leerlo dos veces, no se publica.",
   "Opinar sobre casos en los que intervienes sin advertirlo.",
   "Hacer publicidad de servicios, que ademas choca con el codigo deontologico."],
  "Confilegal, Legal Today, Economist & Jurist e Iberian Lawyer; secciones de tribunales de los "
  "generalistas cuando la sentencia afecta al ciudadano."),
 "turismo": (
  "El hotel X abre sus puertas con las mejores instalaciones",
  "Abre en Valdovino el primer alojamiento de la comarca con acceso directo a la playa para sillas de ruedas",
  "La ocupacion en Ferrolterra alcanza el 86% en el puente de agosto, nueve puntos mas que en 2025",
  "Las secciones de viajes cierran contenidos con semanas de antelacion: manda la nota con quince dias "
  "de margen antes de cada puente o temporada.",
  ["Enviar la nota sin fotos en alta resolucion.",
   "Anunciar ofertas y descuentos, que van a publicidad.",
   "Describir el establecimiento en vez de contar que hay de nuevo."],
  "Hosteltur, Preferente, Tourinews y Smart Travel News; suplementos de viajes y prensa local."),
 "formacion": (
  "El centro X abre matricula para sus cursos",
  "El 82% de los alumnos de un ciclo de FP en Ferrol encuentra trabajo en menos de seis meses",
  "Un centro gallego crea el primer curso de mantenimiento eolico marino de la comunidad",
  "Mayo y junio, cuando se decide la matricula, y septiembre con el arranque de curso. Los datos de "
  "insercion funcionan todo el ano.",
  ["Publicar el catalogo de cursos con precios.",
   "Dar porcentajes de insercion sin decir sobre cuantos alumnos.",
   "Anunciar titulaciones sin aclarar si son oficiales o propias."],
  "Prensa local y secciones de educacion y empleo de los generalistas; medios de RRHH como Equipos y "
  "Talento o RRHH Digital cuando hay acuerdo con empresas."),
 "construccion": (
  "Reformas X, calidad y confianza desde hace 20 anos",
  "Las ayudas a la rehabilitacion dejan sin solicitar el 45% del presupuesto en Ferrolterra",
  "Rehabilitar una vivienda de los anos setenta cuesta de media 31.000 euros en la comarca",
  "Cada apertura de plazo de ayudas es una oportunidad inmediata. El invierno concentra las consultas "
  "sobre aislamiento y humedades.",
  ["Enviar un presupuesto tipo disfrazado de noticia.",
   "Explicar una ayuda sin dar el plazo y el organismo exactos.",
   "Mostrar obras sin permiso del propietario para publicar las imagenes."],
  "Construible, CIC Construccion e Interempresas en lo sectorial; prensa local para ayudas y obras "
  "concretas."),
 "alimentacion": (
  "Nuestros productos, los mejores de la zona",
  "Un obradoiro de Naron gana el premio al mejor pan de centeno de Galicia",
  "La cosecha de mejillon cae un 20% en la ria y los productores adelantan la campana",
  "Las campanas marcan el calendario: vendimia, matanza, Navidad y cada fecha de recoleccion. Los "
  "premios se publican el mismo dia del fallo.",
  ["Describir el producto en vez de contar que ha pasado.",
   "Dar datos de produccion sin fuente ni comparativa.",
   "Olvidar la foto del producto o del productor."],
  "Alimarket, ARAL, Distribucion Actualidad y Agrodigital; prensa local y suplementos gastronomicos."),
 "empresas": (
  "La empresa X sigue creciendo y mirando al futuro",
  "Una empresa de Ferrol cierra 2026 con 4,2 millones de facturacion y doce contrataciones",
  "Dos companias gallegas se fusionan para crear el mayor operador logistico del noroeste",
  "Los resultados anuales se publican entre enero y marzo. Los nombramientos, el mismo dia que son "
  "efectivos.",
  ["Decir que creces mucho sin dar la cifra: se interpreta como que el dato no es bueno.",
   "Anunciar aniversarios sin nada mas que contar.",
   "Hablar de cultura interna de empresa, que no interesa fuera."],
  "Expansion, Cinco Dias, El Economista y Economia Digital; prensa economica regional y local."),
}


def categoria(slug, nombre, intro, si_noticia, no_noticia, consejo):
    tm, tb1, tb2, cuando, errores_l, medios_txt = DETALLE[slug]
    errores = "".join("<li>{}</li>".format(e) for e in errores_l)
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
        ("Cuantas notas al ano conviene publicar en este sector",
         "Entre cuatro y ocho para una pyme, es decir una cada mes o dos. Mas frecuencia sin noticias "
         "reales detras desgasta la relacion con las redacciones y acaba restando."),
        ("Sirve si mi empresa es pequena y local",
         "Si, y suele funcionar mejor que en las grandes: la prensa local tiene menos competencia por el "
         "espacio que la nacional, y un negocio de la comarca con un dato propio entra con facilidad."),
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

<h2>Tres titulares, uno malo y dos buenos</h2>
<p>El titular decide si el periodista sigue leyendo. Estos tres estan escritos sobre casos de este
sector y la diferencia entre ellos explica casi todo:</p>
<table>
  <tr><th>Titular</th><th>Por que</th></tr>
  <tr><td>{tm}</td><td>No hay hecho, no hay dato y el sujeto es la empresa. Se descarta sin leer el resto.</td></tr>
  <tr><td><strong>{tb1}</strong></td><td>Hecho concreto, lugar y cifra. Se puede publicar tal cual.</td></tr>
  <tr><td><strong>{tb2}</strong></td><td>Dato propio que nadie mas tiene, con la muestra implicita.</td></tr>
</table>

<h2>Cuando conviene publicar</h2>
<p>{cuando}</p>

<h2>Errores que se repiten en este sector</h2>
<ul>{errores}</ul>

<h2>Que medios cubren {nombre_min}</h2>
<p>{medios_txt} Puedes filtrarlos por provincia y por tematica en el
<a href="/medios/">directorio de medios</a>.</p>

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
           no=no_noticia, consejo=consejo, otras=otras, faq=faq, caja=CAJA_LATERAL,
           tm=tm, tb1=tb1, tb2=tb2, cuando=cuando, errores=errores, medios_txt=medios_txt)
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
<h2>Lo que comparten todos los sectores</h2>
<p>Cambian los medios y cambia el calendario, pero el criterio que aplica un periodista es el mismo en
los diez: <strong>hay noticia cuando el hecho le importa a alguien que no te conoce</strong>. Todo lo
demas se deriva de ahi.</p>
<p>De ese criterio salen tres constantes que vas a encontrar repetidas en cada categoria:</p>
<ul>
  <li><strong>El dato propio gana siempre.</strong> Sea el precio del alquiler, la ocupacion hotelera o
  el porcentaje de insercion laboral, la cifra que solo tu puedes dar es lo que convierte una nota en
  noticia. Y te convierte a ti en la fuente a la que llaman la proxima vez.</li>
  <li><strong>Lo local pesa mas de lo que parece.</strong> Un medio de tu provincia tiene menos
  competencia por el espacio que uno nacional, y sus lectores son mas probables como clientes. Para una
  pyme, salir en el periodico de la comarca vale mas que una mencion perdida en un medio grande.</li>
  <li><strong>La publicidad se detecta a la primera.</strong> En cuanto aparece un precio, una oferta o
  un adjetivo sin respaldo, el texto deja de ser noticia y pasa a la carpeta de publicidad, que se
  paga aparte y se lee mucho menos.</li>
</ul>

<h2>Como elegimos la categoria de tu nota</h2>
<p>Una misma empresa puede encajar en varias. Una instaladora de placas solares es energia, pero si lo
que anuncia es una contratacion masiva es empresas, y si explica una ayuda publica puede ser
construccion. Lo que decide no es tu actividad, es <em>el hecho que vas a contar</em>.</p>
<p>En la practica elegimos la categoria por donde esta el lector que te interesa. Si buscas clientes
particulares, la prensa generalista y local; si buscas acuerdos con otras empresas, el medio sectorial.
Esa decision cambia el enfoque del texto, no solo donde se envia.</p>

<h2>Si tu sector no esta en la lista</h2>
<p>Trabajamos con cualquier actividad legal. Estas diez son las categorias con mas demanda, pero
publicamos notas de talleres, veterinarios, asociaciones, despachos de arquitectura, clubes deportivos
o ayuntamientos. El criterio para saber si hay noticia es el mismo, y te lo decimos antes de cobrarte
nada.</p>

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
