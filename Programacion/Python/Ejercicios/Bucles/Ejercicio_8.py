'''
Escribir un programa que pida al usuario un número entero
y muestre por pantalla un triángulo rectángulo como el de más abajo.
'''

number = int(input("Enter your number: "))
cadena = " "
for i in range(number):
    if( (i+1) % 2 != 0):
        cadena += str(i+1) +" "
        print(cadena[::-1])