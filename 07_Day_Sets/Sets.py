# --- NIVEL 1 ---
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1. Hallar la longitud del set it_companies
print(len(it_companies))

# 2. Añadir 'Twitter' a it_companies
it_companies.add("Twitter")

# 3. Insertar múltiples empresas IT a la vez en el set it_companies
it_companies.update(["Meta", "OpenAi"])

# 4. Eliminar una de las empresas del set it_companies
it_companies.remove("Google")

# 5. ¿Cuál es la diferencia entre remove y discard?
# remove("Twitter"): Si el elemento NO existe, lanza un error y detiene el programa.
# discard("Twitter"): Si el elemento NO existe, no hace nada. Es más seguro.
it_companies.discard("UJA") # No pasa nada

# --- NIVEL 2 ---
# 1. Unir A con B
C = A.union(B)
print(C)

# 2. Encontrar la intersección de A y B
print(A.intersection(B))

# 3. ¿Es A subconjunto de B?
print(A.issubset(B))

# 4. ¿Son A y B conjuntos disjuntos (sin elementos comunes)?
print(A.isdisjoint(B))

# 5. Unir A con B y B con A (Comprobar si es simétrico)
print(A.union(B))
print(B.union(A))

# 6. ¿Cuál es la diferencia simétrica entre A y B?
print(A.symmetric_difference(B))

# 7. Eliminar los sets completamente
del A
del B

# --- NIVEL 3 ---
# 1. Convertir la lista 'age' a un set y comparar la longitud de la lista vs el set.
age_set = set(age)
print(len(age))
print(len(age_set))

# 2. Explicar la diferencia entre String, List, Tuple y Set.
# String: Texto inmutable ordenado ('hola').
# List: Colección ordenada, mutable, permite duplicados ([]).
# Tuple: Colección ordenada, inmutable, permite duplicados (()).
# Set: Colección desordenada, mutable, NO permite duplicados ({}).

# 3. "I am a teacher and I love to inspire and teach people."
# ¿Cuántas palabras únicas se han usado en la frase? 
sentence = "I am a teacher and I love to inspire and teach people"
lista2 = sentence.split()
unicos = set(lista2)
print(len(unicos))