# Día 11: Funciones 🛠️

Hoy he dado el paso hacia el código modular y reutilizable aprendiendo a crear **Funciones**. En lugar de reescribir la misma lógica de cálculo o limpieza de datos varias veces, ahora puedo empaquetarla en una función y llamarla cuando la necesite.

### 🧠 Conceptos Aprendidos
- **Declaración:** Uso de la palabra clave `def` seguida del nombre y paréntesis.
- **Parámetros y Argumentos:** - Pasar datos a la función para que trabaje con ellos.
  - Uso de parámetros por defecto (ej: `def saludar(nombre="Amigo"):`).
- **El comando `return`:** A diferencia de `print()` (que solo muestra texto en la pantalla), `return` devuelve un valor real que el programa puede guardar en una variable y seguir utilizando.
- **Argumentos Arbitrarios (`*args`):** Cómo crear funciones que acepten un número infinito de parámetros (como hace la función `print()` original).
- **Ámbito (Scope):** Comprender la diferencia entre variables locales (viven solo dentro de la función) y globales (accesibles desde cualquier parte).



### 💻 Ejercicios Realizados
- [x] Funciones matemáticas básicas (sumas, área de un círculo, conversión de temperaturas).
- [x] Funciones con `*args` para sumar listas dinámicas de números.
- [x] Funciones de manipulación de arrays (invertir listas, añadir/eliminar elementos, poner en mayúsculas).
- [x] Funciones lógicas avanzadas (comprobar si todos los elementos de una lista son únicos o del mismo tipo).
- [x] Creación de un validador de variables de Python.

### 🛠️ Aplicación en IA
En Inteligencia Artificial, las funciones lo son absolutamente todo:
1.  **Pipelines de Preprocesamiento:** Se crean funciones como `limpiar_texto(texto)` o `normalizar_imagen(img)` que se aplican automáticamente a millones de datos.
2.  **Modularidad de Modelos:** En PyTorch o TensorFlow, defines la "arquitectura" de tu red neuronal dentro de una función o clase, y la función "forward" decide cómo se mueven los datos a través de las "neuronas".
3.  **Métricas:** Funciones personalizadas para calcular el error o la precisión de un modelo (`def calcular_accuracy(predicciones, reales):`).