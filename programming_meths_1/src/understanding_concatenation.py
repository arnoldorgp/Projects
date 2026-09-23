# Combinación o concatenación de strings
first_name = "arnoldo"
last_name = "gudino"
full_name = first_name + " " + last_name
print(full_name.title())

print("hola", first_name + " " + last_name)
print(first_name, last_name)

#whitespace
"""
se refiere a cualquier caracter que no se imprime
es decir, un espacio, tabuladores y finales
de linea, es decir, in espacio ( ),
tabuladores (\t) y finales de linea (\n)

los withespace se utilizan comunmente para
organizar las aalidas de texto a usuario
de tal manera que sea mas amigable de 
leer o ver para los usuarios
"""

print("Python")
print("\tPython")
print("\t\tPython")
print("Lenguajes:\n\tPython\nC\nJavaScript")

# F-Strings
print("f-strings")
famous_person = "arnoldo gudino"
message = f"{famous_person} una vez dijo: Python is love."
print(message)

#investigar el metodo join()de strings
