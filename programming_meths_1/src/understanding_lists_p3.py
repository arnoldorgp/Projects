# Trabajando con listas
print('\n\tel dia de hoy voy a aprender a trabajar con listas\n'.upper())

magicians = ['harry', 'ron', 'hermione', 'snape', 'voldemort']
print(magicians)

print('imprimir a la mala')
print (magicians[0], magicians[1], magicians[2],magicians[3],magicians[4])

#ciclo for
print('imprimir con un for')
for magician in magicians:
    print(magician, end=" ")
print()
for magician in magicians:
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"No puedo esperar a ver el siguiente hechizo, {magician.upper()}\n")

print('Gracias a todos, ese fue un gran espectaculo')

print(" ".join(magicians))

#Identación

"""
Python utiliza la identación para determinar
cuando una lineade codigo esta conectada a la
linea de código anterior.

Basicamente, se utilizan 4 espacios en blanco para
obligarnos a escribir codigo ordenado y estructurado.
"""

#No olvidemos identar

magicians = ["alice", 'david', 'caroline']
"""
for magician in magicians:
print(magician) #identation error
"""

for magician in magicians:
    print(magician)
print(f"no puedo vesperar a ver el siguente truco, {magician}")#error de logica


#identacion inecesaria
message = "hellow python world"
#    print(message) # error de identación

#No olvidar los dos puntos
for magician in magicians
    print(magician) #error de sintaxix(no puse los 2 puntos)

