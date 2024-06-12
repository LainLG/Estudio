<h2> Fundamentos </h2>

* ¿ Que es un programa?

Un programa es un conjunto de instrucciones o pasos a seguir que se le dan a un ordenador de forma secuencial para que realice una tarea especifica.

EL flujo normal de un programa es el siguiente:

1. El programa recibe datos de entrada, normalmente introducidos por los usuarios de éste.
2. Ejecuta las intrucciones especificas por el programador.
3. El programa obtiene como resultado un conjunto de datos de salida.

![](vx_images/266351790846397.png)


<h3> Manejo de mansajes por pantalla </h3>

En python hay dos comandos (funciones implementadas) que permiten la interacion del usuario con el programa estos son  <strong>print y input</strong>

* Print :  el comando print permite mostrar infromacion al usuario esta informacion puede ser cadenas de caracteres, variables o las dos. El comando print tiene los siguientes partametros.
    * end: permite añadir una cadena de text como elemento final del conjunto de cadenas de texto
    * sep: permite añadir una cadena de texto al final de cada cadena enviada para mostrar por pantalla y sustituir el espacio en blanco que se introduce por defecto entre las diferentes cadenas de texto que son enviadas para mostrarse por pantalla.

* Input:  El comando input te va a permitir leer información introducida por los usuarios de la aplicacion mediante el teclado.

<h4>Variables</h4>

Las variables son datois que residen en la memoria del ordenador. Tienen las siguientes caracteristicas:

1. **Nombre:** identificador dentro del codigo fuente.
2. **Tipo:** tipo de dato que almacena la variable.
3. **Valor:**  valor que almacenan. Al declarar una variable tieens que indicarle un valor inicial, que puede verse modificado a medida que se va ejecutando el programa y según vatas necesitando, de ahí que se llamen variables.

```python
edad = 18  # tipo de dato int
nombre = "juanito" # tipo de datos string
altura = 1.75    # tipo de daton float 
```
<h3>Utilizacion de tipos de datos básicos </h3>

<h4>Tipos de datos</h4>

Las variables en Pyrhon puede ser de los siguientes tipos:

|    Tipo de dato     |                                               Descripción                                               |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| Entero                 | Número sin decimales, tanto positivo como negativo,incluyendo el 0.  |
| Real                    | Número con decimales, tanto positivo como negativo,incluyendo el 0. |
| Complejo            | Número con parte imaginaria                                                                 |
| Cadena de texto | Texto.                                                                                                      |
| Booleanos           | Puede tener dos valores: True o False                                                   |
| Conjuntos           | Coleccion de elementos no ordenados y no repetidos                           |
| Listas                  | Vector de elementos que pueden ser de diferentes tipos de datos        |
| Tuplas                 | Lista inmutable de elementos                                                                 |
| Diccionario          | Lista de elementos que contienen claves y valores.                              |

<h4>Operadores</h4>

En python existe una serie de operadores:

* Operadores de asignación.
* Operadores aritméticos.
* Operadores relacionales.
* Operadores lógicos.

<h5> Operador de asignacion </h5>

el operador de asignacion en paitos es  <strong>" = "</strong>  sirve para asignar un valor a una variable, lo que esté en la parte derecha del operador sera asignado (almacenado) en la variable de la izquierda:

```python
precio = 923
apellido = "Moreno"
numero = 34
```
<h5> Operadores aritmetricos </h5>

Los operadores aritméticos son aquellos operadores que nos van a permitir realizar operaciones aritméticas con los datos 

```python
    a = 2
    b = 4
    suma = a + b 
    resta = a - b
    division = a/b
    mutliplicacion = a*b
    potenciacion = a**b
    
```

<h5>Operadores relacionales</h5>

Los operadores relacionales son aquellos que van a permitirte realizar conparacionetes entre dos elementos :

| Operador |      Significado       |
| ------------- | ------------------------ |
| <              | Menor que             |
| >              | Mayor que             |
| <=            | Menor o igual que |
| >=            | Mayor o igual que |
| ==            | Igual que               |
| !=             | Distinto que           |

El resultado de una operacion relacional puede ser unicamente dos valores:

* **True:** La comparacion se cumple.
* **False:** La comparacion no se cumple

```python
    var1  = 7 < 5  # La variable tendre un valor booleano de False.
     var2 = 9==3  # La variable tendra un valor booleano de False.
     var3 = 2 < 12 # La variable tendra un valor booleano de True.
     var4 = 88>=4  # La variable tendra un valor booleano de True.
```

<h5> Operadores lógicos </h5>
Los operadores lógicos permiten combinar las operaciones relacionales del punto anterior o valores booleanos independientes para obtener un único resultado. 

1.  **AND:** Operador lógico que realiza la operacion lógica en la cual mientra los dos elementos sean True devuelve True en caso contrario devuelve False.
2.  **OR:** Operador lógico que realiza la operacion lógica en la cual mientras un elementos sea True devuelve True en caso contrario devuelve False.
3.  **NOT:** Operador lógico que realiza la operacion lógica la cual niega el valor si el valor era True devuelve False en caso contrario devueve True.

