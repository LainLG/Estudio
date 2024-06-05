'''
Los tramos impositivos para la declaración de la renta en un determinado
país son los siguientes:

Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 20000€ y 35000€	20%
Entre 35000€ y 60000€	30%
Más de 60000€	45%

Escribir un programa que pregunte al usuario su renta anual y 
muestre por pantalla el tipo impositivo que le corresponde.

'''

income = float(input("ENter your economic income: "))

if(income >= 0):
    if(income < 10000):
        print("5%")
    elif(income >= 10000 and income < 20000):
        print("15%")
    elif(income >= 20000 and income < 35000):
        print("20%")
    elif(income >= 35000 and income < 65000):
        print("30%")
    else:
        print("45%")
else:
    print("Enter your economic income correct")