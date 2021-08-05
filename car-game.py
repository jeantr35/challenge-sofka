import random

menu_pistas = """
Bienvenido al menu de pistas

0- Alabama internatonal dragway
1- Atco Dragway
2- Atlanta dragway

Por favor seleccione una ingresando el numero
"""

menu_conductores = """
0- Jean Trujillo
1- Steven Aaron
2- Juan Perez
3- Lucas Hernandez
4- Pedro Vega

Por favor seleccionelo ingresando el numero
"""

lista_conductores = ['Jean Trujillo', 'Steven Aaron', 'Juan Perez', 'Lucas Hernandez', 'Pedro Vega']
menu_pistas = ['Alabama internatonal dragway', 'Atco Dragway', 'Atlanta dragway']


class Conductor:

    def __init__(self, nombre):
        self.nombre = nombre #Nombre del conductor


class Carro:

    def __init__(self, modelo, conductor, distancia=0):
        self.modelo = modelo
        self.distancia = distancia
        self.conductor = None #Conductor aun no asignado
        

    def avanzar(self): #Metodo usado para avanzar aleatoriamente
        dado = random.randrange(1,7)
        self.distancia += dado * 100
        print(f'El carro ha recorrido un total de {self.distancia} metros')

    def asignar_conductor(self, nombre):
        self.conductor = Conductor(nombre)


class Pista:

    def __init__(self, carriles, nombre_pista):
        self.carriles = carriles #Numero de carriles
        self.nombre_pista = nombre_pista
        self.carril = [] #Cada elemento de la lista representa un carril con un carro

    def crear_carriles(self): #Metodo para crear los carriles con sus carros
        self.carril = [Carro('Mazda 3', i, 'Piston') for i in range(self.carriles)] #List comprehension


if __name__ == "__main__":
    jugadores = int(input('Por favor ingrese el numero de jugadores: '))
    nombre_pista = int(input(menu_pistas))
    conductores = [int(input(f'Jugador{i+1} selecciona tu conductor {menu_conductores}')) for i in range(jugadores)]
    
    pista1 = Pista(jugadores, menu_pistas[nombre_pista])
    pista1.crear_carriles()

        #Crearemos los conductores para cada carro

    for i in range(len(pista1.carril)):
        pista1.carril[i].asignar_conductor(lista_conductores[conductores[i]]) 
        print(pista1.carril[i].conductor.nombre)

    