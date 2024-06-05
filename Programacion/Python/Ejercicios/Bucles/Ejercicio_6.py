'''
Escribir un programa que pida al usuario un número entero y
muestre por pantalla un triángulo rectángulo como el de más abajo,
de altura el número introducido.
'''
number = int(input("Enter your number: "))

for i in range(number):
    start = '*'
    print(start*(i+1))