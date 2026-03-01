# Día 7: Sets (Conjuntos) 🎱

En esta sesión he trabajado con los **Sets** (Conjuntos). A diferencia de las listas y tuplas, los sets son colecciones **desordenadas** (no tienen índice 0, 1, 2...) y **sin elementos duplicados**. Son la implementación programática de los conjuntos matemáticos.

### 🧠 Conceptos Aprendidos
- **Características:** No indexados, mutables (podemos añadir/borrar items), pero cada elemento debe ser único.
- **Creación:** Uso de llaves `{}` o la función `set()`.
- **Modificación:**
  - `add()`: Añadir un elemento.
  - `update()`: Añadir múltiples elementos.
- **Eliminación:**
  - `remove()`: Borra (lanza error si no existe).
  - `discard()`: Borra (NO lanza error si no existe).
  - `pop()`: Borra un elemento aleatorio (porque no hay orden).
- **Operaciones Matemáticas (Teoría de Conjuntos):**
  - **Unión (`union` o `|`):** Suma de todos los elementos.
  - **Intersección (`intersection` o `&`):** Elementos comunes en ambos.
  - **Diferencia (`difference` o `-`):** Elementos que están en A pero no en B.
  - **Diferencia Simétrica (`symmetric_difference` o `^`):** Elementos que están en A o B, pero no en ambos.

### 💻 Ejercicios Realizados
- [x] Creación de conjuntos y cálculo de longitud.
- [x] Gestión de elementos (añadir uno o varios, eliminar con seguridad).
- [x] Operaciones avanzadas de conjuntos (unión, intersección, diferencia).
- [x] Relaciones entre conjuntos (subset, superset, disjoint).
- [x] Limpieza de datos: Conversión de Lista a Set para eliminar duplicados.

### 🛠️ Aplicación en IA
Los Sets son cruciales para la **Limpieza de Datos**.
1.  **Eliminar duplicados:** Si tienes una lista de 1 millón de transacciones y quieres saber cuántos usuarios *únicos* hay, conviertes la lista a set: `usuarios_unicos = set(lista_usuarios)`.
2.  **Vocabulario (NLP):** Para entrenar una IA de texto, primero necesitas saber cuántas palabras únicas existen en el libro (el "vocabulario"). Un Set te da esa lista instantáneamente.



