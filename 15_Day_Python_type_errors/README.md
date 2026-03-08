# Día 15: Tipos de Errores de Python 🚨

¡Mitad del reto completada! 🥳 Hoy he dedicado el día a entender a mi mejor amigo y peor enemigo: los mensajes de error de Python. En lugar de asustarme al ver texto en rojo en la terminal, ahora sé leer el *Traceback* para identificar rápidamente dónde y por qué ha fallado mi código.

### 🧠 Conceptos Aprendidos
- **Leer el Traceback:** Empezar a leer el error desde abajo (el tipo de error) hacia arriba (la línea exacta donde ocurrió).
- **Tipos comunes:**
  - `SyntaxError`: Escribir mal el código (olvidar dos puntos `:`, comillas o paréntesis).
  - `NameError`: Usar una variable o función que no existe o no se ha importado.
  - `IndexError`: Intentar sacar el elemento 10 de una lista que solo tiene 5.
  - `KeyError`: Intentar sacar el valor de una clave que no existe en un Diccionario.
  - `TypeError`: Intentar sumar peras con manzanas (ej: sumar un `int` con un `string`).
  - `ValueError`: Pasar un valor inapropiado (ej: intentar convertir la palabra "Hola" a entero con `int("Hola")`).
  - `ZeroDivisionError`: Las matemáticas no permiten dividir entre cero.
  - `AttributeError`: Usar un método que no le corresponde a un objeto (ej: hacer `.append()` a un string).



### 💻 Ejercicios Realizados
- [x] Provocar intencionadamente todos los tipos de errores comunes de Python para familiarizarme con sus mensajes en la consola.

### 🛠️ Aplicación en IA
Saber leer errores es el 90% del tiempo de un Ingeniero de IA.
Cuando construyes redes neuronales, el error más común es el de "incompatibilidad de dimensiones" (Shape mismatch), que en el fondo es un `ValueError` o un `RuntimeError`. Si sabes interpretar los errores base de Python, no entrarás en pánico cuando TensorFlow o PyTorch te devuelvan un error de 50 líneas.