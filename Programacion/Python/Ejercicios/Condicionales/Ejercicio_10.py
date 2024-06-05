'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas 
a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no
, y en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede eligir un ingrediente además de la mozzarella y
el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si
la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

type_pizza = input("Do you want a vegetarian pizza or not?: ").lower()

if(type_pizza[0] == 'y'):
    print("Ingredientes:")
    print("1. Pimiento")
    print("2. Tofu")
elif(type_pizza[0] == 'n'):
    print("Ingredientes:")
    print("1. Peperoni")
    print("2. Jamon")
    print("3. Salmon")