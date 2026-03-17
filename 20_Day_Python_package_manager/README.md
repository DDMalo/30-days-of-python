# Día 20: Gestor de Paquetes de Python (PIP) 📦🌐

Hoy he dado un salto gigante: he aprendido a usar **PIP**, el gestor de paquetes de Python. Esto me abre las puertas a un ecosistema de miles de librerías gratuitas creadas por la comunidad. Además, he hecho mis primeras conexiones a internet directamente desde el código usando la librería `requests`.

### 🧠 Conceptos Aprendidos
- **PIP:** Comandos básicos en la terminal:
  - `pip install <paquete>`: Instala una librería de internet.
  - `pip uninstall <paquete>`: Desinstala una librería.
  - `pip list`: Muestra todo lo que tienes instalado.
  - `pip freeze > requirements.txt`: Guarda una lista con las versiones exactas de tus paquetes (vital para compartir proyectos).
- **Librería `requests`:** El estándar de la industria para hacer peticiones HTTP (descargar HTML de webs o datos en formato JSON desde APIs).
- **APIs (Interfaces de Programación de Aplicaciones):** URLs especiales que, en lugar de devolver una página web bonita para humanos, devuelven datos puros (generalmente en JSON) para que los consuma nuestro código.



### 💻 Ejercicios Realizados
- [x] Conexión a internet mediante `requests.get()`.
- [x] Descarga y análisis de texto de un libro online (Romeo y Julieta).
- [x] Consumo de la API pública de Gatos para calcular estadísticas complejas (media, mediana, desviación estándar de pesos y edades).
- [x] Consumo de la API de Países para clasificar datos a nivel mundial.

### 🛠️ Aplicación en IA
- **El Ecosistema IA:** Literalmente, **TODA** la Inteligencia Artificial en Python funciona gracias a PIP. Cuando quieras crear una red neuronal, no la programarás desde cero, simplemente abrirás la terminal y escribirás: `pip install tensorflow`, `pip install scikit-learn` o `pip install torch`.
- **Recolección de Datos:** Las librerías como `requests` (junto con `BeautifulSoup`) se usan a diario para descargar millones de textos de internet y crear los datasets con los que se entrenan los modelos de lenguaje (como yo).