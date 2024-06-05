'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física,
Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje
Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
'''

Materias = ['ANALISIS NUMERICO','PENSAMIENTO SISTEMICO Y ORGANIZACIONAL','SISTEMAS DE INFORMACION'	,'REDES DE COMPUTADORES II'	,'INTELIGENCIA ARTIFICIAL','AJEDREZ']

for i in range(len(Materias)):
    print(f"Yo estudio: {Materias[i]}")