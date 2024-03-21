while True:
    try:
        digito1 = float(input(f"Ingrese el primer digito: "))
        digito2 = float(input(f"ingrese el segundo digito: "))
        operacion = input(f"Ingrese la operacion que desea realizar (+, -, /, *): ")

        if operacion not in ["+", "-", "/", "*"]:
            raise Exception("Error al seleccionar la operacion.")
        else:
            if operacion == "+":
                print(f"La suma entre {digito1} y {digito2} es = {digito1 + digito2}" )

            elif operacion == "-":
                print(f"La resta entre {digito1} y {digito2} es = {digito1 - digito2}")

            elif operacion == "/":
                if digito2 == 0:
                    raise ZeroDivisionError("No se puede dividir entre cero.")
                else:
                    print(f"La division entre {digito1} y {digito2} es = {digito1 / digito2}")

            elif operacion == "*":
                print(f"La multiplicacion entre {digito1} y {digito2} es = {digito1 * digito2}")

    except Exception as error:
        print(error)