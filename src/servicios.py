# -*- coding: utf-8 -*-
"""Paginas de servicio orientadas a conversion"""
from build import escribir, migas, faq_html, FORMULARIO, CAJA_LATERAL, servicio_schema, articulo_schema
from graficos import cobertura, comparativa, proceso, tasa_publicacion
from paginas import pagina_servicio


def publicar():
    sec = """
<h2>Donde se publica tu nota</h2>
<p>Al contratar el servicio, tu nota de prensa se publica en nuestro medio con titular propio, fecha,
imagen y enlace a tu web. Queda indexada en Google y accesible de forma permanente, con una URL que
puedes compartir en redes, enviar a clientes o enlazar desde tu propia web.</p>
<p>A partir de ahi, la misma nota se distribuye a los periodistas y redacciones que cubren tu sector.
Cada envio es individual y personalizado: nada de listas en copia oculta con doscientos destinatarios,
que es la forma mas rapida de acabar en la carpeta de spam.</p>

<h2>Que incluye publicar una nota de prensa con nosotros</h2>
<table>
  <tr><th>Incluido</th><th>Detalle</th></tr>
  <tr><td>Revision periodistica</td><td>Te decimos si el texto tiene recorrido y que cambiarias antes de enviarlo.</td></tr>
  <tr><td>Publicacion con enlace</td><td>URL propia, indexable, permanente y con enlace a tu web.</td></tr>
  <tr><td>Distribucion segmentada</td><td>Envio a los medios y secciones que cubren tu tema, por sector y provincia.</td></tr>
  <tr><td>Imagen optimizada</td><td>Preparamos la imagen al formato y peso que piden las redacciones.</td></tr>
  <tr><td>Informe de resultados</td><td>Donde ha salido, con enlaces, y a quien se ha enviado.</td></tr>
</table>

<h2>Con la nota ya escrita o sin ella</h2>
<p>Si ya tienes el texto, solo pagas publicacion y distribucion. Si no lo tienes, lo escribimos nosotros
a partir de una conversacion de diez minutos. La mayoria de los clientes eligen lo segundo, porque el
problema casi nunca es tener algo que contar: es contarlo en el formato que una redaccion acepta.</p>
<p>Si prefieres escribirla tu, tienes la <a href="/guia/como-hacer-una-nota-de-prensa/">guia paso a paso</a>
y una <a href="/guia/plantilla-nota-de-prensa/">plantilla en blanco</a>, las dos gratis.</p>

<h2>Cuanto tarda en estar publicada</h2>
<p>Si nos mandas el texto hecho, el mismo dia laborable. Si la escribimos nosotros, el borrador en 48
horas y la publicacion en cuanto des el visto bueno. Para lanzamientos con fecha, avisa al pedir
presupuesto y lo reservamos.</p>
"""
    preguntas = [
        ("Cuanto cuesta publicar una nota de prensa",
         "Desde 95 euros con redaccion incluida. Si nos la envias ya escrita, el precio baja porque solo "
         "cobramos publicacion y distribucion. Puedes ver el detalle en la pagina de precios."),
        ("La nota se queda publicada para siempre",
         "Si. La URL es permanente y no la retiramos pasado un tiempo, como hacen algunos servicios de "
         "suscripcion. Si algun dato queda desfasado y quieres corregirlo, se actualiza sin coste."),
        ("Puedo publicar varias notas al mes",
         "Si, y sale mas barato por unidad. Lo habitual en una pyme es una cada uno o dos meses: mas "
         "frecuencia sin noticias reales detras desgasta la relacion con los periodistas."),
        ("Necesito tener web para publicar una nota de prensa",
         "No es imprescindible, pero ayuda mucho. Si no la tienes, el enlace puede apuntar a tu ficha de "
         "Google, a tu perfil de LinkedIn o a tu tienda."),
    ]
    return pagina_servicio(
        "/publicar-nota-de-prensa/", "Publicar una nota de prensa",
        "Publicar nota de prensa: precio, plazos y donde se publica",
        "Publicamos tu nota de prensa con enlace permanente y la distribuimos a los medios de tu sector. "
        "Desde 95 euros, publicada el mismo dia si ya la tienes escrita.",
        "Publicamos tu nota con enlace permanente y la enviamos a los periodistas que cubren tu sector. "
        "Si ya la tienes escrita, sale hoy mismo.",
        sec, preguntas, "/publicar-nota-de-prensa/", precio=95)


