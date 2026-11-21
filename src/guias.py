# -*- coding: utf-8 -*-
"""Guia de contenidos: el bloque que trae el trafico"""
from build import escribir, migas, faq_html, CAJA_LATERAL, articulo_schema


def guia(ruta, h1, titulo, desc, entradilla, cuerpo_html, preguntas, actualizado="Noviembre de 2026"):
    bar, bar_ld = migas([("Inicio", "/"), ("Guia", "/guia/"), (h1, None)])
    faq, faq_ld = faq_html(preguntas)
    cuerpo = """
{bar}
<main><div class="wrap"><div class="cols">
<article class="contenido">
<h1>{h1}</h1>
<p class="entradilla">{ent}</p>
<p style="font-family:-apple-system,sans-serif;font-size:14px;color:var(--tinta-3);
   border-bottom:1px solid var(--linea);padding-bottom:16px">Actualizado: {act}</p>
{cuerpo}
{faq}
<div class="card" style="margin-top:44px">
  <h3>Prefieres que lo hagamos nosotros</h3>
  <p>Escribimos la nota, la publicamos y la enviamos a los medios de tu sector. Desde 95&nbsp;&euro;, sin permanencia.</p>
  <a href="/precios/#cotizar" class="btn">Ver precios</a>
</div>
</article>
{caja}
</div></div></main>
""".format(bar=bar, h1=h1, ent=entradilla, act=actualizado, cuerpo=cuerpo_html,
           faq=faq, caja=CAJA_LATERAL)
    return escribir(ruta, titulo, desc, cuerpo,
                    [bar_ld, faq_ld, articulo_schema(titulo, desc, ruta)], "/guia/", "article")


def indice():
    bar, bar_ld = migas([("Inicio", "/"), ("Guia", None)])
    cuerpo = """
{bar}
<main><div class="wrap">
<article style="max-width:760px;padding-top:26px">
<h1>Guia de la nota de prensa</h1>
<p class="entradilla">Todo lo que necesitas para escribir y enviar una nota de prensa por tu cuenta.
Publicado entero y gratis: no hay registro, ni correo que dejar, ni PDF que descargar.</p>
</article>

<div class="rejilla" style="margin-top:44px">
  <div class="caja">
    <div class="num">Empieza aqui</div>
    <h3><a href="/guia/que-es-una-nota-de-prensa/">Que es una nota de prensa</a></h3>
    <p>Para que sirve, quien la lee de verdad y cuando merece la pena enviarla.</p>
  </div>
  <div class="caja">
    <div class="num">Lo esencial</div>
    <h3><a href="/guia/estructura-de-una-nota-de-prensa/">Estructura</a></h3>
    <p>Las siete partes, en orden, con lo que va en cada una.</p>
  </div>
  <div class="caja">
    <div class="num">Paso a paso</div>
    <h3><a href="/guia/como-hacer-una-nota-de-prensa/">Como hacerla</a></h3>
    <p>De la idea al texto final, en siete pasos y con los errores senalados.</p>
  </div>
  <div class="caja">
    <div class="num">Modelos</div>
    <h3><a href="/guia/ejemplos-de-notas-de-prensa/">Ejemplos reales</a></h3>
    <p>Notas completas por tipo de anuncio, listas para adaptar.</p>
  </div>
  <div class="caja">
    <div class="num">Descarga</div>
    <h3><a href="/guia/plantilla-nota-de-prensa/">Plantilla</a></h3>
    <p>El esqueleto en blanco con las indicaciones dentro.</p>
  </div>
  <div class="caja">
    <div class="num">Detalle</div>
    <h3><a href="/guia/formato-nota-de-prensa/">Formato</a></h3>
    <p>Tipografia, extension, margenes y como se manda por correo.</p>
  </div>
  <div class="caja">
    <div class="num">Caso concreto</div>
    <h3><a href="/guia/nota-de-prensa-evento/">Para un evento</a></h3>
    <p>Antes, durante y despues: las tres notas que lleva un evento.</p>
  </div>
  <div class="caja">
    <div class="num">Duda comun</div>
    <h3><a href="/guia/diferencia-nota-y-comunicado/">Nota o comunicado</a></h3>
    <p>Si son lo mismo, cuando se usa cada termino y por que da igual.</p>
  </div>
  <div class="caja">
    <div class="num">Internacional</div>
    <h3><a href="/guia/nota-de-prensa-en-ingles/">En ingles</a></h3>
    <p>Press release: estructura, vocabulario y lo que cambia respecto al espanol.</p>
  </div>
</div>

<div style="max-width:760px;margin-top:50px">
<h2>Por que publicamos esto gratis</h2>
<p>Porque la mayoria de la gente que busca como escribir una nota de prensa va a escribirla ella misma,
y eso esta bien. Si la guia te sirve y la escribes tu, perfecto. Y si en algun momento prefieres no
dedicarle la tarde, ya sabes donde estamos.</p>
<p>Lo que no vas a encontrar aqui es contenido recortado para obligarte a pedir presupuesto. Estan los
ejemplos enteros y la plantilla completa.</p>
</div>
</div></main>
""".format(bar=bar)
    return escribir("/guia/", "Guia completa de la nota de prensa: estructura, ejemplos y plantilla",
                    "Guia gratuita para escribir una nota de prensa: que es, estructura, ejemplos reales, "
                    "plantilla descargable, formato y como enviarla a los medios.",
                    cuerpo, [bar_ld], "/guia/")


