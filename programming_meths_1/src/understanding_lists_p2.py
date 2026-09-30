print('                               ')
# Agregando elementos a una lista
print('lista')
motorcycles = ['honda', 'mortalica', 'yamaha']
print(motorcycles)

#Metodo append
print('metodo .append()')
motorcycles.append('kawasaki')
print(motorcycles)
print('                                                   ')
print('###################################################')
print('                                                   ')
motorcycle = "ducati"
motorcycles_2 = []
motorcycles_2.append(motorcycle)
motorcycles_2.append('yamaha')
motorcycles_2.append('suzuki')
print(motorcycles_2)
motorcycles_2.insert(1,'honda')
print(motorcycles_2)

# lista.pop(): tipo entero, el argumento 
#es opcional, si no tiene nada, borra el ultimo, elimina por indice
# nos permite usar el elemento despues de eliminarlo
print('                                                   ')
print('###################################################')
print('                                                   ')
print('metodo .pop()')
motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_4)
deleted_motorcycles = motorcycles_4.pop()
print(f'tu motocicleta borrada es {deleted_motorcycles}')
print(motorcycles_4)
print('                                                   ')
print('###################################################')
print('                                                   ')
motorcycles_4.append(deleted_motorcycles)

# eliminar por indice
print('eliminar por indice')
motorcycles_4.pop(-3)
print(motorcycles_4)
print('                                                   ')
print('###################################################')
print('                                                   ')

# lista.remove(): el argumento es obligatorio y elimina elementos de la lista
#por valor.
print('metodo .remove()')
motorcycles_5 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_5)
motorcycles_5.remove('ducati')
print(motorcycles_5)
print('                                                   ')
print('###################################################')
print('                                                   ')
#investigar meodo .reverse()
#estudiar metodos build-in: .sorted(), .len()

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('metodo .sort()')
print(cars)
cars.sort() #ordena la lista en orden alfabetico permanentemente
# agrumento opcional, .sort(reverse=True)
print(cars)

