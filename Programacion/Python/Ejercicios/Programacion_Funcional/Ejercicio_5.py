'''
Escribir una función que reciba un diccionario con las asignaturas y 
las notas de un alumno y devuelva otro diccionario con las 
asignaturas en mayúsculas y las calificaciones correspondientes
a las notas.
'''

def Notas(dic):
     
    notas = list(dic.values())
    calificacion = []
    new = {}
    for i in range(len(notas)):
        if(notas[i]>=3.0):
            calificacion.append("Aprobado")
        else:
            calificacion.append("Reprobado")

    for j in range(len(notas)):
        new[list(dic.keys())[j].upper()] = calificacion[j]

    return new

dic = {
    'Calculo 1':3.2,
    'algebra lineal':1.6,
    'Programacion':3.7,
    'Fisica':2.5
}

print(Notas(dic))