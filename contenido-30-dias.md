# La Guarida: 30 días de contenido (estilo "Rockstar Games")

## 1. Análisis del canal de referencia (según tu captura)

Rockstar publica poco, con mucho peso y con un ritmo muy marcado:

| Rasgo | Qué se ve en el canal |
|---|---|
| Formato largo | Un vídeo ancla de unos 27 min ("An Extended Look"). |
| Formato corto | Teasers de 20 a 35 s: avance, revelación de portada, evento. |
| Miniaturas | Un solo motivo grande y centrado (logo o dúo de personajes), sin texto extra, con la duración abajo. |
| Paleta | Atardecer neón: rosa, morado, naranja y cielo degradado. Palmeras y costa. En eventos cambia a un color de marca (el verde del evento 420). |
| Títulos | Cortos, serios y sin clickbait: "Official Cover Art Reveal", "Now Available". |
| Cadencia | Un hito grande a la semana, rodeado de piezas pequeñas. |
| Tono | Cinematográfico, con clasificación de edad visible, sin hablar a cámara. |

La fórmula que copiamos es **un ancla larga, teasers cortos, una identidad visual fija y títulos sobrios**.

## 2. Propiedad intelectual

No usamos el logo, los personajes, la música ni el nombre de GTA o Rockstar. Copiamos solo el **estilo**: neón de atardecer costero, encuadre cinematográfico y títulos sobrios. Todo lo demás es original de La Guarida.

## 3. Identidad visual fija (úsala en TODOS los prompts)

> **Bloque de estilo:** cinematic neon sunset, pink-magenta to violet gradient sky, orange rim light, palm tree silhouettes, coastal city, film grain, anamorphic lens, 2.39:1 feel, high contrast, no text, no logos.

- Miniaturas 16:9: un único sujeto centrado, el logotipo "LA GUARIDA" abajo a la derecha y sin más texto.
- Shorts 9:16: el mismo bloque de estilo, 20 a 30 s.
- Color de evento: un verde o cian ácido, usado solo en los días de evento.

## 4. Calendario (4 semanas × 7 días)

Reparto: **4 anclas largas** (una por semana), **12 teasers/shorts**, **8 miniaturas o carteles**, **4 comunitarios** y **2 días de descanso**.

### Semana 1: presentación
| Día | Pieza | Título | Prompt de imagen o vídeo |
|---|---|---|---|
| 1 | Short 25 s | La Guarida: Teaser Oficial | Plano lento sobre costa al atardecer, palmeras, un coche cruzando. [Bloque de estilo] |
| 2 | Miniatura/cartel | Cartel Oficial | Dos siluetas con pañuelos frente a una gasolinera, atardecer. [Bloque de estilo] |
| 3 | Comunitario | Primera mirada | Encuesta y capturas del cartel |
| 4 | Short 20 s | Avance 02 | Calle de noche con neones, lluvia fina. [Bloque de estilo] |
| 5 | Short 30 s | Los personajes | Retratos originales en contraluz. [Bloque de estilo] |
| 6 | Descanso | | |
| 7 | **Ancla 15-25 min** | Una mirada extendida | Montaje con todo lo anterior, voz en off y música |

### Semana 2: mundo
| Día | Pieza | Título |
|---|---|---|
| 8 | Short | El mapa |
| 9 | Cartel | Los barrios |
| 10 | Short | Vida nocturna |
| 11 | Comunitario | Preguntas y respuestas |
| 12 | Short | El puerto |
| 13 | Descanso | |
| 14 | **Ancla** | Dentro del mundo |

### Semana 3: evento
| Día | Pieza | Título |
|---|---|---|
| 15 | Short (color de evento) | Evento especial: anuncio |
| 16 | Cartel | Evento: detalles |
| 17 | Short | Evento: cuenta atrás |
| 18 | Comunitario | Resultados de la encuesta |
| 19 | Short | Evento: ya disponible |
| 20 | Short | Resumen del evento |
| 21 | **Ancla** | Detrás de cámaras |

### Semana 4: cierre
| Día | Pieza | Título |
|---|---|---|
| 22 | Short | Nuevo avance |
| 23 | Cartel | Edición especial |
| 24 | Short | Música y ambiente |
| 25 | Comunitario | Lo mejor de la comunidad |
| 26 | Short | Última mirada |
| 27 | Cartel | Fecha oficial |
| 28 | **Ancla** | Tráiler final |

Los días 29 y 30 son de reserva para repetir lo que mejor funcione.

## 5. Cómo producirlo con Higgsfield

- Carteles y miniaturas: `generate_image`, 16:9, siempre con el bloque de estilo.
- Shorts: `generate_video`, 9:16, partiendo de un cartel como imagen inicial para mantener la coherencia.
- Anclas largas: se montan con los clips anteriores. Higgsfield no genera 20 minutos de golpe.
- **Créditos:** la cuenta es gratuita y tiene 10 créditos. Un mes completo necesita bastantes más. Con 10 créditos salen una o dos piezas de muestra, así que recomiendo empezar por el cartel del día 2.
