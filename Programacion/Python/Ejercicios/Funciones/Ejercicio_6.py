'''
Escribir una función que reciba una muestra de
números en una lista y devuelva su media.
'''
def Media(lista):
    return sum(lista)/len(lista)


a = list(range(1,11))

print(f"La media es: {Media(a)}")

