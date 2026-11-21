# -*- coding: utf-8 -*-
"""Restaura tildes y enes en los fuentes. Reemplazo por palabra completa."""
import re, sys, io

PARES = {
    # -cion / -sion
    "informacion": "información", "publicacion": "publicación", "publicaciones": "publicaciones",
    "comunicacion": "comunicación", "comunicaciones": "comunicaciones",
    "distribucion": "distribución", "redaccion": "redacción", "redacciones": "redacciones",
    "seleccion": "selección", "direccion": "dirección", "direcciones": "direcciones",
    "atencion": "atención", "decision": "decisión", "decisiones": "decisiones",
    "version": "versión", "versiones": "versiones", "extension": "extensión",
    "conversion": "conversión", "mencion": "mención", "menciones": "menciones",
    "relacion": "relación", "relaciones": "relaciones", "situacion": "situación",
    "situaciones": "situaciones", "posicion": "posición", "posiciones": "posiciones",
    "condicion": "condición", "condiciones": "condiciones", "edicion": "edición",
    "revision": "revisión", "revisiones": "revisiones", "television": "televisión",
    "gestion": "gestión", "cuestion": "cuestión", "inversion": "inversión",
    "conexion": "conexión", "ocasion": "ocasión", "razon": "razón", "buzon": "buzón",
    "maquetacion": "maquetación", "alineacion": "alineación", "instalacion": "instalación",
    "instalaciones": "instalaciones", "fermentacion": "fermentación", "produccion": "producción",
    "deteccion": "detección", "rehabilitacion": "rehabilitación", "variacion": "variación",
    "reproduccion": "reproducción", "republicacion": "republicación", "indicacion": "indicación",
    "indicaciones": "indicaciones", "finalidad": "finalidad", "solicitud": "solicitud",
    "apertura": "apertura", "organizacion": "organización", "organizaciones": "organizaciones",
    "asociacion": "asociación", "facturacion": "facturación", "contratacion": "contratación",
    "conservacion": "conservación", "supresion": "supresión", "oposicion": "oposición",
    "limitacion": "limitación", "rectificacion": "rectificación", "obligacion": "obligación",
    "obligaciones": "obligaciones", "prestacion": "prestación", "ejecucion": "ejecución",
    "proteccion": "protección", "navegacion": "navegación", "configuracion": "configuración",
    "actualizaciones": "actualizaciones", "legislacion": "legislación", "resolucion": "resolución",
    "controversia": "controversia", "convocatoria": "convocatoria", "presentacion": "presentación",
    "traduccion": "traducción", "conclusion": "conclusión", "conclusiones": "conclusiones",
    "planificacion": "planificación", "descripcion": "descripción", "declaracion": "declaración",
    "interpretacion": "interpretación", "repeticiones": "repeticiones", "subordinada": "subordinada",
    "sindicacion": "sindicación", "repercusion": "repercusión", "antelacion": "antelación",
    "aparcamiento": "aparcamiento", "confidencialidad": "confidencialidad",
    # acentos varios
    "segun": "según", "tambien": "también", "ademas": "además", "mas": "más",
    "aqui": "aquí", "alli": "allí", "asi": "así", "dia": "día", "dias": "días",
    "economia": "economía", "economico": "económico", "economicos": "económicos",
    "tecnologia": "tecnología", "tecnologica": "tecnológica", "energia": "energía",
    "categoria": "categoría", "categorias": "categorías", "mayoria": "mayoría",
    "compania": "compañía", "garantia": "garantía", "telefono": "teléfono",
    "electronico": "electrónico", "electronica": "electrónica", "electricos": "eléctricos",
    "electrico": "eléctrico", "publico": "público", "publicos": "públicos",
    "practica": "práctica", "practicas": "prácticas", "tipografia": "tipografía",
    "parrafo": "párrafo", "parrafos": "párrafos", "periodico": "periódico",
    "periodicos": "periódicos", "periodistico": "periodístico", "periodistica": "periodística",
    "periodisticos": "periodísticos", "generico": "genérico", "genericos": "genéricos",
    "genericas": "genéricas", "automatico": "automático", "automatica": "automática",
    "basico": "básico", "basicos": "básicos", "basica": "básica", "basicas": "básicas",
    "tecnico": "técnico", "tecnicos": "técnicos", "tecnica": "técnica", "tecnicas": "técnicas",
    "grafico": "gráfico", "graficas": "gráficas", "rapida": "rápida", "rapido": "rápido",
    "rapidez": "rapidez", "unico": "único", "unica": "única", "ultimo": "último",
    "ultima": "última", "minimo": "mínimo", "maximo": "máximo", "maxima": "máxima",
    "numero": "número", "titulo": "título", "titulos": "títulos", "articulo": "artículo",
    "articulos": "artículos", "vehiculo": "vehículo", "vehiculos": "vehículos",
    "ambito": "ámbito", "ambitos": "ámbitos", "interes": "interés", "ingles": "inglés",
    "pagina": "página", "paginas": "páginas", "credito": "crédito", "creditos": "créditos",
    "piramide": "pirámide", "logotipo": "logotipo", "logotipos": "logotipos",
    "margenes": "márgenes", "metricas": "métricas", "tematica": "temática",
    "analitica": "analítica", "estetica": "estética", "politica": "política",
    "politicas": "políticas", "juridicamente": "jurídicamente", "sectoriales": "sectoriales",
    "especifico": "específico", "practicamente": "prácticamente", "facil": "fácil",
    "dificil": "difícil", "util": "útil", "utiles": "útiles", "inutil": "inútil",
    "comun": "común", "comunes": "comunes", "estandar": "estándar", "quizas": "quizás",
    "vacio": "vacío", "frio": "frío", "podria": "podría", "podrian": "podrían",
    "deberia": "debería", "haria": "haría", "seria": "sería", "serian": "serían",
    "tendria": "tendría", "tendran": "tendrán", "estaran": "estarán", "sera": "será",
    "seran": "serán", "hara": "hará", "haran": "harán", "dara": "dará", "daran": "darán",
    "ira": "irá", "iran": "irán", "vera": "verá", "veran": "verán", "pondra": "pondrá",
    "quedara": "quedará", "permitira": "permitirá", "reducira": "reducirá",
    "aumentara": "aumentará", "costaria": "costaría", "valdria": "valdría",
    "equivale": "equivale", "analisis": "análisis", "sintesis": "síntesis",
    "despues": "después", "detras": "detrás", "atras": "atrás", "quiza": "quizá",
    "ningun": "ningún", "algun": "algún", "cuanto": "cuánto", "cuanta": "cuánta",
    "cuantos": "cuántos", "cuantas": "cuántas", "fundo": "fundó", "presento": "presentó",
    "valoro": "valoró", "obtuvo": "obtuvo", "situo": "situó",
    "acusacion": "acusación",
    "administracion": "administración",
    "bateria": "batería",
    "cabia": "cabía",
    "cambiarias": "cambiarías",
    "cercania": "cercanía",
    "certificacion": "certificación",
    "comprobacion": "comprobación",
    "convencion": "convención",
    "conversacion": "conversación",
    "correccion": "corrección",
    "definicion": "definición",
    "delegacion": "delegación",
    "desconfia": "desconfía",
    "distincion": "distinción",
    "duracion": "duración",
    "envia": "envía",
    "envias": "envías",
    "envio": "envío",
    "envios": "envíos",
    "escribio": "escribió",
    "estacion": "estación",
    "exclamacion": "exclamación",
    "existia": "existía",
    "expansion": "expansión",
    "funcion": "función",
    "guia": "guía",
    "guias": "guías",
    "institucion": "institución",
    "instrumentacion": "instrumentación",
    "opcion": "opción",
    "panaderia": "panadería",
    "participacion": "participación",
    "penalizacion": "penalización",
    "perfeccion": "perfección",
    "pondria": "pondría",
    "publicaria": "publicaría",
    "realizacion": "realización",
    "recomendacion": "recomendación",
    "reduccion": "reducción",
    "reenvia": "reenvía",
    "renovacion": "renovación",
    "reputacion": "reputación",
    "salio": "salió",
    "seccion": "sección",
    "suscripcion": "suscripción",
    "todavia": "todavía",
    "vacia": "vacía",
    "vias": "vías",
    "Agroinformacion": "Agroinformación",
    "anglosajon": "anglosajón",
    "galardon": "galardón",
    "patron": "patrón",
    "disponian": "disponían",
    "tenian": "tenían",
    "Razon": "Razón",
    "adquisicion": "adquisición",
    "aprobacion": "aprobación",
    "asesoria": "asesoría",
    "educacion": "educación",
    "eolico": "eólico",
    "decadas": "décadas",
    "afectacion": "afectación",
    "afirmacion": "afirmación",
    "afirmaciones": "afirmaciones",
    "alimentacion": "alimentación",
    "construccion": "construcción",
    "demas": "demás",
    "denominacion": "denominación",
    "eleccion": "elección",
    "estimacion": "estimación",
    "exportacion": "exportación",
    "formacion": "formación",
    "fusion": "fusión",
    "fusiones": "fusiones",
    "incorporacion": "incorporación",
    "incorporaciones": "incorporaciones",
    "indexacion": "indexación",
    "insercion": "inserción",
    "integracion": "integración",
    "matriculacion": "matriculación",
    "ocupacion": "ocupación",
    "optimizacion": "optimización",
    "prevencion": "prevención",
    "restauracion": "restauración",
    "Motorpasion": "Motorpasión",
    "YMAS": "YMÁS",
    "previsión": "previsión",
    "generacional": "generacional",
    # enes
    "Espana": "España", "espanol": "español", "espanola": "española",
    "espanoles": "españoles", "espanolas": "españolas", "ano": "año", "anos": "años",
    "manana": "mañana", "pequeno": "pequeño", "pequena": "pequeña", "pequenos": "pequeños",
    "pequenas": "pequeñas", "senala": "señala", "senalar": "señalar", "senalado": "señalado",
    "senalados": "señalados", "senal": "señal", "diseno": "diseño", "tamano": "tamaño",
    "Coruna": "Coruña", "Cataluna": "Cataluña", "Naron": "Narón", "Malasana": "Malasaña",
    "Montanes": "Montañés", "acompanarse": "acompañarse", "acompanan": "acompañan",
    # toponimos y nombres
    "Leon": "León", "Aragon": "Aragón", "Castellon": "Castellón", "Almeria": "Almería",
    "Cadiz": "Cádiz", "Cordoba": "Córdoba", "Malaga": "Málaga", "Jaen": "Jaén",
    "Avila": "Ávila", "Pais": "País", "Andalucia": "Andalucía", "Mediterraneo": "Mediterráneo",
    "Atlantico": "Atlántico", "Codigo": "Código", "Opinion": "Opinión", "Region": "Región",
    "Nacio": "Nació", "Medica": "Médica", "Logistica": "Logística", "Automocion": "Automoción",
    "Construccion": "Construcción", "Distribucion": "Distribución", "Emprendimiento": "Emprendimiento",
}

