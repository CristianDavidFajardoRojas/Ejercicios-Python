numero = float(input(f"Esacriba un numero con decimales: "))
if numero < 0:
    decimales = numero + int(abs(numero))
else:
    decimales = numero - int(numero)

print(f"Los decimales del numero son: {abs(decimales)}")