def comprar():
    sec = """
<h2>Que estas comprando exactamente</h2>
<p>Cuando alguien busca comprar una nota de prensa normalmente quiere una de estas tres cosas, y
conviene distinguirlas porque el precio y el resultado son muy distintos:</p>
<table>
  <tr><th>Lo que quieres</th><th>Lo que necesitas</th><th>Desde</th></tr>
  <tr><td>Que alguien la escriba bien</td><td>Redaccion periodistica</td><td>95 &euro;</td></tr>
  <tr><td>Que llegue a periodistas</td><td>Redaccion + distribucion segmentada</td><td>195 &euro;</td></tr>
  <tr><td>Un enlace en un medio concreto</td><td><a href="/comprar-enlaces-prensa/">Publicacion patrocinada</a></td><td>Segun medio</td></tr>
</table>
<p>Las dos primeras son comunicacion. La tercera es SEO, se contrata por medio y tiene su propia pagina
porque funciona de otra manera.</p>

<h2>Por que comprarla en vez de escribirla</h2>
<p>Por el mismo motivo por el que no te haces tu la declaracion de sociedades: se puede, pero el coste
de hacerlo mal no compensa lo que ahorras. Una nota mal escrita no es que rinda poco, es que no la lee
nadie, y ademas te quema el contacto con esa redaccion para la siguiente.</p>
<p>Si aun asi quieres intentarlo, no te vamos a vender lo contrario: la <a href="/guia/">guia completa</a>
esta publicada entera y gratis, con ejemplos y plantillas.</p>

<h2>Que te entregamos</h2>
<ul>
  <li>La nota redactada en formato periodistico, lista para enviar o publicar.</li>
  <li>Dos titulares alternativos, por si quieres probar otro enfoque.</li>
  <li>El texto adaptado para redes sociales y para email, sin coste adicional.</li>
  <li>La publicacion con enlace permanente, si contratas el pack completo.</li>
  <li>El informe de distribucion con los medios a los que ha ido.</li>
</ul>

<h2>Pago y facturacion</h2>
<p>Se paga por trabajo, no por suscripcion. Factura con IVA emitida por Grupo Seocar S.L., y no hay
permanencia ni renovacion automatica. Si el resultado no se parece a lo acordado, se rehace.</p>
"""
    preguntas = [
        ("Cuanto cuesta comprar una nota de prensa",
         "Desde 95 euros la redaccion con publicacion basica. El pack con distribucion segmentada a "
         "medios cuesta 195 euros y el de campana completa 395. Sin cuotas ni permanencia."),
        ("Se paga antes o despues",
         "La mitad al encargar y la mitad al entregar, o el total por adelantado si prefieres factura "
         "unica. Para clientes recurrentes, facturacion mensual."),
        ("Puedo ver un ejemplo antes de contratar",
         "Si, tienes ejemplos completos y reales en la guia, con el texto integro de notas por tipo de "
         "anuncio. Y si nos lo pides, te mandamos trabajos anteriores del sector que mas se parezca al tuyo."),
        ("Que pasa si no me gusta como ha quedado",
         "Se corrige las veces que haga falta hasta que la apruebes. Nada se publica ni se envia sin tu "
         "visto bueno por escrito."),
    ]
    return pagina_servicio(
        "/comprar-nota-de-prensa/", "Comprar una nota de prensa",
        "Comprar nota de prensa: precios y que incluye cada opcion",
        "Compra tu nota de prensa redactada por periodistas desde 95 euros. Publicacion, distribucion a "
        "medios e informe incluidos. Sin permanencia y con factura.",
        "Te la escribimos, la publicamos y la enviamos a los medios. Pagas por trabajo, no por suscripcion, "
        "y no se publica nada sin tu visto bueno.",
        sec, preguntas, precio=95)


