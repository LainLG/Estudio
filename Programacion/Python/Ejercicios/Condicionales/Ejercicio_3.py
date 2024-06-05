'''
Escribir un programa que pida al usuario dos números y muestre 
por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

if( n2 == 0):
    print("impossible error dividing a number by zero")
else:
    div = n1/n2
    print("The result is:",div)