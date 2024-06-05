'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al 
usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

gender = input("Enter your gender: ").lower()
name = input("Enter your name: ").lower()

if( (gender[0] == 'f' and (ord(name[0]) >= 97 and  ord(name[0]) < 109)) or (gender[0] == 'm' and (ord(name[0]) > 110 and  ord(name[0]) <= 122))):
    print("You is the group A")
else:
    print("You is the group B")

