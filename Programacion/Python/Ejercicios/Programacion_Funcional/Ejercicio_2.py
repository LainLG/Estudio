'''
Escribir una función que reciba otra función y una lista,
y devuelva otra lista con el resultado de aplicar la
función dada a cada uno de los elementos de la lista.

'''

def Cuadrada(n):
    return n**2

def Devuelve(Cuadrada,lista):
    return [Cuadrada(x) for x in lista]

lista = list(range(10))

print(Devuelve(Cuadrada,lista))