```python
var1 = (5<3) AND (4==7) # Almacena el valor de False.
var2 = (1<7) OR (3==3) # Almacena el valor de True.
var3 = NOT(6==7) # Almacena el valor de True.
var4 =True AND False # Almacena el valor de False.
```

<h3>Estrucutras de control</h3>

<h4>Condicionales</h4>

son las estrucuturas en las cuales el codigo se ejecuta dependiendo de una condicion si la condicion es True  se ejecuta si no se pasa a la siguente condicion, si ninguna de las condiciones es True entonces se ejecuta el condigo de una del else.

```python
    
    edad = 18
    if(edad >= 0 ): 
        if(edad >= 18 ):
            print("Es mayor de edad")
        else:
        print("Es menor de edad")    
    else:
        print("Edad mal digitada")
```

<h4>Bucles condicionales</h4>

El bucle <strong>While</strong> es el cual se ejecuta el codigo hasta que se cumpla cierta condicion.

```python
    num = None
    while(num != 0):
        num = int(input("Introdusca un numero: "))
        
```
<h4>Bucles iterativos</h4>

El bucle for ejecuta el bloque de codigo la canditdad de veces definida por la secuencia iterativa.

```python
    palabra = "The world is connect"
    for letra in range(palabra):
    print(letra)
```

<h3>Tipos de datos estructurados</h3>

<h4>Listas</h4>

Una **Lista** es una secuencias ordenadas de objetos de distintos tipos.

Se construyen poniendo los elementos entre corchetes ``[  ]`` separados por comas.
Se caracterizan por:

* Tienen orden
* Pueden contener elementos de distintos tipos.
* Son mutables, es decir, pueden alterarse durante la ejecución de una programa.

```python
    type([ ])
    [1, ''dos", True ] # Listas con elementos de distintos tipos.
    [ 1, [2,3] ,4 ] #  Listas anidadas.
```

<h5>Creacion de listas mediante la  funcion list</h5>

Otro forma de crear listas es mediante la funcion  `` list()`` 

* ``list(c)`` : Crea una lista con los elementos de la secuencia o colección c.

Se pueden indicar los elementos separados por comas, mediante una cadena, o mediante una colección de elementos iterable.

```python
    list()
    list(1,2,3)
    list("Python")
``` 

<h5>Acceso a los elementos de una lista</h5>

Se utiliza los mismos operadores de acceso que para cadenas de caracteres.

* `l[i]` : Devuelve el elemento de la lista *l* con el índice *i*

```python
a = [ 'P', 'y','t','h','o','n']
a[0]
a[5]
a[6]
```

<h5>Sublistas</h5>

* `l[ i : j : k ]`: Devuelve la sublista desde el elemento de *l* con el índice *i* hasta el elemento anterior al índice *j*, tomando elementos cada *k*.

```python
a = [ 'P', 'y','t','h','o','n']
a[1:4]
a[1:1]
a[:-3]
a[:]
a[0:6:2]
```

<h5>Operaciones que no modifican una lista</h5>

* `len(l)` : Devuelve el número de elementos de la lista *l*.
*  `min(l)`: Devuelve el mínimo elemento de la lista *l* siempre que los datos sean comparables.
*  `max(l)` : Devuelve el máximo elemento de la lista *l* siempre que los datos sean comparables.
*  `sum(l)` : Devuelve la suma de los elementos de la lista *l* , siempre que los datos se puedan sumar.
* `dato in l` : Devuelve `True` si el dato `dato` pertenece a la lista *l* y `False` en caso contrario.
* `l.index(dato)` : Devuelve la posición que ocupa en la lista *l* el primer elemento con valor `dato`.
* `l.count(dato)` : Devuelve el número de veces que el valor `dato` está contenido en la lista *l*.
* `all(l)` : Devuelve `True` si todos los elementos de la lista *l* son `True` y `False` en caso contrario.
* `any(l)` : Devuelve `True` si algún elemento de la lista *l* es `True` y `False` en caso contrario.

```python
    a = [1,2,2,3]
    len(a)
    min(a)
    max(a)
    sum(a)
    3 in a  # True
```

<h5>Operaciones que modifican una lista</h5>

* `l1 + l2` : Crea una nueva lista concatenan los elementos de la listas `l1` y `l2`.
* `l.append(dato)` : Añade dato al final de la lista *`l`*.
* `l.extend(sequencia)` : Añade los datos de sequencia al final de la lista *`l`*.
* `l.insert(índice, dato)` : Inserta dato en la posición índice de la lista *`l`* y desplaza los elementos una posición a partir de la posición índice.
* `l.remove(dato)` : Elimina el primer elemento con valor dato en la lista *`l`* y desplaza los que están por detrás de él una posición hacia delante.
* `l.pop([índice])` : Devuelve el dato en la posición índice y lo elimina de la lista *`l`*, desplazando los elementos por detrás de él una posición hacia delante.
*  `l.sort()` : Ordena los elementos de la lista *`l`* de acuerdo al orden predefinido, siempre que los elementos sean comparables.
* `l.reverse()` : invierte el orden de los elementos de la lista *`l`*.