def enviar():
    sec = """
<h2>A quien hay que enviar una nota de prensa</h2>
<p>El error mas comun es enviarla a la direccion generica de contacto del medio. Ese buzon lo vacia
alguien de administracion y casi nunca llega a una redaccion. Lo que funciona es identificar al
redactor que cubre tu tema en ese medio concreto y escribirle a el.</p>
<p>El orden de prioridad que seguimos nosotros es este:</p>
<ol>
  <li><strong>Periodista de la seccion</strong> que cubre tu sector en ese medio. Es quien decide.</li>
  <li><strong>Jefe de seccion</strong>, si el tema es transversal o no hay un redactor claro.</li>
  <li><strong>Redaccion general</strong>, solo en medios pequenos donde no hay secciones.</li>
  <li><strong>Agencias y newsletters sectoriales</strong>, que replican a otros medios.</li>
</ol>
<p>Puedes consultar que medios cubren tu provincia y tu sector en nuestro
<a href="/medios/">directorio de medios espanoles</a>.</p>

<h2>Como se envia, en la practica</h2>
<p>En el cuerpo del correo, nunca como adjunto. Un periodista con cuarenta correos sin abrir no va a
descargar un PDF para ver si le interesa. El asunto debe ser el titular de la noticia, no
<em>&laquo;nota de prensa de empresa X&raquo;</em>.</p>
<p>Las imagenes van enlazadas a una carpeta o en baja resolucion dentro del correo, con las de alta
disponibles para descargar. Y el envio es uno a uno: ver cien direcciones en copia le dice al redactor
que no es una exclusiva y que puede ignorarla sin coste.</p>

<h2>A que hora y que dia</h2>
<p>De martes a jueves, entre las ocho y las diez de la manana. Los lunes las redacciones estan
planificando la semana y los viernes cerrando. En agosto hay menos competencia por el espacio, asi que
una noticia mediana tiene mas posibilidades que en octubre.</p>

<h2>El seguimiento</h2>
<p>Una llamada o un correo breve, a las 48 horas, y solo uno. Insistir mas quema el contacto para
siempre. Si no ha interesado, lo util es preguntar por que, no volver a enviar lo mismo.</p>

<h2>Lo hacemos por ti</h2>
<p>El envio segmentado esta incluido en los planes de 195&nbsp;&euro; en adelante: seleccion de medios por
sector y provincia, envio individual, seguimiento y el informe con lo que ha salido.</p>
"""
    preguntas = [
        ("A cuantos medios hay que enviar una nota de prensa",
         "Entre quince y cuarenta bien elegidos rinde mucho mas que doscientos genericos. Lo que importa "
         "es que el medio cubra tu tema, no el tamano de la lista."),
        ("Se puede enviar una nota de prensa por WhatsApp",
         "A un periodista con el que ya tienes trato, si, y a veces funciona mejor que el correo. A uno "
         "que no te conoce, no: se percibe como intrusivo."),
        ("Cuantas veces puedo hacer seguimiento",
         "Una. A las 48 horas del envio, breve y aportando algo nuevo si puedes. Una segunda insistencia "
         "casi siempre resta."),
        ("Hay que enviarla tambien a los medios que no cubren mi sector",
         "No. Ensucia tu reputacion como remitente y aumenta la probabilidad de que tus correos acaben "
         "filtrados como spam en todo ese dominio."),
    ]
    return pagina_servicio(
        "/enviar-nota-de-prensa/", "Enviar una nota de prensa a los medios",
        "Enviar nota de prensa a medios: a quien, como y cuando",
        "Como enviar una nota de prensa para que la publiquen: a que periodista, en que formato, que dia "
        "y a que hora. Y el servicio de envio segmentado desde 195 euros.",
        "A quien enviarla, en que formato y en que momento. Y si prefieres no hacerlo tu, lo hacemos "
        "nosotros con envio individual a los medios de tu sector.",
        sec, preguntas, precio=195)


