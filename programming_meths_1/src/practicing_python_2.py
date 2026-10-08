# metodos de listas

sports = ['basketball', 'soccer', 'football', 'baseball', 'bolleyball', 'swimming']
print(sports)
print()

print('el metodo .append() agrega elementos al final de la lista,\n este debe de llevar un argumento, que es el\n elemento que se va a agregar'.upper())
print()
sports.append('running')
print(sports)
print()

print('El metodo .pop() cuando no lleva argumento\nborra el ultimo elemento de la lista\npara llevar argumento se le debe poner el indice del\nelemento que se desea borra'.upper())
print()
sports.pop()
print(sports)
print()
sports.pop(3)
print(sports)
print()

print('el metodo insert agrega elementos a la lista\npero en un indice en especifico, el cual se indica con el numero'.upper())
print()
sports.insert(3,'baseball')

sports.insert(4,'running')
print(sports)
print()
print('el metodo .remove() tambien sirve para eliminar elementos\n de una lista, pero para indicar stos elementos\n se debe poner el valor del elemento como argumento'.upper())
print()
sports.remove('running')
print(sports)
print()

print('El metodo .sort() sirve para ordenar una lista\n en orden alfabetico u ordenar listas \nde nuemros de menor a mayor'.upper())
print()
sports.sort()
print(sports)

print()
print('El metodo .sort() puede llevar el argumento\n reverse = True que ordena la lista de la Z-A, osea, al reves\n y en listas de numeros sirve para ordenarla\n de mayor a menor'.upper())
print()
sports.sort(reverse = True)
print(sports)

