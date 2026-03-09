# Día 17: Excepciones y Desempaquetado 📦🛡️

Hoy he aprendido a proteger mi código contra errores inesperados usando bloques `try/except`. Además, he descubierto técnicas de "desempaquetado" (*unpacking*) para extraer datos de listas y diccionarios de forma rápida y elegante.

### 🧠 Conceptos Aprendidos
- **Manejo de Excepciones:**
  - `try`: Bloque de código donde "intentamos" hacer algo que podría fallar.
  - `except`: Se ejecuta solo si el bloque `try` produce un error.
  - `else`: Se ejecuta si *no* hubo ningún error en el `try`.
  - `finally`: Se ejecuta *siempre*, sin importar si hubo error o no (útil para cerrar archivos o conexiones a bases de datos).
  
  

- **Desempaquetado (Unpacking):**
  - Uso del operador `*` para agrupar el "resto" de una lista en una nueva variable.
  - Desempaquetado de diccionarios con `**`.
- **`enumerate(lista)`:** Nos permite recorrer una lista en un bucle `for` obteniendo tanto el *índice* (la posición) como el *valor* al mismo tiempo.
- **`zip(lista1, lista2)`:** Como la cremallera de una chaqueta, une los elementos de dos o más listas en base a su posición.

### 💻 Ejercicios Realizados
- [x] Extracción y agrupación de listas usando el operador `*`.
- [x] Control de errores de usuario con `try/except` para evitar el colapso del programa.
- [x] Unión de múltiples secuencias de datos mediante iteradores como `zip` y `enumerate`.

### 🛠️ Aplicación en IA
- **Try/Except:** Al hacer *web scraping* para conseguir datos, es muy normal que una página no cargue o una imagen esté rota. Si no usas `try/except`, tu programa de IA se detendrá después de descargar 5.000 fotos porque la 5.001 dio un "Error 404".
- **Zip & Enumerate:** Súper útiles cuando estás entrenando un modelo y tienes una lista de *inputs* (imágenes) y otra lista de *labels* (etiquetas correctas). Con `zip()` las unes perfectamente para pasárselas a la red neuronal.