def donde():
    sec = """
<h2>Las cuatro vias que existen</h2>
<p>Para publicar una nota de prensa en Espana tienes cuatro caminos, y conviene saber que te da cada uno
antes de gastar dinero:</p>
<table>
  <tr><th>Via</th><th>Que consigues</th><th>Coste</th><th>Enlace SEO</th></tr>
  <tr><td>Envio directo a periodistas</td><td>Cobertura real si la noticia interesa</td><td>Tu tiempo</td><td>Solo si deciden enlazarte</td></tr>
  <tr><td>Portales de notas de prensa</td><td>Publicacion garantizada, poca lectura</td><td>0&nbsp;&euro; a 150&nbsp;&euro;</td><td>Normalmente nofollow</td></tr>
  <tr><td>Publicacion patrocinada en medios</td><td>Salir en un medio concreto</td><td>50&nbsp;&euro; a 600&nbsp;&euro;</td><td>Si, acordado</td></tr>
  <tr><td>Agencia de comunicacion</td><td>Relacion continuada con prensa</td><td>Desde 800&nbsp;&euro;/mes</td><td>Indirecto</td></tr>
</table>

<h2>Portales donde publicar notas de prensa</h2>
<p>Existen portales de publicacion de notas de prensa, algunos gratuitos y otros de pago. Sirven para
tener la nota colgada en una URL indexable y poco mas: el trafico de lectura de estos portales es bajo
y los enlaces suelen ser nofollow, que es lo que marcan las directrices de Google para comunicados.</p>
<p>No es que no sirvan, es que sirven para lo que sirven. Si lo que buscas es que te lea alguien, el
envio directo a periodistas rinde mucho mas. Si lo que buscas es autoridad SEO, lo que necesitas es
<a href="/comprar-enlaces-prensa/">publicacion patrocinada en medios</a>, que es otra cosa.</p>

<h2>Medios por provincia y por sector</h2>
<p>Tenemos publicado un <a href="/medios/">directorio de medios espanoles</a> ordenado por provincia y
por sector, con enlace a la pagina de contacto de cada uno. Es gratuito, no pide registro y lo vamos
ampliando.</p>

<h2>Donde la publicamos nosotros</h2>
<p>En nuestro propio medio, con URL permanente y enlace a tu web, y en los medios con los que trabajamos
cuando el tema encaja. Ademas la enviamos a los periodistas del sector. El detalle esta en
<a href="/publicar-nota-de-prensa/">publicar una nota de prensa</a>.</p>
"""
    preguntas = [
        ("Donde puedo publicar una nota de prensa gratis",
         "Hay portales gratuitos de publicacion de notas de prensa, y el envio directo a periodistas no "
         "cuesta dinero, solo tiempo. Lo explicamos en la pagina de notas de prensa gratis."),
        ("Merece la pena pagar por publicar en un portal de notas de prensa",
         "Depende de para que. Para tener la nota en una URL indexable y poder compartirla, puede valer. "
         "Para conseguir lectores o autoridad SEO, normalmente no: el trafico es bajo y los enlaces nofollow."),
        ("Cual es la diferencia entre un portal de notas de prensa y un medio",
         "Un medio tiene redaccion propia, audiencia y criterio editorial: alguien decide si tu nota entra. "
         "Un portal publica lo que le mandas. Eso hace que un enlace o una mencion en un medio valgan mucho mas."),
    ]
    return pagina_servicio(
        "/donde-publicar-notas-de-prensa/", "Donde publicar notas de prensa en Espana",
        "Donde publicar notas de prensa: portales, medios y precios",
        "Las cuatro vias para publicar una nota de prensa en Espana, con lo que cuesta cada una y lo que "
        "consigues de verdad. Incluye directorio de medios por provincia.",
        "Portales, medios, envio directo o agencia. Que te da cada via, cuanto cuesta y cual te conviene "
        "segun lo que busques.",
        sec, preguntas)


def gratis():
    sec = """
<h2>Lo que de verdad es gratis</h2>
<p>Hay dos formas de publicar una nota de prensa sin pagar, y una de ellas funciona mucho mejor que
la otra.</p>

<h3>1. Enviarla tu mismo a los periodistas</h3>
<p>Es gratis, es lo que mas rinde y es lo que hace cualquier agencia por dentro. Necesitas una noticia
de verdad, el texto bien escrito y saber a quien mandarsela. Las tres cosas las tienes resueltas aqui:
la <a href="/guia/como-hacer-una-nota-de-prensa/">guia de redaccion</a>, la
<a href="/guia/plantilla-nota-de-prensa/">plantilla</a> y el
<a href="/medios/">directorio de medios</a>, todo publicado y sin registro.</p>
<p>El coste es tu tiempo: calcula una tarde para escribirla bien y otra para seleccionar y enviar.</p>

<h3>2. Portales gratuitos de notas de prensa</h3>
<p>Publican lo que les mandas sin filtro editorial. Te dan una URL indexable y poco mas: la lectura es
escasa y el enlace suele ser nofollow. Sirve para tener la nota colgada en algun sitio, no para
conseguir cobertura ni autoridad.</p>

<h2>Lo que no es gratis aunque lo parezca</h2>
<p>Desconfia de cualquier servicio que te prometa aparecer en medios conocidos sin coste. O es
publicidad encubierta que pagas de otra forma, o la publicacion es en un subdominio sin valor, o
simplemente no va a ocurrir. Recuerda el dato: solo entre el tres y el cinco por ciento de las notas
enviadas acaban publicadas, y las que lo consiguen es porque tenian algo que contar.</p>

<h2>Cuando conviene pagar</h2>
<p>Cuando no tienes la tarde, cuando el lanzamiento tiene fecha y no admite ensayo, o cuando ya lo
intentaste gratis y no salio. Pagar no compra cobertura garantizada en prensa generalista, pero si
compra que el texto este bien escrito y que llegue a la persona correcta, que es donde falla el
noventa por ciento de los intentos.</p>
<p>Si llegas a ese punto, empieza por la <a href="/precios/">pagina de precios</a>: la opcion mas barata
son 95&nbsp;&euro; y no tiene permanencia.</p>
"""
    preguntas = [
        ("Se puede publicar una nota de prensa gratis de verdad",
         "Si: enviandola tu mismo a los periodistas no cuesta dinero, y hay portales que publican sin "
         "cobrar. Lo que no existe gratis es la cobertura garantizada en medios con audiencia."),
        ("Los portales gratuitos de notas de prensa sirven para SEO",
         "Poco. Los enlaces suelen ser nofollow, que es lo que marcan las directrices de Google para notas "
         "de prensa, y la autoridad que transmiten es minima. Para SEO sirve la publicacion patrocinada en medios."),
        ("Que necesito para enviarla yo mismo",
         "Una noticia real, el texto en formato periodistico y la lista de periodistas que cubren tu tema. "
         "Las tres cosas estan publicadas gratis en esta web."),
    ]
    return pagina_servicio(
        "/notas-de-prensa-gratis/", "Publicar notas de prensa gratis",
        "Notas de prensa gratis: como publicarla sin pagar (y que esperar)",
        "Como publicar una nota de prensa gratis en Espana: envio directo a periodistas y portales "
        "gratuitos. Que consigues con cada via y cuando conviene pagar.",
        "Se puede publicar sin pagar, y te contamos exactamente como. Tambien te contamos que esperar de "
        "cada via, porque no todas sirven para lo mismo.",
        sec, preguntas)


