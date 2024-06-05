'''
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones
múltiplos de 3, y muestre por pantalla la lista resultante.
'''
abecedareo = []

for i in range(97,123):
    abecedareo.append(chr(i))

ind_multi = []

for j in range(len(abecedareo)):
    if( j % 3 == 0):
        ind_multi.append(abecedareo[j])

for k in range(len(ind_multi)):
    abecedareo.remove(ind_multi[k])

print(abecedareo)