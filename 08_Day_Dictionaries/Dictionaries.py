# 1. Crear un diccionario vacío llamado 'dog'
dog = {}

# 2. Añadir nombre, color, raza, patas y edad al diccionario 'dog'
dog["nombre"] = "Gusy" 
dog["color"] = "Marron"
dog["Raza"] = "Pastor aleman"
dog["Piernas"] = 4
dog["Edad"] = 5
print(dog)

# 3. Crear un diccionario 'student' con: first_name, last_name, age, country, marital_status, skills (una lista), address (un diccionario)
student = {
    "first_name" : "David",
    "last_name" : "Donoso",
    "age" : "20",
    "country" : "Spain", 
    "marital_status" : False,
    "skills" : ["C++", "Python", "Java"],
    "address" : {
        "Street" : "Calle San Lucas",
        "Code" : "23000"
    }
    
}

# 4. Obtener la longitud del diccionario 'student'
print(len(student))

# 5. Obtener el valor de 'skills' y comprobar el tipo de dato
skill = student["skills"]
print(skill)
print(type(skill))

# 6. Modificar 'skills': Añadir dos habilidades nuevas a la lista (ej: 'Python', 'Git')
student["skills"].append("CSS")
student["skills"].append("Git")
print(student["skills"])
# 7. Obtener todas las claves (keys) del diccionario 'student' como una lista
keys = list(student.keys())
print(keys)

# 8. Obtener todos los valores (values) del diccionario 'student' como una lista
valores = list(student.values())
print(valores)

# 9. Cambiar el diccionario a una lista de tuplas usando el método items()
print(student.items())

# 10. Eliminar uno de los ítems del diccionario (ej: 'marital_status')
student.pop("marital_status")

# 11. Borrar el diccionario 'dog' completamente
del dog