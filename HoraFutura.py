hora = int(input(f"Escriba la hora actual sin minutos: "))
horasextra = int(input(f"Escriba un numero entero de horas que desea agregar: "))
HoraFutura = ( hora + horasextra ) % 24
if HoraFutura < 12:
    print(f"la hora despues de {horasextra} horas extra sera: {HoraFutura}am")
elif HoraFutura == 12:
     print(f"la hora despues de {horasextra} horas extra sera: {HoraFutura}pm")
else:
    print(f"la hora despues de {horasextra} horas extra sera: {HoraFutura - 12}pm")
    
