'''
Escribir un programa que pida al usuario un número entero y
muestre por pantalla si es un número primo o no.
'''

n = int(input("Enter a number: "))

cont = 0

for i in range(n):
    if( n % (i+1) == 0):
        cont += 1

if(cont == 2):
    print("Es primo")
else: 
    print("No es primo")