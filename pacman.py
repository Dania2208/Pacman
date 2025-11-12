import pygame
import math
from game_object import GameObject
from constants import *

class Pacman(GameObject):
    """Pacman player class"""
    
    def __init__(self, x, y):
        super().__init__(x, y, CELL_WIDTH//1.8, CELL_HEIGHT//1.8, YELLOW)
        self.start_x = x
        self.start_y = y
        self.direction = 0  # 0=right, 1=down, 2=left, 3=up
        self.next_direction = 0
        self.speed = PACMAN_SPEED
        self.mouth_open = True
        self.mouth_timer = 0
        self.x = x - self.width // 2
        self.y = y - self.height // 2
        self.can_teleport = True
        self.teleport_cooldown = 0.     # cooldown pour empêcher Pacman de se téléporter plusieurs fois d'affilée

    def handle_input(self, key):
        """Handle keyboard input for movement"""
        # TODO: Écrire votre code ici
        if key==pygame.K_RIGHT:
            self.next_direction=0
        elif key== pygame.K_DOWN:
            self.next_direction=1
        elif key==pygame.K_LEFT:
            self.next_direction=2
        elif pygame.K_UP:
            self.next_direction=3


    
    def update(self, maze):
    #"""Update Pacman's position and state"""
    # Animation de la bouche
        self.mouth_timer += 1
        if self.mouth_timer >= 10:
            self.mouth_open = not self.mouth_open
            self.mouth_timer = 0

        # Gestion du cooldown de téléportation
        if not hasattr(self, "portal_cooldown"):
            self.portal_cooldown = 0
        if self.portal_cooldown > 0:
            self.portal_cooldown -= 1

        # Calcul de la prochaine position
        new_x, new_y, hitbox = self.get_next_position()

        # Collision avec un mur
        if not maze.is_wall_collision(hitbox):
            self.direction = self.next_direction
            self.x = new_x
            self.y = new_y

        # Vérifier collision avec un portail
        if self.portal_cooldown == 0:
            teleport_pos = maze.check_portal_collision(hitbox)
            if teleport_pos:
                #entrer Pacman sur le portail
                self.x = teleport_pos[0] - self.width // 2
                self.y = teleport_pos[1] - self.height // 2
                self.portal_cooldown = 30  # ⏱️ empêche de re-téléporter pendant 30 frames


    def get_next_position(self):
       
        new_x, new_y = self.x, self.y
       

        # TODO: Écrire votre code ici
        if self.next_direction==0:
            new_x+=self.speed
        elif self.next_direction==1:
            new_y+=self.speed
        elif self.next_direction==2:
            new_x-=self.speed
        elif self.next_direction==3:
            new_y-=self.speed
            
        hitbox = pygame.Rect(new_x,new_y,self.width,self.height)
        return new_x, new_y, hitbox
    
    def draw(self, screen):
        
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        radius = self.width // 2
        mouth_angle = 60 

        # TODO: Écrire votre code ici
        # Pacman body
        if not self.mouth_open:
            pygame.draw.circle(screen,(255, 255, 0),(center_x,center_y),radius)
        else:
            centre_angle = 0
            if self.direction == 0:   # droite
                centre_angle = 0
            elif self.direction == 1: # bas
                centre_angle = 90
            elif self.direction == 2: # gauche
                centre_angle = 180
            elif self.direction == 3: # haut
                centre_angle = 270

            start_angle = centre_angle + mouth_angle // 2
            end_angle = centre_angle + 360 - mouth_angle // 2
        

            points = [(center_x, center_y)]

            for angle in range(start_angle, end_angle + 1, 5):
                rad = math.radians(angle)
                x = center_x + int(radius * math.cos(rad))
                y = center_y + int(radius * math.sin(rad))
                points.append((x, y))
            pygame.draw.polygon(screen, (255, 255, 0), points)
            
        # Pacman eye
        eye_offset = radius // 2
        eye_radius = radius // 5
        if self.direction == 0:  # droite
            eye_x = center_x + eye_offset // 2
            eye_y = center_y - eye_offset
        elif self.direction == 1:  # bas
            eye_x = center_x + eye_offset
            eye_y = center_y - eye_offset // 2
        elif self.direction == 2:  # gauche
            eye_x = center_x - eye_offset // 2
            eye_y = center_y - eye_offset
        elif self.direction == 3:  # haut
            eye_x = center_x - eye_offset
            eye_y = center_y - eye_offset // 2
        pygame.draw.circle(screen, (0, 0, 0), (eye_x, eye_y), eye_radius)
    
    def reset_position(self):
        """Reset Pacman to starting position"""
        self.x = self.start_x - self.width // 2
        self.y = self.start_y - self.height // 2
        self.direction = 0
        self.next_direction = 0