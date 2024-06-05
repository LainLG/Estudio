'''
Escribir una función que calcule
el área de un círculo y otra que calcule
el volumen de un cilindro usando la primera función.
'''


def area_circulo(r):
    PI = 3.1416
    return 2*PI*(r**2)

def vol_cilindro(are_circulo,r, h):
    return area_circulo(r)*h


radio = float(input("Ingrese el radio: "))
altura = float(input("Ingrese la altura: "))

circulo = area_circulo(radio)
cilindro = vol_cilindro(area_circulo,radio,altura)

print(f"El area del ciculo es: {circulo}")
print(f"El volumen del cilindro es: {cilindro}")