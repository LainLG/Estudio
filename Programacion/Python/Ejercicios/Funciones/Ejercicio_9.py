'''
Escribir una función que calcule el máximo común divisor
de dos números y otra que calcule el mínimo común múltiplo.
'''

def Mcd(n1,n2):
   div_n1 = list([ x for x in range(1,n1+1) if n1 % x == 0 ])
   div_n2 = list([ y for y in range(1,n2+1) if n2 % y == 0 ])
   
   return max(list(set(div_n1) & set(div_n2)))
print(Mcd(15,20))