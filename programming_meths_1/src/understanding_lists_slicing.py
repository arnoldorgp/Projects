players = ['peter', 'mercado', 'aron', 'fatima', 'renata']
print('lista original: ', players)

print('casos basicos')
print()

print(players[3:5])
print(players[1:4])
print(players[:3])
print(players[2:])
print(players[-3:])

print( )

print('casos especiales')
print( )
print(players[1:10])
print(players[4:1])
print(players[:0])
print(players[0:1])

students = players

print()
print('Looping through a slice')

for student in students[3:5]:
    print(f'El estudiante {student}, va a pasar la materia')

print(students)

# ¿como copiar una lista?

my_food = ['tacos', 'pizza'. 'flautas']
my_friend_food = my_food # ASI NO SE COPIA UNA LISTA

# materas correctas (hay 3)
# metodo 1
my_friend_food_2 = my_food[:]
# metodo 2
my_friend_food_3 = my_food.copy()
# metodo 3
my_friend_food_4 = list(my_food)