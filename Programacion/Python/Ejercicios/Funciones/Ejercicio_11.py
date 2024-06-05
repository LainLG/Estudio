'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el
diccionario generado con la función anterior y devuelva una tupla con la palabra
más repetida y su frecuencia.
'''

def funcion(datos):
    datos = list(datos.split())
    datos_unicos = list(set(datos))
    cantidad = list([ datos.count(x) for x in datos_unicos])
    dic_frec = {}
    for i in range(len(cantidad)):
        dic_frec[datos_unicos[i]] = cantidad[i] 
    return dic_frec

def funcion2(datos):
    valor = max(datos.values())
    indice = list(datos.values()).index(valor)
    clave = list(datos.keys())[indice]
    return (clave,valor)


datos = "Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia."

diccionario = funcion(datos)

print(diccionario)
print("\n")
print(funcion2(diccionario))