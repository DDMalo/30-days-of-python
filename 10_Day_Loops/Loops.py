# 1. Iterar del 0 al 10 usando un bucle 'for' y luego hacer lo mismo con un bucle 'while'.
for i in range(11):
    print(i)

condicion = 0
while condicion < 11:
    print(condicion)
    condicion += 1


# 2. Iterar del 10 al 0 usando un bucle 'for' y luego hacer lo mismo con un bucle 'while'.
for i in range(11, -1, -1):
    print(i)

condicion2 = 10
while condicion2 > 0:
    print(condicion2)
    condicion2 -= 1


# 3. Escribir un bucle que haga 7 llamadas a print() para imprimir un triángulo:
for i in range(7):
    print("#" * i)

# 4. Usar bucles anidados para crear una cuadrícula de 8x8 con el símbolo #.
for fila in range(8):
    for columna in range(8):
        print('#', end=" ") 
    print()

# 5. Imprimir la tabla de multiplicar del 0 al 10:
for i in range(10):
    print(f"{i} * {i} = {i*i}")

# 6. Iterar a través de la lista
lista = ['Python', 'Numpy','Pandas','Django', 'Flask']
for palabra in lista:
    print(palabra, end=" ")
print()
# 7. Usar un bucle 'for' para iterar del 0 al 100 e imprimir solo los números pares.
for i in range(100):
    if i%2 == 0: print(i, end=" ")
print()
# 8. Usar un bucle 'for' para iterar del 0 al 100 e imprimir solo los números impares.
for i in range(100):
    if i%2 != 0: print(i, end=" ")

# Nivel 2
# 1. Usar un bucle 'for' para iterar del 0 al 100 e imprimir la suma de todos los números (La suma es 5050).
suma = 0
for i in range(101):
    suma += i
print(f"La suma de los 100 primeros numeros son: {suma}")

# 2. Iterar del 0 al 100 e imprimir la suma de todos los pares y la suma de todos los impares por separado.
sumapar = 0
sumaimp = 0
for i in range(101):
    if i % 2 == 0:
        sumapar += i
    else:
        sumaimp += i 
print(f"Suma par: {sumapar}")
print(f"Suma par: {sumaimp}")

# --- NIVEL AVANZADO ---
# 1. Ve a la carpeta data y usa el archivo countries.py.
from countries import countries
lista_paises = []
for pais in countries:
    if "land" in pais:
        lista_paises.append(pais)

print(lista_paises)

# 2. Dada la lista invierte los elementos
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = []
for i in range(len(fruits)-1, -1, -1):
    new_fruit.append(fruits[i])

print(new_fruit)

# 13. countries-data.py
from countries_data import countries_data
new_lista = set()

for countries in countries_data:
    for idiomas in countries["languages"]:
        new_lista.add(idiomas)

print(f"El total de idiamas son {len(new_lista)}")

contar_pais = {}
for countries in countries_data:
    for idiomas in countries["languages"]:
        if idiomas in contar_pais:
            contar_pais[idiomas] += 1
        else:
            contar_pais[idiomas] = 1 

pais_max = ""
numero_max = 0 

for lenguajes, count in contar_pais.items():
    if count > numero_max:
        pais_max = lenguajes
        numero_max = count

print(f"El pais mas hablado es: {pais_max} con un total de: {numero_max}")

poblacion_lista = []
for pais in countries_data:
    poblacion_lista.append((pais['population'], pais['name']))

poblacion_lista.sort(reverse=True)

for i in range(10):
    pop = poblacion_lista[i][0]
    name = poblacion_lista[i][1]
    print(f"{i + 1}. {name} - {pop} habitantes")