# Tramos que NO deben tocarse: scripts, estilos, etiquetas, urls, dominios, correos
PROTEGIDAS = re.compile(
    r'(<script[\s\S]*?</script>|'        # bloques de javascript
    r'<style[\s\S]*?</style>|'           # bloques de css
    r'https?://[^\s"\'<>)]+|'            # urls
    r'[\w.-]+\.(?:com|es|net|org|cat|eus|info|news|io|tech|xml|css|svg|html)\b|'  # dominios y ficheros
    r'<[^>]+>|'                          # etiquetas html con sus atributos
    r'[\w-]+@[\w.-]+)',                  # correos
    re.IGNORECASE)


# Un unico patron con todas las formas, ordenadas de mas larga a mas corta
_TABLA = {}
for _m, _b in PARES.items():
    _TABLA[_m] = _b
    if _m[0].islower():
        _TABLA[_m.capitalize()] = _b.capitalize()
_PATRON = re.compile(
    r'\b(' + "|".join(sorted(map(re.escape, _TABLA), key=len, reverse=True)) + r')\b')


def acentua_texto(txt):
    partes = PROTEGIDAS.split(txt)
    for i in range(0, len(partes), 2):     # solo los tramos no protegidos
        partes[i] = _PATRON.sub(lambda m: _TABLA[m.group(1)], partes[i])
    return "".join(partes)


