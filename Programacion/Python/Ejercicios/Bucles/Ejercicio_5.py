'''
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el
capital obtenido en la inversión cada año que dura la inversión.
'''

years = int(input("Enter the number of years to invest: "))
cash = float(input("Enter the cash to invest: "))
interest = float(input("Enter to interest: "))
capital = 0
for i in range(years):
    capital += cash*interest
    print("Capital:",capital,"Años invertidos:",(i+1))