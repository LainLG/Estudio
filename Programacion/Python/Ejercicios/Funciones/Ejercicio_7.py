'''
Escribir una función que reciba una muestra de
números en una lista y devuelva otra lista con sus cuadrados.
'''

def Cuadrados(numeros):
    return [ x**2 for x in numeros]


numeros = list(range(1,11))

print(f"Lista al cuadrado : {Cuadrados(numeros)}")

