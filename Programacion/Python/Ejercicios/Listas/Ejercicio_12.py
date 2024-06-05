'''
Escribir un programa que pregunte por una muestra de
números, separados por comas, los guarde en una lista y
muestre por pantalla su media y desviación típica.
'''

datos =  input("Ingrese los datos: ")

datos = datos.split(",")

for i in range(len(datos)):
    datos[i] = float(datos[i])

media = sum(datos)/len(datos)

suma = 0 

for i in range(len(datos)):
    suma +=(datos[i] - media)**2

desv_est = pow(suma/(len(datos)-1),1/2)

print(f"Media: {media}")
print(f"Desviasion estandar: {desv_est}")