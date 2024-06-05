'''
Escribir un programa que pregunte al usuario su edad
y muestre por pantalla si es mayor de edad o no.
'''

age = None

age = int(input("Enter your age: "))

if(age >= 0):
    if(age >= 18):
        print("You is adult")
    else:
      print("You isn´t adult")  
else:
    print("the enter age is incorret the age not can negative")