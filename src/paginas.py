# -*- coding: utf-8 -*-
"""Paginas comerciales"""
from build import (escribir, migas, faq_html, FORMULARIO, CAJA_LATERAL,
                   ORG, servicio_schema, articulo_schema)


def home():
    cuerpo = """
<section class="hero">
  <div class="wrap">
    <h1>Un comunicado de prensa que los medios publican</h1>
    <p class="entradilla">Lo escribimos, lo publicamos y lo enviamos a los periodistas de tu sector.
    Sin cuotas, sin permanencia y con el enlace y la cobertura por escrito antes de que pagues.</p>
    <div class="hero-cta">
      <a href="/precios/#cotizar" class="btn lg">Pedir presupuesto</a>
      <a href="/guia/" class="btn ghost lg">Aprender a escribirlo</a>
    </div>
    <p class="hero-nota">Respuesta en menos de 24&nbsp;horas &middot; Desde 95&nbsp;&euro; por nota</p>
  </div>
</section>

<div class="bloque crema">
  <div class="wrap">
    <h2>Solo tres de cada cien notas de prensa llegan a publicarse</h2>
    <p class="sub">Y no es por falta de suerte. Casi la mitad de las que se envian tienen errores de
    redaccion periodistica, y la mayoria aterrizan en la bandeja equivocada.</p>
    <div class="rejilla">
      <div class="caja">
        <div class="num">El problema</div>
        <h3>Escrita como publicidad</h3>
        <p>Un periodista descarta en cinco segundos cualquier texto que suene a folleto. La nota tiene
        que estar escrita como una noticia, no como un anuncio de tu empresa.</p>
      </div>
      <div class="caja">
        <div class="num">El problema</div>
        <h3>Enviada a quien no toca</h3>
        <p>Mandar la misma nota a doscientas direcciones genericas no funciona. Hay que saber que
        seccion cubre tu tema y en que medio.</p>
      </div>
      <div class="caja">
        <div class="num">El problema</div>
        <h3>Sin nada noticiable</h3>
        <p>Si la noticia es que tu empresa existe, no hay noticia. Nuestro trabajo empieza por
        encontrar el angulo que si interesa.</p>
      </div>
    </div>
  </div>
</div>

<div class="bloque">
  <div class="wrap">
    <h2>Como trabajamos</h2>
    <p class="sub">Cuatro pasos. Tu solo intervienes en el primero y en el visto bueno.</p>
    <div class="rejilla dos">
      <div class="caja">
        <div class="num">Paso 1</div>
        <h3>Nos cuentas que quieres anunciar</h3>
        <p>Por telefono o por escrito, como prefieras. Diez minutos bastan. Si lo que tienes no da
        para una noticia, te lo decimos y buscamos otro enfoque.</p>
      </div>
      <div class="caja">
        <div class="num">Paso 2</div>
        <h3>Redactamos la nota</h3>
        <p>Con estructura de piramide invertida, titular de prensa y las cinco W resueltas en el primer
        parrafo. La recibes para aprobarla antes de que salga.</p>
      </div>
      <div class="caja">
        <div class="num">Paso 3</div>
        <h3>La publicamos y la distribuimos</h3>
        <p>Se publica en nuestro medio y se envia a los periodistas que cubren tu sector y tu provincia,
        uno a uno, no en copia oculta masiva.</p>
      </div>
      <div class="caja">
        <div class="num">Paso 4</div>
        <h3>Te pasamos el informe</h3>
        <p>Listado de medios donde ha salido, enlaces y a quien se ha enviado. Sin cifras infladas:
        lo que hay es lo que ves.</p>
      </div>
    </div>
  </div>
</div>

<div class="bloque crema">
  <div class="wrap">
    <div class="cols" style="padding-top:0">
      <div class="contenido">
        <h2 style="margin-top:0">Que es un comunicado de prensa</h2>
        <p>Un comunicado de prensa, tambien llamado nota de prensa, es un texto breve que una empresa o
        una institucion envia a los medios de comunicacion para anunciar algo que considera noticiable.
        Su objetivo no es que lo lea el publico directamente, sino que un periodista lo tome como punto
        de partida para escribir una noticia.</p>
        <p>Esa diferencia lo cambia todo. El destinatario real no es tu cliente, es el redactor que
        decide que entra en la seccion de manana. Por eso un comunicado se escribe en tercera persona,
        con los datos verificables por delante y sin adjetivos que el periodista tendria que borrar.</p>
        <p>En Espana se usan indistintamente los terminos <strong>comunicado de prensa</strong> y
        <strong>nota de prensa</strong>. Hay quien reserva el primero para mensajes institucionales o de
        crisis y el segundo para anuncios ordinarios, pero en la practica diaria de las redacciones
        significan lo mismo. Lo explicamos a fondo en
        <a href="/guia/diferencia-nota-y-comunicado/">nota de prensa y comunicado de prensa</a>.</p>

        <h2>Cuando merece la pena enviar uno</h2>
        <p>No todo lo que pasa en una empresa es noticia. Estos son los casos que si suelen interesar
        a un medio:</p>
        <ul>
          <li>Apertura de un local, una sede o una delegacion nueva.</li>
          <li>Lanzamiento de un producto o un servicio que no existia antes.</li>
          <li>Datos propios: un estudio, una encuesta o cifras del sector que nadie mas tiene.</li>
          <li>Un premio, una certificacion o un reconocimiento otorgado por un tercero.</li>
          <li>Una contratacion relevante, una alianza o una ronda de inversion.</li>
          <li>Un aniversario redondo con algo que contar detras.</li>
          <li>Una posicion publica sobre algo que esta siendo noticia en tu sector.</li>
        </ul>
        <p>Si tu caso no esta en esa lista, lo hablamos antes de cobrarte nada. A veces la noticia esta
        ahi pero hay que buscarla por otro lado.</p>

        <h2>Que incluye el servicio</h2>
        <p>Redaccion periodistica completa, revision contigo, publicacion con enlace a tu web,
        distribucion segmentada a medios y un informe final con todo lo que ha salido. Puedes ver el
        detalle y las tarifas en la <a href="/precios/">pagina de precios</a>, o empezar por
        <a href="/publicar-nota-de-prensa/">publicar una nota de prensa</a> si ya la tienes escrita.</p>
      </div>
      {caja}
    </div>
  </div>
</div>

<div class="bloque">
  <div class="wrap">
    <h2>Aprende a hacerlo tu mismo</h2>
    <p class="sub">Si prefieres escribirla por tu cuenta, la guia es gratis y esta completa.
    No hay registro ni correo que dejar.</p>
    <div class="rejilla">
      <div class="caja">
        <h3><a href="/guia/estructura-de-una-nota-de-prensa/">Estructura de una nota de prensa</a></h3>
        <p>Las siete partes que tiene que llevar, en orden, y que va en cada una.</p>
      </div>
      <div class="caja">
        <h3><a href="/guia/ejemplos-de-notas-de-prensa/">Ejemplos reales</a></h3>
        <p>Modelos completos por tipo de anuncio, listos para adaptar.</p>
      </div>
      <div class="caja">
        <h3><a href="/guia/plantilla-nota-de-prensa/">Plantilla descargable</a></h3>
        <p>El esqueleto en blanco con las indicaciones dentro.</p>
      </div>
    </div>
  </div>
</div>

<div class="bloque crema">
  <div class="wrap">
    <div style="max-width:720px">
      {faq}
    </div>
  </div>
</div>

<div class="bloque">
  <div class="wrap">
    <h2 id="cotizar">Cuentanos que quieres anunciar</h2>
    <p class="sub">Te decimos si da para noticia y cuanto costaria. Sin compromiso.</p>
    {form}
  </div>
</div>
"""
    preguntas = [
        ("Cuanto cuesta publicar un comunicado de prensa",
         "Desde 95 euros la nota suelta, que incluye redaccion, publicacion y distribucion basica. "
         "Los planes con distribucion ampliada y seguimiento van de 195 a 395 euros. No hay cuotas "
         "mensuales obligatorias ni permanencia."),
        ("Garantizais que salga publicado",
         "Garantizamos la publicacion en nuestro medio con enlace, y el envio a los periodistas del "
         "sector. Lo que ningun servicio serio puede garantizar es que un medio ajeno decida publicarla: "
         "esa decision es del redactor. Quien te garantice cobertura en prensa generalista te esta "
         "vendiendo humo o publicidad encubierta."),
        ("Cuanto tarda",
         "El borrador lo tienes en 48 horas laborables desde que nos cuentas la noticia. Una vez lo "
         "apruebas, la publicacion y el envio salen el mismo dia. Si tienes una fecha limite, dilo al "
         "pedir el presupuesto."),
        ("Puedo enviaros la nota ya escrita",
         "Si. En ese caso solo cobramos la publicacion y la distribucion, que sale mas barato. La "
         "revisamos igualmente y te avisamos si vemos algo que vaya a hacer que la descarten."),
        ("Los enlaces son dofollow",
         "En las publicaciones de pago en medios, si, y se indica en cada caso. En nuestro propio medio "
         "el enlace es nofollow por defecto, que es lo que marcan las directrices de Google para notas "
         "de prensa. Si lo que buscas es enlace SEO, mira la pagina de "
         "<a href='/comprar-enlaces-prensa/'>enlaces en prensa</a>, que es un servicio distinto."),
        ("Trabajais con empresas de fuera de Galicia",
         "Si, trabajamos en toda Espana. Tenemos mas musculo en medios gallegos por cercania, pero la "
         "distribucion es nacional y segmentada por sector."),
    ]
    faq, faq_ld = faq_html(preguntas)
    cuerpo = cuerpo.format(caja=CAJA_LATERAL, faq=faq, form=FORMULARIO)
    return escribir("/", "Comunicado de prensa: redaccion, publicacion y envio a medios",
                    "Escribimos, publicamos y distribuimos tu comunicado de prensa a los medios de tu sector. "
                    "Desde 95 euros, sin permanencia. Presupuesto en 24 horas.",
                    cuerpo, [ORG, faq_ld,
                             servicio_schema("Redaccion y distribucion de comunicados de prensa",
                                             "Servicio de redaccion periodistica, publicacion y envio a medios.", 95)])


def pagina_servicio(ruta, h1, titulo, desc, entradilla, secciones, preguntas, activo="",
                    migas_items=None, precio=None):
    bar, bar_ld = migas(migas_items or [("Inicio", "/"), (h1, None)])
    faq, faq_ld = faq_html(preguntas)
    cuerpo = """
{bar}
<main><div class="wrap"><div class="cols">
<article class="contenido">
<h1>{h1}</h1>
<p class="entradilla">{ent}</p>
{sec}
{faq}
<h2 id="cotizar">Pide presupuesto</h2>
{form}
</article>
{caja}
</div></div></main>
""".format(bar=bar, h1=h1, ent=entradilla, sec=secciones, faq=faq,
           form=FORMULARIO, caja=CAJA_LATERAL)
    schemas = [bar_ld, faq_ld, servicio_schema(h1, desc, precio)]
    return escribir(ruta, titulo, desc, cuerpo, schemas, activo, "article")
