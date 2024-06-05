'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

data = input("Enter your password: ").lower()

password = "password"

if(password == data):
    print("Your password is correct")
else:
    print("Your password isn´t correct")