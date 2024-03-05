palabra1 = input(f"Escriba una palabra: ")
palabra2 = input(f"Escriba una segunda palabra: ")

letrasP1 = len(palabra1)
letrasP2 = len(palabra2)

if letrasP1 > letrasP2:
    print(f"La primera palabra es mas larga por {letrasP1 - letrasP2} letra(s).")
else:
    print(f"La segunda palabra es mas larga por {letrasP2 - letrasP1} letra(s).")