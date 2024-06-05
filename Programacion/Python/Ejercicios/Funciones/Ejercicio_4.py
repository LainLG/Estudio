'''
Escribir una función que calcule el total de una factura tras
aplicarle el IVA. La función debe recibir la cantidad sin IVA
y el porcentaje de IVA a aplicar, y devolver el total de la factura.
Si se invoca la función sin pasarle el porcentaje de IVA, deberá
aplicar un 21%.
'''

def Aplica(precio,iva = 0.21):
     return precio*iva + precio


valor = float(input("Ingrese el valor a pagar: "))
iva = float(input("Ingrese el valor del iva: "))

print(f"Valor a pagar: {Aplica(valor,iva)}")