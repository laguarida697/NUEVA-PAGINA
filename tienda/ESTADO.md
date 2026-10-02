# Estado del proyecto — La Guarida del Terror (Halloween, Colombia)

- Tienda: qf1mmk-ew.myshopify.com (tema base: Horizon)
- Tema de trabajo (sin publicar): 167161987211 — tema publicado actual: 167158677643 (NO tocado)
- Vía de trabajo: Admin API (themeFilesUpsert) con `node pull.mjs` / `node push.mjs`, porque el login de `shopify theme` está bloqueado por Cloudflare desde el entorno en la nube.
- Token de `store auth` caduca ~24 h: repetir `shopify store auth --store qf1mmk-ew.myshopify.com --scopes read_products,write_products,read_files,write_files,read_themes,write_themes`.
- Producto existente: LUZ DE NAVIDAD USB (gid .../Product/10331622080651) — fuera del enfoque; sin tocar.
- Colecciones creadas: disfraces-ninos, disfraces-adultos, accesorios-halloween (vacías).

## Diseño
Halloween: noche #120b1a, naranja #ff7a1a, hueso #f6efe2, morado #3b2a52. Títulos Creepster, texto Poppins.

## Secciones (prefijo gt-)
gt-hero (luna, murciélagos, cuenta atrás al 2026-10-31), gt-marquesina, gt-categorias, gt-productos, gt-beneficios, gt-faq; snippet gt-icono; assets gt-styles.css / gt-scripts.js.
Portada: templates/index.json. Ajustes globales de color en config/settings_data.json.

## Pendiente
- Cambiar nombre de la tienda en Configuración (el logo del header usa el nombre de la tienda).
- Productos reales (sin proveedor aún), medios de pago/envío, políticas.
- Revisión visual (storefront con contraseña): pendiente de que el usuario abra la previsualización.
- Publicar el tema solo con visto bueno.
