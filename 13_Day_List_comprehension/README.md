# Día 13: List Comprehension & Funciones Lambda 🪄

Hoy he descubierto cómo escribir código más conciso y elegante en Python. La **Comprensión de Listas** (*List Comprehension*) es una forma compacta de crear listas a partir de secuencias existentes, combinando bucles `for` y condicionales `if` en una sola línea. 

También he aprendido sobre las **Funciones Lambda**, que son funciones anónimas de usar y tirar, perfectas para operaciones rápidas donde no hace falta usar `def`.

### 🧠 Conceptos Aprendidos
- **Sintaxis de List Comprehension:** `[expresión for elemento in iterable if condición]`
- **Aplanamiento de Listas (Flattening):** Convertir listas dentro de listas (matrices) en una lista simple de una sola dimensión.
- **Funciones Lambda:** `lambda parametros: operacion`
  Son ideales para pasarlas como argumentos a otras funciones (como `sort`, `map` o `filter`).



### 💻 Ejercicios Realizados
- [x] Filtrado de números negativos usando list comprehension.
- [x] Aplanamiento de arrays tridimensionales.
- [x] Creación de tuplas y estructuras complejas (diccionarios) en una sola línea.
- [x] Concatenación avanzada de strings extraídos de listas de tuplas.
- [x] Creación de funciones matemáticas rápidas usando `lambda`.

### 🛠️ Aplicación en IA
La comprensión de listas y las funciones lambda son **el pan de cada día** en el preprocesamiento de datos para Machine Learning:
1.  **Limpieza Rápida:** Si tienes un dataset con 1 millón de textos y quieres pasarlos todos a minúsculas: `textos_limpios = [texto.lower() for texto in corpus]`. ¡Es mucho más rápido que un bucle `for` tradicional!
2.  **Pandas:** Al aplicar transformaciones a columnas enteras de datos, se usa constantemente `df['columna'].apply(lambda x: x * 2)`.