def nota_pilar():
    sec = """
<h2>Que es una nota de prensa</h2>
<p>Una nota de prensa es un texto breve, escrito con criterio periodistico, que una empresa o
institucion envia a los medios para anunciar un hecho que considera noticiable. No se escribe para que
lo lea el publico: se escribe para que un periodista decida convertirlo en noticia.</p>
<p>Esa es la clave que casi nadie tiene en cuenta. El lector al que te diriges es un profesional con
decenas de correos sin abrir que dedica cinco segundos a decidir si sigue leyendo. Todo lo demas
(estructura, titular, extension, tono) se deriva de ese hecho.</p>

<h2>Las partes que tiene que llevar</h2>
<p>El orden importa, porque un periodista lee de arriba abajo y abandona en cuanto deja de interesarle:</p>
<ol>
  <li><strong>Titular.</strong> La noticia en una linea, como la publicaria el medio.</li>
  <li><strong>Subtitulo.</strong> El dato que refuerza el titular.</li>
  <li><strong>Lugar y fecha.</strong> Donde y cuando, al principio del primer parrafo.</li>
  <li><strong>Entradilla.</strong> Las cinco W resueltas: que, quien, cuando, donde y por que.</li>
  <li><strong>Cuerpo.</strong> El desarrollo, de mas a menos importante.</li>
  <li><strong>Cita.</strong> Una declaracion atribuida a una persona con nombre y cargo.</li>
  <li><strong>Datos de contacto.</strong> Nombre, telefono y correo de alguien que coja el telefono.</li>
</ol>
<p>Lo desarrollamos entero, con ejemplos de cada parte, en
<a href="/guia/estructura-de-una-nota-de-prensa/">la estructura de una nota de prensa</a>.</p>

<h2>Cuanto debe medir</h2>
<p>Entre 300 y 500 palabras. Una pagina. Si no cabe en una pagina, o la noticia es mas grande de lo que
crees y conviene partirla, o estas metiendo relleno que el periodista va a borrar.</p>

<h2>Los errores que hacen que la descarten</h2>
<ul>
  <li>Escribirla en primera persona o con tono comercial.</li>
  <li>Abrir con la historia de la empresa en vez de con la noticia.</li>
  <li>Adjetivos sin respaldo: lider, innovador, revolucionario, unico.</li>
  <li>Titular de folleto en lugar de titular de periodico.</li>
  <li>Mandarla como PDF adjunto sin texto en el cuerpo del correo.</li>
  <li>No dar un telefono de contacto que responda.</li>
</ul>

<h2>Nota de prensa o comunicado de prensa</h2>
<p>En las redacciones espanolas se usan como sinonimos. Hay quien reserva comunicado para mensajes
institucionales o situaciones de crisis, pero no es una distincion que cambie como se escribe. Lo
detallamos en <a href="/guia/diferencia-nota-y-comunicado/">la diferencia entre ambos</a>.</p>

<h2>Como seguir desde aqui</h2>
<p>Si vas a escribirla tu, empieza por la <a href="/guia/como-hacer-una-nota-de-prensa/">guia paso a
paso</a> y coge la <a href="/guia/plantilla-nota-de-prensa/">plantilla</a>. Si prefieres que la
escribamos nosotros y la distribuyamos, mira los <a href="/precios/">precios</a>.</p>
"""
    preguntas = [
        ("Que es una nota de prensa",
         "Un texto breve con formato periodistico que una empresa envia a los medios para anunciar algo "
         "noticiable, con el objetivo de que un periodista lo convierta en noticia."),
        ("Cuanto mide una nota de prensa",
         "Entre 300 y 500 palabras, una pagina. Mas extension no mejora las posibilidades: las reduce."),
        ("Que diferencia hay entre nota de prensa y comunicado de prensa",
         "En la practica profesional espanola son lo mismo. Algunos reservan comunicado para mensajes "
         "institucionales o de crisis, pero se escriben igual."),
        ("Quien escribe las notas de prensa",
         "El departamento de comunicacion en empresas grandes, y una agencia o un profesional externo en "
         "pymes. Tambien puede escribirla el propio empresario si sigue el formato."),
    ]
    return pagina_servicio(
        "/nota-de-prensa/", "Nota de prensa: que es, como se escribe y donde se envia",
        "Nota de prensa: que es, estructura, ejemplos y como enviarla",
        "Que es una nota de prensa, que partes lleva, cuanto debe medir y como enviarla a los medios para "
        "que la publiquen. Con ejemplos, plantilla y directorio de medios.",
        "Todo lo que necesitas saber para escribir una nota de prensa que un periodista lea hasta el "
        "final: estructura, extension, errores que la hunden y a quien enviarla.",
        sec, preguntas, migas_items=[("Inicio", "/"), ("Nota de prensa", None)])


