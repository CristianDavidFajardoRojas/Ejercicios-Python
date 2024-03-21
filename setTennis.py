def verificar_ganador(m, n):
    if abs(m - n) >= 2 and (m < 6 or n < 6):
        return "Invalido"
    elif m >= 6 and m - n >= 2:
        return "Gano A"
    elif n >= 6 and n - m >= 2:
        return "Gano B"
    elif m == 6 and n == 6:
        return "Aun no termina"
    elif m == 5 and n == 5:
        return "Aun no termina"
    else:
        return "Aun no termina"
juegosA = int(input("Ingrese los juegos ganados por el jugador A: "))
juegosB = int(input("Ingrese los juegos ganados por el jugador B: "))

resultado = verificar_ganador(juegosA, juegosB)
print("Resultado:", resultado)