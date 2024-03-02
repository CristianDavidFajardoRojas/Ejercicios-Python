import math

M_pequeno = 47  
M_grande = 67   
rho = 1.038     
c = 3.7         
K = 5.4 * 10 ** (-3)  
Tw = 100

grande = input(f"El huevo es grande? ( Si / No ): ").lower
if grande == "si":
    M = M_grande
    To = float(input(f"Escriba la temperatura original del huevo en grados Celsius: "))
    t = (M**(2/3) * c * rho**(1/3)) / (K * 3.1416**2) * (4 * 3.1416 / 3)**(2/3) * math.log(0.76 * (To - Tw) / (70 - Tw))
else:
    M = M_pequeno
    To = float(input(f"Escriba la temperatura original del huevo en grados Celsius: "))
    t = (M**(2/3) * c * rho**(1/3)) / (K * 3.1416**2) * (4 * 3.1416 / 3)**(2/3) * math.log(0.76 * (To - Tw) / (70 - Tw))

print(f"El tiempo necesario para preparar el huevo a la copa es de aproximadamente {t:.2f} segundos.")
