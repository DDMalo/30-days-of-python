# Dia 3 - Operators

# 1,2,3.Variables basicas
edad = 20
altura = 1.68
imaginario = 1 + 1j

# 4.Area triangulo
alturat = float(input("La altura del triangulo es: "))
baset = float(input("La base del triangulo es: "))
print(f"El area del triangulo es de: {0.5 * alturat * baset}")

# 5.Perimetro
a = float(input("El lado a del triangulo es: "))
b = float(input("El lado b del triangulo es: "))
c = float(input("El lado c del triangulo es: "))
print(f"El perimetro del triangulo es de: {a + b + c}")

# 6.Area y perimetro cuadrado
a1 = float(input("El lado a del cuadrado es: "))
b1 = float(input("El lado b del cuadrado es: "))
print(f"El area del cuadrado es: {a * b}")
print(f"El perimetro del cuadrado es: {2*(a + b)}")

# 7.Circulo
r = float(input("Radio circunferencia: "))
pi = 3.14
print(f"Area: {pi * r * r} Circumference: {2 * pi * r}")

# 8.Ecuacion
pendiente = 2
y_interseccion = -2
x_interseccion = 1  # 0 = 2x - 2 -> 2 = 2x -> x = 1
print(f"Pendiente: {pendiente}, Y-interseccion: {y_interseccion}, X-interseccion: {x_interseccion}")

# 9.Ecuaccion 2
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente1 = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Slope: {pendiente1}, Distance: {distancia}")

# 10.
print(f"La pendiente de ambos ejercicios son iguales? {pendiente == pendiente1} ")

# 11.Valor de "y" para y = x^2 + 6x + 9
for x in [-3, -2, 0, 1]:
    y = x**2 + 6*x + 9
    print(f"Cuando x es {x}, y es {y}")

# 12.Longitud de "python" y "dragon" y comparacion falsa
print(f"Son las palabras 'python' y 'dragon' de diferente logitud? {len("python") != len("dragon")}")

# 13. Opereador AND
print("on" in "python" and "on" in "dragon")

# 14. "Jargon"
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

# 15. Negacion
print(not("on" in "python" and "on" in "dragon"))

# 16. Conversion valores
longitud_py = len("python")
float_len = float(longitud_py)
str_len = str(float_len)

# 17. Par
num = 10
print(f"Apartado 17: {num%2==0}")

# 18.
print(f"Apartado 18: {7 // 3 == int(2.7)}")

# 19. '10' igual que 10?
print(f"Apartado 19: {type('10') == type(10)}")

# 20. int(9.8) == 10?
print(f"Apartado 20: {int(9.8) == 10}")

# 21. Salario
horas = int(input("Horas trabajadas: "))
s_hora= int(input("Cuanto cobras por hora?: "))
print(f"Salario: {horas * s_hora}")

# 22. Segundos de vida
anio= int(input("Introduce los años de vida: "))
print(f"Tu has vivido por: {anio * 365 * 24 * 60 * 60} segundos")

# 23. Tabla
for i in range(1, 6):
    print(f"{i} 1 {i} {i**2} {i**3}")

