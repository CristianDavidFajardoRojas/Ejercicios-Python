def triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return "El triángulo es inválido"
    elif a == b == c:
        return "El triángulo es equilátero"
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles"
    else:
        return "El triángulo es escaleno"

a = float(input("Ingrese la longitud del primer lado del triángulo: "))
b = float(input("Ingrese la longitud del segundo lado del triángulo: "))
c = float(input("Ingrese la longitud del tercer lado del triángulo: "))

resultado = triangulo(a, b, c)
print(resultado)