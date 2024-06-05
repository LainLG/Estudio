'''
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un
diccionario con las palabras y sus traducciones. Después pedirá una frase en español
y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está
en el diccionario debe dejarla sin traducir.
'''

traslate = {}

condiccion = 1

while(condiccion != 0):
    palabra = input("Ingrese la palabra a agregar: ").split(':')
    traslate[palabra[0]] = palabra[1]
    condiccion =  int(input("Ingrese 0 para Salir: "))

frase = input("Ingrese una frase a traducir: ").split()

frase_traducida = ""
for i in range(len(frase)):
    if(frase[i] in traslate):    
        frase_traducida += traslate[frase[i]] +" "
    else:
        frase_traducida += frase[i] + " "

print(frase_traducida)