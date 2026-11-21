# -*- coding: utf-8 -*-
"""Ejemplos, plantilla y casos concretos"""
from guias import guia

EJ = """
<div style="border:1px solid var(--linea);border-left:4px solid var(--acento);
     border-radius:8px;padding:24px 26px;margin:22px 0;background:#fcfcfb">
{contenido}
</div>
"""


def ejemplos():
    c = """
<p>Cuatro notas de prensa completas, de los tipos que mas se envian. Estan escritas enteras, no
recortadas: puedes copiar la estructura y cambiar los datos por los tuyos.</p>
<p>Los nombres de empresa son inventados. Los datos tambien. Lo que importa es el patron.</p>

<h2>1. Apertura de un negocio</h2>
""" + EJ.format(contenido="""
<p><strong>Un taller de Ferrol instala el primer punto de carga rapida para coches electricos de Ferrolterra</strong></p>
<p><em>La estacion permite recargar el 80% de la bateria en 25 minutos y dara servicio a unos 40 vehiculos al dia</em></p>
<p>Ferrol, 21 de noviembre de 2026. Talleres Noroeste ha puesto en marcha el primer punto de carga
rapida de 150 kW de la comarca de Ferrolterra, en su sede de la avenida de Esteiro. La instalacion, que
ha supuesto una inversion de 70.000 euros, estara operativa las 24 horas y podra atender a unos 40
vehiculos diarios.</p>
<p>Hasta ahora los conductores de vehiculos electricos de la comarca disponian unicamente de cargadores
de potencia media, que requieren entre tres y cuatro horas para una recarga completa. El nuevo punto
reduce ese tiempo a 25 minutos para el 80% de la bateria.</p>
<p>La instalacion llega en un momento de crecimiento del parque electrico en la provincia de A Coruna,
que ha pasado de 1.200 a 3.400 vehiculos matriculados en tres anos segun los datos de la DGT.</p>
<p>&laquo;Si la demanda sigue el ritmo del primer mes, en 2027 tendremos que instalar un segundo
punto&raquo;, senala Marcos Rey, gerente de Talleres Noroeste.</p>
<p style="text-align:center">###</p>
<p style="font-size:15px"><strong>Contacto de prensa:</strong> Marcos Rey &middot; 981 000 000 &middot; prensa@tallenoroeste.es<br>
<em>Talleres Noroeste es un taller multimarca fundado en 1994 en Ferrol. Cuenta con 12 empleados y
atiende a unos 2.000 clientes al ano.</em></p>
""") + """

<h3>Por que funciona</h3>
<ul>
  <li>El titular contiene el hecho, el lugar y la primicia (<em>el primero de la comarca</em>).</li>
  <li>El primer parrafo resuelve las cinco W con cifras concretas.</li>
  <li>Hay un dato de contexto externo y verificable (los datos de la DGT).</li>
  <li>La cita mira al futuro en vez de celebrar el presente.</li>
</ul>

<h2>2. Lanzamiento de producto o servicio</h2>
""" + EJ.format(contenido="""
<p><strong>Una empresa gallega lanza un sistema que detecta fugas de agua en edificios antes de que sean visibles</strong></p>
<p><em>El dispositivo analiza el consumo cada diez minutos y avisa al administrador cuando detecta un patron anomalo</em></p>
<p>A Coruna, 21 de noviembre de 2026. La tecnologica Hidralab ha presentado Caudal, un sistema de
deteccion temprana de fugas de agua en edificios residenciales que identifica perdidas a partir de 0,2
litros por minuto, muy por debajo del umbral en que una fuga resulta visible.</p>
<p>El sistema se instala en la acometida general del edificio y analiza el consumo en intervalos de diez
minutos. Cuando detecta un flujo continuo en franjas horarias de consumo habitualmente nulo, envia un
aviso al administrador de la finca.</p>
<p>Segun datos del sector, las fugas no detectadas suponen entre el 15% y el 25% del agua facturada en
edificios de mas de treinta anos. En una comunidad de 40 viviendas eso equivale a varios miles de euros
anuales.</p>
<p>&laquo;La mayoria de las fugas se descubren cuando aparece una mancha en el techo del vecino de
abajo, y para entonces llevan meses&raquo;, explica Laura Vazquez, directora tecnica de Hidralab.</p>
<p style="text-align:center">###</p>
<p style="font-size:15px"><strong>Contacto de prensa:</strong> Laura Vazquez &middot; 981 000 000 &middot; prensa@hidralab.es<br>
<em>Hidralab es una empresa de instrumentacion fundada en 2019 en A Coruna. Trabaja con administradores
de fincas en Galicia y Asturias.</em></p>
""") + """

<h3>Por que funciona</h3>
<p>El titular no dice que lanzan un producto: dice que problema resuelve. Y la cita describe el dolor
del cliente, que es lo que hace que un periodista vea una historia y no un anuncio.</p>

<h2>3. Resultados o datos propios</h2>
""" + EJ.format(contenido="""
<p><strong>El precio del alquiler en Ferrol sube un 11% en un ano, el mayor aumento de la provincia</strong></p>
<p><em>El informe analiza 1.400 contratos firmados entre enero y octubre en las siete principales ciudades gallegas</em></p>
<p>Ferrol, 21 de noviembre de 2026. El precio medio del alquiler en Ferrol se ha situado en 6,8 euros
por metro cuadrado, un 11% mas que hace un ano, segun el informe elaborado por SC Inmobiliarias a
partir de 1.400 contratos firmados en lo que va de ano.</p>
<p>El incremento situa a la ciudad por delante de A Coruna (8%) y Santiago (6%) en variacion
interanual, aunque sigue siendo la capital comarcal con el precio absoluto mas bajo de las analizadas.</p>
<p>El informe apunta a la reduccion de la oferta como principal factor: el numero de viviendas
disponibles en alquiler en el centro ha caido un 23% respecto a 2025.</p>
<p>&laquo;Lo preocupante no es la subida, es que la oferta se esta vaciando mas rapido de lo que sube
el precio&raquo;, apunta Diego Carballeira, responsable del estudio.</p>
<p style="text-align:center">###</p>
<p style="font-size:15px"><strong>Contacto de prensa:</strong> 981 000 000 &middot; prensa@ejemplo.es<br>
<em>Informe disponible completo para los medios que lo soliciten.</em></p>
""") + """

<h3>Por que funciona</h3>
<p>Este es el tipo de nota que mas se publica, con diferencia. Los medios necesitan datos locales y casi
nunca los tienen. Si puedes generar cifras propias de tu sector, tienes una via de entrada permanente.</p>

<h2>4. Premio o reconocimiento</h2>
""" + EJ.format(contenido="""
<p><strong>Una panaderia de Naron, premiada como mejor pan de centeno de Galicia</strong></p>
<p><em>El galardon lo concede la Asociacion Galega de Obradoiros tras una cata ciega con 94 participantes</em></p>
<p>Naron, 21 de noviembre de 2026. El obradoiro Pan da Ria ha obtenido el primer premio en la categoria
de pan de centeno de los Premios Galegos do Pan 2026, concedidos por la Asociacion Galega de Obradoiros
tras una cata ciega en la que participaron 94 establecimientos de las cuatro provincias.</p>
<p>El jurado, formado por siete profesionales del sector y dos criticos gastronomicos, valoro la
fermentacion con masa madre de cultivo propio y el uso de centeno de produccion gallega.</p>
<p>&laquo;Llevamos nueve anos con la misma masa madre; esto premia la constancia mas que una receta&raquo;,
afirma Ana Pardo, responsable del obradoiro.</p>
<p style="text-align:center">###</p>
<p style="font-size:15px"><strong>Contacto de prensa:</strong> Ana Pardo &middot; 981 000 000 &middot; info@pandaria.es<br>
<em>Pan da Ria es un obradoiro artesanal fundado en 2017 en Naron, con dos puntos de venta.</em></p>
""") + """

<h3>Por que funciona</h3>
<p>El premio lo concede un tercero, no la propia empresa, y se explica el procedimiento (cata ciega, 94
participantes, jurado). Un reconocimiento sin ese detalle parece autobombo y no se publica.</p>

<h2>Lo que tienen en comun los cuatro</h2>
<table>
  <tr><th>Elemento</th><th>En los cuatro ejemplos</th></tr>
  <tr><td>Titular</td><td>Contiene el hecho y el lugar, sin el nombre de la empresa delante</td></tr>
  <tr><td>Primer parrafo</td><td>Resuelve que, quien, cuando, donde y por que</td></tr>
  <tr><td>Cifras</td><td>Al menos tres datos concretos y verificables</td></tr>
  <tr><td>Cita</td><td>Una sola, que aporta algo que no esta en los datos</td></tr>
  <tr><td>Extension</td><td>Entre 250 y 350 palabras</td></tr>
  <tr><td>Cierre</td><td>###, contacto y boilerplate</td></tr>
</table>

<p>Coge el esqueleto en blanco en la <a href="/guia/plantilla-nota-de-prensa/">plantilla</a> o repasa
el orden en <a href="/guia/estructura-de-una-nota-de-prensa/">la estructura</a>.</p>
"""
    preguntas = [
        ("Donde puedo ver ejemplos de notas de prensa",
         "En esta pagina tienes cuatro ejemplos completos y gratuitos: apertura de negocio, lanzamiento de "
         "producto, publicacion de datos propios y premio o reconocimiento."),
        ("Que tipo de nota de prensa se publica mas",
         "Las que aportan datos propios locales. Los medios necesitan cifras de su zona y casi nunca las "
         "tienen, asi que un estudio con datos reales tiene muchas mas posibilidades que un anuncio."),
        ("Puedo copiar estos ejemplos",
         "Puedes copiar la estructura y adaptarla con tus datos, para eso estan. Los nombres de empresa y "
         "las cifras son inventados."),
        ("Cuantas palabras tienen estos ejemplos",
         "Entre 250 y 350 palabras cada uno, que es la extension que mejor funciona en una redaccion."),
    ]
    return guia("/guia/ejemplos-de-notas-de-prensa/",
                "Ejemplos de notas de prensa",
                "4 ejemplos de notas de prensa reales y completos (2026)",
                "Cuatro ejemplos completos de nota de prensa: apertura de negocio, lanzamiento de producto, "
                "datos propios y premio. Con el analisis de por que funciona cada uno.",
                "Cuatro notas completas, de los tipos que mas se envian, con el analisis de por que cada una "
                "pasa el filtro de una redaccion.", c, preguntas)


