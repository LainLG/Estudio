'''
Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
, pregunte al usuario por una divisa y
muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''

dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Ingrese su divisa: ")

print(f"Su divisa: {dic.get(divisa,'No se encontro')}")

