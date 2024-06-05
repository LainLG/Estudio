'''
Escribir un programa que almacene en una lista los siguientes precios
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor
y el mayor de los precios.
'''

precios = [ 50,75,46,22,80,65,8]

suma = 0

for i in range(len(precios)):
    suma += precios[i]

media = suma/len(precios)

for i in range(len(precios)):
    if(media < precios[i]):
        media = precios[i]

maximo = media

media = suma/len(precios)

for i in range(len(precios)):
    if(media > precios[i]):
        media = precios[i]

minimo = media

print(f"El minimo es: {minimo}")
print(f"EL maximo es: {maximo}")