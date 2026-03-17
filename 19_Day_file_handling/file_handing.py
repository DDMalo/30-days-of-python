import os
import json
# ---  NIVEL 1 ---

# 1. Escribe una función que reciba un parámetro (nombre de archivo) y cuente el número de palabras del archivo.
def contar(archivo):
    try:
        with open(archivo , "r", encoding="utf-8") as f:
            texto = f.read()
            palabras = texto.split()
            return len(palabras)
    except FileExistsError:
        return f"No se encontro el archivo {archivo}"

# 2. Lee el archivo obama_speech.txt y cuenta las palabras.
print(f"Palabras del archivo obama_speech.txt: {contar("19_Day_file_handling/obama_speech.txt")}")

# 3. Lee michelle_obama_speech.txt y cuenta las palabras.
print(f"Palabras del archivo michelle_obama_speech.txt: {contar("19_Day_file_handling/michelle_obama_speech.txt")}")

# 4. Lee donald_speech.txt y cuenta las palabras.
print(f"Palabras del archivo donald_speech.txt: {contar("19_Day_file_handling/donald_speech.txt")}")

# 5. Lee melina_trump_speech.txt y cuenta las palabras.
print(f"Palabras del archivo melina_trump_speech.txt: {contar("19_Day_file_handling/melina_trump_speech.txt")}")

# --- NIVEL 2 ---

# 1. Extrae todos los archivos Python del directorio del curso:
#    a) Recorre la carpeta 30DaysOfPython, extrae todos los archivos .py y guarda sus nombres en files_list.txt
#    b) Crea un script llamado find_python.py que pueda ejecutarse desde la línea de comandos
#    c) Añade una opción --version para manejar argumentos de línea de comandos
def extraer():
    archivos_py = [archivo for archivo in os.listdir(".") if archivo.endswith(".py")]
    with open("files_list.txt", "w", encoding="utf-8") as f:
        for archivo in archivos_py:
            f.write(archivo + "\n")
    print(f"Se han guardado {len(archivos_py)} nombres de archivos Python en 'files_list.txt'")

extraer()

# --- NIVEL 3 ---

# 1. Crea un archivo JSON a partir del siguiente dataset:

python_libraries = [
    {
        "nombre_librería": "Django",
        "creador": "Adrian Holovaty",
        "primer_año_lanzamiento": 2005,
        "versión": "4.0.2",
        "uso": "Desarrollo web",
        "descripción": "Django permite construir aplicaciones web mejores y más rápido."
    },
    {
        "nombre_librería": "Flask",
        "creador": "Armin Ronacher",
        "primer_año_lanzamiento": 2010,
        "versión": "2.0.2",
        "uso": "Desarrollo web",
        "descripción": "Flask es un micro framework WSGI para aplicaciones web."
    },
    {
        "nombre_librería": "NumPy",
        "creador": "Travis Oliphant",
        "primer_año_lanzamiento": 2005,
        "versión": "1.22.0",
        "uso": "Cómputo científico",
        "descripción": "NumPy es la biblioteca fundamental para el cómputo científico en Python."
    },
    {
        "nombre_librería": "Pandas",
        "creador": "Wes McKinney",
        "primer_año_lanzamiento": 2008,
        "versión": "1.4.0",
        "uso": "Análisis de datos",
        "descripción": "pandas es una librería open source para análisis y manipulación de datos."
    },
    {
        "nombre_librería": "Matplotlib",
        "creador": "John D. Hunter",
        "primer_año_lanzamiento": 2003,
        "versión": "3.5.1",
        "uso": "Visualización de datos",
        "descripción": "Matplotlib es una librería para crear visualizaciones estáticas, animadas e interactivas en Python."
    }
]
with open("python_libraries.json", "w", encoding="utf=8") as f:
    json.dump(python_libraries, f, ensure_ascii=False, indent=4)