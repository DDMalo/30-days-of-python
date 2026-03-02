# 1. Obtener la entrada del usuario usando input("Enter your age: ").
edad = int(input("Introduce tu edad: "))

if edad >= 18:
    print("Ya tienes la edad suficiente para conducir")
else:
    print(f"Aun necesitas esperar {18 - edad} años para aprender a conducir")

# 2. Comparar los valores de 'my_age' y 'your_age' usando input().
mi_edad = 20
su_edad = int(input("Dime que edad tienes: "))

if mi_edad > su_edad:
    dif = mi_edad - su_edad
    if dif == 1:
        print(f"Yo soy {dif} año mas grande que tu")
    else:
        print(f"Yo soy {dif} años mas grande que tu")
elif mi_edad < su_edad:
    dif = su_edad - mi_edad
    if dif == 1:
        print(f"Tu eres {dif} año mas grande que yo")
    else:
        print(f"Tu eres {dif} años mas grande que yo")
else:
    print("Tenemos la misma edad")


# 3. Obtener dos números del usuario.
a = int(input("Dime el numero a: "))
b = int(input("Dime el numero b: "))

if a > b:
    print(f"El {a} es mayor que el {b}")
elif a < b:
    print(f"El {a} es menor que el {b}")
else:
    print(f"El {a} es igual que el {b}")

#Nivel 2
# 1. Escribir un código que califique a los estudiantes según sus puntuaciones:
calificacion = int(input("Introduce la calificacion del alumno: "))
if calificacion >= 80:
    print("A")
elif calificacion >= 70:
    print("B")
elif calificacion >= 60:
    print("C")
elif calificacion >= 50:
    print("D")
else:
    print("F")

# 2. Comprobar la estación del año.
mes = input("Introduce el mes: ").lower()
if mes in ['september', 'october', 'november']:
    print("Estamos en Otoño")
elif mes in ['december', 'january', 'february']:
    print("Estamos en Invierno")
elif mes in ['march', 'april', 'may']:
    print("Estamos en Primavera")
elif mes in ['june', 'july', 'august']:
    print("Estamos en Verano")
else:
    print("Mes no valido")

# 3. Lista de frutas: fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = ['banana', 'orange', 'mango', 'lemon']
frutas_in = input("introduce una fruta: ").lower()

if frutas_in in fruits:
    print(f"La fruta {frutas_in} ya se encuentra en la lista")
else:
    fruits.append(frutas_in)
    print(fruits)

# Nivel 3
# 1. Ejercicio de lógica con Diccionarios:
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    medio = len(skills) // 2
    print(f"Skill media: {skills[medio]}")

if 'skills' in person:
    if 'Python' in person['skills']:
        print("El sabe Python")

if 'skills' in person:
    skills_set = set(person['skills']) 
    
    if {'JavaScript', 'React'}.issubset(skills_set):
        print('Es desarrollador frontend')
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print('Es desarrollador backend')
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print('Es desarrollador full-stack')
    else:
        print('Título desconocido')

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} vive en {person['country']}. Esta casado.")