```python
>>> a = [1, 3]
>>> b = [2 , 4, 6]
>>> a.append(5)
>>> a
[1, 3, 5]
>>> a.remove(3)
>>> a
[1, 5]
>>> a.insert(1, 3)
>>> a
[1, 3, 5]
>>> b.pop()
6
>>> c = a + b
>>> c
[1, 3, 5, 2, 4]
>>> c.sort()
>>> c
[1, 2, 3, 4, 5]
>>> c.reverse()
>>> c
[5, 4, 3, 2, 1]
```

<h5>Copia de listas</h5>

Existen dos formas de copiar listas:

* **Copia por referencia** `l1 = l2:` Asocia la la variable *`l1`* la misma lista que tiene asociada la variable l2, es decir, ambas variables apuntan a la misma dirección de memoria. Cualquier cambio que hagamos a través de *`l1`* o *`l2`* afectará a la misma lista.
* **Copia por valor** `l1 = list(l2):` Crea una copia de la lista asociada a *`l2`* en una dirección de memoria
diferente y se la asocia a *`l1`*. Las variables apuntan a direcciones de memoria diferentes que contienen los mismos datos. Cualquier cambio que hagamos a través de *`l1`* no afectará a la lista de *`l2`* y viceversa.

```python
>>> a = [1, 2, 3]
>>> # copia por referencia
>>> b = a
>>> b
[1, 2, 3]
>>> b.remove(2)
>>> b
[1, 3]
>>> a
[1, 3]

>>> a = [1, 2, 3]
>>> # copia por referencia
>>> b = list(a)
>>> b
[1, 2, 3]
>>> b.remove(2)
>>> b
[1, 3]
>>> a
[1, 2, 3]
```

<h4>Tuplas</h4>

Una **tupla** es una secuencias ordenadas de objetos de distintos tipos.
Se construyen poniendo los elementos entre corchetes `( )` separados por comas.
Se caracterizan por:

* Tienen orden.
* Pueden contener elementos de distintos tipos.
* Son inmutables, es decir, no pueden alterarse durante la ejecución de un programa.

Se usan habitualmente para representar colecciones de datos una determinada estructura semántica, como por ejemplo un vector o una matriz.

```python
# Tupla vacía
type(())
<class 'tuple'>
# Tupla con elementos de distintos tipos
(1, "dos", True)
# Vector
(1, 2, 3)
# Matriz
((1, 2, 3), (4, 5, 6))
```
<h5>Creación de tuplas mediante la función tuple()</h5>

Otra forma de crear tuplas es mediante la función tuple().

* `tuple(c)` : Crea una tupla con los elementos de la secuencia o colección `c`.

Se pueden indicar los elementos separados por comas, mediante una cadena, o mediante una colección de
elementos iterable.

```python
>>> tuple()
()
>>> tuple(1, 2, 3)
(1, 2, 3)
>>> tuple("Python")
('P', 'y', 't', 'h', 'o', 'n')
>>> tuple([1, 2, 3])
(1, 2, 3)
```
<h5>Operaciones con tuplas</h5>

El acceso a los elementos de una tupla se realiza del mismo modo que en las listas. También se pueden obtener subtuplas de la misma manera que las sublistas.
Las operaciones de listas que no modifican la lista también son aplicables a las tuplas.

```python
>>> a = (1, 2, 3)
>>> a[1]
2
>>> len(a)
3
>>> a.index(3)
2
>>> 0 in a
False
>>> b = ((1, 2, 3), (4, 5, 6))
>>> b[1]
(4, 5, 6)
>>> b[1][2]
6
```

<h4>Diccionarios</h4>

Un diccionario es una colección de pares formados por una clave y un valor asociado a la clave.
Se construyen poniendo los pares entre llaves `{ }` separados por comas, y separando la clave del valor con dos puntos `:`. Se caracterizan por:

* No tienen orden.
* Pueden contener elementos de distintos tipos.
* Son mutables, es decir, pueden alterarse durante la ejecución de un programa.
* Las claves son únicas, es decir, no pueden repetirse en un mismo diccionario, y pueden ser de cualquier tipo de datos inmutable.


```python
# Diccionario vacío
type({})
<class 'dict'>
# Diccionario con elementos de distintos tipos
{'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
# Diccionarios anidados
{'nombre_completo':{'nombre': 'Alfredo', 'Apellidos': 'Sánchez Alberca'
}}
```

<h5>Acceso a los elementos de un diccionario</h5>

* `d[clave]` devuelve el valor del diccionario `d` asociado a la clave clave. Si en el diccionario no existe esa clave devuelve un error.

