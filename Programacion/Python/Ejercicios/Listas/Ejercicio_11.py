
'''
Escribir un programa que almacene las matrices
 
 

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas
usar listas anidadas, representando cada vector fila en una lista.

'''

A = [ [1,2,3],
      [4,5,6]]

B = [ [-1,0],
      [ 0,1],
      [ 1,1]]

lista1 = []
lista2 = []
suma = 0
for i in range(2):
    for j in range(2):
        for k in range(3):
            suma += A[i][k]*B[k][j]
        lista1.append(suma)
        suma = 0
    lista2.append(lista1)
    lista1 =[]

print(lista2)
    