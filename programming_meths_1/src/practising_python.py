"""
SI LLEGA A VER ESTO, PROFE CHARLY,
LE QUIERO PEDIR UNA DISCULPA POR LO QUE 
ESTA A PUNTO DE PRECENCIAR.
Y SI ALGUIEN MAS LO ESTA VIENDO, 
PINSHI CHISMOSO, QUE ANDA HACIENDO AQUI
NO TIENES NADA QUE HACER O PEDO
DE ANTEMANO, GRACIAS.

:)
"""
#variables

print("---VARIABLES---")
print('caguama = "esto es una variable tipo string"\nchela = 5+6 \nguama = "tambien string"')

caguama = "esto es una variable tipo string"
chela = 5+6 
guama = "tambien string"

#concatenación

print("---CONCATENACIÓN---")

print(r'print(caguama+"\n"+guama+"\n"+str(chela))')

print(caguama+"\n"+guama+"\n"+str(chela))

"""str()convierte cualquier variable
o resultado de variable en un string"""

#f-string
print("---F-STRINGS---")

coca = "perro"
pepsi = "gato"

refresco = f"{coca+" y "+pepsi} quieren comida"
print(refresco)

#metodos

print("---MÉTODOS---")

chilaquiles = "tacos y pozole"
barbacoa = "los domingos"
cabrito = "migadas"

comida = f"los {chilaquiles} y las {cabrito} caen conmadre en {barbacoa}"

mole = "adrian"

tostadas = comida + " 8==D " + mole

print(comida.title()+"\n\t"+tostadas.upper())

#join ()

print("---TAREA DEL METODO JOIN---")

rompecabezas = ["que pedo", "ma nigga", mole,",", "que opinas de que", comida.upper()]
gol = " ".join(rompecabezas)
print(gol)