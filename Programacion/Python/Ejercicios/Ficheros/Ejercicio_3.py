'''
Escribir una función que pida dos números n y m entre 1 y 10
lea el fichero tabla-n.txt con la tabla de multiplicar de ese
número, y muestre por pantalla la línea m del fichero.
Si el fichero no existe debe mostrar un mensaje por pantalla
informando de ello.
'''

import os


def Mostrar(ruta,m):
    fichero = open(ruta,'r')
    if(os.path.isfile(ruta)):
        return print(list(fichero.readlines())[m-1])
    else:
        return print("fichero no encontrado")


n = int(input("Ingrese un numero: "))
m = int(input("Ingrese un numero: "))

ruta = "../Datos/"

ruta += "tabla-"+str(n) + ".txt"

Mostrar(ruta,m)