* `d.get(clave, valor)` devuelve el valor del diccionario `d` asociado a la clave clave. Si en el diccionario no existe esa clave devuelve valor, y si no se especifica un valor por defecto devuelve `None`.

```python
>>> a = {'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
>>> a['nombre']
'Alfredo'
>>> a['despacho'] = 210
>>> a
{'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
>>> a.get('email')
'asalber@ceu.es'
>>> a.get('universidad', 'CEU')
'CEU
```

<h5>Operaciones que no modifican un diccionario</h5>

* `len(d)` : Devuelve el número de elementos del diccionario `d`.
* `min(d)` : Devuelve la mínima clave del diccionario `d` siempre que las claves sean comparables.
* `max(d)` : Devuelve la máxima clave del diccionario `d` siempre que las claves sean comparables.
* `sum(d)` : Devuelve la suma de las claves del diccionario `d`, siempre que las claves se puedan sumar.
* `clave in d` : Devuelve  `True` si la clave clave pertenece al diccionario `d` y `False` en caso contrario.
* `d.keys()` : Devuelve un iterador sobre las claves de un diccionario.
* `d.values()` : Devuelve un iterador sobre los valores de un diccionario.
* `d.items()` : Devuelve un iterador sobre los pares clave‑valor de un diccionario.


```python
>>> a = {'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
>>> len(a)
3
>>> min(a)
'despacho'
>>> 'email' in a
True
>>> a.keys()
dict_keys(['nombre', 'despacho', 'email'])
>>> a.values()
dict_values(['Alfredo', 218, 'asalber@ceu.es'])
>>> a.items()
dict_items([('nombre', 'Alfredo'), ('despacho', 218), ('email', '
asalber@ceu.es')])
```

<h5>Operaciones que modifican un diccionario</h5>

* `d[clave] = valor` : Añade al diccionario d el par formado por la clave clave y el valor valor.
* `d.update(d2)`. Añade los pares del diccionario `d2` al diccionario `d`.
* `d.pop(clave, alternativo)` : Devuelve del valor asociado a la clave clave del diccionario `d` y
lo elimina del diccionario. Si la clave no está devuelve el valor alternativo.
* `d.popitem()` : Devuelve la tupla formada por la clave y el valor del último par añadido al diccionario `d` y lo elimina del diccionario.
* `del d[clave]` : Elimina del diccionario `d` el par con la clave clave.
* `d.clear()` : Elimina todos los pares del diccionario `d` de manera que se queda vacío.

```python
>>> a = {'nombre':'Alfredo', 'despacho': 218, 'email':'asalber@ceu.es'}
>>> a['universidad'] = 'CEU'
>>> a
{'nombre': 'Alfredo', 'despacho': 218, 'email': 'asalber@ceu.es', '
universidad': 'CEU'}
>>> a.pop('despacho')
218
>>> a
{'nombre': 'Alfredo', 'email': 'asalber@ceu.es', 'universidad': 'CEU'}
>>> a.popitem()
('universidad', 'CEU')
>>> a
{'nombre': 'Alfredo', 'email': 'asalber@ceu.es'}
>>> del a['email']
>>> a
{'nombre': 'Alfredo'}
>>> a.clear()
>>> a
{}
```

<h5>Copia de diccionarios</h5>

Existen dos formas de copiar diccionarios:

* **Copia por referencia** `d1 = d2`: Asocia la la variable `d1` el mismo diccionario que tiene asociado la variable `d2`, es decir, ambas variables apuntan a la misma dirección de memoria. Cualquier cambio que hagamos a través de `l1` o `l2` afectará al mismo diccionario.

* **Copia por valor** `d1 = dict(d2)`: Crea una copia del diccionario asociado a `d2` en una dirección de memoria diferente y se la asocia a `d1`. Las variables apuntan a direcciones de memoria diferentes que contienen los mismos datos. Cualquier cambio que hagamos a través de `d1` no afectará al diccionario de `d2` y viceversa.


```python
>>> a = {1:'A', 2:'B', 3:'C'}
>>> # copia por referencia
>>> b = a
>>> b
{1:'A', 2:'B', 3:'C'}
>>> b.pop(2)
>>> b
{1:'A', 3:'C'}
>>> a
{1:'A', 3:'C'}

>>> a = {1:'A', 2:'B', 3:'C'}
>>> # copia por referencia
>>> b = dict(a)
>>> b
{1:'A', 2:'B', 3:'C'}
>>> b.pop(2)
>>> b
{1:'A', 3:'C'}
>>> a
{1:'A', 2:'B', 3:'C'}
```
<h3>Funciones</h3>

<h4>Funciones (def)</h4>

Una función es un bloque de código que tiene asociado un nombre, de manera que cada vez que se quiera ejecutar el bloque de código basta con invocar el nombre de la función.

Para declarar una función se utiliza la siguiente sintaxis:


```python
>>> def bienvenida():
...
print('¡Bienvenido a Python!')
...
return
...
>>> type(bienvenida)
<class 'function'>
>>> bienvenida()
¡Bienvenido a Python!
```

