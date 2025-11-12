import pygame
from constants import *
import numpy as np
import random

class Maze:
    """Maze class that handles the game board and collision detection"""
    
    def __init__(self):
        self.width = MAZE_WIDTH
        self.height = MAZE_HEIGHT
        self.cell_width = CELL_WIDTH
        self.cell_height = CELL_HEIGHT

        # Create a simple maze layout (1 = wall, 0 = empty)
        self.layout = np.array([
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1],
            [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
            [1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1],
            [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
            [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ])
        self.portal_orange = None
        self.portal_blue = None
        # Génère automatiquement les deux portails (orange et bleu) dès la création du labyrinthe
        self.generate_portals()

    def generate_portals(self): 
        # Génère deux portails (orange et bleu) à des positions aléatoires valides dans le labyrinthe
        valid_positions = self.get_valid_positions()
        self.portal_orange, self.portal_blue = random.sample(valid_positions, 2)
    
    def check_portal_collision(self, hitbox):
    #Vérifie si Pacman entre dans un des portails(rectangle:pygame.Rect(x, y, largeur, hauteur))
        if self.portal_orange and self.portal_blue:
            orange_rect = pygame.Rect(self.portal_orange[0] - 10, self.portal_orange[1] - 10, 20, 20)
            blue_rect = pygame.Rect(self.portal_blue[0] - 10, self.portal_blue[1] - 10, 20, 20)

            # Si Pacman touche le portail orange : il va au bleu
            if hitbox.colliderect(orange_rect):
                return self.portal_blue[0], self.portal_blue[1]
            # Si Pacman touche le portail bleu : il va à l’orange
            elif hitbox.colliderect(blue_rect):
                return self.portal_orange[0], self.portal_orange[1]

        return None
    def is_wall_collision(self, hitbox):
        """Check if the given rectangle collides with any walls"""
        # TODO: Écrire votre code ici
        #trouver le centre de hitbox
        center_x = hitbox.centerx
        center_y = hitbox.centery

        #trouver dans quelle colonne et ligne du labyrinthe se trouve le centre

        col_center = int(center_x // self.cell_width)
        row_center = int(center_y // self.cell_height)

        #Parcourir les 3x3 cases autour du centre
        for row in range(max(0, row_center-1), min(self.height, row_center+2)):
            for col in range(max(0, col_center-1), min(self.width, col_center+2)):
                if self.layout[row, col] == 1:  # veut dire que c un mur
                    x = col * self.cell_width
                    y = row * self.cell_height

                    wall_rect = pygame.Rect(x, y, self.cell_width, self.cell_height)
                    if hitbox.colliderect(wall_rect):
                        return True
        return False
    
    
    
    def draw(self, screen):
        #dessiner les bordures de maze:
    
        for row in range(self.height):
            for col in range(self.width):
                if self.layout[row,col] == 1:  # Wall
                    x = col * self.cell_width
                    y = row * self.cell_height
                    wall_rect = pygame.Rect(x, y, self.cell_width, self.cell_height)
                    pygame.draw.rect(screen, BLUE, wall_rect)
                    
                    # bordures
                    pygame.draw.rect(screen, WHITE, wall_rect, 1)

         # Dessiner les portails
         #pygame.draw.circle(surface, couleur, centre, rayon)
        if self.portal_orange:
            pygame.draw.circle(screen, (255, 165, 0),
                               (self.portal_orange[0], self.portal_orange[1]), 10)
        if self.portal_blue:
            pygame.draw.circle(screen, (0, 100, 255),
                               (self.portal_blue[0], self.portal_blue[1]), 10)

    
    def get_valid_positions(self):
        """Get all valid (non-wall) positions for placing objects"""
        valid_positions = []
        
        for row in range(self.height):
            for col in range(self.width):
                if self.layout[row,col] == 0:  # Empty space
                    x = col * self.cell_width + self.cell_width // 2
                    y = row * self.cell_height + self.cell_height // 2
                    valid_positions.append((x, y))

        return valid_positions
    
    