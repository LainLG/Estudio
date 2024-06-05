'''
Escribir un programa que pida al usuario una palabra y
muestre por pantalla el número de veces que contiene cada vocal.
'''

palabra = input("Ingrese una palabra: ")

palabra = palabra.lower()

cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

vocales = ['a' ,'e','i','o','u']

for i in range(len(palabra)):
    if(palabra[i] == 'a' ):
        cont_a +=1
    elif(palabra[i] == 'e' ):
        cont_e +=1
    elif(palabra[i] == 'i' ):
        cont_i +=1
    elif(palabra[i] == 'o' ):
        cont_o +=1
    elif(palabra[i] == 'u' ):
        cont_u +=1

lista = [ cont_a,cont_e,cont_i,cont_o,cont_u]

for j in range(len(lista)):
    print(f"La vocal: {vocales[j]} sale : {lista[j]}")