<h5>Parametros de una funcion</h5>

Una función puede recibir valores cuando se invoca a travez de unas variables conocidad como parámetros que se definen entre paréntesis en declaración de la función. En el cuerpo de la función se pueden usar estos parámetros como si fuesen variables.

```python
>>> def bienvenida(nombre):
...
print('¡Bienvenido a Python', nombre + '!')
...
return
...
>>> bienvenida('Alf')
¡Bienvenido a Python Lain!
```

<h5>Argumentos de la llamada a una función</h5>

Los valores que se pasan a la función en una llamada o invocación concreta de ella se conocen como argumentos y se asocian a los parámetros de la declaracion de la función.
Los argumentos se puede indicar de dos formas:

* **Argumentos posicionales**: Se asocian a los parámetros de la función en el mismo orden que aparecen en la definición de la función.
* **Argumentos por nombre**: Se indica explícitamente el nombre del parámetro al que se asocia un argumento de la forma `parametro` = `argumento`.

```python
>>> def bienvenida(nombre, apellido):
...
print('¡Bienvenido a Python', nombre, apellido + '!')
...
return
...
>>> bienvenida('Alfredo', 'Sánchez)
¡Bienvenido a Python Alfredo Sánchez!
>>> bienvenida(apellido = 'Sánchez', nombre = 'Alfredo')
¡Bienvenido a Python Alfredo Sánchez!
```

<h5>Retorno de una funcion</h5>

Una función puede devolver un objeto de cualquier tipo tras su invocación. Para ello el objeto a devolver debe escribirse detras de la palabra reservada `return`. Si no se indica ningún objeto, la función no devolverá nada.

```python
>>> def area_triangulo(base, altura):
...
return base * altura / 2
...
>>> area_triangulo(2, 3)
3
>>> area_triangulo(4, 5)
10
```
<h5>Argmentos por defecto</h5>

En la definición de una función se puede asignar a cada parámetro un argumento por defecto, de manera que si se invoca la función sin proporcionar ningún argumento para ese parámetro, se utiliza el argumento por defecto.

```python
>>> def bienvenida(nombre, lenguaje = 'Python'):
...
print('¡Bienvenido a', lenguaje, nombre + '!')
...
return
...
>>> bienvenida('Lain')
¡Bienvenido a Python Lain!
>>> bienvenida('Lain', 'Java')
¡Bienvenido a Java Lain!
```

<h5>Pasar un número indeterminado de argumentos</h5>

Por último, es posible pasar un numero variable de argumentos a un parametro. Esto se puede hacer de dos formas.

* *`Parametro`: Se antepone un asterisco al nombre del parametro y en la invocacion de la funcion se pasa al numero variable de argumentos separados por comas. Los argumentos se guardan en una lista que se asocia al parametro.
* **`Parametro`: Se antepone dos asteriscos al nombre del parametro y en la invocacion de al funcian se pasa el numero variable de argumentos por pares `nombre` =  `valor`, separados por comas. Los argumentos se guardan en un dicionario que se asocia al parametro.

```python
>>> def menu(*platos):
...
print('Hoy tenemos: ', end='')
...
for plato in platos:
...
print(plato, end=', ')
...
return
...
>>> menu('pasta', 'pizza', 'ensalada')
Hoy tenemos: pasta, pizza, ensalada,
```

<h5>Ambito de los parametros y variables de una funcion</h5>

Los parametros y las variables declaradas dentro de una funcion son de **ambito local**, mientras que las definidas fuera de ella son de **ambito global.**

Tanto los parametros como las variables del ambito local de una funcion solo estan accesibles durante la ejecucion de la funcion, es decir, cuando termina la ejecucion de la funcion esta variables desaparecen y no son accesibles desde fuera de la funcion.

```python
>>> def bienvenida(nombre):
...
lenguaje = 'Python'
...
print('¡Bienvenido a', lenguaje, nombre + '!')
...
return
...
>>> bienvenida('Alf')
¡Bienvenido a Python Alf!
>>> lenguaje
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'lenguaje' is not defined
```

<h5>Ambito de los parametros y variables de una funcion</h5>

Si en el ambito local de una funcion existe una variable que tambien existe en el ambito global, durante la ejecucion de la funcion la variable global queda eclipsada por la variable local y no es accesible hasta que finalize la ejecucion de la funcion.

```python
>>> lenguaje = 'Java'
>>> def bienvenida():
...
lenguaje = 'Python'
...
print('¡Bienvenido a', lenguaje + '!')
...
return
...
>>> bienvenida()
¡Bienvenido a Python!
>>> print(lenguaje)
Java
```

<h5> Paso de argumentos por referencia</h5>

En Python el paso de argumentos a una funcion es siempre por referencia, es decir, se pasa una referencia al objeto del argumentos, de manera que cualquer cambioo que se haga dentro de la funcion mediante el parametro asociado afectara al objeto original, siempre y cuando este sea mutable.

