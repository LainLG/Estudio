'''
Escribir un programa que pregunte al usuario su nombre, edad, dirección
y teléfono y lo guarde en un diccionario. Después debe mostrar por
pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección>
y su número de teléfono es <teléfono>.
'''

lista = ['nombre','edad','dirección','telefono']

d = {}


for i in range(len(lista)):
    print(f"Ingrese su {lista[i]}")
    enter = input(": ")
    d[lista[i]] = enter


print(f"{d[lista[0]]} tienne {d[lista[1]]} años, vive en {d[lista[2]]} y su numero de telefono es {d[lista[3]]}")