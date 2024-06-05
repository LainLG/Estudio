
'''
Escribir una función que simule una calculadora científica que permita
calcular el seno, coseno, tangente, exponencial y logaritmo neperiano.
La función preguntará al usuario el valor y la función a aplicar, y mostrará
por pantalla una tabla con los enteros de 1 al valor introducido y 
el resultado de aplicar la función a esos enteros.
'''
import math as mt

def Seno(numero):
    return mt.sin(numero)

def Coseno(numero):
    return mt.cos(numero)

def Tangente(numero):
    return mt.tan(numero)

def Exponecial(numero):
    return mt.exp(numero)

def Log(numero):
    return mt.log(numero)


numero = int(input("Ingrese un numero: "))
Funcion = input("Ingrese el nombre de la funcion: ").lower()

numero = list(range(1,numero+1))

if(Funcion == "sen"):
    print(list(map(Seno,numero)))
elif(Funcion == "cos"):
    print(list(map(Coseno,numero)))
elif(Funcion == "tan"):
    print(list(map(Tangente,numero)))
elif(Funcion == "exp"):
    print(list(map(Exponecial,numero)))
elif(Funcion == "ln"):
   print(list(map(Log,numero)))
else:
    print(f"Funcion {Funcion} no encontrada.")