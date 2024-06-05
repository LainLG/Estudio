'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas
que el usuario tiene que repetir
'''

lista = ['Matematicas','Fisica','Quimica','Historia','Lengua']
notas = []

for i in range(len(lista)):
    print(f"Ingrese la nota de {lista[i]}")
    nota = float(input(": "))
    notas.append(nota)

materias_apro = []

for k in range(len(lista)):
    if( notas[k] >= 3.0 ):
        materias_apro.append(lista[k])



for j in range(len(materias_apro)):
    lista.remove(materias_apro[j])

print(lista)