def plantilla():
    c = """
<p>El esqueleto en blanco, con las indicaciones de que va en cada hueco. Copialo, pega los corchetes
por tus datos y borra las notas en cursiva.</p>

<h2>Plantilla de nota de prensa</h2>
<div style="border:1px solid var(--linea);border-left:4px solid var(--acento);border-radius:8px;
     padding:24px 26px;margin:22px 0;background:#fcfcfb;font-family:-apple-system,sans-serif;font-size:16px">
<p><strong>[TITULAR: el hecho en menos de 15 palabras, como lo publicaria el periodico]</strong></p>
<p><em>[SUBTITULO: el dato o la cifra que sostiene el titular]</em></p>
<p>[CIUDAD], [fecha completa]. [ENTRADILLA: que ha pasado, quien lo ha hecho, cuando, donde y por que
importa. Tres o cuatro lineas. Si alguien solo lee esto, tiene que poder contar la noticia entera.]</p>
<p>[PARRAFO 2: el dato mas importante que no cabia arriba. Cifras concretas, plazos, caracteristicas.]</p>
<p>[PARRAFO 3: contexto. Como esta el sector, con que se compara, que datos externos lo respaldan.]</p>
<p>&laquo;[CITA: una declaracion que aporte interpretacion o compromiso, no entusiasmo]&raquo;, senala
[NOMBRE], [CARGO] de [EMPRESA].</p>
<p>[PARRAFO 4, opcional: detalles practicos. Horarios, precios, donde se puede ver o probar.]</p>
<p style="text-align:center">###</p>
<p><strong>Contacto de prensa</strong><br>
[Nombre]<br>
[Telefono directo que alguien va a coger]<br>
[Correo]</p>
<p><em>[BOILERPLATE: parrafo fijo sobre la empresa. A que se dedica, desde cuando, tamano, donde opera.
El mismo en todas tus notas.]</em></p>
</div>

<h2>Plantilla del correo de envio</h2>
<div style="border:1px solid var(--linea);border-left:4px solid var(--tinta-3);border-radius:8px;
     padding:24px 26px;margin:22px 0;background:#fcfcfb;font-family:-apple-system,sans-serif;font-size:16px">
<p><strong>Asunto:</strong> [El titular de la noticia, tal cual]</p>
<p>Hola [nombre del periodista]:</p>
<p>[Una linea diciendo por que le escribes a el en concreto: porque cubre ese sector, porque escribio
sobre un tema parecido, porque es de esa comarca.]</p>
<p>[Dos lineas resumiendo la noticia.]</p>
<p>Te dejo la nota completa debajo y quedo disponible para ampliar o para concertar una entrevista.</p>
<p>Un saludo,<br>[Tu nombre y telefono]</p>
<p>---</p>
<p>[AQUI LA NOTA COMPLETA, pegada en el cuerpo del correo, nunca solo como adjunto]</p>
</div>

<h2>Lista de comprobacion antes de enviar</h2>
<ul>
  <li>Entre 300 y 500 palabras, una pagina.</li>
  <li>Titular sin el nombre de la empresa delante.</li>
  <li>Las cinco W resueltas en el primer parrafo.</li>
  <li>Al menos tres datos verificables.</li>
  <li>Todo en tercera persona, salvo dentro de la cita.</li>
  <li>Sin lider, innovador, revolucionario ni unico.</li>
  <li>Telefono operativo.</li>
  <li>Texto en el cuerpo del correo.</li>
  <li>Imagen horizontal de al menos 1200 px, con pie.</li>
  <li>Enviada un martes, miercoles o jueves por la manana.</li>
</ul>

<h2>Como usarla</h2>
<p>Lo mas practico es guardarla como documento y duplicarla cada vez. El boilerplate y los datos de
contacto no cambian nunca, asi que a partir de la segunda nota solo rellenas la mitad.</p>
<p>Si quieres ver la plantilla rellenada, tienes cuatro
<a href="/guia/ejemplos-de-notas-de-prensa/">ejemplos completos</a>.</p>
"""
    preguntas = [
        ("Donde descargar una plantilla de nota de prensa",
         "En esta pagina tienes la plantilla completa para copiar y pegar, sin registro ni correo. Incluye "
         "tambien la plantilla del correo de envio."),
        ("Que va en el boilerplate de la plantilla",
         "Un parrafo corto y fijo sobre la empresa: a que se dedica, desde cuando existe, tamano y donde "
         "opera. Es identico en todas tus notas."),
        ("La plantilla sirve para cualquier tipo de nota",
         "Si. La estructura es la misma para una apertura, un lanzamiento, un premio o unos datos propios. "
         "Lo que cambia es el contenido de cada hueco."),
    ]
    return guia("/guia/plantilla-nota-de-prensa/",
                "Plantilla de nota de prensa",
                "Plantilla de nota de prensa gratis para copiar (2026)",
                "Plantilla de nota de prensa lista para copiar, con las indicaciones de que va en cada "
                "parte, plantilla del correo de envio y lista de comprobacion. Sin registro.",
                "El esqueleto en blanco con las indicaciones dentro, mas la plantilla del correo y la lista "
                "de comprobacion. Sin registro ni descarga.", c, preguntas)


