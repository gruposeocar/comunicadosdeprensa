# -*- coding: utf-8 -*-
"""Directorio de medios espanoles. Solo medios verificables; sin datos de contacto inventados."""
from build import escribir, migas, faq_html, CAJA_LATERAL

# (nombre, dominio, ambito, sector)
MEDIOS = [
    # Nacionales generalistas
    ("El Pais", "elpais.com", "Nacional", "Generalista"),
    ("El Mundo", "elmundo.es", "Nacional", "Generalista"),
    ("ABC", "abc.es", "Nacional", "Generalista"),
    ("La Vanguardia", "lavanguardia.com", "Nacional", "Generalista"),
    ("La Razon", "larazon.es", "Nacional", "Generalista"),
    ("El Periodico", "elperiodico.com", "Nacional", "Generalista"),
    ("eldiario.es", "eldiario.es", "Nacional", "Generalista"),
    ("El Confidencial", "elconfidencial.com", "Nacional", "Generalista"),
    ("El Espanol", "elespanol.com", "Nacional", "Generalista"),
    ("20minutos", "20minutos.es", "Nacional", "Generalista"),
    ("Publico", "publico.es", "Nacional", "Generalista"),
    ("infoLibre", "infolibre.es", "Nacional", "Generalista"),
    ("El Independiente", "elindependiente.com", "Nacional", "Generalista"),
    ("Voz Populi", "vozpopuli.com", "Nacional", "Generalista"),
    ("OKdiario", "okdiario.com", "Nacional", "Generalista"),
    ("El HuffPost", "huffingtonpost.es", "Nacional", "Generalista"),
    ("RTVE", "rtve.es", "Nacional", "Generalista"),
    ("Cadena SER", "cadenaser.com", "Nacional", "Generalista"),
    ("COPE", "cope.es", "Nacional", "Generalista"),
    ("Onda Cero", "ondacero.es", "Nacional", "Generalista"),
    ("Europa Press", "europapress.es", "Nacional", "Agencia"),
    ("EFE", "efe.com", "Nacional", "Agencia"),

    # Economia y empresa
    ("Expansion", "expansion.com", "Nacional", "Economia"),
    ("Cinco Dias", "cincodias.elpais.com", "Nacional", "Economia"),
    ("El Economista", "eleconomista.es", "Nacional", "Economia"),
    ("Libre Mercado", "libremercado.com", "Nacional", "Economia"),
    ("Economia Digital", "economiadigital.es", "Nacional", "Economia"),
    ("Merca2", "merca2.es", "Nacional", "Economia"),
    ("Business Insider Espana", "businessinsider.es", "Nacional", "Economia"),
    ("Emprendedores", "emprendedores.es", "Nacional", "Emprendimiento"),
    ("El Referente", "elreferente.es", "Nacional", "Emprendimiento"),

    # Tecnologia
    ("Xataka", "xataka.com", "Nacional", "Tecnologia"),
    ("Genbeta", "genbeta.com", "Nacional", "Tecnologia"),
    ("Hipertextual", "hipertextual.com", "Nacional", "Tecnologia"),
    ("Computer Hoy", "computerhoy.com", "Nacional", "Tecnologia"),
    ("MuyComputer", "muycomputer.com", "Nacional", "Tecnologia"),
    ("ADSLZone", "adslzone.net", "Nacional", "Tecnologia"),

    # Marketing y comunicacion
    ("Marketing Directo", "marketingdirecto.com", "Nacional", "Marketing"),
    ("PuroMarketing", "puromarketing.com", "Nacional", "Marketing"),
    ("Reason Why", "reasonwhy.es", "Nacional", "Marketing"),
    ("PRNoticias", "prnoticias.com", "Nacional", "Marketing"),
    ("Dircomfidencial", "dircomfidencial.com", "Nacional", "Marketing"),
    ("El Publicista", "elpublicista.es", "Nacional", "Marketing"),

    # Inmobiliario y construccion
    ("Idealista News", "idealista.com/news", "Nacional", "Inmobiliario"),
    ("Brainsre News", "brainsre.news", "Nacional", "Inmobiliario"),
    ("El Inmobiliario mes a mes", "elinmobiliariomesames.com", "Nacional", "Inmobiliario"),
    ("Construible", "construible.es", "Nacional", "Construccion"),
    ("CIC Construccion", "cicconstruccion.com", "Nacional", "Construccion"),

    # Legal
    ("Confilegal", "confilegal.com", "Nacional", "Legal"),
    ("Lawyerpress", "lawyerpress.com", "Nacional", "Legal"),
    ("Economist & Jurist", "economistjurist.es", "Nacional", "Legal"),

    # Salud
    ("Redaccion Medica", "redaccionmedica.com", "Nacional", "Salud"),
    ("ConSalud", "consalud.es", "Nacional", "Salud"),
    ("Gaceta Medica", "gacetamedica.com", "Nacional", "Salud"),
    ("Diariofarma", "diariofarma.com", "Nacional", "Salud"),

    # Energia
    ("El Periodico de la Energia", "elperiodicodelaenergia.com", "Nacional", "Energia"),
    ("Energias Renovables", "energias-renovables.com", "Nacional", "Energia"),
    ("PV Magazine Espana", "pv-magazine.es", "Nacional", "Energia"),

    # Turismo
    ("Hosteltur", "hosteltur.com", "Nacional", "Turismo"),
    ("Preferente", "preferente.com", "Nacional", "Turismo"),
    ("Tourinews", "tourinews.es", "Nacional", "Turismo"),
    ("Agent Travel", "agenttravel.es", "Nacional", "Turismo"),

    # Otros sectoriales
    ("Alimarket", "alimarket.es", "Nacional", "Distribucion"),
    ("Cadena de Suministro", "cadenadesuministro.es", "Nacional", "Logistica"),
    ("Motor.es", "motor.es", "Nacional", "Automocion"),
    ("km77", "km77.com", "Nacional", "Automocion"),
    ("Agronegocios", "agronegocios.es", "Nacional", "Agroalimentario"),
    ("Agroinformacion", "agroinformacion.com", "Nacional", "Agroalimentario"),

    # Galicia
    ("La Voz de Galicia", "lavozdegalicia.es", "Galicia", "Generalista"),
    ("Faro de Vigo", "farodevigo.es", "Pontevedra", "Generalista"),
    ("El Correo Gallego", "elcorreogallego.es", "A Coruna", "Generalista"),
    ("La Opinion A Coruna", "laopinioncoruna.es", "A Coruna", "Generalista"),
    ("Diario de Ferrol", "diariodeferrol.com", "A Coruna", "Generalista"),
    ("El Progreso", "elprogreso.es", "Lugo", "Generalista"),
    ("La Region", "laregion.es", "Ourense", "Generalista"),
    ("Atlantico Diario", "atlantico.net", "Pontevedra", "Generalista"),
    ("Galicia Press", "galiciapress.es", "Galicia", "Generalista"),
    ("Codigo Cero", "codigocero.com", "Galicia", "Tecnologia"),
    ("CRTVG", "crtvg.es", "Galicia", "Generalista"),

    # Cataluna
    ("Ara", "ara.cat", "Cataluna", "Generalista"),
    ("El Nacional", "elnacional.cat", "Cataluna", "Generalista"),
    ("Nacio Digital", "naciodigital.cat", "Cataluna", "Generalista"),
    ("Diari de Tarragona", "diaridetarragona.com", "Tarragona", "Generalista"),
    ("Segre", "segre.com", "Lleida", "Generalista"),
    ("Diari de Girona", "diaridegirona.cat", "Girona", "Generalista"),

    # Pais Vasco y Navarra
    ("El Correo", "elcorreo.com", "Bizkaia", "Generalista"),
    ("El Diario Vasco", "diariovasco.com", "Gipuzkoa", "Generalista"),
    ("Deia", "deia.eus", "Bizkaia", "Generalista"),
    ("Noticias de Gipuzkoa", "noticiasdegipuzkoa.eus", "Gipuzkoa", "Generalista"),
    ("EITB", "eitb.eus", "Pais Vasco", "Generalista"),
    ("Diario de Navarra", "diariodenavarra.es", "Navarra", "Generalista"),
    ("Noticias de Navarra", "noticiasdenavarra.com", "Navarra", "Generalista"),
    ("El Correo de Alava", "elcorreo.com/alava", "Araba", "Generalista"),

    # Comunidad Valenciana y Murcia
    ("Las Provincias", "lasprovincias.es", "Valencia", "Generalista"),
    ("Levante-EMV", "levante-emv.com", "Valencia", "Generalista"),
    ("Valencia Plaza", "valenciaplaza.com", "Valencia", "Economia"),
    ("Informacion", "informacion.es", "Alicante", "Generalista"),
    ("Alicante Plaza", "alicanteplaza.es", "Alicante", "Economia"),
    ("El Periodico Mediterraneo", "elperiodicomediterraneo.com", "Castellon", "Generalista"),
    ("Castellon Plaza", "castellonplaza.com", "Castellon", "Economia"),
    ("La Verdad", "laverdad.es", "Murcia", "Generalista"),
    ("La Opinion de Murcia", "laopiniondemurcia.es", "Murcia", "Generalista"),
    ("Murcia Plaza", "murciaplaza.com", "Murcia", "Economia"),

    # Andalucia
    ("Diario de Sevilla", "diariodesevilla.es", "Sevilla", "Generalista"),
    ("El Correo de Andalucia", "elcorreoweb.es", "Sevilla", "Generalista"),
    ("Ideal", "ideal.es", "Granada", "Generalista"),
    ("Granada Hoy", "granadahoy.com", "Granada", "Generalista"),
    ("Diario Sur", "diariosur.es", "Malaga", "Generalista"),
    ("La Opinion de Malaga", "laopiniondemalaga.es", "Malaga", "Generalista"),
    ("Diario de Cadiz", "diariodecadiz.es", "Cadiz", "Generalista"),
    ("Diario de Jerez", "diariodejerez.es", "Cadiz", "Generalista"),
    ("Europa Sur", "europasur.es", "Cadiz", "Generalista"),
    ("El Dia de Cordoba", "eldiadecordoba.es", "Cordoba", "Generalista"),
    ("Huelva Informacion", "huelvainformacion.es", "Huelva", "Generalista"),
    ("Diario de Almeria", "diariodealmeria.es", "Almeria", "Generalista"),
    ("Jaen Hoy", "jaenhoy.es", "Jaen", "Generalista"),

    # Castilla y Leon
    ("El Norte de Castilla", "elnortedecastilla.es", "Valladolid", "Generalista"),
    ("Diario de Burgos", "diariodeburgos.es", "Burgos", "Generalista"),
    ("Diario de Leon", "diariodeleon.es", "Leon", "Generalista"),
    ("Leonoticias", "leonoticias.com", "Leon", "Generalista"),
    ("La Gaceta de Salamanca", "lagacetadesalamanca.es", "Salamanca", "Generalista"),
    ("Salamanca24horas", "salamanca24horas.com", "Salamanca", "Generalista"),
    ("La Opinion de Zamora", "laopiniondezamora.es", "Zamora", "Generalista"),
    ("Diario Palentino", "diariopalentino.es", "Palencia", "Generalista"),
    ("Heraldo-Diario de Soria", "heraldodiariodesoria.es", "Soria", "Generalista"),
    ("El Dia de Segovia", "eldiasegovia.es", "Segovia", "Generalista"),
    ("Diario de Avila", "diariodeavila.es", "Avila", "Generalista"),

    # Castilla-La Mancha
    ("La Tribuna de Toledo", "latribunadetoledo.es", "Toledo", "Generalista"),
    ("La Tribuna de Albacete", "latribunadealbacete.es", "Albacete", "Generalista"),
    ("Lanza Digital", "lanzadigital.com", "Ciudad Real", "Generalista"),
    ("El Dia de Ciudad Real", "eldiadigital.es", "Castilla-La Mancha", "Generalista"),

    # Aragon, Asturias, Cantabria, La Rioja
    ("Heraldo de Aragon", "heraldo.es", "Zaragoza", "Generalista"),
    ("El Periodico de Aragon", "elperiodicodearagon.com", "Zaragoza", "Generalista"),
    ("La Nueva Espana", "lne.es", "Asturias", "Generalista"),
    ("El Comercio", "elcomercio.es", "Asturias", "Generalista"),
    ("El Diario Montanes", "eldiariomontanes.es", "Cantabria", "Generalista"),
    ("La Rioja", "larioja.com", "La Rioja", "Generalista"),
    ("Nueve Cuatro Uno", "nuevecuatrouno.com", "La Rioja", "Generalista"),

    # Extremadura
    ("Hoy", "hoy.es", "Extremadura", "Generalista"),
    ("El Periodico Extremadura", "elperiodicoextremadura.com", "Extremadura", "Generalista"),

    # Canarias y Baleares
    ("Canarias7", "canarias7.es", "Las Palmas", "Generalista"),
    ("La Provincia", "laprovincia.es", "Las Palmas", "Generalista"),
    ("El Dia", "eldia.es", "Santa Cruz de Tenerife", "Generalista"),
    ("Diario de Avisos", "diariodeavisos.com", "Santa Cruz de Tenerife", "Generalista"),
    ("Ultima Hora", "ultimahora.es", "Baleares", "Generalista"),
    ("Diario de Mallorca", "diariodemallorca.es", "Baleares", "Generalista"),
    ("Menorca.info", "menorca.info", "Baleares", "Generalista"),
    ("Periodico de Ibiza", "periodicodeibiza.es", "Baleares", "Generalista"),

    # Madrid
    ("Madridiario", "madridiario.es", "Madrid", "Generalista"),
    ("Telemadrid", "telemadrid.es", "Madrid", "Generalista"),
    ("Somos Malasana", "somosmalasana.com", "Madrid", "Local"),
]


