'''
Escribir una función que reciba una frase y devuelva un
diccionario con las palabras que contiene y su longitud.
'''

def Diccionario(frase):
    return {palabra :len(palabra) for palabra in list(frase.split())}


frase = "Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."

print(Diccionario(frase))