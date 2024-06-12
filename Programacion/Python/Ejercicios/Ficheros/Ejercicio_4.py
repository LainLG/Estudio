
'''
Escribir un programa que acceda a un fichero de internet
mediante su url y muestre por pantalla el número de palabras
que contiene.
'''

from urllib import request

f = request.urlopen('https://drive.google.com/file/d/1XD0dgzOqSrun-i3L3K8ye8sOQrA27UR-/view?usp=sharing')
datos = f.read()
print(datos.decode())