def estructura():
    c = """
<p>Una nota de prensa tiene siete partes y el orden no es negociable. Un periodista lee de arriba abajo
y abandona en cuanto deja de encontrar informacion nueva, asi que lo mas importante va primero. Es lo
que en redaccion se llama piramide invertida.</p>

<h2>1. Titular</h2>
<p>Una linea, maximo quince palabras, escrita como la publicaria el medio. No es el nombre de tu
empresa seguido de dos puntos: es la noticia.</p>
<p><strong>Mal:</strong> <em>Talleres Gomez: nueva apertura</em><br>
<strong>Bien:</strong> <em>Un taller de Ferrol abre el primer punto de carga rapida para electricos de la comarca</em></p>
<p>El segundo funciona porque contiene el hecho, el lugar y por que importa. El primero obliga al
periodista a investigar para saber si le interesa, y no lo va a hacer.</p>

<h2>2. Subtitulo</h2>
<p>Una frase que anada el dato que refuerza el titular. Cifras, plazos o contexto. Si el titular dice
que abre un punto de carga, el subtitulo dice cuantos vehiculos atendera al dia y cuanto se ha invertido.</p>

<h2>3. Lugar y fecha</h2>
<p>Al inicio del primer parrafo, con el formato que usan las agencias: <em>Ferrol, 21 de noviembre de
2026.</em> Parece un detalle menor pero le dice al redactor que sabes como funciona esto.</p>

<h2>4. Entradilla</h2>
<p>El parrafo clave. Debe responder las cinco preguntas basicas del periodismo en tres o cuatro lineas:</p>
<ul>
  <li><strong>Que</strong> ha pasado.</li>
  <li><strong>Quien</strong> lo ha hecho.</li>
  <li><strong>Cuando</strong> ocurre o ha ocurrido.</li>
  <li><strong>Donde</strong>.</li>
  <li><strong>Por que</strong> es relevante.</li>
</ul>
<p>Si un periodista solo lee este parrafo, debe poder escribir una noticia breve con el. Esa es la
prueba de que esta bien hecho.</p>

<h2>5. Cuerpo</h2>
<p>Dos o tres parrafos de desarrollo, de mas a menos importante. Aqui van los datos concretos: cifras,
plazos, caracteristicas, contexto del sector. Cada parrafo debe poder cortarse sin que el texto se
rompa, porque es exactamente lo que va a hacer el redactor si le falta espacio.</p>
<p>Nada de adjetivos sin respaldo. <em>Lider del sector</em> no significa nada; <em>la empresa con mas
instalaciones en la provincia segun el registro X</em> si.</p>

<h2>6. Cita</h2>
<p>Una declaracion entrecomillada, atribuida a una persona con nombre y cargo. No una, dos o tres:
una, buena. Debe aportar interpretacion o compromiso, algo que no cabe en la parte informativa.</p>
<p><strong>Inutil:</strong> <em>&laquo;Estamos muy contentos con este proyecto&raquo;</em><br>
<strong>Util:</strong> <em>&laquo;Si la demanda sigue como el primer mes, en 2027 tendremos que doblar
los puntos de carga&raquo;</em></p>

<h2>7. Datos de contacto y boilerplate</h2>
<p>Al final, nombre, telefono directo y correo de una persona que vaya a responder. Un telefono que
nadie coge mata la noticia: el periodista tiene plazo de cierre y pasa a otra cosa.</p>
<p>Debajo, el boilerplate: un parrafo corto y fijo sobre la empresa (a que se dedica, desde cuando,
tamano, donde opera). Siempre el mismo en todas tus notas.</p>

<h2>El esquema completo</h2>
<table>
  <tr><th>Parte</th><th>Extension</th><th>Funcion</th></tr>
  <tr><td>Titular</td><td>1 linea</td><td>Que entre a leer</td></tr>
  <tr><td>Subtitulo</td><td>1 frase</td><td>El dato que lo sostiene</td></tr>
  <tr><td>Lugar y fecha</td><td>5 palabras</td><td>Contexto y profesionalidad</td></tr>
  <tr><td>Entradilla</td><td>3-4 lineas</td><td>Las cinco W</td></tr>
  <tr><td>Cuerpo</td><td>2-3 parrafos</td><td>Datos y desarrollo</td></tr>
  <tr><td>Cita</td><td>1-2 frases</td><td>Voz humana</td></tr>
  <tr><td>Contacto</td><td>3 lineas</td><td>Que puedan ampliar</td></tr>
</table>
<p>Total: entre 300 y 500 palabras. Si te pasas, sobra algo.</p>

<p>Tienes el esqueleto listo para rellenar en la <a href="/guia/plantilla-nota-de-prensa/">plantilla</a>
y modelos completos en los <a href="/guia/ejemplos-de-notas-de-prensa/">ejemplos</a>.</p>
"""
    preguntas = [
        ("Cuales son las partes de una nota de prensa",
         "Titular, subtitulo, lugar y fecha, entradilla con las cinco W, cuerpo, una cita atribuida y los "
         "datos de contacto con el boilerplate de la empresa."),
        ("Que es la piramide invertida",
         "La tecnica de redaccion periodistica que coloca lo mas importante al principio y lo menos "
         "relevante al final, para que el texto pueda cortarse por abajo sin perder sentido."),
        ("Cuantas citas debe llevar una nota de prensa",
         "Una, bien elegida. Varias citas seguidas diluyen el mensaje y el periodista acaba cortando todas."),
        ("Que es el boilerplate",
         "El parrafo fijo sobre la empresa que cierra todas tus notas de prensa: a que se dedica, desde "
         "cuando, tamano y donde opera. Siempre identico."),
    ]
    return guia("/guia/estructura-de-una-nota-de-prensa/",
                "Estructura de una nota de prensa",
                "Estructura de una nota de prensa: las 7 partes en orden",
                "Las siete partes de una nota de prensa explicadas en orden, con ejemplos de cada una y la "
                "extension que debe tener cada bloque. Incluye esquema resumen.",
                "Siete partes, en este orden. Con ejemplos de lo que funciona y lo que hace que un "
                "periodista deje de leer en la segunda linea.", c, preguntas)