def evento():
    c = """
<p>Un evento no lleva una nota de prensa: lleva tres, y cada una tiene un objetivo distinto. Enviar
solo la primera, que es lo habitual, desaprovecha la mitad de la cobertura posible.</p>

<h2>Nota 1: la convocatoria (10-15 dias antes)</h2>
<p>El objetivo no es que publiquen nada, es que <strong>vaya un periodista</strong>. Por eso es corta y
practica: que, cuando, donde, quien estara y por que merece cubrirlo.</p>
<ul>
  <li>Fecha, hora de inicio y duracion aproximada.</li>
  <li>Direccion exacta y como llegar.</li>
  <li>Quien asiste: nombres y cargos relevantes.</li>
  <li>Si hay posibilidad de entrevistas y a que hora.</li>
  <li>Si habra material grafico disponible.</li>
</ul>
<p>Se reenvia 48 horas antes como recordatorio, esta vez si, porque es informacion de agenda.</p>

<h2>Nota 2: la del dia (durante o justo despues)</h2>
<p>Aqui si hay noticia. Se envia el mismo dia, lo antes posible: un medio que no pudo ir puede publicar
con tu material si le llega a tiempo.</p>
<ul>
  <li>Que ha ocurrido y cuanta gente ha asistido, con cifra concreta.</li>
  <li>Lo mas destacado que se ha dicho, en forma de cita.</li>
  <li>Cualquier anuncio o acuerdo que se haya hecho publico.</li>
  <li>Dos o tres fotos en alta, horizontales, con pie y autor.</li>
</ul>
<p>La rapidez vale mas que la perfeccion: una nota enviada a las dos horas con una foto decente se
publica; la misma nota al dia siguiente, ya no.</p>

<h2>Nota 3: resultados o balance (3-7 dias despues)</h2>
<p>La que casi nadie envia y la que mas rinde a medio plazo. Cuando ya tienes datos: asistentes
totales, acuerdos cerrados, impacto economico, conclusiones.</p>
<p>Esta nota entra en medios sectoriales y economicos que no cubren eventos pero si publican datos.</p>

<h2>Ejemplo de convocatoria</h2>
<div style="border:1px solid var(--linea);border-left:4px solid var(--acento);border-radius:8px;
     padding:24px 26px;margin:22px 0;background:#fcfcfb">
<p><strong>Convocatoria: la comarca de Ferrolterra acoge la primera feria de rehabilitacion de vivienda del noroeste</strong></p>
<p><em>Participan 40 empresas y se celebrara el sabado 13 de diciembre en el recinto ferial de Ferrol</em></p>
<p>Ferrol, 1 de diciembre de 2026. El sabado 13 de diciembre se celebra en el recinto ferial de Ferrol
la primera edicion de Rehabita, feria dedicada a la rehabilitacion de vivienda, con la participacion de
40 empresas del sector y una previsión de 2.000 visitantes.</p>
<p><strong>Cuando:</strong> sabado 13 de diciembre, de 10:00 a 20:00<br>
<strong>Donde:</strong> Recinto ferial de Ferrol, Punta Arnela<br>
<strong>Apertura oficial:</strong> 10:00, con la alcaldesa de Ferrol<br>
<strong>Entrevistas:</strong> organizacion disponible de 11:00 a 13:00<br>
<strong>Material grafico:</strong> disponible para descarga desde el dia 12</p>
<p style="text-align:center">###</p>
<p style="font-size:15px"><strong>Contacto:</strong> [nombre] &middot; [telefono] &middot; [correo]</p>
</div>

<h2>Errores que cuestan la cobertura</h2>
<ul>
  <li>Convocar con dos dias de antelacion: las agendas se cierran con una semana.</li>
  <li>Convocar en viernes tarde o en fin de semana sin avisar con tiempo.</li>
  <li>No dar una direccion exacta ni indicaciones de aparcamiento.</li>
  <li>No tener a nadie disponible para hablar cuando llega el periodista.</li>
  <li>Enviar la nota del dia 48 horas despues, cuando ya no es actualidad.</li>
</ul>

<p>Si el evento es importante y no quieres jugartela, el <a href="/precios/">plan de campana</a> cubre
las tres notas y la gestion de entrevistas.</p>
"""
    preguntas = [
        ("Cuantas notas de prensa lleva un evento",
         "Tres: la convocatoria entre diez y quince dias antes, la del mismo dia del evento y una de "
         "balance con datos entre tres y siete dias despues."),
        ("Con cuanta antelacion se convoca a la prensa",
         "Entre diez y quince dias, con un recordatorio 48 horas antes. Las agendas de las redacciones se "
         "cierran con alrededor de una semana de margen."),
        ("Que debe llevar una convocatoria de prensa",
         "Fecha, hora, duracion, direccion exacta, quien asiste con nombres y cargos, si hay entrevistas "
         "disponibles y a que hora, y si habra material grafico."),
        ("Que pasa si no viene ningun periodista",
         "Por eso existe la nota del mismo dia con fotos en alta: un medio que no pudo ir puede publicar "
         "con tu material si le llega en las primeras horas."),
    ]
    return guia("/guia/nota-de-prensa-evento/",
                "Nota de prensa para un evento",
                "Nota de prensa de un evento: las 3 que hay que enviar",
                "Como hacer la nota de prensa de un evento: convocatoria, nota del dia y balance posterior. "
                "Con ejemplo de convocatoria y los plazos de cada una.",
                "Un evento lleva tres notas, no una. Convocatoria, la del dia y la de balance, cada una con "
                "su objetivo y su plazo.", c, preguntas)


