# -*- coding: utf-8 -*-
"""Paginas legales y contacto"""
from build import escribir, migas, FORMULARIO

EMPRESA = "Grupo Seocar S.L."
DIR = "Rua Republica Argentina 30-32, 3 Izq, 15404 Ferrol (A Coruna)"
MAIL = "hola@comunicadosdeprensa.es"


def simple(ruta, h1, titulo, desc, cuerpo_html):
    bar, bar_ld = migas([("Inicio", "/"), (h1, None)])
    cuerpo = """
{bar}
<main><div class="wrap">
<article class="contenido" style="padding-top:26px">
<h1>{h1}</h1>
{c}
</article>
</div></main>
""".format(bar=bar, h1=h1, c=cuerpo_html)
    return escribir(ruta, titulo, desc, cuerpo, [bar_ld])


def contacto():
    bar, bar_ld = migas([("Inicio", "/"), ("Contacto", None)])
    cuerpo = """
{bar}
<main><div class="wrap"><div class="cols">
<article class="contenido">
<h1>Contacto</h1>
<p class="entradilla">Cuentanos que quieres anunciar y te decimos si da para noticia, que plan encaja y
cuanto costaria. Respondemos en menos de 24 horas laborables.</p>
{form}
<h2>Otros datos</h2>
<p><strong>Correo:</strong> <a href="mailto:{mail}">{mail}</a><br>
<strong>Empresa:</strong> {emp}<br>
<strong>Direccion:</strong> {dir}</p>
<h2>Si eres periodista</h2>
<p>Si trabajas en un medio y quieres recibir las notas de prensa que distribuimos de tu sector o tu
provincia, escribenos y te damos de alta en el envio. Puedes darte de baja cuando quieras con un
solo correo.</p>
<h2>Si quieres aparecer en el directorio</h2>
<p>Si llevas un medio que no esta en nuestro <a href="/medios/">directorio</a> y crees que deberia
estar, dinoslo. Es gratuito y no pedimos nada a cambio.</p>
</article>
<aside class="aside">
  <div class="card">
    <h3>Respuesta rapida</h3>
    <p>De lunes a viernes respondemos el mismo dia. Si tienes un lanzamiento con fecha, dilo en el
    mensaje y lo priorizamos.</p>
  </div>
</aside>
</div></div></main>
""".format(bar=bar, form=FORMULARIO, mail=MAIL, emp=EMPRESA, dir=DIR)
    return escribir("/contacto/", "Contacto | ComunicadosdePrensa.es",
                    "Contacta con nosotros para publicar y distribuir tu nota de prensa. Respuesta en "
                    "menos de 24 horas laborables.", cuerpo, [bar_ld])


def aviso_legal():
    c = """
<h2>Datos identificativos</h2>
<p>En cumplimiento de la Ley 34/2002, de Servicios de la Sociedad de la Informacion y de Comercio
Electronico, se informa de que este sitio web es titularidad de:</p>
<ul>
  <li><strong>Titular:</strong> {emp}</li>
  <li><strong>Domicilio:</strong> {dir}</li>
  <li><strong>Correo electronico:</strong> {mail}</li>
  <li><strong>Dominio:</strong> comunicadosdeprensa.es</li>
</ul>

<h2>Objeto</h2>
<p>Este sitio web ofrece servicios de redaccion, publicacion y distribucion de notas de prensa, asi
como contenidos informativos gratuitos sobre comunicacion corporativa.</p>

<h2>Condiciones de uso</h2>
<p>El acceso a este sitio web es gratuito salvo en lo relativo al coste de la conexion. El usuario se
compromete a utilizar el sitio conforme a la ley, a este aviso legal y a la buena fe.</p>

<h2>Propiedad intelectual</h2>
<p>Los contenidos de este sitio (textos, guias, plantillas y diseno) son titularidad de {emp} salvo
indicacion en contrario. Las plantillas y ejemplos publicados pueden utilizarse libremente para
elaborar notas de prensa propias. Queda prohibida su reproduccion masiva o su republicacion como
contenido propio en otros sitios web.</p>
<p>Las marcas, nombres comerciales y logotipos de terceros que puedan aparecer pertenecen a sus
titulares. Su mencion no implica relacion comercial ni recomendacion mutua.</p>

<h2>Enlaces a terceros</h2>
<p>Este sitio incluye enlaces a webs de medios de comunicacion con finalidad informativa. {emp} no se
responsabiliza de sus contenidos ni de su politica de privacidad.</p>

<h2>Responsabilidad</h2>
<p>{emp} no garantiza la publicacion de las notas de prensa distribuidas en medios de comunicacion
ajenos, dado que la decision editorial corresponde exclusivamente a cada medio. Si garantiza la
publicacion en sus propios canales y la realizacion del envio contratado.</p>

<h2>Legislacion aplicable</h2>
<p>Las presentes condiciones se rigen por la legislacion espanola. Para la resolucion de cualquier
controversia las partes se someten a los juzgados y tribunales del domicilio del usuario cuando este
tenga la condicion de consumidor.</p>
""".format(emp=EMPRESA, dir=DIR, mail=MAIL)
    return simple("/aviso-legal/", "Aviso legal", "Aviso legal | ComunicadosdePrensa.es",
                  "Aviso legal e informacion del titular de comunicadosdeprensa.es.", c)


