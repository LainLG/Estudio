'''
Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde
1 hasta ese número separados por comas.
'''
number = int(input("Enter a number integer positive: "))

for i in range(number):
    if( (i+1) % 2 != 0):
        print(i+1)