#STRINGS

"""
un srtrin es de manera sencillal una serie de caracteres.
En Python,t todo lo que se encuentre entre comillas simples ''
o dentro de comillas dobles "" es considerado un string

Ejemplo:

"Esto es un string"
'Esto es un string'
'Le dije a un amigo, "Python es mi lenguaje favorito"'
"El lenguaje 'Python'lleva el nombre por Monty Python, no por la serpiente "

Ejemplo incorrecto:
(x) "Charly'
"""
name = "ARNOLDO rene GUDINO ponce"
"""
la variable name es de tipo string
"""
print(name)


print(name.title())
name = name.title()
print(name)

#Metodos

"""
 Un metodos es una accion que
 python puede realizar sobre una 
 variable.

 el punto . sobre una variable despues de 
 una variable seguido por el nombre del 
 metodo en este caso title ()
 dice que se tiene que ejecutar title()
 de la variable name

 Todos los metoos van seguidos de parentesis
 porque en ocaciones necesitan informacion 
 adicional para funcionar. En esta ocacion el
  metodo title() no requiere informacion 
  adicional para ejecutarse
"""
print(name.upper())
print(name.lower())