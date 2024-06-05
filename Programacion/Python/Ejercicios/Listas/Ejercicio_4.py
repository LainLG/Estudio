'''
Escribir un programa que almacene en una lista los números
del 1 al 10 y los muestre por pantalla en orden inverso separados por comas
'''
lista = []

for i in range(10):
    lista.append(i+1)


condicicion = len(lista)-1

cadena = ""

while(condicicion != -1):
    if(condicicion != 0):
        cadena += str(lista[condicicion]) +","
    else:
        cadena +=str(lista[condicicion])
    condicicion -=1

print(cadena)