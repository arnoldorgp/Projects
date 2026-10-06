# Listas de numeros
"""
Las listas tambien pueden almacenar numeros. Python
ofrece varias herramientas que ayudan a trabajar
eficientemente con listas de numeros
"""
# Método built-in range()

"""
El metodo range() nos ayuda a crear facilmente 
series de nuemros

Ejemplo:
"""

for value in range(1,10): #range hace esto [a,b), osea imprime desde el numero que esta en la hizquierda hasta 1 antes del de lla derecha
    print(value, end = " ")

numbers = list(range(0,10))
print(numbers)

even_numbers = list(range(0,10,2))
print(even_numbers)

odd_numbers = list(range(1,10,2))
print(odd_numbers)

table_7  = list (range(7,71,7))
print(table_7)