```python
>>> primer_curso = ['Matemáticas', 'Física']
>>> def añade_asignatura(curso, asignatura):
...
curso.append(asignatura)
...
return
...
>>> añade_asignatura(primer_curso, 'Química')
>>> print(primer_curso)
['Matemáticas', 'Física', 'Química']
```

<h5>Documentación de funciones</h5>

Una practica muy recomendable cuando se define una funcion es escribir lo que la funcion hace en un comentario.

En Python esto se hace con un **docstring** que es un tipo de compentario especial se hace en la linea siguiente al encabezado de la funcion entre tres comillas simples `' ' '` o doble `" " "`.
Despues se puede haceder a la documentacion de la función con la función `help`(<`nombre-función`>).

```python
>>> def area_triangulo(base, altura):
... """Función que calcula el área de un triángulo.
...
... Parámetros:
...
- base: La base del triángulo.
...
- altura: La altura del triángulo.
... Resultado:
...
El área del triángulo con la base y altura especificadas.
... """
...
return base * altura / 2
...
>>> help(area_triangulo)
area_triangulo(base, altura)
Función que calcula el área de un triángulo.
Parámetros:
- base: La base del triángulo.
- altura: La altura del triángulo.
Resultado:
El área del triángulo con la base y altura especificadas.
```

<h4>Funcion recursivas</h4>

Una funcion recursiva es una función que en su cuerpo contien una llamada a si misma.

La recursion es una practica comun en la mayoria de lenguajes de porgramación ya que permite resolver las tareas recursivas de manera más natural.

Para garantizar el final de una funcion recursiva, las sucesiva llamadas tiene que reducir el grado de complejidad del problema, hasta que este pueda resolver directamente sin necesidad de volver a llamar a la función.

```python
>>> def factorial(n):
...
if n == 0:
...
return 1
...
else:
...
return n * factorial(n-1)
...
>>> f(5)
120
```

<h5>Funciones recursivas multiples</h5>

Una funcion recursiva puede invocarse a si misma tantas veces como quiera en su cuerpo.


```python
>>> def fibonacci(n):
...
if n <= 1:
...
return n
...
else:
...
return fibonacci(n - 1) + fibonacci(n - 2)
...
>>> fibonacci(6)
8
```

<h5>Los riesgos de la recursividad</h5>

Aunque la recursión permite resolver las tareas recursivas de forma más natural, hay que tener cuidad con ella porque suele consumir bastante memoria, ya que cada llamada a la función crea un nuevo ámbito local con las variable sy los parámetros de la función.

En muchos casos es más eficiente la tarea recursiva de forma iterativa usando bucles.

```python
>>> def fibonacci(n):
...
a, b = 0, 1
...
for i in range(n):
...
a, b = b, a + b
...
return a
...
>>> fibonacci(6)
8
```

<h4>Programación funcional</h4>

En **Python** las funciones son objetos de primera clase, es decir, que pueden pasarse como argumentos de una funcion, al igual que el resto de los tipos de datos.

```python
>>> def aplica(funcion, argumento):
...
return funcion(argumento)
...
>>> def cuadrado(n):
...
return n*n
...
>>> def cubo(n):
...
return n**3
...
>>> aplica(cuadrado, 5)
25
>>> aplica(cubo, 5)
125
```

<h5>Funciones anónimas (lambda)</h5>

Existen un tipo especial de funciones que no tienen nombre asociado y se conoces como **funciones anónimas** o **Funciones lamdba**.

La sintaxis para definir una función anonima es:

`lambda` <`Parametro`> : <`Expresion`>

Esta funcion se suele asociar a una variable o prametro desde la que hacer la llamada.

```python
>>> area = lambda base, altura : base * altura
>>> area(4, 5)
10
```

<h5>Aplicar una función a todos los elementos de una colección iterable (map)</h5>

`map`(`f`,`c`): Devuelve un objeto iterable con los resultados de aplicar la funcion `f` a los elementos de la coleccion `c`. Si la funcion `f` requiere `n` argumentos entonces deben pasarse `n` colecciones con los argumentos.
Para convertir el objeto en una lista, tupla o diccionario hay que aplicar explicitamente las funciones `list`( ), `tuple`( ) o `dic`( ) respectivamente.

```python
>>> def cuadrado(n):
...
return n * n
...
>>> list(map(cuadrado, [1, 2, 3])
[1, 4, 9]

>>> def rectangulo(a, b):
...
return a * b
...
>>> tuple(map(rectangulo, (1, 2, 3), (4, 5, 6)))
(4, 10, 18)
```

<h5>Filtrar los elementos de una colección iterable (filter)</h5>

`filter`(`f`,`c`): Devuelve un objeto iterable con los elementos de al colección `c` que devuelven `True` al aplicarles la funcion `f`. Para convertir el objeto en una lista, tupla, o diccionario hay que aplicar explicitamente las funciones `list`( ) , `tuple`() , `dict`( ) respectivamente.

