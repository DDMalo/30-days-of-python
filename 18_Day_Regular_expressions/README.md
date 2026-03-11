# Día 18: Expresiones Regulares (RegEx) 🔍

Hoy he desbloqueado una de las herramientas más potentes para la manipulación de texto: las **Expresiones Regulares**. Aunque la sintaxis parece un idioma alienígena al principio, es la forma más rápida y eficiente de buscar, validar y limpiar patrones dentro de cadenas de texto utilizando el módulo integrado `re`.

### 🧠 Conceptos Aprendidos
- **El módulo `re`:** Importación de la librería estándar de Python para RegEx.
- **Funciones Principales:**
  - `re.match()`: Busca el patrón solo al principio del string.
  - `re.search()`: Busca el patrón en toda la cadena y devuelve la primera coincidencia.
  - `re.findall()`: Devuelve una lista con TODAS las coincidencias encontradas.
  - `re.sub()`: Sustituye las coincidencias por otro texto (ideal para limpiar).
- **Patrones Básicos:** Uso de comodines (`.`, `*`, `+`, `?`), clases de caracteres (`[a-z]`, `\d` para dígitos, `\w` para palabras) y anclas (`^` para inicio, `$` para fin).



### 💻 Ejercicios Realizados
- [x] Extracción de números enteros (positivos y negativos) de un texto para cálculos matemáticos.
- [x] Validación de nombres de variables de Python mediante patrones estrictos.
- [x] Limpieza de texto y conteo de palabras más frecuentes en un párrafo.

### 🛠️ Aplicación en IA
En la IA, las Expresiones Regulares son la herramienta número uno en **NLP (Procesamiento de Lenguaje Natural)**:
1.  **Limpieza de Datasets:** Antes de pasarle un millón de tweets a un modelo de Machine Learning, usas `re.sub()` para eliminar automáticamente todos los hashtags, menciones (`@usuario`), URLs y emojis.
2.  **Extracción de Entidades (NER):** Buscar patrones específicos como números de teléfono, DNI o fechas dentro de historiales médicos desestructurados.