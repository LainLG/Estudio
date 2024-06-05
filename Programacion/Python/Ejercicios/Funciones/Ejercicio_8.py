'''
Escribir una función que reciba una muestra de números
en una lista y devuelva un diccionario con su
media, varianza y desviación típica.
'''

def Estadistica(muestra):
    
    media = sum(muestra)/len(muestra)
    var = sum(list([(x -media)**2 for x in muestra]))/(len(muestra)-1)
    desv_est = pow(var,1/2)
    keys = ['media','varianza','desviazion estandar']
    values = [media, var, desv_est]
    dic_estadistica = {}
    for i in range(len(keys)):
        dic_estadistica[keys[i]] = values[i]
    return dic_estadistica


muestra = list(range(1,11))

print(Estadistica(muestra))