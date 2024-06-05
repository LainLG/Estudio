'''
Escribir un programa que gestione las facturas pendientes
de cobro de una empresa. Las facturas se almacenarán en un
diccionario donde la clave de cada factura será el número
de factura y el valor el coste de la factura. El programa
debe preguntar al usuario si quiere añadir una nueva factura,
pagar una existente o terminar. Si desea añadir una nueva factura
se preguntará por el número de factura y su coste y se añadirá al
diccionario. Si se desea pagar una factura se preguntará por el
número de factura y se eliminará del diccionario. Después de cada
operación el programa debe mostrar por pantalla la cantidad cobrada
hasta el momento y la cantidad pendiente de cobro.
'''

sistema = {}
suma = 0
condicion = None
while(condicion != 0 ):
    print('''
    1) Ingrese 1 para ingresar una factura.
    2) Ingrese 2 para pagar una factura.
    3) Ingrese 0 para salir.
''')
    condicion = int(input("Ingrese: "))
    if(condicion == 1):
        factura = input("Ingrese el nombre de la factura: ")
        valor = float(input("Ingrese el valor de la factura: "))
        sistema[factura] = valor
    elif(condicion == 2):
        factura = input("Ingrese el nombre de la factura: ")
        cobro = sistema.pop(factura,False)
        if(cobro != False):
            suma += cobro 
        else:
            print(f"Factura no encontrada")

    print(f"Valor pendiente a pago: {sum(sistema.values())}")
    print(f"Cantidad cobrada: {suma}")