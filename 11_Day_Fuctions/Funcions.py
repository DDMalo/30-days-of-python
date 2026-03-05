# 1. Declarar una función add_two_numbers. Toma dos parámetros y devuelve su suma.
def add_two_numbers(num1, num2):
    return num1 + num2
print(add_two_numbers(2,3))

# 2. El área de un círculo se calcula así: area = π x r x r. Escribe una función area_of_circle que calcule el área.
def area_of_circle(area):
    return 3.14 * area * area
print(area_of_circle(3))

# 3. Escribir una función add_all_nums que tome un número arbitrario de argumentos (*args) y sume todos los que sean números.
def add_all_nums(*args):
    total = 0
    for i in args:
        if type(i) in (int, float):
            total += i
        else:
            print("Error: Todos los elementos deben ser numeros")
    return total
print(add_all_nums(3,5,1))

# 4. Temperatura en °C se puede convertir a °F usando: °F = (°C x 9/5) + 32. Escribe una función convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32
print(convert_celsius_to_fahrenheit(30))

# 5. Escribe una función check_season que tome un mes como parámetro y devuelva la estación (Otoño, Invierno, Primavera, Verano).
def check_season(mes):
    if mes in ["Septiembre", "Octubre", "Noviembre"]:
        print("Es otoño")
    elif mes in ["Diciembre", "Enero", "Febrero"]:
        print("Es invierno")
    elif mes in ["Marzo", "Abril", "Mayo"]:
        print("Es primavera")
    elif mes in ["Junio", "Julio", "Agosto"]:
        print("Es verano")
    else:
        print("Mes no valido")

check_season("Agosto")

# 6. Escribe una función calculate_slope que devuelva la pendiente de una ecuación lineal.
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Pendiente indefinida (división por cero)"
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(1,3,2,1))

# 7. Ecuación cuadrática: ax² + bx + c = 0. Escribe una función solve_quadratic_eqn que devuelva las soluciones.
def solve_quadratic_eqn(a, b , c):
    dis = (b**2) - (4*a*c)
    if dis < 0:
        return "No hay soluciones reales"
    
    x1 = (-b + (dis**0.5)) / (2*a)
    x2 = (-b - (dis**0.5)) / (2*a)
    return x1, x2 
print(solve_quadratic_eqn(1, 4, 1))
# 8. Declarar una función print_list que tome una lista como parámetro e imprima cada elemento.
def print_list(lista):
    for i in lista:
        print(i, end=" ")
    print()
print_list(["Hola", "Adios"])
# 9. Declarar una función reverse_list que tome un array como parámetro y devuelva el array invertido (sin usar el método reverse()).
def reverse_list(lista):
    new_lista = []
    for i in range(len(lista) - 1, -1, -1):
        new_lista.append(lista[i])
    return new_lista

print(reverse_list(["Hola", "Adios"]))
    
# 10. Declarar una función capitalize_list_items que devuelva una lista con todos los elementos en mayúsculas.
def capitalize_list_items(lista):
    min_lista = []
    for i in lista:
        min_lista.append(i.upper())
    return min_lista
print(capitalize_list_items(["a", "b", "c"]))

# 11. Declarar una función add_item que tome una lista y un ítem como parámetros, y devuelva la lista con el ítem añadido al final.
def add_item(lista, arg):
    lista.append(arg)
    return lista
print(add_item(["Si", "No"], "Vale"))

# 12. Declarar una función remove_item que tome una lista y un ítem, y devuelva la lista sin ese ítem.
def add_item(lista, arg):
    lista.remove(arg)
    return lista
print(add_item(["Si", "No", "Vale"], "Si"))

# 13. Declarar una función sum_of_numbers que tome un número y devuelva la suma de todos los números desde 1 hasta ese número.
def sum_of_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum
print(sum_of_numbers(5))

# 14. Declarar una función sum_of_odds que tome un número y devuelva la suma de todos los números impares hasta ese número.
def sum_of_odds(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 != 0:
            sum += i
    return sum
print(sum_of_odds(5))

# 15. Declarar una función sum_of_even que tome un número y devuelva la suma de todos los números pares hasta ese número.
def sum_of_even(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum += i
    return sum
print(sum_of_even(5))
# --- NIVEL 2  ---

# 1. Declarar una función evens_and_odds que tome un entero positivo y cuente el número de pares e impares.
def evens_and_odds(num):
    num_par = 0
    num_imp = 0
    for i in range(num + 1):
        if i % 2 == 0:
            num_par += 1
        else:
            num_imp += 1
    print(f"El numero de pares es de: {num_par}")
    print(f"El numero de impares es: {num_imp}")
evens_and_odds(100)

# 2. Escribir una función factorial que tome un entero y devuelva su factorial.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total
print(factorial(5))
# 3. Escribir una función is_empty que compruebe si un parámetro está vacío.
def is_empty(comp):
    if not comp:
        return True
    return False


# ---- Nivel 3 ----
# 1. Escribe una función is_prime que verifique si un número es primo.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. Escribir una función que compruebe si todos los elementos de una lista son únicos.
def all_unique(my_list):
    return len(my_list) == len(set(my_list))

# 5. Accede al archivo de datos countries-data.py
def the_most_spoken_languages(data, top=10):
    language_counts = {}
    for country in data:
        for language in country['languages']:
            language_counts[language] = language_counts.get(language, 0) + 1

    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_languages[:top]

def the_most_populated_countries(data, top=10):
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    result = []

    for country in sorted_countries[:top]:
        result.append({'country': country['name'], 'population': country['population']})
        
    return result