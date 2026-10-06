"""
una list comprenhension combina
el for loop y la creacion de nuevos elementos
en una sola linea y automaticamente agrega
cada nuevo elemento a la lista, es decir,
sin utilizar el metodo append
"""
squares = [value**2 for value in range(1,11)]
print(squares)

students = ['montes', 'farid', 'el de las flautas', 'el diactador', 'dante']
student_email = [student + '@upv.edu.mx'  for student in students]
print(f'lista original{students}')
print(student_email)
