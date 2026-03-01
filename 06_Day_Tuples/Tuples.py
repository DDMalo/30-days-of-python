# 1. Crear una tupla vacía
tupla = ()

# 2. Crear una tupla con nombres de tus hermanas y otra con tus hermanos.
hermanos = ("Raul", "Angel")
hermanas = ("Miriam", "Patricia")

# 3. Unir las tuplas de hermanos y hermanas en una sola llamada 'siblings'
siblings = hermanos + hermanas

# 4. ¿Cuántos hermanos/hermanas tienes? (Imprimir longitud de siblings)
print(len(siblings))

# 5. Modificar la tupla 'siblings' para añadir el nombre de tu padre y madre y guardarlo en 'family_members'
padres = ("Carmen", "Juan")
family_members = siblings + padres
print(family_members)

# Nivel 2
# 1. Desempaquetar 'family_members' para separar a los padres de los hermanos.
*resto_hermanos, madre, padre = family_members
print(madre)
print(padre)
print(resto_hermanos)

# 2. Crear tuplas de frutas, verduras y productos animales
frutas = ("Naranjas", "Peras", "Manzanas")
verduras = ("Patatas", "Cebollas", "Zanahorias")
productos_animales = ("Leche", "huevos", "Carne")
food_stuff_tp = frutas + verduras + productos_animales

# 3. Cambiar la tupla 'food_stuff_tp' a una lista llamada 'food_stuff_lt'
food_stuff_lt = list(food_stuff_tp)

# 4. Cortar el ítem o ítems del medio de la tupla food_stuff_tp o la lista food_stuff_lt
medio = len(food_stuff_tp) // 2
print(food_stuff_tp[medio])

# 5. Cortar los primeros 3 y los últimos 3 ítems de la lista food_stuff_lt
tres_p = food_stuff_lt[:3]
tres_u = food_stuff_lt[-3:]
print(tres_p)
print(tres_u)

# 6. Eliminar la tupla food_stuff_tp completamente
del food_stuff_tp

# 7. Comprobar si 'Estonia' es un país nórdico, Comprobar si 'Iceland' es un país nórdico
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
