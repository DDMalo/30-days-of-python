import os
import argparse

def encontrar_archivos(directorio = "."):
    lista_py = []
    for root, dir, arc in os.walk(directorio):
        for f in arc:
            if f.endswith(".py"):
                lista_py.append(os.path.join(root, f))
    return lista_py

def main():
    parser = argparse.ArgumentParser(description="Analizar archivos .py")
    parser.add_argument("--version", action="version", version="find_python script v1.0", help="Muestra la versión actual del script")
    parser.add_argument('path', nargs='?', default='.', help="Ruta de la carpeta a escanear")
    args = parser.parse_args()
    archivos = encontrar_archivos(args.path)
    print(f"Se encontraron {len(archivos)} archivos .py: ")
    for arc in archivos:
        print(arc)

if __name__ == "__main__":
    main()