if __name__ == "__main__":
    total = 0
    for ruta in sys.argv[1:]:
        with io.open(ruta, encoding="utf-8") as f:
            antes = f.read()
        despues = acentua_texto(antes)
        if antes != despues:
            with io.open(ruta, "w", encoding="utf-8") as f:
                f.write(despues)
            cambios = sum(1 for a, b in zip(antes.split(), despues.split()) if a != b)
            print("{}: {} palabras corregidas".format(ruta, cambios))
            total += cambios
    print("Total: {}".format(total))


# ---- pase adicional: atributos visibles y JSON-LD ----
import json as _json

_ATRS = re.compile(r'(\s(?:content|placeholder|alt|aria-label|title)=")([^"]*)(")', re.I)
_LD = re.compile(r'(<script type="application/ld\+json">)([\s\S]*?)(</script>)', re.I)


def _acentua_llano(s):
    return _PATRON.sub(lambda m: _TABLA[m.group(1)], s)


def _ld_rec(v):
    if isinstance(v, str):
        if v.startswith(("http://", "https://")) or v.startswith("@"):
            return v
        return _acentua_llano(v)
    if isinstance(v, list):
        return [_ld_rec(x) for x in v]
    if isinstance(v, dict):
        return {k: (v[k] if k.startswith("@") and k != "@type" else _ld_rec(v[k])) for k in v}
    return v


def acentua_html(txt):
    txt = acentua_texto(txt)
    txt = _ATRS.sub(lambda m: m.group(1) + _acentua_llano(m.group(2)) + m.group(3), txt)

    def _ld_sub(m):
        try:
            datos = _json.loads(m.group(2))
        except Exception:
            return m.group(0)
        return m.group(1) + _json.dumps(_ld_rec(datos), ensure_ascii=False) + m.group(3)
    return _LD.sub(_ld_sub, txt)
