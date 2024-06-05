'''
Escribir un programa que pida al usuario un número entero 
y muestre por pantalla si es par o impar.
'''

number = int(input("Enter a number: "))

if(number % 2 == 0):
    print("The number enter is even:",number)
else:
    print("The number enter is odd:",number)

