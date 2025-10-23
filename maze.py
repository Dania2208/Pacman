import pygame
from constants import *
import numpy as np

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

    def is_wall_collision(self, hitbox):
        """Check if the given rectangle collides with any walls"""
        # TODO: Écrire votre code ici
        
        return False
    
    def draw(self, screen):
        """Draw the maze on the screen"""
        
        for row in range(self.height):
            for col in range(self.width):
                if self.layout[row,col] == 1:  # Wall
                    x = col * self.cell_width
                    y = row * self.cell_height
                    wall_rect = pygame.Rect(x, y, self.cell_width, self.cell_height)
                    pygame.draw.rect(screen, BLUE, wall_rect)
                    
                    # Add border for better visibility
                    pygame.draw.rect(screen, WHITE, wall_rect, 1)
    
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