def enlaces():
    sec = """
<h2>Que es un enlace en prensa</h2>
<p>Es un articulo publicado en un medio de comunicacion digital, acordado y pagado, que incluye un
enlace a tu web. No es una nota de prensa enviada a una redaccion con la esperanza de que la publiquen:
es una publicacion contratada, con medio concreto, fecha y enlace pactados por escrito.</p>
<p>Se usa para SEO. El enlace desde un dominio con autoridad e historia transmite parte de esa autoridad
a tu web, y eso mueve posiciones en Google para las palabras clave que trabajes.</p>

<h2>En que se diferencia de una nota de prensa</h2>
{COMPARATIVA}
<table>
  <tr><th></th><th>Nota de prensa</th><th>Enlace en prensa</th></tr>
  <tr><td>Objetivo</td><td>Cobertura y notoriedad</td><td>Autoridad SEO</td></tr>
  <tr><td>Publicacion</td><td>Decide el periodista</td><td>Garantizada por contrato</td></tr>
  <tr><td>Medio</td><td>El que acepte</td><td>Lo eliges tu de un catalogo</td></tr>
  <tr><td>Enlace</td><td>Normalmente nofollow</td><td>Dofollow, acordado</td></tr>
  <tr><td>Precio</td><td>Desde 95&nbsp;&euro;</td><td>Segun autoridad del medio</td></tr>
</table>

<h2>Como elegimos el medio</h2>
<p>Esta es la parte donde se pierde el dinero. Los catalogos de publicacion patrocinada muestran metricas
propias de trafico y autoridad que muchas veces no se sostienen al comprobarlas con una herramienta
independiente. Nosotros verificamos cada medio antes de recomendarlo:</p>
<ul>
  <li>Autoridad y trafico organico reales, medidos con herramienta externa, no las cifras del catalogo.</li>
  <li>Que el medio tenga trafico de verdad y no solo metricas infladas por enlaces.</li>
  <li>Variedad de dominios raiz: no repetir varios subdominios del mismo grupo editorial.</li>
  <li>Coherencia tematica entre el medio y tu sector.</li>
  <li>Prensa local para palabras clave con provincia, prensa nacional para las genericas.</li>
</ul>

<h2>Lo que debes saber antes de contratar</h2>
<p>Te lo decimos aunque no nos convenga comercialmente: Google considera los enlaces de pago un esquema
de enlaces, y sus directrices piden que los enlaces en comunicados y publicaciones patrocinadas vayan
marcados. Es una practica extendidisima en Espana y funciona, pero el riesgo existe y es tuyo.</p>
<p>Por eso trabajamos con ritmo escalonado, variedad de dominios y anchors naturales, en vez de
veinte enlaces el mismo dia con la misma palabra clave, que es el patron que mas llama la atencion.</p>

<h2>Como se contrata</h2>
<p>Nos dices la web, las palabras clave que quieres mover y el presupuesto. Te mandamos una propuesta
con los medios concretos, sus metricas verificadas, el precio de cada uno y las fechas escalonadas de
publicacion. Tu apruebas los que quieras. Redaccion del articulo incluida.</p>
"""
    preguntas = [
        ("Cuanto cuesta un enlace en prensa",
         "Depende de la autoridad del medio. Un medio local pequeno puede estar en 50 o 70 euros y una "
         "cabecera nacional pasar de 600. Te pasamos siempre el precio por medio antes de contratar."),
        ("Los enlaces son dofollow",
         "En las publicaciones patrocinadas, si, y se verifica tras la publicacion. Si un medio solo "
         "acepta nofollow, te lo decimos antes y decides tu."),
        ("Cuanto tarda en notarse en Google",
         "Entre uno y tres meses desde la publicacion, y no de golpe. Quien te prometa resultados en dos "
         "semanas no esta siendo honesto contigo."),
        ("Puedo elegir el medio",
         "Si. Te mandamos la propuesta con los medios, sus metricas comprobadas y el precio, y apruebas "
         "los que quieras. No contratamos nada sin tu visto bueno."),
        ("Es seguro para mi web",
         "Es una practica extendida y funciona, pero los enlaces de pago van contra las directrices de "
         "Google y el riesgo existe. Lo reducimos escalonando fechas, variando dominios y usando anchors "
         "naturales, pero no te vamos a decir que el riesgo sea cero."),
    ]
    sec_c = sec.replace("{COMPARATIVA}", comparativa())
    return pagina_servicio(
        "/comprar-enlaces-prensa/", "Comprar enlaces en prensa",
        "Comprar enlaces en prensa: medios verificados y precio por medio",
        "Publicaciones patrocinadas con enlace en medios digitales espanoles. Metricas verificadas con "
        "herramienta independiente, precio por medio y fechas escalonadas.",
        "Publicaciones patrocinadas con enlace dofollow en medios digitales. Verificamos las metricas de "
        "cada medio por nuestra cuenta, porque las de los catalogos casi nunca cuadran.",
        sec_c, preguntas, "/comprar-enlaces-prensa/")


