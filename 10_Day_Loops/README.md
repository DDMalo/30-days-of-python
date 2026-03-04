# Día 10: Bucles (Loops) 🔄

Hoy he aprendido a automatizar tareas repetitivas utilizando **Bucles**. En lugar de copiar y pegar código, los bucles permiten iterar sobre secuencias de datos o ejecutar bloques de código mientras se cumpla una condición.

### 🧠 Conceptos Aprendidos
- **Bucle `while`:** Se ejecuta *mientras* una condición sea verdadera. Requiere tener cuidado con los bucles infinitos.
- **Bucle `for`:** Ideal para iterar sobre secuencias (Listas, Cadenas, Diccionarios, Tuplas, Sets).
- **La función `range()`:** Genera secuencias de números fácilmente `range(inicio, fin, paso)`.
- **Control de Flujo en Bucles:**
  - `break`: Rompe y sale del bucle por completo.
  - `continue`: Salta la iteración actual y pasa a la siguiente.
  - `pass`: Operación nula (útil como placeholder).
- **Bucles Anidados:** Un bucle dentro de otro bucle (útil para matrices o tablas).
- **`else` en bucles:** Un bloque que se ejecuta cuando el bucle termina de forma natural (sin un `break`).

### 💻 Ejercicios Realizados
- [x] Iteraciones básicas con `for` y `while` (ascendente y descendente).
- [x] Creación de patrones geométricos (triángulos y cuadrículas) usando bucles anidados.
- [x] Generación de tablas de multiplicar dinámicas.
- [x] Filtrado de datos en iteraciones (separar números pares e impares).
- [x] Sumatorios y acumuladores de datos.

### 🛠️ Aplicación en IA
Los bucles son el "motor" del Machine Learning:
1.  **Épocas de Entrenamiento (Epochs):** Un modelo de IA no aprende a la primera. Se usa un bucle `for` para que el modelo repase los datos miles de veces (`for epoch in range(1000): entrenar_modelo()`).
2.  **Procesamiento en Lotes (Batches):** En visión artificial, no puedes cargar 1 millón de imágenes de golpe en la memoria, así que usas un bucle para procesarlas de 32 en 32.
3.  **Limpieza de Datos:** Recorrer un dataset fila por fila para rellenar valores nulos o eliminar errores.