`f` debe ser una función que reciba un argumento y devuelve un valor booleano.

```python
>>> def par(n):
...
return n % 2 == 0
...
>>> list(filter(par, range(10))
[0, 2, 4, 6, 8]
```

<h5>Combinar los elementos de varias colecciones iterables (zip)</h5>

`zip`(`c1`,`c2`, ...): Devuelve un objeto iterable cuyos elementos son tuplas formadas por los elementos que ocupan la misma posición en las colecciones `c1`,`c2`, etc. El número de elementos de las tuplas es el número de colecciones que se pasen. Para convertir el objeto en una lista, tupla o diccionario, hay que aplicar explicitamente las funciones  `list`( ) , `tuple`() , `dict`( ) respectivamente.


```python
>>> asignaturas = ['Matemáticas', 'Física', 'Química', 'Economía']
>>> notas = [6.0, 3.5, 7.5, 8.0]
>>> list(zip(asignaturas, notas))
[('Matemáticas', 6.0), ('Física', 3.5), ('Química', 7.5), ('Economía',8.0)]
>>> dict(zip(asignaturas, notas[:3]))
{'Matemáticas': 6.0, 'Física': 3.5, 'Química': 7.5}
```

<h5>Operar todos los elementos de una colección iterable (reduce)</h5>


`reduce`(`f`, `l`) : Aplicar la función `f` a los dos primeros elementos de la secuencia `l`. Con el valor obtenido vuelve a aplicar la función `f` a ese valor y el siguiente de la secuencia, y así hasta que no quedan más elementos en la lista. Devuelve el valor resultado de la última aplicación de la función `f`.
La función reduce está definida en el módulo `functools`.

```python
>>> from functools import reduce
>>> def producto(n, m):
...
return n * m
...
>>> reduce(producto, range(1, 5))
24
```

<h4>Comprensión de colecciones</h4>

En muchas aplicaciones es habitual aplicar una función o realizar una operación con los elementos de una colección (lista, tupla o diccionario) y obtener una nueva colección de elementos transformados. Aunque esto se puede hacer recorriendo la secuencia con un bucle iterativo, y en programación funcional mediante la función `map`, Python incorpora un mecanismo muy potente que permite esto mismo de manera más simple.

<h5>Comprensión de listas</h5>

`[`expresion `for` variable `in` lista `if` condicion`]`

Esta instrucción genera la lista cuyos elementos son el resultado de evaluar la expresión *`expresion`*, para cada valor que toma la variable *`variable`*, donde variable toma todos los valores de la lista lista que cumplen la condición condición.

```python
>>> [x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x for x in range(10) if x % 2 == 0]
[0, 2, 4, 6, 8]
>>> [x ** 2 for x in range(10) if x % 2 == 0]
[0, 4, 16, 36, 64]
>>> notas = {'Carmen':5, 'Antonio':4, 'Juan':8, 'Mónica':9, 'María': 6,
'Pablo':3}
>>> [nombre for (nombre, nota) in notas.items() if nota >= 5]
['Carmen', 'Juan', 'Mónica', 'María']
```

<h5>Comprensión de diccionarios </h5>

`{`*expresion‑clave*:*expresion‑valor* `for` *variables* `in` *lista* `if` *condicion*`}`

Esta instrucción genera el diccionario formado por los pares cuyas claves son el resultado de evaluar la expresión `expresion‑clave` y cuyos valores son el resultado de evaluar la expresión `expresion‑valor`, para cada valor que toma la variable `variable`, donde `variable` toma todos los valores de la lista `lista` que cumplen la condición `condición`.

```python
>>> {palabra:len(palabra) for palabra in ['I', 'love', 'Python']}
{'I': 1, 'love': 4, 'Python': 6}
>>> notas = {'Carmen':5, 'Antonio':4, 'Juan':8, 'Mónica':9, 'María': 6,'Pablo':3}
>>> {nombre: nota +1 for (nombre, nota) in notas.items() if nota >= 5])
{'Carmen': 6, 'Juan': 9, 'Mónica': 10, 'María': 7}
```

<h3>Ficheros</h3>

Hasta ahora visto como iteratuar con un programa a través del teclado (Entrada de datos) y la terminal (Salida), pero en el mayor parte de las aplicaciones reales tendremos que leer y escribir datos de ficheros.

Al utilizar ficheros para guardar los datos estos perduraran tras la ejecución del programa, pudiendo ser consultados o utilizados más tarde.

Las operaciones más habituales con ficheros son: 

* Crear un fichero.
* Escribir datos en un fichero.
* Leer datos de un fichero.
* Borrar un fichero.

<h4>Creacion  y escritura de un fichero</h4>

Para crear un fichero nuevo se utiliza la instrucción 

`open`(`ruta`,'w'): Crear el fichero con la ruta `ruta`, lo abre en modo escritura (El argumentos `'w'` significa write) y lo devuelve un objeto que lo referencia.

