import pygame
import sys
import random
import constants
from functions import Personaje, Enemigo, PowerUp, ShieldPowerUp, display_text, detect_collision, detect_powerup_collision

pygame.init()

# Ventana
window = pygame.display.set_mode((constants.ANCHO_VENTANA, constants.ALTO_VENTANA))
pygame.display.set_caption("My Kodland Game")

# Jugador
player = Personaje(constants.ANCHO_VENTANA//2, constants.ALTO_VENTANA-50)

# Enemigos
enemies = [Enemigo(constants.ANCHO_VENTANA,constants.ALTO_VENTANA, constants.TAMAÑO_ENEMIGO, constants.VELOCIDAD_ENEMIGO) for _ in range(6)]

# Power-Ups
power_ups = [PowerUp(constants.ANCHO_VENTANA, constants.ALTO_VENTANA, constants.TAMAÑO_POWER_UP) for _ in range(2)]
shield_power_ups = [ShieldPowerUp(constants.ANCHO_VENTANA, constants.ALTO_VENTANA, constants.TAMAÑO_POWER_UP) for _ in range(1)]

# Fuente de Textos
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Estado del Juego
game_over = False
menu = True
pause = False

# Puntuacion y Escudo
score = 0
shield_active = False
shield_duration = 0


#----------------------------------------------------------------------------------------------------------------------------


# Estructura principal
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
       
    keys = pygame.key.get_pressed()
    
    # Menu Inicial
    if menu:
        window.fill(constants.BLACK)
        display_text(window, font, "Juego con PyGame", constants.WHITE, (constants.ANCHO_VENTANA / 2, constants.ALTO_VENTANA / 2 - 50))
        display_text(window, small_font, "Presiona Enter para empezar", constants.WHITE, (constants.ANCHO_VENTANA / 2, constants.ALTO_VENTANA / 2 + 50))
        pygame.display.flip()
            
        if keys[pygame.K_RETURN]:
            menu = False
            game_over = False
            pause = False
            score = 0
            shield_active = False
            shield_duration = 0
            enemies = [Enemigo(constants.ANCHO_VENTANA, constants.ALTO_VENTANA, constants.TAMAÑO_ENEMIGO, constants.VELOCIDAD_ENEMIGO) for _ in range(6)]
            power_ups = [PowerUp(constants.ANCHO_VENTANA, constants.ALTO_VENTANA, constants.TAMAÑO_POWER_UP) for _ in range(2)]
            shield_power_ups = [ShieldPowerUp(constants.ANCHO_VENTANA, constants.ALTO_VENTANA, constants.TAMAÑO_POWER_UP) for _ in range(1)]

    # Fin de Juego        
    elif game_over:
        window.fill(constants.BLACK)
        display_text(window, font, "Fin del Juego", constants.RED, (constants.ANCHO_VENTANA / 2, constants.ALTO_VENTANA / 2 - 50))
        display_text(window, small_font, f"Puntuación: {score}", constants.WHITE, (constants.ANCHO_VENTANA / 2, constants.ALTO_VENTANA / 2 + 50))
        display_text(window, small_font, "Presiona Enter para reiniciar", constants.WHITE, (constants.ANCHO_VENTANA / 2, constants.ALTO_VENTANA / 2 + 100))
        pygame.display.flip()
        
        if keys[pygame.K_RETURN]:
            menu = True
            
    # Pantalla de Pausa
    elif pause:
        window.fill(constants.BLACK)
        display_text(window, font, "Juego en Pausa", constants.WHITE, (constants.ANCHO_VENTANA / 2, constants.ALTO_VENTANA / 2 - 50))
        display_text(window, small_font, "Presiona P para continuar", constants.WHITE, (constants.ANCHO_VENTANA / 2, constants.ALTO_VENTANA / 2 + 50))
        pygame.display.flip()              
            
        if keys[pygame.K_p]:
            pause = False
            
    else:
        if keys[pygame.K_p]:
            pause = True   
            
            
    # Mover el jugador
        if keys[pygame.K_a]:
            player.shape.x -= constants.VELOCIDAD_PERSONAJE
        if keys[pygame.K_d]:
            player.shape.x += constants.VELOCIDAD_PERSONAJE
        if keys[pygame.K_w]:
            player.shape.y -= constants.VELOCIDAD_PERSONAJE
        if keys[pygame.K_s]:
            player.shape.y += constants.VELOCIDAD_PERSONAJE
    
    # Limpiar pantalla
        window.fill(constants.BLACK)
    
    
    # Enemigos
        for enemy in enemies:
            enemy.move()
            enemy.draw(window, constants.COLOR_ENEMIGO)
        
    # Jugador
        player.draw_player(window)
    
    # Power-Ups
        for power_up in power_ups:
            power_up.move()
            power_up.draw(window)
        
        for shield_power_up in shield_power_ups:
            shield_power_up.move()
            shield_power_up.draw(window)
        
    # Colisiones con enemigos
        if detect_collision(player.shape.topleft, constants.ALTO_PERSONAJE, [(e.x, e.y) for e in enemies], constants.TAMAÑO_ENEMIGO):
            if not shield_active:
                game_over = True
                
    # Colisiones con Power-Ups
        if detect_powerup_collision(player.shape.topleft, constants.ALTO_PERSONAJE, [(p.x, p.y) for p in power_ups], constants.TAMAÑO_POWER_UP):
            score += 50  # Aumentar puntuación al recoger un power-up
            power_ups = [PowerUp(constants.ANCHO_VENTANA, constants.ALTO_VENTANA, constants.TAMAÑO_POWER_UP) for _ in range(2)]  # Generar nuevos power-ups

        if detect_powerup_collision(player.shape.topleft, constants.ALTO_PERSONAJE, [(s.x, s.y) for s in shield_power_ups], constants.TAMAÑO_POWER_UP):
            shield_active = True
            shield_duration = 300  # Duración del escudo en cuadros
            shield_power_ups = [ShieldPowerUp(constants.ANCHO_VENTANA, constants.ALTO_VENTANA, constants.TAMAÑO_POWER_UP) for _ in range(1)]  # Generar nuevos power-ups de escudo

        if shield_active:
            shield_duration -= 1
            if shield_duration <= 0:
                shield_active = False

            
    # Aumentar puntuacion y velocidad con el tiempo
        score += 1
        if score % 100 == 0:
            for enemy in enemies:
                enemy.speed += 1
            
    # Puntuacion
        display_text(window, small_font, f"Puntuación: {score}", constants.WHITE, (constants.ANCHO_VENTANA - 150, 30))
        pygame.display.flip()
        
        
    pygame.time.Clock().tick(constants.FPS)
            
        
pygame.quit()
sys.exit()
    