def que_es():
    c = """
<p>Una nota de prensa es un texto breve con formato periodistico que una empresa, una institucion o un
profesional envia a los medios de comunicacion para anunciar algo que considera noticiable.</p>
<p>La definicion es facil. Lo que casi nadie entiende es la consecuencia: <strong>el destinatario no es
tu cliente, es un periodista</strong>. No se escribe para convencer a nadie de que compre. Se escribe
para que un redactor decida que eso merece una noticia.</p>

<h2>Para que sirve realmente</h2>
<p>Una nota de prensa bien colocada te da tres cosas:</p>
<ul>
  <li><strong>Credibilidad prestada.</strong> Que hable de ti un medio vale mas que cualquier anuncio,
  porque el lector sabe que no lo has escrito tu.</li>
  <li><strong>Presencia en busquedas.</strong> Las publicaciones quedan indexadas y aparecen cuando
  alguien busca tu marca.</li>
  <li><strong>Contacto con periodistas.</strong> La primera nota casi nunca sale. La quinta, si las
  anteriores fueron serias, empieza a salir.</li>
</ul>

<h2>Lo que no sirve para nada</h2>
<p>Una nota de prensa no vende directamente. Si la escribes esperando llamadas al dia siguiente, vas a
decepcionarte. Tampoco sirve si no hay noticia: que tu empresa exista, que tengas una web nueva o que
estes contento con tu equipo no son hechos noticiables para nadie de fuera.</p>

<h2>Quien la lee, en orden</h2>
<ol>
  <li>El redactor que recibe el correo y decide en cinco segundos si sigue leyendo.</li>
  <li>Si sigue, el jefe de seccion, que decide si entra en la planificacion del dia.</li>
  <li>Si entra, el lector final, que leera la version reescrita por el periodista, no la tuya.</li>
</ol>
<p>Esto explica por que una nota escrita como publicidad no pasa del primer filtro, y por que las que
funcionan parecen ya una noticia hecha: le estas ahorrando trabajo a alguien que va con prisa.</p>

<h2>Cuando si tienes una noticia</h2>
<p>La prueba es sencilla: si lo que vas a contar le importa a alguien que no te conoce, hay noticia.
Casos tipicos:</p>
<ul>
  <li>Abres, cierras, te mudas o creces de forma visible para tu comunidad.</li>
  <li>Lanzas algo que antes no existia, no una version nueva de lo mismo.</li>
  <li>Tienes datos propios que nadie mas tiene: un estudio, cifras de tu sector.</li>
  <li>Alguien de fuera te reconoce: un premio, una certificacion.</li>
  <li>Te posicionas publicamente sobre algo que ya es noticia.</li>
  <li>Hay una historia humana detras: la primera mujer que hace X en la comarca, un relevo generacional.</li>
</ul>

<h2>Cuanto mide y como se manda</h2>
<p>Entre 300 y 500 palabras, una pagina. Se manda en el cuerpo del correo, nunca como PDF adjunto, con
el titular en el asunto. Lo desarrollamos en <a href="/guia/formato-nota-de-prensa/">formato</a> y en
<a href="/enviar-nota-de-prensa/">como enviarla</a>.</p>

<h2>El dato que conviene conocer</h2>
<p>Entre el tres y el cinco por ciento de las notas de prensa que se envian acaban publicadas, y
alrededor del cuarenta por ciento contienen errores de redaccion periodistica. Dicho de otra forma: la
mayoria de la competencia lo hace mal, y eso es una oportunidad si tu lo haces bien.</p>
"""
    preguntas = [
        ("Que es una nota de prensa y para que sirve",
         "Es un texto breve con formato periodistico que se envia a los medios para anunciar algo "
         "noticiable. Sirve para conseguir cobertura, credibilidad y contacto con periodistas, no para "
         "vender directamente."),
        ("Quien lee una nota de prensa",
         "Primero el redactor que decide si le interesa, despues el jefe de seccion y por ultimo el lector, "
         "que leera la version reescrita por el periodista."),
        ("Cuando hay que enviar una nota de prensa",
         "Cuando hay un hecho que le importa a alguien que no te conoce: una apertura, un lanzamiento real, "
         "datos propios, un premio o una posicion publica sobre algo de actualidad."),
        ("Una nota de prensa sirve para vender",
         "No directamente. Sirve para que un medio hable de ti, lo que genera credibilidad y presencia. "
         "Quien espere ventas inmediatas se va a llevar un chasco."),
    ]
    return guia("/guia/que-es-una-nota-de-prensa/",
                "Que es una nota de prensa",
                "Que es una nota de prensa: definicion, para que sirve y cuando enviarla",
                "Que es una nota de prensa, para que sirve de verdad, quien la lee y en que casos merece "
                "la pena enviarla. Con los criterios para saber si tienes noticia.",
                "Un texto para periodistas, no para clientes. Esa distincion explica casi todo lo que hay "
                "que saber sobre como se escribe y por que la mayoria fracasan.", c, preguntas)


