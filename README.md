# Juego Kodland

Este es un proyecto de juego sencillo creado con Pygame donde el usuario controla un personaje que debe esquivar enemigos que caen desde la parte superior de la pantalla mientras recolecta power ups para aumentar su puntuacion y obtener ventajas adicionales como un escudo de proteccion. El objetivo del juego es obtener la mayor puntuacion posible sin colisionar con los enemigos.


# Caracteristicas

- Movimiento del jugadors: El jugador puede moverse en todas las direccion usando las teclas WASD.
- Enemigos: Los enemigos caen desde la parte superior de la pantalla con velocidad creciente a medida que avanza el juego.
- Menu Inicial: El juego muestra un menu inicial.
- Pausa: El juego puede ser pausado y reanudado.
- Pantalla de fin de juego: Al colisionar con un enemigo, el juego muestra una pantalla de "Game Over" con la puntuacion obtenida y la opcion de reintentar.


# Instalacion

1. Clonar repositorio
2. Instalar Pygame ("pip install pygame")
3. ejecutar el juego: "python main.py"


# Controles

- "W": Mover hacia arriba
- "A": Mover hacia la izquierda
- "S": Mover hacia abajo
- "D": Mover hacia la derecha

- "P": Pausar juego
- Enter: Empezar/Reiniciar juego


# Estructura del proyecto

- "main.py": contiene la logica principal del juego, incluyendo el bucle principal y la gestion de eventos.
- "functions.py": contiene las clases y funciones utilizadas en el juego.
- "constants.py": define las constantes utilizadas en el juego, a modo de que una futura posible edicion de dichos valores sea mas sencillo. 