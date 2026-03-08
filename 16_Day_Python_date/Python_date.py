from datetime import datetime, date, timedelta

# 1. Obtén el día actual, mes, año, hora, minuto y el timestamp (marca de tiempo) usando el módulo datetime.
now = datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
timetamp = now.timetuple()
print(timetamp)

# 2. Formatea la fecha actual usando este formato: "%m/%d/%Y, %H:%M:%S"
formato = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formato)

# 3. Hoy es 5 de Diciembre de 2019. 
fecha_string = "5 December, 2019"
fecha = datetime.strptime(fecha_string, "%d %B, %Y")
print(fecha)

# 4. Calcula la diferencia de tiempo entre ahora y el día de Año Nuevo (1 de Enero del año que viene).
# Pista: Crea un objeto date para hoy y otro para el 1 de enero del año que viene, y réstalos.
f1 = datetime.now()
f2 = datetime(year=f1.year + 1, month=1, day=1)
f3 = f2 - f1
print(f3)

# 5. Calcula la diferencia de tiempo entre el 1 de Enero de 1970 y ahora.
fecha1970 = datetime(year=1970, month=1, day=1)
print(f1 - fecha1970) 