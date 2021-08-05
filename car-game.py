import random

class Carro:

    def __init__(self, conductor, distancia=0):
        self.conductor = conductor
        self.distancia = distancia

    def avanzar(self):
        dado = random.randrange(1,7)
        self.distancia += dado * 100
        print(f'El carro ha recorrido un total de {self.distancia} metros')


if __name__ == "__main__":
    car1 = Carro('Jean')
    car1.avanzar()
    car1.avanzar()