def como_hacer():
    c = """
<p>Siete pasos. Si los sigues en orden, en una tarde tienes una nota de prensa que un periodista al
menos va a leer entera.</p>

<h2>Paso 1: comprueba que tienes noticia</h2>
<p>Antes de escribir nada, responde a esto: <em>por que deberia importarle esto a alguien que no me
conoce de nada</em>. Si la respuesta tiene que ver con lo contento que estas o con lo bueno que es tu
producto, no hay noticia todavia. Busca el angulo: un dato, una primera vez, un impacto en la comarca,
una cifra.</p>

<h2>Paso 2: escribe el titular antes que el texto</h2>
<p>Suena al reves, pero obliga a concretar. Si no consigues meter la noticia en quince palabras, es que
aun no sabes cual es. Escribelo como lo publicaria el periodico, no como lo pondria tu folleto.</p>

<h2>Paso 3: resuelve las cinco W en el primer parrafo</h2>
<p>Que, quien, cuando, donde y por que. Tres o cuatro lineas. La prueba: si alguien solo lee ese
parrafo, debe poder contar la noticia entera. Si falta algo, no esta terminado.</p>

<h2>Paso 4: anade los datos, de mas a menos importante</h2>
<p>Dos o tres parrafos. Cifras concretas, plazos, nombres. Cada parrafo tiene que poder borrarse por
abajo sin romper el texto, porque es lo que hara el redactor si va justo de espacio.</p>
<p>Prohibido: lider, innovador, revolucionario, pionero, unico, de referencia. Si no puedes demostrarlo
con un dato, fuera.</p>

<h2>Paso 5: mete una cita que diga algo</h2>
<p>Una sola, con nombre y cargo. Que aporte interpretacion o compromiso, no entusiasmo. Comparalo:</p>
<ul>
  <li><em>&laquo;Es un dia muy importante para nosotros&raquo;</em> &rarr; no aporta nada, se corta.</li>
  <li><em>&laquo;Con esta planta dejamos de depender del suministro exterior en un 60%&raquo;</em> &rarr; eso
  se publica.</li>
</ul>

<h2>Paso 6: cierra con contacto y boilerplate</h2>
<p>Nombre, telefono directo, correo. Y el parrafo fijo de la empresa. El telefono tiene que estar
operativo: si el periodista llama para confirmar un dato y no le cogen, la noticia no sale.</p>

<h2>Paso 7: quita el treinta por ciento</h2>
<p>Esto es lo que separa una nota decente de una buena. Dejalo reposar, vuelve y borra todo lo que no
sea informacion. Normalmente sobra un tercio: adjetivos, repeticiones, la historia de la empresa metida
en medio y las frases de relleno del tipo <em>en un mercado cada vez mas competitivo</em>.</p>

<h2>Antes de enviarla, comprueba</h2>
<ul>
  <li>&iquest;Cabe en una pagina? Entre 300 y 500 palabras.</li>
  <li>&iquest;El titular funciona sin leer el resto?</li>
  <li>&iquest;Esta todo en tercera persona?</li>
  <li>&iquest;Hay al menos tres datos verificables?</li>
  <li>&iquest;Alguien coge ese telefono?</li>
  <li>&iquest;Va en el cuerpo del correo y no como adjunto?</li>
</ul>

<p>Cuando la tengas, lo siguiente es <a href="/enviar-nota-de-prensa/">enviarla a quien toca</a>, que es
donde se pierde la mitad del trabajo. Y si quieres atajar, coge la
<a href="/guia/plantilla-nota-de-prensa/">plantilla</a>.</p>
"""
    preguntas = [
        ("Como se hace una nota de prensa paso a paso",
         "Comprueba que hay noticia, escribe el titular primero, resuelve las cinco W en el primer parrafo, "
         "anade los datos de mas a menos importante, mete una cita con nombre y cargo, cierra con contacto "
         "y boilerplate, y recorta un treinta por ciento."),
        ("Cuanto se tarda en escribir una nota de prensa",
         "Una tarde la primera vez. Con practica y una plantilla, entre una y dos horas."),
        ("Se escribe en primera o en tercera persona",
         "Siempre en tercera. La primera persona solo aparece dentro de la cita entrecomillada."),
        ("Que palabras hay que evitar en una nota de prensa",
         "Lider, innovador, revolucionario, pionero, unico, de referencia y cualquier adjetivo que no "
         "puedas respaldar con un dato concreto."),
    ]
    return guia("/guia/como-hacer-una-nota-de-prensa/",
                "Como hacer una nota de prensa paso a paso",
                "Como hacer una nota de prensa: 7 pasos y checklist final",
                "Como escribir una nota de prensa en siete pasos, con los errores que hacen que la "
                "descarten y una lista de comprobacion antes de enviarla.",
                "De la idea al texto final en siete pasos. El septimo, recortar un tercio, es el que "
                "separa una nota decente de una que se publica.", c, preguntas)


