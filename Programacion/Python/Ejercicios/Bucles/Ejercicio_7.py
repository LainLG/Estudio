'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

number = int(input("Enter a number: "))

for i in range(10):
    print(f"{i+1} X {number} = {number*(i+1)}")