'''
Escribir una función que
reciba un número entero positivo y devuelva su factorial.
'''

def factorial(n):
    if(n == 0):
        return 1
    else:
        return n*factorial(n-1)


n = int(input("Ingrese un numero: "))

print(f"El factorial de : {n} es : {factorial(n)}")