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
