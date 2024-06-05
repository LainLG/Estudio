'''
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''

number = int(input("Enter a number integer positive: "))

while(number != -1):
    print(number)
    number -= 1