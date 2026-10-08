"""
TUPLAS

Las tuplas son listas de elementos que no cambias de tamaño.
Las tuplas son listas inmutables


Se utilizan los parentesis () para definir una tupla.

Ejemplo:
    Si tenemos un rectángulo (largo, ancho) que siempre va
    a tener cierto tamaño, podemos asegurar que sus dimenciones
    no va a cambiar si colocamos sus valores en una tupla.
"""


dimensions = (200,50) # 200 de largo x 50 de ancho
print('tupla original', dimensions)

# Vamos a imprimir elementos de una tupla
# Se realiza de la misma forma que en una lista
print(dimensions[0])
print(dimensions[1])
#print(dir(dimensions))

names = ['carlos', 'charly', 'juan', 'wendy']
print(names)
names[0] = 'mercury'
names[1] = 'mercury'
names[2] = 'mercury'
print(names)

#dimensions[0] = 500
#print(dimensions)

for dimension in dimensions:
    print(dimension)

trying_slicing = ('rgb', 'rwgb', 'wrggbb', 'wrg')

print(trying_slicing[1:])

"""
No se puede modificar una tupla
pero si se puede redefinir en el codigo
"""

dimensions = (500, 1000, 20)
print('tupla re-definida', dimensions)

answer = True
print(answer)