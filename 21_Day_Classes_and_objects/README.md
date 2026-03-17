# Día 21: Clases y Objetos (POO) 🏗️

Hoy he dado el paso más importante en la estructuración de código: he aprendido **Programación Orientada a Objetos (POO)**. Ahora puedo modelar elementos del mundo real directamente en mi código usando Clases, lo que hace que mis programas sean mucho más escalables y profesionales.

### 🧠 Conceptos Aprendidos
- **Clases (`class`):** Son los "planos" o "moldes". Definen qué características y acciones tendrá un objeto.
- **Objetos (Instancias):** Son las creaciones físicas hechas a partir del molde de la clase.
- **El Constructor (`__init__`):** Una función mágica que se ejecuta automáticamente al crear un objeto para darle sus valores iniciales.
- **`self`:** La palabra clave que permite a un objeto referirse a sí mismo y a sus propios datos.
- **Herencia:** La capacidad de crear una clase nueva (hija) que hereda todas las propiedades y métodos de una clase existente (padre).

### 💻 Ejercicios Realizados
- [x] Creación de una clase `Statistics` para calcular media, mediana, moda y varianza de un conjunto de datos sin usar librerías externas.
- [x] Creación de una clase `PersonAccount` para gestionar ingresos, gastos y el balance financiero de una persona.

### 🛠️ Aplicación en IA
- **La base de todo:** En la Inteligencia Artificial, TODO es un objeto. Cuando usas librerías como *Scikit-Learn* o *PyTorch*, lo que haces es instanciar una clase (ej. `modelo = RedNeuronal()`) y luego usar sus métodos (ej. `modelo.entrenar(datos)` o `modelo.predecir(imagen)`). Entender cómo funcionan las clases por dentro es obligatorio para poder crear o modificar arquitecturas de IA.