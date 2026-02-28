# Día 5: Listas 📜

Hoy he aprendido sobre las **Listas**, una de las estructuras de datos más potentes y usadas en Python. A diferencia de las cadenas (que son inmutables), las listas son colecciones ordenadas y modificables que permiten almacenar múltiples elementos de diferentes tipos.

### 🧠 Conceptos Aprendidos
- **Creación de Listas:** Uso de corchetes `[]` o la función `list()`.
- **Acceso a Elementos:** Indexación positiva (0 a n) y negativa (-1 para el último elemento).
- **Desempaquetado (Unpacking):** Asignar elementos de una lista a variables individuales en una sola línea `item1, *resto = lista`.
- **Slicing (Rebanado):** Extraer subconjuntos de listas `[inicio:fin:paso]`.
- **Métodos de Modificación:**
  - `append()`: Añadir al final.
  - `insert()`: Añadir en una posición específica.
  - `extend()`: Añadir otra lista.
- **Métodos de Eliminación:**
  - `remove()`: Borrar por valor.
  - `pop()`: Borrar por índice (y devuelve el valor).
  - `clear()`: Vaciar la lista.
  - `del`: Palabra clave para eliminar elementos o la lista entera.
- **Organización:**
  - `sort()`: Ordenar la lista (modifica la original).
  - `sorted()`: Devuelve una copia ordenada (no modifica la original).
  - `reverse()`: Invertir el orden.
  - `copy()`: Crear copias independientes.

### 💻 Ejercicios Realizados
- [x] Creación de listas vacías y con datos mixtos.
- [x] Manipulación de empresas tecnológicas (añadir, insertar, ordenar, invertir).
- [x] Acceso dinámico a elementos centrales (cálculo de índices medios).
- [x] Filtrado y extracción de rangos (primeros/últimos elementos).
- [x] Desempaquetado avanzado de listas de países.

### 🛠️ Aplicación en IA
Las listas son los "bloques de construcción" de los datos en IA. Antes de usar librerías avanzadas como **NumPy** o **Pandas**, los datos suelen cargarse o limpiarse en listas.
Por ejemplo, en Procesamiento de Lenguaje Natural (NLP), una frase se convierte en una **lista de palabras** (tokens): `['Hola', 'mundo']`. En Visión por Computadora, una imagen puede representarse simplificadamente como una lista de valores de píxeles.