# Números
# Enteros - Integers
"""
 Los números enteros los podemos
 sumar (+), restar (-), multiplicar(*)
 y dividir (/)
"""
print(2+3)
print(3-2)
print(2*3)
print(3/2)
number_1 = 5
number_2 = 10
print(number_1+number_2)

#investigar que es el zen de python, que es?, de que se compone?, porque existe?

#Enteros
# Sumar +
# Restar -
# Multiplicar *
# Dividir /
#División entera //
# Potencias **n
print(3**2) #3^2
print(3**3) #3^3
print(10**6) # 10^6
print(10%2) # Módulo (mod)
age = 17
print(age)
name = "Arnoldo Gudiño"
print(name, age)

# Floats
"""
 Python le llama floats a cualquier 
 número con punto decimal
"""
print(0.1+0.1)
print(0.2-0.2)
print(2*0.1)

#imprimir la edad de alguine

age = 34 # variable del tipo int
message = "Charly tiene " + str(age) + " años"
print(message)

# str() es un built-in method como print()

#TypeError
"""
 TypeError: Python no puede reconocer el tipo 
 de información que se está utilizando
 """

message_f = f"Charly tiene {34} años"
print(message_f)

# Método built-in type()
print(type(age), type("hola"), type(0.54), type (True))