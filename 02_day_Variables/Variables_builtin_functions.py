# Dia 2 - Variables


# Nivel 1
nombre = "David"
apellido = "Donoso"
nombre_completo = f"{nombre} {apellido}"
pais = "España"
ciudad = "Jaén"
edad = 20
anio = 2026
is_married = False
is_true = True
is_light_on = True
profesion, universidad, motivacion = "Estudiante", "UJA", "IA"

# Nivel 2
# 1.Verificar datos
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(anio))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# 2.Longitud nombre
longitud = (len(nombre))
print(f"Mi nombre posee {longitud} letras")

# 3.Comparar losgitud nombre y apellido
print(f"¿Es mi nombre más largo que mi apellido? {len(nombre) > len(apellido)}")

# 4.Operaciones
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
mull = num_two * num_one
div = num_one/num_two
residuo = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two
print(f"Suma: {total}, Resta: {diff}, Multiplicación: {mull}")
print(f"División: {div}, Exponente: {exp}, División de piso: {floor_division}")

# 5.Geometria
radio = 30
pi = 3.1415
area_of_circle = pi * (radio**2)
circum_of_circle = 2 * pi * radio
print(f"Área del círculo: {area_of_circle} m2")
print(f"Circunferencia: {circum_of_circle} m")
radio_usuario = float(input("Introduce el radio de la circunferencia: "))
area_usuario = pi * (radio_usuario**2)
print(f"El area del circulo del usuario es de: {area_usuario} m2")

# 6.Introducir valores
user_first_name = input("Dime tu nombre: ")
user_last_name = input("Dime tu apellido: ")
user_country = input("¿De qué país eres?: ")
user_age = input("¿Qué edad tienes?: ")

# 7. Run help("keywords")
help("keywords")