# if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car)


# Elcondicional es el corazon de un if
# Condicional verdadero - Conditional True
# Condicional == paradeterminar igualdad
truck = 'ford'
print(truck == 'ford') #True

#Condicional False
print(truck == 'toyota') #false

#Condicional != para determinar desigualdad
print(truck != 'toyota') #True
print(truck != 'ford') # false

print('Condicionales con numeros')
age = 34
print(age == 18)# false

answer = 17
if answer !=42:
    print('incorrecto')