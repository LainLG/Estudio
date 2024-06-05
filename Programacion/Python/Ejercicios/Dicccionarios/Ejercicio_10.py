'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos del cliente
(nombre, dirección, teléfono, correo, preferente),
donde preferente tendrá el valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente,
(2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
(5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa
tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
'''

base_datos = {}
datos = ['nombre', 'direccion', 'telefono', 'correo', 'preferente']
suma = 0
condicion = None
while(condicion != 0 ):
    print('''
    1) Ingrese 1 para ingresar un cliente
    2) Ingrese 2 para eliminar un cliente
    3) Ingrese 3 para ver los datos del cliente
    4) Ingrese 4 para ver los cientes con su NIF y nombre.
    5) Ingrese 5 para ver los cientes preferentes.
    6) Ingrese 0 para salir
''')
    condicion = int(input("Ingrese: "))
    if(condicion == 1):
        datos_user = {}
        Nif = input("Ingrese el nif del cliente: ")
        for i in range(len(datos)):
            print(f"Ingrese el {datos[i]}")
            info = input("Ingrese: ")
            datos_user[datos[i]] = info.lower()
        base_datos[Nif] = datos_user
        
    elif(condicion == 2):
        Nif = input("Ingrese el nif a eliminar: ")
        delete = base_datos.pop(Nif,False)
        if(delete != False):
            print(f"{Nif} eliminado") 
        else:
            print(f"CLiente {Nif} no encontrado")

    elif(condicion == 3):
        Nif = input("Ingrese el nif del cliente: ")
        if(Nif in base_datos):
            user = dict(base_datos[Nif])
            datos_usuario = list(user.values())
            print(f"Datos del cliente: {Nif}")
            for i in range(len(datos_usuario)):
                print(f"{datos[i]} es : {datos_usuario[i]}")
    elif(condicion == 4):
        nifs = list(base_datos.keys())
        for i in range(len(nifs)):
           usuario = base_datos[nifs[i]]
           name = usuario['nombre']
           print(f"El cliente {name} identificado con el nif: {nifs[i]}")
    elif(condicion == 5):
        nifs = list(base_datos.keys())
        for i in range(len(nifs)):
           usuario = dict(base_datos[nifs[i]])
           if(usuario['preferente'] == "true"):
                print(f"El cliente {usuario['nombre']} identificado con el nif: {nifs[i]}")
