'''
Escribir una función que pida un número entero entre 1 y 10
lea el fichero tabla-n.txt con la tabla de multiplicar de ese
número, done n es el número introducido, y la muestre por pantalla.
Si el fichero no existe debe mostrar un mensaje por pantalla
informando de ello.
'''

import os

def Mostrar(ruta):
    if(os.path.isfile(ruta)):
        fichero = open(ruta,'r')
        print(fichero.read())
    else:
        print(f"Fichero no encontrado.")


n = int(input("Ingrese un numero: "))

ruta = "../Datos/"

ruta += "tabla-"+str(n) + ".txt"

Mostrar(ruta)