def formato():
    c = """
<p>El formato de una nota de prensa no es una cuestion estetica: cada convencion existe porque le
ahorra tiempo a quien la recibe. Esto es lo que esperan en una redaccion.</p>

<h2>Extension</h2>
<p>Entre 300 y 500 palabras. Una pagina A4. Las notas de mas de una pagina se leen en diagonal o
directamente no se leen.</p>

<h2>Como se envia</h2>
<p>En el <strong>cuerpo del correo electronico</strong>, siempre. El PDF adjunto es el error mas comun y
el mas caro: un periodista con cuarenta correos sin abrir no va a descargar nada para averiguar si le
interesa. Si quieres mandar tambien el PDF maquetado, adjuntalo ademas, nunca en lugar del texto.</p>

<h3>El asunto del correo</h3>
<p>El titular de la noticia, tal cual. No <em>&laquo;Nota de prensa &ndash; Empresa S.L.&raquo;</em>, que
no dice nada y se borra sin abrir.</p>

<h2>Tipografia y maquetacion</h2>
<p>Si preparas tambien la version en documento:</p>
<table>
  <tr><th>Elemento</th><th>Convencion</th></tr>
  <tr><td>Tipografia</td><td>Arial o Times New Roman, 11 o 12 puntos</td></tr>
  <tr><td>Interlineado</td><td>1,5 para que se pueda anotar</td></tr>
  <tr><td>Margenes</td><td>2,5 cm</td></tr>
  <tr><td>Alineacion</td><td>Izquierda, sin justificar</td></tr>
  <tr><td>Titular</td><td>Negrita, 14-16 puntos</td></tr>
  <tr><td>Logotipo</td><td>Arriba, discreto</td></tr>
  <tr><td>Cierre</td><td>Tres almohadillas centradas: ###</td></tr>
</table>
<p>Las tres almohadillas al final son la marca clasica de que el texto ha terminado y lo que sigue son
datos de contacto, no contenido publicable. Es un detalle que reconocen en cualquier redaccion.</p>

<h2>Imagenes</h2>
<p>Una o dos, no diez. En el correo van en baja resolucion o enlazadas a una carpeta de descarga, con
las de alta disponibles. Formato horizontal, minimo 1200 pixeles de ancho, con pie de foto y autor.</p>
<p>Las fotos de archivo genericas no aportan nada. Una foto real del local, el producto o la persona
multiplica las posibilidades de que te publiquen, porque el medio necesita ilustrar la noticia y no
siempre puede mandar a un fotografo.</p>

<h2>Nombre del archivo</h2>
<p>Si adjuntas documento o imagenes, nombralos de forma descriptiva:
<em>nota-prensa-apertura-taller-ferrol.pdf</em>, no <em>documento final v3 definitivo.pdf</em>. El
periodista lo archiva y lo busca luego.</p>

<h2>Lo que nunca debe llevar</h2>
<ul>
  <li>Texto en mayusculas o con signos de exclamacion.</li>
  <li>Colores corporativos en el cuerpo del texto.</li>
  <li>Precios y condiciones comerciales como si fuera un anuncio.</li>
  <li>Enlaces de afiliado o de seguimiento con parametros larguisimos.</li>
  <li>Avisos de confidencialidad al pie: se envia a medios, es publico.</li>
</ul>

<p>El esqueleto ya formateado lo tienes en la <a href="/guia/plantilla-nota-de-prensa/">plantilla</a>.</p>
"""
    preguntas = [
        ("Que formato debe tener una nota de prensa",
         "Entre 300 y 500 palabras, una pagina, Arial o Times New Roman a 11 o 12 puntos, interlineado 1,5, "
         "alineacion a la izquierda y cierre con tres almohadillas."),
        ("Se envia en PDF o en el cuerpo del correo",
         "Siempre en el cuerpo del correo. El PDF puede ir adjunto ademas, nunca en lugar del texto."),
        ("Que significan las tres almohadillas al final",
         "Son la marca convencional de que el texto publicable ha terminado y lo que viene despues son "
         "datos de contacto."),
        ("Cuantas imagenes se adjuntan a una nota de prensa",
         "Una o dos, horizontales, de al menos 1200 pixeles de ancho, con pie de foto y autor. Mejor reales "
         "que de banco de imagenes."),
    ]
    return guia("/guia/formato-nota-de-prensa/",
                "Formato de una nota de prensa",
                "Formato de nota de prensa: extension, tipografia y envio",
                "El formato que esperan las redacciones: extension, tipografia, margenes, imagenes, nombre "
                "de archivo y como enviarla por correo.",
                "Cada convencion de formato existe porque le ahorra tiempo al que la recibe. Esto es lo que "
                "espera una redaccion, incluido el detalle de las tres almohadillas.", c, preguntas)
