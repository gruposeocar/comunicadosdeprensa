# comunicadosdeprensa.es

Web estática de ComunicadosdePrensa.es. Servicio de redacción, publicación y
distribución de notas de prensa, más guía de contenidos y directorio de medios.

## Estructura

- Raíz: la web ya generada, lista para servir. Es lo que Hostinger despliega.
- `src/`: el generador en Python que produce esa web.

## Cómo pedir cambios

Para cambios de texto puntuales, se editan directamente los `.html` de la raíz.

Para cambios que afecten a varias páginas (menú, pie, diseño, plantillas) se
edita el generador y se regenera:

```bash
cd src && python3 main.py      # escribe en src/dist/
cp -r src/dist/. .             # lleva el resultado a la raíz
```

## Ficheros del generador

| Fichero | Contenido |
| --- | --- |
| `build.py` | Plantilla HTML, CSS, schema.org y utilidades |
| `paginas.py` | Portada y función base de páginas de servicio |
| `servicios.py` | Páginas comerciales y precios |
| `guias.py` | Índice de la guía, estructura, qué es, cómo hacerla, formato |
| `guias2.py` | Ejemplos, plantilla, eventos, diferencias, inglés |
| `medios.py` | Directorio de medios |
| `legal.py` | Contacto, aviso legal, privacidad y cookies |
| `acentos.py` | Pase de acentuación del HTML generado |
| `main.py` | Orquesta todo y genera sitemap, robots y 404 |

## Pendiente

- Crear la cuenta de correo `hola@comunicadosdeprensa.es` en Hostinger (el
  formulario de contacto envía ahí).
- Revisar los precios de `/precios/`.
- Ampliar el directorio de medios por tandas verificadas.
