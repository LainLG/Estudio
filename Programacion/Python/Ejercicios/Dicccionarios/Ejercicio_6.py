'''
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el
contenido del diccionario.
'''
lista = ['nombre', 'edad', 'genero', 'telefono', 'correo']

datos = {}

for i in range(len(lista)):
    print(f"Ingrese su: {lista[i]}")
    info = input(": ")
    datos[lista[i]] = info
    print(datos)