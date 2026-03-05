import random
import string

# --- NIVEL 1 ---

# 1. Escribe una función 'random_user_id' que genere un string de seis caracteres/números aleatorios.

def random_user_id():
    caracteres = string.ascii_letters + string.digits
    id_generado = "".join(random.choices(caracteres, k=6))
    return id_generado
print(random_user_id())

# 2. Modifica la tarea anterior. Declara una función 'user_id_gen_by_user'. 
def user_id_gen_by_user():
    longitud = int(input("Introduce la longitud de la cadena: "))
    cantidad = int(input("introduce cuantos codigos quieres generar: "))
    caracteres = string.ascii_letters + string.digits
    for i in range(cantidad):
        id_generado = "".join(random.choices(caracteres, k=longitud))
        print(id_generado)
#user_id_gen_by_user()
    

# 3. Escribe una función 'rgb_color_gen'. 
def rgb_color_gen():
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    return f"rgb {color1}, {color2}, {color3}"

# --- NIVEL 2 ---

# 1. Escribe una función 'list_of_hexa_colors' que devuelva una lista con cualquier cantidad de colores hexadecimales aleatorios.
def list_of_hexa_colors(n):
    hex = string.hexdigits
    colores = []
    for i in range(n):
        color = '#' + ''.join(random.choices(hex, k=6))
        colores.append(color)
    return colores
print(list_of_hexa_colors(5))

# 2. Escribe una función 'list_of_rgb_colors' que devuelva una lista con cualquier cantidad de colores RGB aleatorios.
def list_of_rgb_colors(n):
    rgb = []
    for i in range(n):
        rgb.append(rgb_color_gen())
    return rgb
print(list_of_rgb_colors(5))

# 3. Escribe una función 'generate_colors' que pueda generar colores hex o rgb.
def generate_colors(tipo, cantidad):
    tipo1 = tipo.lower()
    if "hexa" in tipo1:
        return list_of_hexa_colors(cantidad)
    elif "rgb" in tipo1:
        return list_of_rgb_colors(cantidad)
    else:
        return "Tipo no valido"

print(generate_colors("rgb", 5))

# --- NIVEL 3 ---

# 1. Llama a tu función 'shuffle_list', que toma una lista como parámetro y devuelve una lista mezclada (desordenada aleatoriamente).
def shuffle_list(lista):
    random.shuffle(lista)
    return lista
print(shuffle_list(["Hola", "adios", "si", "no"]))

# 2. Escribe una función que devuelva un array de 7 números aleatorios en un rango de 0-9.
def seven_random_numbers():
    return random.sample(range(10), 7)

print( seven_random_numbers())