# 1. Filtrar solo los números negativos y el cero en la lista usando list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numeros_filtrados = [i for i in numbers if i <= 0]
print(numeros_filtrados)

# 2. Aplanar la siguiente lista de listas en una lista unidimensional:
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
juntar_lista = [num for i in list_of_lists for i2 in i for num in i2]
print(juntar_lista)

# 3. Usando list comprehension, crear la siguiente lista de tuplas:
lista_tuplas = [(i, 1, i, i**2, i**3, i**3, i**4, i**5 ) for i in range(11)]
print(lista_tuplas)

# 4. Aplanar esta lista de países en una nueva lista (País en mayúsculas, código de 3 letras, ciudad en mayúsculas):
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
lista_paises = [[pais.upper(), pais[:3].upper(), capital.upper()] for i in countries for pais, capital in i ]
print(lista_paises)

# 5. Cambiar la lista anterior a una lista de diccionarios:
diccionario = [{"country": pais.upper(), "city": ciudad.upper(),} for i in countries for pais, ciudad in i]
print(diccionario)

# 6. Cambiar la siguiente lista de listas a una lista de strings concatenados:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lista_nombres = [f"{nombre} {apellido}" for sub in names for nombre, apellido in sub]
print(lista_nombres)

# 7. Escribir una función lambda que pueda resolver la pendiente (slope) de una función lineal (m = (y2 - y1) / (x2 - x1)).
solucion = lambda x1, x2, y1, y2 : (y2 - y1)/(x2 - x1)
print(solucion(1,2,2,1))