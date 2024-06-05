'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura, y después las muestre por pantalla con el mensaje
En <asignatura> has sacado <nota> donde <asignatura> es cada
una des las asignaturas de la lista y <nota> cada una de las
correspondientes notas introducidas por el usuario.
'''

Materias = ['ANALISIS NUMERICO','PENSAMIENTO SISTEMICO Y ORGANIZACIONAL','SISTEMAS DE INFORMACION'	,'REDES DE COMPUTADORES II'	,'INTELIGENCIA ARTIFICIAL','AJEDREZ']
Notas = []
for i in range(len(Materias)):
    print(f"NOTA DE {Materias[i]}")
    nota = float(input("Ingrese:"))
    Notas.append(nota)

for j in range(len(Materias)):
    print(f"En {Materias[j].lower()} has sacado {Notas[j]}")