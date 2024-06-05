'''
Escribir una función que convierta un número decimal en binario
y otra que convierta un número binario en decimal.
'''

def Decimal(Numero):
    Numero = Numero[::-1]
    binary = []
    decimal = 0
    for i in range(len(Numero)):
        binary.append(int(Numero[i]))
    for j in range(len(binary)):
        decimal += binary[j]*(2**j)
    return decimal

def Binario(Numero):
    binary = ""
    while(Numero != 0):
        if( Numero // 2 != 0):
            binary += str(Numero % 2)
            Numero = Numero // 2
        else:
            binary += "1"
            return binary[::-1]


Numero = input("Ingrese un numero: ")
decimal = Decimal(Numero)

print(f"El valor decimal de {Numero} es: {Decimal(Numero)}")
print(Binario(decimal))