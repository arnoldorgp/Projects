age = input("\n ingresa tu edad")
print(age)
age = int(age)

"""if age <= 4:
    cost = 0

if age > 4 and age < 18:
    cost = 200

if age >= 18:
    cost = 500

print('chorros de if')
print(f"El costo de boleto es: {cost}")"""

# Bloque if-elif-else

if age <= 4:
    cost = 0
elif age > 4 and age < 18:
    cost = 200
elif age >= 18 and age < 65:
    cost = 500
elif age >= 65:
    cost = 0


print('bloque if-else-if')
print(f"El costo de boleto es: {cost}")