# Challenge-Sofka
Solucion al CHALLENGE - JUEGO DE CARROS POR CONSOLA

Se usó el lenguaje de programacion python. Dentro del script se crearon las clases:
- Juego: Encargado de contener la pista que se va jugar y el indice de llegada de cada uno de los carros
- Pista: Encargada de contener el numero de carriles, nombre de la pista, los carriles que contienen a cada jugador y la longitud de la pista
- Podio: Encargado de contener los primeros 3 jugadores que lleguen a la meta, asi como de guardar la informacion y montrar el historico de cada conductor
- Jugador: Encargado de contener los carros elegidos, y su posicion
- Carro: Encargado de guardar la informacion del modelo elegido, la distancia recorrida y el conductor asignado
- Conductor: Encargado de guardar el nombre del conductor selecconado por el jugador
  
Para el avance del Carro por medio de dado se usó la librera random, con un metodo del carro.

La informacion es guardada en un archivo llamado 'podio.txt' que de no existir es creado automaticamente. Se guarda la posicion de llegada, el nombre del conductor, el modelo del carro y el nombre de la pista.
