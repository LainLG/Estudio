'''
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar.
'''
vec1 = [1,2,3]
vec2 = [-1,0,2]

pro_esc = 0

for i in range(len(vec1)):
        pro_esc += vec1[i]*vec2[i]

print(f"El producto escalar es: {pro_esc}")