def diferencia():
    c = """
<p>Respuesta corta: en la practica profesional espanola son lo mismo y se usan indistintamente. Si
alguien te corrige porque has dicho uno en vez de otro, esta hilando mas fino de lo que hila cualquier
redaccion.</p>

<h2>La distincion que a veces se hace</h2>
<p>Hay profesionales que reservan cada termino para un uso:</p>
<table>
  <tr><th></th><th>Nota de prensa</th><th>Comunicado de prensa</th></tr>
  <tr><td>Uso tipico</td><td>Anuncios ordinarios: aperturas, lanzamientos, datos</td><td>Mensajes institucionales o situaciones de crisis</td></tr>
  <tr><td>Tono</td><td>Informativo</td><td>Formal, a veces defensivo</td></tr>
  <tr><td>Quien lo firma</td><td>Departamento de comunicacion</td><td>La direccion o el consejo</td></tr>
  <tr><td>Frecuencia</td><td>Regular</td><td>Excepcional</td></tr>
</table>
<p>Es una distincion util cuando trabajas dentro de un gabinete y necesitas nombrar cosas distintas.
Fuera de ahi, no la aplica casi nadie.</p>

<h2>Por que en la practica da igual</h2>
<p>Porque <strong>se escriben exactamente igual</strong>. Mismo formato, misma estructura de piramide
invertida, misma extension, mismos destinatarios y mismo canal de envio. Un periodista que recibe un
texto no mira como lo llamas: mira si tiene noticia dentro.</p>
<p>En las redacciones espanolas se dice mas &laquo;nota de prensa&raquo; en el dia a dia. En America
Latina se usa mas &laquo;comunicado de prensa&raquo;. En ingles, ambos son <em>press release</em>.</p>

<h2>El caso en que si conviene decir comunicado</h2>
<p>Cuando estas respondiendo publicamente a una situacion delicada: un accidente, una polemica, una
acusacion, un despido colectivo. Ahi la palabra <em>comunicado</em> transmite formalidad y posicion
oficial, y eso ayuda al tono del mensaje.</p>
<p>En ese caso ademas cambian algunas cosas de la redaccion:</p>
<ul>
  <li>Se escribe mas corto, a veces tres parrafos.</li>
  <li>Se evita cualquier cifra o dato que pueda discutirse despues.</li>
  <li>La cita la firma la maxima responsabilidad, no un portavoz.</li>
  <li>Se publica tambien en la propia web, no solo se envia.</li>
  <li>Se revisa juridicamente antes de salir.</li>
</ul>

<h2>Y la rueda de prensa</h2>
<p>Esa si es otra cosa: es un acto presencial donde convocas a los medios para contarlo en persona y
responder preguntas. La nota o el comunicado son texto; la rueda de prensa es un evento. Lo normal es
que la rueda de prensa lleve ademas una nota, que se entrega alli mismo.</p>

<p>Como se escriben los dos, lo tienes en <a href="/guia/estructura-de-una-nota-de-prensa/">la
estructura</a> y en los <a href="/guia/ejemplos-de-notas-de-prensa/">ejemplos</a>.</p>
"""
    preguntas = [
        ("Que diferencia hay entre nota de prensa y comunicado de prensa",
         "En la practica ninguna: se escriben igual y se envian igual. Algunos reservan comunicado para "
         "mensajes institucionales o de crisis y nota para anuncios ordinarios, pero no es una distincion "
         "que apliquen las redacciones."),
        ("Cual de los dos terminos se usa mas en Espana",
         "En el dia a dia de las redacciones espanolas se dice mas nota de prensa. Comunicado de prensa es "
         "mas habitual en America Latina y en contextos institucionales."),
        ("Que es una rueda de prensa",
         "Un acto presencial al que se convoca a los medios para contar algo en persona y responder "
         "preguntas. Suele acompanarse de una nota que se entrega alli."),
        ("Como se dice nota de prensa en ingles",
         "Press release, que sirve tanto para nota como para comunicado."),
    ]
    return guia("/guia/diferencia-nota-y-comunicado/",
                "Nota de prensa y comunicado de prensa: la diferencia",
                "Diferencia entre nota de prensa y comunicado de prensa",
                "Si nota de prensa y comunicado de prensa son lo mismo, cuando se usa cada termino y que "
                "cambia de verdad en la redaccion cuando se trata de una crisis.",
                "Son lo mismo, con un matiz que solo importa en situaciones de crisis. Aqui esta la "
                "distincion y cuando conviene aplicarla.", c, preguntas)


