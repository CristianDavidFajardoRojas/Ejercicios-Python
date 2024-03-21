while True:
    variable = input(f"Ingrese una tecla: ")
    if variable.isdigit():
        print(f"{variable} es un numero")
    elif variable.isalpha():
        if variable.isupper():
            print(f"{variable} es una letra mayúscula")
        else:
            print(f"{variable} es una letra minúscula")
    else:
        print(f"{variable} no es un numero ni una letra")

