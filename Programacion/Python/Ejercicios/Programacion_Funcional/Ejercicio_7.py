

import random

def Atipicos(lista):
    media = sum(lista)/len(lista)
    desv_est = pow(sum([ (x -media)**2 for x in lista])/len(lista),1/2)
    return [ n for n in lista if ((n - media)/desv_est > 3) or ((n - media)/desv_est < -3)]

lista = [ random.randint(1,800) for i in range(0,50)]
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]

print(lista)
print("\n")
print(sum(lista)/len(lista))

print(pow(sum([ (x -sum(lista)/len(lista))**2 for x in lista])/len(lista),1/2))

print(Atipicos(lista))