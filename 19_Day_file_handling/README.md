# Día 19: Manejo de Archivos y JSON 📁

Hoy he aprendido a conectar mi código con el "mundo exterior". He dominado la lectura y escritura de archivos de texto (`.txt`), la navegación por directorios usando el sistema operativo y la creación de archivos `.json`.

### 🧠 Conceptos Aprendidos
- **Abrir Archivos (`open`):** Uso de la función `open(archivo, modo)` con los modos:
  - `'r'`: Lectura (Read).
  - `'w'`: Escritura (Write - sobrescribe el archivo).
  - `'a'`: Añadir (Append - añade al final).
- **Cierre Seguro:** Uso del bloque `with open(...) as file:` para asegurar que el archivo se cierra automáticamente al terminar, evitando bloqueos en la memoria.
- **Módulo `os`:** Para interactuar con el sistema operativo (listar archivos de una carpeta, crear directorios).
- **Módulo `json`:** Transformar estructuras de datos de Python (como listas de diccionarios) en archivos JSON reales usando `json.dump()`.

### 💻 Ejercicios Realizados
- [x] Lectura de múltiples discursos políticos en `.txt` y conteo automatizado de palabras.
- [x] Script para escanear un directorio, encontrar todos los archivos `.py` y guardar sus nombres en un documento de texto.
- [x] Conversión de una base de datos simulada de Python a un archivo `.json` formateado.

### 🛠️ Aplicación en IA
- **Carga de Datasets:** Prácticamente todos los modelos de Machine Learning (como los de NLP que procesan texto) se entrenan leyendo miles de archivos `.txt`, `.csv` o `.json`. 
- **APIs:** El formato JSON es el estándar absoluto para comunicarse con las APIs de modelos de IA (como cuando le mandas un prompt a OpenAI o Anthropic y recibes la respuesta).