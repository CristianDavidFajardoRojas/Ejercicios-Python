numero1 = int(input(f"Escriba el numerador: "))
numero2 = int(input(f"Escriba el denominador: "))

cociente = numero1 / numero2
resto = numero1 % numero2

if resto == 0:
    print(f"""La division es exacta.
          Cociente = {int(cociente)}.
          resto = {resto}""")
else:
    print(f"""La division NO es exacta.
          Cociente = {int(cociente)}.
          resto = {resto}""")
