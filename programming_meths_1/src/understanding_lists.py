"""
 Las listas nos permiten almacenar información en un
 lugar, la cantidad que se desee: ya sean pocos
 elementos o millones de elementos

 Una lista es una colección de items (elementos) que 
 tienen un orden particular. Se pueden crear listas que
 incluyan strings; integers (enteros), loatings (flotantes), los nombres
 de las personas de tu familia, etcétera, podemos almacenar
 (los tipos de datos permitidos en Python) lo que queramos en una lista

 Son elementos mutables: puede modificarse ele tamaño de la lista

 Se recomienda nombrar una variable del tipo lista en plural

 En Python los corchetes [] indican listas,
 sus elementos se separan por comas.
 """
bicycles = ['trek', "cannondale", "redline", "specialized", "apache"]
print(bicycles)

"""

    Accessando a los elementos de una lista.
    
"""
# Para acceder al primer elemento de una lista
print(bicycles[0])

# Los índices comienzan en 0, no en 1.
print(bicycles[1]) # imprime cannondale
print(bicycles[3]) # imprime specialized

# Accesando al último elemento
print(bicycles[-1]) # specialized

#Accesando al penúltimo
print(bicycles[-2]) # imprime redline

# Utilizando valores individuales de una lista
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# Utilizando f-strings
message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)

