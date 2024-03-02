nota1 = int(input(f"Escriba la nota del certamen 1:  "))
nota2 = int(input(f"Escriba la nota del certamen 2: "))
laboratorio = float(input(f"Escriba el promedio de laboratorio: "))

nc = ( 60 - (laboratorio * 0.3 )) / ( 0.7 )
nota3 = 3 * nc - nota1 - nota2

print(f"Necesitas {nota3} de nota en el certamen 3.")