def privacidad():
    c = """
<h2>Responsable del tratamiento</h2>
<p><strong>{emp}</strong>, con domicilio en {dir} y correo de contacto {mail}.</p>

<h2>Que datos tratamos y para que</h2>
<table>
  <tr><th>Finalidad</th><th>Datos</th><th>Base legal</th><th>Conservacion</th></tr>
  <tr><td>Responder solicitudes de presupuesto</td><td>Nombre, email, telefono y mensaje</td>
      <td>Consentimiento del interesado</td><td>1 ano desde el ultimo contacto</td></tr>
  <tr><td>Prestacion del servicio contratado</td><td>Datos identificativos y de facturacion</td>
      <td>Ejecucion del contrato</td><td>6 anos (obligaciones fiscales)</td></tr>
  <tr><td>Envio de notas de prensa a periodistas</td><td>Datos profesionales de contacto</td>
      <td>Interes legitimo en comunicacion corporativa</td><td>Hasta solicitud de baja</td></tr>
</table>

<h2>Destinatarios</h2>
<p>No cedemos datos a terceros salvo obligacion legal. Utilizamos proveedores de alojamiento y de
correo electronico que actuan como encargados del tratamiento con contrato firmado.</p>
<p>Cuando contratas un servicio de distribucion, los datos de contacto que figuren en tu nota de prensa
se envian a los medios seleccionados, ya que esa es la finalidad del servicio.</p>

<h2>Tus derechos</h2>
<p>Puedes ejercer los derechos de acceso, rectificacion, supresion, oposicion, limitacion y
portabilidad escribiendo a {mail}, indicando el derecho que ejerces. Si consideras que no hemos
atendido correctamente tu solicitud, puedes reclamar ante la Agencia Espanola de Proteccion de Datos
(<a href="https://www.aepd.es" rel="nofollow noopener" target="_blank">aepd.es</a>).</p>

<h2>Periodistas y medios</h2>
<p>Si eres periodista y has recibido una nota de prensa nuestra, tus datos profesionales proceden de
fuentes publicas (la web del propio medio) y los tratamos por interes legitimo en el marco de la
comunicacion corporativa. Puedes solicitar la baja respondiendo a cualquiera de nuestros correos o
escribiendo a {mail}, y la aplicamos de forma inmediata y definitiva.</p>

<h2>Seguridad</h2>
<p>Aplicamos medidas tecnicas y organizativas para proteger los datos. La web utiliza conexion cifrada
mediante certificado SSL.</p>
""".format(emp=EMPRESA, dir=DIR, mail=MAIL)
    return simple("/privacidad/", "Politica de privacidad",
                  "Politica de privacidad | ComunicadosdePrensa.es",
                  "Como tratamos tus datos personales: finalidades, base legal, plazos de conservacion y "
                  "como ejercer tus derechos.", c)


def cookies():
    c = """
<h2>Que cookies usamos</h2>
<p>Este sitio web <strong>no utiliza cookies de analitica, de publicidad ni de seguimiento de
terceros</strong>. No hay rastreadores, ni pixeles publicitarios, ni perfilado de visitantes.</p>

<h2>Cookies tecnicas</h2>
<p>El servidor puede generar cookies estrictamente necesarias para el funcionamiento del sitio y para
la seguridad de la conexion. Estas cookies estan exentas del deber de consentimiento previo segun el
articulo 22.2 de la LSSI y la guia de la Agencia Espanola de Proteccion de Datos.</p>

<h2>Servicios de terceros</h2>
<p>El formulario de contacto se procesa mediante un servicio externo de envio de formularios, que trata
unicamente los datos que tu introduces para hacernoslos llegar.</p>
<p>Los enlaces a medios de comunicacion que aparecen en el directorio llevan a webs de terceros que si
pueden utilizar cookies propias. Te recomendamos consultar sus respectivas politicas.</p>

<h2>Como gestionar las cookies</h2>
<p>Puedes configurar tu navegador para bloquear o eliminar cookies en cualquier momento desde las
opciones de privacidad de Chrome, Firefox, Safari o Edge. Bloquear las cookies tecnicas de este sitio
no impide su navegacion.</p>

<h2>Actualizaciones</h2>
<p>Si en el futuro incorporamos herramientas de analitica, actualizaremos esta politica y solicitaremos
tu consentimiento previo mediante un banner antes de instalar ninguna cookie no exenta.</p>
"""
    return simple("/cookies/", "Politica de cookies", "Politica de cookies | ComunicadosdePrensa.es",
                  "Este sitio no utiliza cookies de analitica ni publicitarias. Informacion sobre cookies "
                  "tecnicas y servicios de terceros.", c)
