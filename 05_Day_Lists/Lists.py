# 1. Declarar una lista vacía
lista1 = list()

# 2. Declarar una lista con más de 5 ítems
frutas = ["Peras", "Manzanas", "Sandias", "Melones", "Naranjas"]

# 3. Encontrar la longitud de tu lista
print(len(frutas))

# 4. Obtener el primer ítem, el ítem del medio y el último ítem
print(frutas[0])
print(frutas[len(frutas) // 2])
print(frutas[len(frutas) - 1])

# 5. Declarar una lista llamada mixed_data_types con: nombre, edad, altura, estado civil, dirección
mixed_data_types = ["David", 20, 1.69, False, "Ubeda, Jaen"]

# 6. Declarar una lista variable llamada it_companies con: Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Imprimir la lista usando print()
print(it_companies)

# 8. Imprimir el número de empresas en la lista
print(len(it_companies))

# 9. Imprimir la primera, la del medio y la última empresa
print(it_companies[0])
print(it_companies[len(it_companies) // 2])
print(it_companies[-1])

# 10. Imprimir la lista después de modificar una de las empresas
it_companies[0] = "OpenAi"
print(it_companies)

# 11. Añadir una empresa IT a it_companies
it_companies.append("Meta") 

# 12. Insertar una empresa IT en el medio de la lista
it_companies.insert(len(it_companies) // 2, "Samsung")

# 13. Cambiar uno de los nombres de las empresas a mayúsculas (todo mayúsculas)
it_companies[1] = it_companies[1].upper()

# 14. Unir la lista it_companies con una cadena '#; '
print("#; ".join(it_companies))

# 15. Comprobar si una empresa determinada existe en la lista it_companies
print("OpenAi" in it_companies)

# 16. Ordenar la lista usando el método sort()
it_companies.sort()
print(it_companies)

# 17. Invertir la lista en orden descendente usando el método reverse()
it_companies.reverse()
print(it_companies)

# 18. Cortar (slice) las primeras 3 empresas de la lista
print(it_companies[:3])

# 19. Cortar (slice) las últimas 3 empresas de la lista
print(it_companies[-3:])

# 20. Cortar (slice) la empresa o empresas IT del medio de la lista
medio = len(it_companies) // 2
print(it_companies[medio:medio+1])

# 21. Eliminar la primera empresa IT de la lista
it_companies.pop(0)

# 22. Eliminar la empresa o empresas IT del medio de la lista
it_companies.pop(len(it_companies) // 2)

# 23. Eliminar la última empresa IT de la lista
it_companies.pop()

# 24. Eliminar todas las empresas IT de la lista
it_companies.clear()

# 25. Destruir la lista it_companies completamente
del it_companies

# 26. Unir las siguientes listas:
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node","Express", "MongoDB"]
completa = front_end + back_end
print(completa)

# 27. Copiar la lista unida y asignarla a una variable full_stack. Luego insertar Python y SQL después de Redux.
completa_copia = completa.copy()
encontrado = completa_copia.index('Redux') 
completa_copia.insert(encontrado + 1, 'Python')
completa_copia.insert(encontrado + 2, 'SQL')
print(completa_copia)

# Nivel 2
# Dada la siguiente lista de edades: ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# - Ordenar la lista y encontrar la edad mínima y máxima
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minima = ages[0]
maxima = ages[-1]
print(f"Minima: {minima}")
print(f"Maxima: {maxima}")

# - Añadir la edad mínima y máxima de nuevo a la lista
ages.append(minima)
ages.append(maxima)

# - Encontrar la edad media
media = sum(ages) / len(ages)
print(f"La edad media es de: {media}")

# - Encontrar el rango de las edades (máximo menos mínimo)
age_range = maxima - minima

# - Comparar el valor de (min - promedio) y (max - promedio), usar método abs()
dif_min = abs(minima - media)
dif_max = abs(maxima - maxima)
print(f"Diferencia Min-Media: {dif_min}")
print(f"Diferencia Max-Media: {dif_max}")

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# - Encontrar el país o países del medio
medio2 = len(countries) // 2
print(f"País central: {countries[medio2]}")

# - Dividir la lista de países en dos listas iguales (si es impar, un país más para la primera mitad)
first_half = countries[:medio2 + 1] # De 0 a 4
second_half = countries[medio2 + 1:]

# - Desempaquetar los primeros tres países y el resto como 'scandic_countries'
c1, c2, c3, *resto = countries
print(c1, c2, c3)
print(resto)