def precios():
    bar, bar_ld = migas([("Inicio", "/"), ("Precios", None)])
    preguntas = [
        ("Que significa publicacion garantizada",
         "Que la nota se publica en el numero de medios del plan o te devolvemos el dinero. No es una "
         "estimacion ni una previsión: es el compromiso que adquirimos al cobrarte."),
        ("Hay permanencia",
         "No. Se paga mes a mes y se cancela cuando quieras. Si un mes no tienes nada que contar, lo pausas "
         "y no pagas."),
        ("Que pasa si un mes no publico",
         "El plan no se acumula de un mes para otro, asi que si no vas a publicar conviene pausarlo. "
         "Avisanos antes de la renovacion y no se cobra."),
        ("Los precios llevan IVA",
         "Los importes mostrados son sin IVA. Facturamos desde Grupo Seocar S.L. con el 21% correspondiente."),
        ("Puedo ver en que medios ha salido",
         "Si. Con cada publicacion recibes un informe con el enlace directo a cada medio que la ha publicado."),
        ("Y si solo quiero una nota suelta",
         "Los planes son mensuales y sin permanencia, asi que contratar un mes y pausarlo equivale a una "
         "nota suelta. Es la forma mas barata de probarlo."),
    ]
    faq, faq_ld = faq_html(preguntas)
    planes = [
        ("Basico", "Para empezar y probarlo", 179, 50,
         ["Redaccion periodistica incluida", "Publicacion en 50 medios digitales",
          "Enlace a tu web en cada publicacion", "Indexacion en Google News",
          "Informe con el enlace de cada medio", "Publicacion en 2 a 5 dias"], False),
        ("Alcance", "El que contrata casi todo el mundo", 349, 70,
         ["Todo lo del plan Basico", "Publicacion en 70 medios digitales",
          "Distribucion por agencia nacional", "Optimizacion para buscadores con IA",
          "Publicacion en 1 a 3 dias", "Revision del texto contigo"], True),
        ("Autoridad", "Para lanzamientos y marcas", 599, 80,
         ["Todo lo del plan Alcance", "Publicacion en 80 medios digitales",
          "Distribucion por dos agencias nacionales", "Prioridad de publicacion",
          "Asesoramiento sobre el angulo noticiable", "Informe ampliado de repercusion"], False),
    ]
    tarjetas = ""
    for nombre, lema, precio, medios_n, puntos, destacado in planes:
        lis = "".join("<li>{}</li>".format(p) for p in puntos)
        tarjetas += """
  <div class="plan{dest}">
    {etq}
    <h3>{nombre}</h3>
    <p style="color:var(--tinta-3);font-size:15px;margin:0">{lema}</p>
    <div class="precio">{precio} <small>&euro;/mes</small></div>
    <p style="font-size:14px;color:var(--tinta-3);margin:0">sin IVA, sin permanencia</p>
    <div class="cobertura">{cob}</div>
    <ul>{lis}</ul>
    <a href="#cotizar" class="btn{ghost}">Empezar con {nombre}</a>
  </div>""".format(
            dest=" destacado" if destacado else "",
            etq='<span class="etiqueta">El mas contratado</span>' if destacado else "",
            nombre=nombre, lema=lema, precio=precio, lis=lis,
            ghost="" if destacado else " ghost",
            cob=cobertura(medios_n, "{} MEDIOS".format(medios_n)))

    cuerpo = """
{bar}
<main><div class="wrap">
<article style="max-width:760px;padding-top:26px">
<h1>Precios</h1>
<p class="entradilla">Planes mensuales con publicacion garantizada. Si tu nota no sale en el numero de
medios contratado, te devolvemos el dinero. Sin permanencia: pausas el mes que no tengas nada que contar.</p>
</article>

<div class="precios" style="margin:40px 0 20px">
{tarjetas}
</div>

<div style="max-width:760px">
<article>
<h2>Que incluyen todos los planes</h2>
<p>La redaccion la hacemos nosotros: nos cuentas que quieres anunciar y te devolvemos el texto escrito en
formato periodistico para que lo apruebes. Nada se publica sin tu visto bueno.</p>
<p>Cada publicacion lleva enlace a tu web, queda indexada y entra en Google News. Al terminar recibes un
informe con el enlace directo a cada medio donde ha salido, para que puedas comprobarlo tu mismo o
enviarselo a quien quieras.</p>

<h2>Enlaces en prensa, aparte</h2>
<p>Los enlaces en medios concretos se presupuestan por separado, porque el precio depende de la autoridad
de cada cabecera: desde unos 50&nbsp;&euro; en prensa local hasta mas de 600&nbsp;&euro; en cabeceras
nacionales. Es un producto distinto y lo explicamos en
<a href="/comprar-enlaces-prensa/">comprar enlaces en prensa</a>.</p>

<h2>Descuentos</h2>
<table>
  <tr><th>Situacion</th><th>Descuento</th></tr>
  <tr><td>Pago trimestral por adelantado</td><td>-10%</td></tr>
  <tr><td>Pago anual por adelantado</td><td>-20%</td></tr>
  <tr><td>Agencias y revendedores</td><td>Tarifa en marca blanca, consultar</td></tr>
  <tr><td>Asociaciones y colegios profesionales</td><td>Condiciones para sus asociados</td></tr>
</table>

<h2>Lo que no cobramos</h2>
<p>La consulta inicial, las revisiones del texto hasta que lo apruebes y el informe final. Tampoco
cobramos si al escuchar tu caso vemos que no da para nota de prensa: preferimos decirtelo a venderte
algo que no va a funcionar.</p>

{faq}

<h2 id="cotizar">Pide tu presupuesto</h2>
<p>Cuentanos que quieres anunciar y te decimos que plan te encaja, o si te conviene otra cosa.</p>
{form}
</article>
</div>
</div></main>
""".format(bar=bar, tarjetas=tarjetas, faq=faq, form=FORMULARIO)
    return escribir("/precios/", "Precios: planes de notas de prensa desde 179 euros al mes",
                    "Planes mensuales de notas de prensa con publicacion garantizada en 50, 70 u 80 medios "
                    "digitales. Desde 179 euros al mes, sin permanencia y con informe de resultados.",
                    cuerpo, [bar_ld, faq_ld,
                             servicio_schema("Publicacion garantizada de notas de prensa",
                                             "Planes mensuales con publicacion garantizada en medios digitales", 179)],
                    "/precios/")
