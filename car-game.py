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

menu_carros = """

0- Mercedes W11
1- Red Bull RB16
2- McLaren MCL35
3- Toyota TS050 Hybrid
4- Toyota Yaris WRC

Por favor seleccionelo ingresando el numero
"""

lista_conductores = ['Jean Trujillo', 'Steven Aaron', 'Juan Perez', 'Lucas Hernandez', 'Pedro Vega']
lista_carros = ['Mercedes W11','Red Bull RB16','McLaren MCL35','Toyota TS050 Hybrid','Toyota Yaris WRC.']


class Conductor:

    def __init__(self, nombre):
        self.nombre = nombre #Nombre del conductor


class Carro:

    def __init__(self, modelo, distancia=0):
        self.modelo = modelo
        self.distancia = distancia
        self.conductor = None #Conductor aun no asignado
        

    def avanzar(self): #Metodo usado para avanzar aleatoriamente
        dado = random.randrange(1,7)
        self.distancia += dado * 100
        if self.distancia >= juego1.pista.longitud:
            self.distancia = juego1.pista.longitud
            print(f'El carro de {self.conductor.nombre} ha sacado un {dado} y ha llegado a la meta')
            return
        print(f'El carro de {self.conductor.nombre} ha sacado un {dado} y ha recorrido un total de {self.distancia} metros')

    def asignar_conductor(self, nombre):
        self.conductor = Conductor(nombre)


class Jugador:

    def __init__(self, carro):
        self.carro = carro
        self.posicion = None

    def asignar_posicion(self,posicion):
        self.posicion = posicion


class Podio:

    def __init__(self, primero=None, segundo=None, tercero=None):
        self.primero = primero
        self.segundo = segundo
        self.tercero = tercero

    def asignar_podio(self,jugador):
        if jugador.posicion == 1:
            self.primero = jugador
        elif jugador.posicion == 2:
            self.segundo = jugador
        elif jugador.posicion == 3:
            self.tercero = jugador

    def guardar_podio(self):
        with open("./podio.txt", "a", encoding="utf-8") as f:
            f.write(f'Primer lugar: {self.primero.carro.conductor.nombre} con el carro: {self.primero.carro.modelo}\n')
            f.write(f'Segundo lugar: {self.segundo.carro.conductor.nombre} con el carro: {self.segundo.carro.modelo}\n')
            f.write(f'Tercer lugar: {self.tercero.carro.conductor.nombre} con el carro: {self.tercero.carro.modelo}\n')
            f.write(f'Pista: {pista1.nombre_pista}\n')
            f.close()
    
    def mostrar_victorias(self, jugador, contador=0):
        with open("./podio.txt", "r", encoding="utf-8") as f:
            for linea in f:
                if jugador.carro.conductor.nombre in linea:
                    contador +=1
        return contador

class Pista:

    def __init__(self, carriles, nombre_pista, longitud=2000):
        self.carriles = carriles #Numero de carriles
        self.nombre_pista = nombre_pista
        self.carril = [] #Cada elemento de la lista representa un carril con un jugador
        self.longitud = longitud

    def crear_carriles(self): #Metodo para crear los carriles con sus jugadores
        self.carril = [Jugador(carros[i]) for i in range(self.carriles)] #List comprehension


class Juego:

    def __init__(self, pista):
        self.pista = pista
        self.podio = 1

    def iniciar_juego(self):
        for jugador in self.pista.carril:
            if jugador.carro.distancia < self.pista.longitud:
                jugador.carro.avanzar()     
            elif jugador != podio1.primero and jugador != podio1.segundo:
                self.asignar_podio(jugador)

    def asignar_podio(self, jugador):
        jugador.asignar_posicion(self.podio)
        podio1.asignar_podio(jugador)
        self.podio +=1


if __name__ == "__main__":
    jugadores = int(input('Por favor ingrese el numero de jugadores (Minimo 3): '))
    nombre_pista = int(input(menu_pistas))
    conductores = [int(input(f'Jugador{i+1} selecciona tu conductor {menu_conductores}')) for i in range(jugadores)]
    menu_pistas = ['Alabama internatonal dragway', 'Atco Dragway', 'Atlanta dragway']
    carros = [lista_carros[int(input(f'Jugador{i+1} selecciona tu carro {menu_carros}'))] for i in range(jugadores)]
    carros = [Carro(carros[i]) for i in range(len(carros))] 

    pista1 = Pista(jugadores, menu_pistas[nombre_pista])
    pista1.crear_carriles()
    podio1 = Podio()

        #Crearemos los conductores para cada carro

    for i in range(len(pista1.carril)): 
        pista1.carril[i].carro.asignar_conductor(lista_conductores[conductores[i]])
        print(f'Jugador{i+1} {pista1.carril[i].carro.modelo} {pista1.carril[i].carro.conductor.nombre}')

    #Iniciamos el juego
    juego1 = Juego(pista1)
    while True:
        print('')
        juego1.iniciar_juego()
        if (podio1.primero != None) and (podio1.segundo != None) and (podio1.tercero != None):
            break
    podio1.guardar_podio()

    print(f"""
El podio queda de la siguiente manera:
    1 {podio1.primero.carro.conductor.nombre} con un total de {podio1.mostrar_victorias(podio1.primero)} victorias
        2 {podio1.segundo.carro.conductor.nombre} con un total de {podio1.mostrar_victorias(podio1.segundo)} victorias
            3 {podio1.tercero.carro.conductor.nombre} con un total de {podio1.mostrar_victorias(podio1.tercero)} victorias
    """)