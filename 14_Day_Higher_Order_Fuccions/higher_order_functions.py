from functools import reduce

countries1 = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- NIVEL 1 ---

# 1. Explica brevemente la diferencia entre map, filter y reduce (escribe tu respuesta como comentario).
# - map: Aplica una función a TODOS los elementos de un iterable y devuelve uno nuevo modificado.
# - filter: Devuelve solo los elementos que cumplen una condición (donde la función devuelve True).
# - reduce: Aplica una función acumulativa de izquierda a derecha para reducir el iterable a un solo valor.

# 2. Usa map para crear una nueva lista cambiando cada país a mayúsculas en la lista 'countries1'.
# - Funciones de Orden Superior (HOF): Funciones que toman otras funciones como parámetros o las devuelven.
# - Closures: Funciones anidadas que "recuerdan" las variables de su entorno incluso después de que la función externa haya terminado.
# - Decoradores: Un patrón de diseño (usando closures y HOF) que permite añadir nueva funcionalidad a una función existente sin modificar su código original (usando la sintaxis @).

# 3. Define la función que llama
def fun_cuadrado(x):
    return x ** 2
print(list(map(fun_cuadrado, numbers)))

# 4. Imprime cada país
for pais in countries1:
    print(pais)

# 5. Imprime cada nombre
for nombre in names:
    print(nombre)

# 6. Imprime cada número
for numero in numbers:
    print(numero)

# ---- Nivel Intermedio ----
# 1. Usa map para convertir cada país en countries1 a mayúsculas y genera una nueva lista.
pais_ma = list(map(lambda x: x.upper(), countries1))
print(pais_ma)

# 2. Usa map para elevar al cuadrado cada número en numbers y genera una nueva lista.
numbers_cuadrado = list(map(lambda x : x ** 2, numbers))
print(numbers_cuadrado)

# 3. Usa map para convertir cada nombre en names a mayúsculas y genera una nueva lista.
nombres_ma = list(map(lambda x: x.upper(), names))
print(nombres_ma)

# 4. Usa filter para filtrar países que contienen 'land'.
filtrar_paises = list(filter(lambda x : "land" in x, countries1))
print(filtrar_paises)

# 5. Usa filter para filtrar países con exactamente seis caracteres.
long_pais = list(filter(lambda x: len(x) == 6, countries1))
print(long_pais)

# 6. Usa filter para filtrar países con seis o más caracteres.
long2_pais = list(filter(lambda x: len(x) >= 6, countries1))
print(long2_pais)

# 7. Usa filter para filtrar países que comienzan con 'E'.
e_pais = list(filter(lambda x: x.startswith("E"), countries1))
print(e_pais)

# 8. Encadena dos o más iteradores de lista.
tres_iteradores = reduce(lambda acc, x: acc + x, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(tres_iteradores)

# 9. Declara una función get_string_lists que reciba una lista y devuelva una lista con solo los elementos de tipo cadena.
lista_pr = ["Hola", 9, False, "Adios"]
def get_string_lists(lista):
    return list(filter(lambda x: type(x) == str, lista))
print(get_string_lists(lista_pr))

# 10. Usa reduce para sumar todos los números en la lista numbers.
suma = reduce(lambda ac, x: ac + x, numbers)
print(suma)

# 11. Usa reduce para concatenar todos los países en una oración: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries1.
def sentencia(acc, curr):
    if curr == countries1[-1]:
        return f"{acc}, and {curr}"
    return f"{acc}, {curr}"
frase = reduce(sentencia, countries1) + " are north European countries1."
print(frase)

# 12. Declara una función categorize_countries que retorne una lista de países que siguen un patrón común.
from countries import countries
def categorize_countries(busqueda, lista):
    return list(filter(lambda x: busqueda.lower() in x.lower(), lista))
print(categorize_countries("land", countries))
        
# 13. Crea una función que devuelva un diccionario donde las claves sean la primera letra de los nombres de país y el valor sea el número de países que comienzan con esa letra.
def diccionario(paises):
    diccionario = {}
    iniciales = list(map(lambda c: c[0], paises))
    for letra in iniciales:
        diccionario[letra] = diccionario.get(letra, 0) + 1
    return diccionario
print(diccionario(countries))


# ---- Nivel Avanzado ----
# 1. Usando el archivo countries_data.py, completa lo siguiente:
#    - Ordena los países por nombre, capital y población.
#    - Ordena y obtiene los diez idiomas más usados.
#    - Ordena y obtiene los diez países con mayor población.
from countries_data import countries_data
def resolver_avanzados(countries_data):
    nombre = sorted(countries_data, key=lambda c: c['name'])
    capital = sorted(countries_data, key=lambda c: c.get('capital', ''))
    poblacion = sorted(countries_data, key=lambda c: c['population'], reverse=True)
    lenguajes = []
    for c in countries_data:
        lenguajes.extend(c['languages'])
    
    lang_cont = {}
    for lang in lenguajes:
        lang_cont[lang] = lang_cont.get(lang, 0) + 1
        
    top_10_languajes = sorted(lang_cont.items(), key=lambda x: x[1], reverse=True)[:10]

    top_10_poblacion = poblacion[:10]
    
    return top_10_languajes, top_10_poblacion
print(resolver_avanzados(countries_data))