'''
Escribir una función que reciba otra función booleana y una lista,
y devuelva otra lista con los elementos de la lista que devuelvan
True al aplicarles la función booleana.
'''

import random

def Mayor(edad):
    if( edad >= 18):
        return True
    else: 
        return False

def Devuelve(Mayor, lista):
    return [Mayor(edad) for edad in lista]
 
    

lista =   [random.randint(0, 60) for x in range(30)]

print(lista)
print(Devuelve(Mayor,lista))