def directorio():
    bar, bar_ld = migas([("Inicio", "/"), ("Directorio de medios", None)])
    ambitos = sorted(set(m[2] for m in MEDIOS))
    sectores = sorted(set(m[3] for m in MEDIOS))

    filas = []
    for nombre, dominio, ambito, sector in sorted(MEDIOS, key=lambda x: (x[2], x[0])):
        filas.append(
            '<tr data-ambito="{a}" data-sector="{s}" data-nombre="{n}">'
            '<td><strong>{n}</strong></td><td>{a}</td><td>{s}</td>'
            '<td><a href="https://{d}" target="_blank" rel="nofollow noopener">{d}</a></td></tr>'.format(
                n=nombre, d=dominio, a=ambito, s=sector))

    opciones_a = "".join('<option value="{0}">{0}</option>'.format(a) for a in ambitos)
    opciones_s = "".join('<option value="{0}">{0}</option>'.format(s) for s in sectores)

    preguntas = [
        ("Como encuentro el correo de contacto de un medio",
         "Entrando en su web y buscando la seccion de contacto o el directorio de la redaccion. "
         "Publicamos el enlace de cada medio precisamente para eso: no publicamos correos de periodistas "
         "porque son datos personales y cambian constantemente."),
        ("A cuantos medios de esta lista deberia escribir",
         "Entre quince y cuarenta bien elegidos. Filtra por tu provincia y por tu sector, y olvidate del "
         "resto: enviar a todos reduce tus posibilidades en vez de aumentarlas."),
        ("Por que no publicais los emails de los periodistas",
         "Porque son datos personales sujetos al RGPD, cambian cada pocos meses y publicarlos en abierto "
         "solo sirve para que esas direcciones acaben saturadas de spam. Lo util es escribir al redactor "
         "concreto que cubre tu tema, y eso se localiza en la web del medio."),
        ("Este directorio esta completo",
         "No, y no pretende estarlo. Estan los medios nacionales, los principales regionales y los "
         "sectoriales mas relevantes. Lo ampliamos por tandas; si falta uno que conoces, escribenos."),
    ]
    faq, faq_ld = faq_html(preguntas)

    cuerpo = """
{bar}
<main><div class="wrap">
<article style="max-width:760px;padding-top:26px">
<h1>Directorio de medios de comunicacion de Espana</h1>
<p class="entradilla">{total} medios nacionales, regionales y sectoriales, con su ambito, su sector y el
enlace a su web. Filtra por provincia o por tematica para preparar tu envio.</p>
<p>No publicamos correos de periodistas. Son datos personales, cambian cada pocos meses y una lista
publica de direcciones solo sirve para saturarlas. Lo que funciona es entrar en el medio, localizar al
redactor que cubre tu tema y escribirle a el: te lo explicamos en
<a href="/enviar-nota-de-prensa/">como enviar una nota de prensa</a>.</p>
</article>

<div class="filtros">
  <input type="text" id="busca" placeholder="Buscar medio..." onkeyup="filtra()" style="min-width:200px">
  <select id="fa" onchange="filtra()"><option value="">Todos los ambitos</option>{opa}</select>
  <select id="fs" onchange="filtra()"><option value="">Todos los sectores</option>{ops}</select>
</div>
<p class="contador" id="contador">{total} medios</p>

<table id="tabla">
<thead><tr><th>Medio</th><th>Ambito</th><th>Sector</th><th>Web</th></tr></thead>
<tbody>
{filas}
</tbody>
</table>

<div style="max-width:760px;margin-top:46px">
<h2>Como usar este directorio</h2>
<ol>
  <li><strong>Filtra por tu provincia.</strong> La prensa local publica mucho mas que la nacional y tiene
  menos competencia por el espacio.</li>
  <li><strong>Filtra por tu sector.</strong> Un medio sectorial con 20.000 lectores de tu ramo vale mas
  que un generalista con dos millones a los que no les interesa.</li>
  <li><strong>Entra en cada medio</strong> y localiza quien firma las noticias de tu tema.</li>
  <li><strong>Escribe a esa persona</strong>, uno a uno, nunca en copia oculta masiva.</li>
</ol>

<h2>Si prefieres no hacerlo tu</h2>
<p>La distribucion segmentada esta incluida en el <a href="/precios/">plan de 195&nbsp;&euro;</a>:
seleccionamos los medios, enviamos uno a uno y te pasamos el informe de lo que ha salido.</p>

{faq}
</div>
</div></main>

<script>
function sinTildes(s){{
  return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();
}}
function filtra(){{
  var q=sinTildes(document.getElementById('busca').value);
  var a=document.getElementById('fa').value;
  var s=document.getElementById('fs').value;
  var fs=document.querySelectorAll('#tabla tbody tr');
  var n=0;
  for(var i=0;i<fs.length;i++){{
    var r=fs[i];
    var ok=(!a||r.dataset.ambito===a)&&(!s||r.dataset.sector===s)&&
           (!q||sinTildes(r.dataset.nombre).indexOf(q)>-1);
    r.style.display=ok?'':'none';
    if(ok)n++;
  }}
  document.getElementById('contador').textContent=n+(n===1?' medio':' medios');
}}
</script>
""".format(bar=bar, total=len(MEDIOS), opa=opciones_a, ops=opciones_s,
           filas="\n".join(filas), faq=faq)

    lista_ld = {
        "@context": "https://schema.org", "@type": "ItemList",
        "name": "Directorio de medios de comunicacion de Espana",
        "numberOfItems": len(MEDIOS),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": m[0], "url": "https://" + m[1]}
            for i, m in enumerate(MEDIOS[:60])
        ],
    }
    return escribir("/medios/",
                    "Directorio de medios de comunicacion de Espana por provincia y sector",
                    "Directorio con {} medios espanoles: nacionales, regionales y sectoriales, filtrables "
                    "por provincia y tematica, con enlace a cada web.".format(len(MEDIOS)),
                    cuerpo, [bar_ld, faq_ld, lista_ld], "/medios/")
