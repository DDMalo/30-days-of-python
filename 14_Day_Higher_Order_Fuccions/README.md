# Día 14: Funciones de Orden Superior 🧠

Hoy he entrado en el terreno de la programación funcional en Python. He aprendido sobre las **Funciones de Orden Superior**, que son funciones que pueden tomar otras funciones como parámetros o devolver funciones como resultado.

### 🧠 Conceptos Aprendidos
- **Funciones como ciudadanos de primera clase:** En Python, puedes pasar funciones como argumentos.
- **`map(funcion, iterable)`:** Aplica una función a todos los elementos de una lista y devuelve una nueva lista (modificada).
- **`filter(funcion, iterable)`:** Filtra los elementos de una lista devolviendo solo aquellos que cumplen una condición (es decir, donde la función devuelve `True`).
- **`reduce(funcion, iterable)`:** Aplica una función de manera acumulativa a los elementos de una lista, de izquierda a derecha, para reducirla a un solo valor (requiere importar el módulo `functools`).



### 💻 Ejercicios Realizados
- [x] Teoría: Explicar la diferencia entre `map`, `filter` y `reduce`.
- [x] Uso de `map` para transformar listas de strings (mayúsculas) y números (cuadrados).
- [x] Uso de `filter` para extraer datos específicos (países con 'land', nombres de 6 letras).
- [x] Uso de `reduce` para sumar arrays y concatenar cadenas complejas.

### 🛠️ Aplicación en IA
En la limpieza y preparación de datos (Data Wrangling), estas funciones son vitales:
1.  **Transformación Masiva (`map`):** Normalizar una lista de 100,000 imágenes para que todas tengan un tamaño de 256x256 píxeles.
2.  **Limpieza (`filter`):** Eliminar de un dataset todos los registros que tengan campos vacíos o valores nulos antes de entrenar la IA.
3.  **Agregación (`reduce`):** Calcular el error total acumulado en una red neuronal sumando los errores individuales de cada predicción.