def ingles():
    c = """
<p>Un <em>press release</em> sigue la misma logica que una nota de prensa espanola, pero hay
convenciones de formato que si cambian y que delatan inmediatamente a quien ha traducido en vez de
redactar.</p>

<h2>Estructura y vocabulario</h2>
<table>
  <tr><th>Parte</th><th>En ingles</th><th>Nota</th></tr>
  <tr><td>Titular</td><td>Headline</td><td>Title Case o sentence case, nunca mayusculas</td></tr>
  <tr><td>Subtitulo</td><td>Subheadline / Dek</td><td>Una linea</td></tr>
  <tr><td>Lugar y fecha</td><td>Dateline</td><td><em>FERROL, Spain, Nov. 21, 2026</em></td></tr>
  <tr><td>Entradilla</td><td>Lead / Lede</td><td>Las cinco W</td></tr>
  <tr><td>Cuerpo</td><td>Body</td><td>Piramide invertida igual</td></tr>
  <tr><td>Cita</td><td>Quote</td><td>Con nombre y titulo</td></tr>
  <tr><td>Parrafo de empresa</td><td>Boilerplate</td><td>Encabezado <em>About [Empresa]</em></td></tr>
  <tr><td>Contacto</td><td>Media Contact</td><td>Al final</td></tr>
  <tr><td>Cierre</td><td>###</td><td>Igual que en espanol</td></tr>
</table>

<h2>Lo que cambia de verdad</h2>

<h3>La dateline</h3>
<p>Va en mayusculas la ciudad, seguida del pais si no es obvio, y la fecha abreviada al estilo
anglosajon: <em>FERROL, Spain, Nov. 21, 2026</em>. En prensa estadounidense los meses de mas de cinco
letras se abrevian (Jan., Feb., Aug., Sept., Oct., Nov., Dec.), pero March, April, May, June y July se
escriben enteros.</p>

<h3>FOR IMMEDIATE RELEASE</h3>
<p>Es la formula que encabeza el documento en el mercado estadounidense, arriba a la izquierda. Si la
nota esta embargada hasta una fecha, se sustituye por <em>EMBARGOED UNTIL [fecha y hora con zona
horaria]</em>. En Espana no se usa, en Estados Unidos se espera.</p>

<h3>Las comillas</h3>
<p>Dobles rectas (&quot;) y el punto final dentro de la comilla en ingles americano. Nada de comillas
angulares.</p>

<h3>Cifras y unidades</h3>
<p>Separador decimal con punto y de miles con coma, al reves que en espanol: 1,400 contracts y 6.8
euros per square metre. Y si la noticia va a un medio estadounidense, conviene dar la conversion a
dolares y a unidades imperiales entre parentesis.</p>

<h3>Longitud</h3>
<p>Mas corto: entre 300 y 400 palabras. La tolerancia a la extension es menor que en prensa espanola.</p>

<h2>Errores tipicos del traductor automatico</h2>
<ul>
  <li>Traducir el titular literalmente: en ingles el titular se reescribe, no se traduce.</li>
  <li>Dejar la estructura de frase espanola, mucho mas larga y subordinada.</li>
  <li>Usar <em>actually</em> por <em>actualmente</em> (significa <em>en realidad</em>).</li>
  <li>Usar <em>notice</em> o <em>note</em> por nota de prensa: es <em>press release</em>.</li>
  <li>Mantener el tratamiento formal: en ingles de prensa se usa el apellido a secas tras la primera mencion.</li>
</ul>

<h2>Si vas a enviarla a medios internacionales</h2>
<p>No basta con traducir: hay que adaptar el contexto. Una cifra de A Coruna no dice nada a un redactor
de Londres salvo que la compares con algo que conozca. Y la noticia tiene que tener relevancia fuera de
tu mercado, que es la parte donde fracasan la mayoria de los intentos.</p>
"""
    preguntas = [
        ("Como se dice nota de prensa en ingles",
         "Press release. Tambien se usa news release, sobre todo en medios estadounidenses. Nunca note o "
         "notice, que significan otra cosa."),
        ("Que significa FOR IMMEDIATE RELEASE",
         "Es la formula que encabeza un press release en el mercado estadounidense e indica que puede "
         "publicarse ya. Si hay embargo, se sustituye por EMBARGOED UNTIL con la fecha y la hora."),
        ("Cuanto mide un press release",
         "Entre 300 y 400 palabras, algo mas corto que la nota de prensa espanola."),
        ("Puedo traducir mi nota de prensa espanola al ingles",
         "Traducirla literalmente no funciona: el titular se reescribe, la estructura de frase es mas corta "
         "y hay que adaptar cifras, unidades y contexto para que signifiquen algo fuera de Espana."),
    ]
    return guia("/guia/nota-de-prensa-en-ingles/",
                "Nota de prensa en ingles (press release)",
                "Nota de prensa en ingles: estructura y formato del press release",
                "Como escribir una nota de prensa en ingles: estructura del press release, dateline, "
                "FOR IMMEDIATE RELEASE, formato de cifras y errores tipicos al traducir.",
                "Misma logica, distintas convenciones. Lo que cambia de verdad entre una nota de prensa "
                "espanola y un press release, y los errores que delatan una traduccion.", c, preguntas)
