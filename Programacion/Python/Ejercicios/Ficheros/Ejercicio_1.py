'''
Escribir una función que pida un número entero entre
1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla
de multiplicar de ese número, done n es el número introducido.
'''


def Write(ruta,n):
    tabla = open(ruta,'w')
    for i in range(10):
        cadena =  str(i+1) +" X " + str(n) + " = " + str((i+1)*n)+"\n" 
        tabla.write(cadena)
    return tabla




ruta = "../Datos/"


n = int(input("Ingrese un numero: "))

ruta += "tabla-"+str(n) + ".txt"


Write(ruta,n)

fichero = open(ruta,'r')
print(fichero.read())
lineas = print(fichero.readlines())
print(lineas)

fichero.close()