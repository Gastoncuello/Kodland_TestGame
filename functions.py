import pygame
import random
import constants


class Personaje():
    def __init__(self, x , y):
        self.shape = pygame.Rect(0, 0, constants.ANCHO_PERSONAJE, constants.ALTO_PERSONAJE)
        self.shape.center = (x, y)
    
    def draw_player(self, interfaz):
        pygame.draw.rect(interfaz, constants.COLOR_PERSONAJE, self.shape)
        
        
class Enemigo():
    def __init__(self, screen_width, screen_height, size, speed):
        self.screen_width = screen_width
        self.screen_height = screen_height        
        self.size = size
        self.speed = speed
        self.x = random.randint(0, screen_width - size)
        self.y = random.randint(-screen_height, 0)
        
    def move(self):
        self.y += self.speed
        if self.y > self.screen_height:
            self.y = 0
            self.x = random.randint(0, self.screen_width - self.size)
    
    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.size, self.size))


class PowerUp:
    def __init__(self, screen_width, screen_height, size):
        self.size = size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(0, screen_width - size)
        self.y = random.randint(-screen_height, 0)
        self.color = (0, 255, 0)
        
    def move(self):
        self.y += 5  # Velocidad del power-up
        if self.y > self.screen_height:
            self.y = 0
            self.x = random.randint(0,self.screen_width - self.size)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
    

class ShieldPowerUp(PowerUp):
    def __init__(self, screen_width, screen_height, size):
        super().__init__(screen_width, screen_height, size)
        self.color = (0, 0, 255)
    
    def draw(self, screen):
         pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))



def display_text(screen, font, message, color, center):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=center)
    screen.blit(text, text_rect)

def detect_collision(player_position, player_size, enemies, enemy_size):
    for enemy_pos in enemies:
        if (player_position[0] < enemy_pos[0] < player_position[0] + player_size or player_position[0] < enemy_pos[0] + enemy_size < player_position[0] + player_size) and \
           (player_position[1] < enemy_pos[1] < player_position[1] + player_size or player_position[1] < enemy_pos[1] + enemy_size < player_position[1] + player_size):
            return True
    return False

def detect_powerup_collision(player_position, player_size, power_ups, power_up_size):
    for powerup_pos in power_ups:
        if (player_position[0] < powerup_pos[0] < player_position[0] + player_size or player_position[0] < powerup_pos[0] + power_up_size < player_position[0] + player_size) and \
           (player_position[1] < powerup_pos[1] < player_position[1] + player_size or player_position[1] < powerup_pos[1] + power_up_size < player_position[1] + player_size):
            return True
    return False