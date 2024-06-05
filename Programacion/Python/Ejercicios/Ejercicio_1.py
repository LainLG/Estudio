'''
print("Hello World !!!")

print(1,2,3,4,5)
print(1,2,3,4,5,sep=',')

print(1,2,3,4,5, sep=',',end='.')

print()

name = input("hello what is your name: ")

print('nice too meet you',name)

'''

def datos(n1,n2):
    suma = n1 + n2 
    resta = n1 - n2
    multi = n1*n2
    division = n1 /n2

    print("El resultado de la suma es:", suma)
    print("El resultado de la resta es:",resta)
    print("El resultado de la multiplicacion es:" ,multi)
    print("El resultado de la division es:" ,division)



n1 = int(input("Ingrese el primer sumando: "))
n2 = int(input("Ingrese el segundo sumando: "))

datos(n1,n2)

n1 = float(input("Ingrese el primer sumando: "))
n2 = float(input("Ingrese el segundo sumando: "))

datos(n1,n2)

# Funcion round redondea desimales ejemplo

div = n1/n2

print("Division redondeada a dos digitos:",round(div,2))