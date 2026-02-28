# 1. Concatenar cadenas (Thirty, Days...)
print("Thirty " + "Days " + "Of " + "Python")

# 2. Concatenar cadenas (Coding, For...)
print("Coding " + "For " + "All")
# 3. Declarar variable company
company = "Coding For All"

# 4. Imprimir variable company
print(company)

# 5. Imprimir longitud len()
print(len(company))

# 6. Cambiar a mayúsculas
print(company.upper())

# 7. Cambiar a minúsculas
print(company.lower())

# 8. Formatear con capitalize(), title(), swapcase()
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. Cortar (slice) primera palabra
print(company[0:6])

# 10. Comprobar si contiene "Coding"
print(company.find("Coding"))
print("Coding" in company)

# 11. Reemplazar "Coding" por "Python"
print(company.replace("Coding", "Python"))

# 12. Reemplazar "Everyone" por "All"
texto = "Python for Everyone"
print(texto.replace('Everyone', 'All'))

# 13. Split por espacio
print(company.split())

# 14. Split por coma
companias = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companias.split(', '))

# 15. Carácter en índice 0
print(company[0])

# 16. Último índice
print(len(company) - 1)

# 17. Carácter en índice 10
print(company[10])

# 18. Acrónimo de 'Python For Everyone'
texto2 = "Python For Everyone"
print(texto2[0] + texto2[7] + texto2[11])

# 19. Acrónimo de 'Coding For All'
print(company[0] + company[7] + company[11])

# 20. Posición primera 'C' (index)
print(company.index("C"))

# 21. Posición primera 'F' (index)
print(company.index("F"))

# 22. Posición última 'l' (rfind)
print(company.rfind("l"))

# 23. Primera aparición de 'because'
texto3 = "You cannot end a sentence with because because because is a conjunction"
print(texto3.index("because"))

# 24. Última aparición de 'because'
print(texto3.rfind("because"))

# 25. Cortar la frase 'because because because'
print(texto3[:30] + texto3[54:])

# 26. Primera aparición de 'because' (Repetido)
print(texto3.find("because"))

# 27. Cortar la frase 'because...' (Repetido)
print(texto3[:30] + texto3[54:])

# 28. ¿Empieza por 'Coding'?
print(company.startswith('Coding'))

# 29. ¿Termina por 'coding'?
print(company.endswith('coding'))

# 30. Eliminar espacios sobrantes (strip)
texto_espacios = '   Coding For All      '
print(texto_espacios.strip())

# 31. Validar identificadores (isidentifier)
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier()) 
print(var2.isidentifier())

# 32. Unir lista de librerías con '# '
var3 = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" ".join(var3))

# 33. Secuencia de escape nueva línea (\n)
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Secuencia de escape tabulación (\t)
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Formateo de string (Radio/Área)
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square")

# 36. Tabla de operaciones matemáticas
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")