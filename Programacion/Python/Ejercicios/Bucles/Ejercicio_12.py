'''
Escribir un programa en el que se pregunte al usuario
por una frase y una letra, y muestre por pantalla el
número de veces que aparece la letra en la frase.
'''

letra = input("Ingrese una letra: ")
palabra = input("Ingrese una palabra: ")
cont = 0
for i in palabra:
    if( i == letra):
        cont += 1


print("La letra:",letra,"Aparece:",cont)