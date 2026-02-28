# Día 4: Manipulación de Strings (Cadenas de Texto) ✍️

En esta sesión he trabajado con uno de los tipos de datos más versátiles en Python: los strings. El dominio de las cadenas es el primer paso hacia el Procesamiento de Lenguaje Natural (NLP).

### 🧠 Conceptos Aprendidos
- **Creación y Formateo:** Uso de comillas simples, dobles y triples (multilínea).
- **Secuencias de Escape:** Uso de `\n` (nueva línea) y `\t` (tabulación).
- **Formateo Avanzado:** Implementación de `f-strings` (introducidos en Python 3.6+) y el método `.format()`.
- **Métodos de String:**
  - Transformación: `.upper()`, `.lower()`, `.capitalize()`, `.title()`, `.swapcase()`.
  - Búsqueda/Validación: `.startswith()`, `.endswith()`, `.find()`, `.replace()`.
  - Limpieza y División: `.strip()`, `.split()`, `.join()`.
- **Slicing (Semejanza con Arrays):** Acceso a subcadenas mediante índices `[inicio:fin:paso]`.

### 💻 Ejercicios Realizados
- [x] Concatenación dinámica de múltiples variables en una sola sentencia.
- [x] Uso de métodos para transformar frases complejas (ej: 'Coding For All').
- [x] Extracción de subcadenas mediante técnicas de *slicing*.
- [x] Validación de patrones de texto (chequear si una frase contiene una palabra específica).

### 🛠️ Aplicación en IA (NLP)
El manejo de strings es la base de la **Inteligencia Artificial Conversacional**. Antes de entrenar un modelo como GPT, los ingenieros realizamos "limpieza de texto" (*tokenización* y *normalization*), usando precisamente métodos como `.split()`, `.lower()` y `.replace()` para que la máquina pueda procesar el lenguaje humano sin ruido.