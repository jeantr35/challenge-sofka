import random

class Carro:

    def __init__(self, modelo, carril, pista, distancia=0):
        self.modelo = modelo
        self.carril = carril #Carril de la pista a la cual esta asociado
        self.pista = pista
        self.distancia = distancia
        

    def avanzar(self): #Metodo usado para avanzar aleatoriamente
        dado = random.randrange(1,7)
        self.distancia += dado * 100
        print(f'El carro ha recorrido un total de {self.distancia} metros')


class Conductor:

    def __init__(self, carro, nombre):
        self.carro = carro #Carro asociado al conductor
        self.nombre = nombre #Nombre del conductor


if __name__ == "__main__":
    car1 = Carro('Mazda 3', 0, 'Tokio')
    conductor1 = Conductor(car1, 'Jean')
    print(f'Hola soy {conductor1.nombre}, y manejo un {conductor1.carro.modelo}')
    conductor1.carro.avanzar()