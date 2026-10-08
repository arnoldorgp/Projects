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