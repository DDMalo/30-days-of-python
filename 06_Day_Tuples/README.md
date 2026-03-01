# Día 6: Tuplas 🔒

Hoy he aprendido sobre las **Tuplas**. A diferencia de las listas, las tuplas son inmutables, lo que significa que una vez creadas, no se pueden modificar, añadir ni borrar elementos individuales. Son más rápidas y seguras para datos que no deben cambiar.

### 🧠 Conceptos Aprendidos
- **Inmutabilidad:** La característica clave. Protege los datos contra cambios accidentales.
- **Sintaxis:** Se usan paréntesis `()` en lugar de corchetes `[]`.
- **Operaciones Permitidas:**
  - Indexación (`tuple[0]`) y Slicing (`tuple[1:3]`).
  - Concatenación (`+`) para unir dos tuplas en una nueva.
  - Verificación de existencia (`in`).
- **Conversión:** Truco para modificar una tupla: `tuple` ➡️ `list` ➡️ *modificar* ➡️ `tuple`.
- **Métodos:** Al ser inmutables, tienen pocos métodos:
  - `.count()`: Cuenta cuántas veces aparece un elemento.
  - `.index()`: Busca la posición de un elemento.

### 💻 Ejercicios Realizados
- [x] Creación y manipulación básica de tuplas familiares.
- [x] Unión de tuplas (concatenación).
- [x] Desempaquetado (Unpacking) de elementos en variables.
- [x] Conversión entre tuplas y listas para permitir modificaciones.
- [x] Slicing avanzado (extraer elementos centrales y extremos).
- [x] Borrado completo de tuplas con `del`.

### 🛠️ Aplicación en IA
En Inteligencia Artificial, las tuplas se usan para **hiperparámetros** y configuraciones que no deben cambiar durante el entrenamiento del modelo. Por ejemplo, la forma (*shape*) de los tensores en TensorFlow o PyTorch se define siempre como una tupla `(3, 224, 224)` porque las dimensiones de una imagen no deben alterarse por error.