Si el fichero indicado por la ruta ya existe en el sistema, se reemplazara por el nuevo.
Una vez creado el fichero, para escribir datoa en él se utiliza el método `fichero`.`write`(`c`): Escribe `c` en el fichero referenciado por `fichero`.

```python
>>> f = open('bienvenida.txt', 'w')
... f.write('¡Bienvenido a Python!')
```
<h4>Añadir datos a un fichero</h4>

Si en lugar de crear un fichero nuevo queremos añadir datos a un fichero existente se debe utilizar la instrución

 `open`(`ruta`,'a'): Abre el fichero con la ruta  `ruta` en modo añadir (el argumento 'a' significa append) y devuelve un objeto que lo referencia.
 
Una vez abierto el ficheri, se utiliza el método de escritura anterio y los datos se añaden al final del fichero.


```python
>>> f = open('bienvenida.txt', 'a')
.. f.write('\n¡Hasta pronto!')
```

<h4>Leer datos de un fichero</h4>

Para abrir un fichero en modo lectura se utiliza la instruccion

 `open`(`ruta`,'r'): Abre el fichero con la ruta `ruta` en modo lectura (El argumento 'r' significa read) y devuelve un objeto que lo referencia.
 Una vez abierto el fichero, se puede leer todo el contenido del fichero o se puede leer linea a linea.
 
`fichero`.`read`( ): Devuelve todos los datos contenidos en `fichero` como una cadena de caracteres.
`fichero`.`readlines`( ): Devuelve una lista de cadenas de caracteres donde cada cadena es una linea del fichero referenciado por `fichero`.

```python
>>> f = open('bienvenida.txt', 'r')
... print(f.read())
¡Bienvenido a Python!
¡Hasta pronto!

>>> f = open('bienvenida.txt', 'r')
... lineas = print(f.readlines())
>>> print(lineas)
['Bienvenido a Python!\n', '¡Hasta pronto!']
```

<h4>Cerrar un fichero</h4>

Para cerrar un fichero se utiliza el método

`fichero`.`close`( ): Cierra el fichero referenciado por el objeto `fichero`.

Cuando se termina de trabajar con un fichero convien cerrarlo, sobre todo si se abre en modo escritura, ya que mientras está abierto en este modo no se puede abrir por otra aplicación. Si no se cierra explícitamente un fichero, Python intentará cerralo cuando estime que ya no se va a usar más.

```python
>>> f = open('bienvenida.txt'):
... print(f.read())
... f.close() # Cierre del fichero
...
¡Bienvenido a Python!
¡Hasta pronto!
```

<h4>Renombrando y borrado de un fichero</h4>

Para renombra o borrar un fichero se utiliza funciones del modulo `os`.
`os`.`rename`(`ruta1`,`ruta2`): Renombra y mueve el fichero de la `ruta1` a la `ruta2`
`os`.`remove`(`ruta`): Borra el fichero de la ruta `ruta`.

Antes de borrar o renombrar un directorio conviene comprobar que existe para que no se produzca un error. Para ello se utiliza la funcion. 

`os`.`path`.`isfile`(`ruta`) : Devuelve `True` si existe un fichero en la ruta ruta y `False` en caso contrario.

```python
>>> import os
>>> f = 'bienvenida.txt'
>>> if os.path.isfile(f):
...
os.rename(f, 'saludo.txt') # renombrado
... else:
...
print('¡El fichero', f, 'no existe!')
...
>>> f = 'saludo.txt'
>>> if os.path.isfile(f):
...
os.remove(f) # borrado
... else:
...
print('¡El fichero', f, 'no existe!'
```

<h4>Creación, cambio y eliminación de directorios</h4>


Para trabajar con directorios también se utilizan funciones del módulo os.

`os`.`listdir`(`ruta`) : Devuelve una lista con los ficheros y directiorios contenidos en la ruta `ruta`.
`os`.`mkdir`(`ruta`) : Crea un nuevo directorio en la ruta `ruta`.
`os`.`chdir`(`ruta`) : Cambia el directorio actual al indicado por la ruta `ruta`.
`os`.`getcwd`( ) : Devuelve una cadena con la ruta del directorio actual.
`os`.`rmdir`(`ruta`) : Borra el directorio de la ruta `ruta`, siempre y cuando esté vacío.

<h4>Leer un fichero de internet</h4>

Para leer un fichero de internet hay que utilizar la función `urlopen` del módulo `urllib`.`request`.
`urlopen`(`url`) : Abre el fichero con la `url` especificada y devuelve un objeto del tipo fichero al que se puede
acceder con los métodos de lectura de ficheros anteriores.


```python
>>> from urllib import request
>>> f = request.urlopen('https://raw.githubusercontent.com/asalber/
asalber.github.io/master/README.md')
>>> datos = f.read()
>>> print(datos.decode('utf-8'))
Aprende con Alf
===============

Este es el repositorio del sitio web Aprende con Alf: http://
aprendeconalf.es
```