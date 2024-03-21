from datetime import datetime

fecha = datetime.now()

diaNacimiento = int(input("Ingrese su día de nacimiento: "))
mesNacimiento = int(input("Ingrese su mes de nacimiento: "))
añoNacimiento = int(input("Ingrese su año de nacimiento: "))

fechaNacimiento = datetime(añoNacimiento, mesNacimiento, diaNacimiento)

if (fecha.month, fecha.day) < (mesNacimiento, fechaNacimiento):
    diferenciaAños = fecha.year - fechaNacimiento.year - 1
else:
    diferenciaAños = fecha.year - fechaNacimiento.year

print(f"Usted tiene {diferenciaAños} años.")