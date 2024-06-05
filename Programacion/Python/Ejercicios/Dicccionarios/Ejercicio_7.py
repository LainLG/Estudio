'''
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la
lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
'''
cesta = {}
condiccion = True

while(condiccion != False):
    producto = input("Ingrese su producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cesta[producto] = precio
    condiccion = int(input("Ingrese 1 para continuar: "))


print("Lista de la compra")
for i in range(len(cesta)):
    print(f"{list(cesta.keys())[i]} precio: {cesta[list(cesta.keys())[i]]}")

print(f"Total Coste: {sum(cesta.values())}")