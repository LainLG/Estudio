
'''
Escribir una función que calcule el módulo de un vector.
'''

def Modulo(vector):
    return pow(sum([ v**2 for v in vector]),1/2)


vector = [4 ,6,3]

print(Modulo(vector))