import random

menu_pistas = """
Bienvenido al menu de pistas

0- Alabama internatonal dragway
1- Atco Dragway
2- Atlanta dragway

Por favor seleccione una ingresando el numero
"""

class Carro:

    def __init__(self, modelo, conductor, distancia=0):
        self.modelo = modelo
        self.distancia = distancia
        self.conductor = None #Conductor aun no asignado
        

    def avanzar(self): #Metodo usado para avanzar aleatoriamente
        dado = random.randrange(1,7)
        self.distancia += dado * 100
        print(f'El carro ha recorrido un total de {self.distancia} metros')


class Conductor:

    def __init__(self, nombre):
        self.nombre = nombre #Nombre del conductor


class Pista:

    def __init__(self, carriles, nombre_pista):
        self.carriles = carriles #Numero de carriles
        self.nombre_pista = nombre_pista
        self.carril = [] #Cada elemento de la lista representa un carril con un carro

    def crear_carriles(self): #Metodo para crear los carriles con sus carros
        self.carril = [Carro('Mazda 3', i, 'Piston') for i in range(self.carriles)] 


if __name__ == "__main__":
    jugadores = int(input('Por favor ingrese el numero de jugadores: '))
    nombre_pista = int(input(menu_pistas))
    menu_pistas = ['Alabama internatonal dragway', 'Atco Dragway', 'Atlanta dragway']
    pista1 = Pista(jugadores, menu_pistas[nombre_pista])
    pista1.crear_carriles()



    