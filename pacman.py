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

    def handle_input(self, key):
        """Handle keyboard input for movement"""
        # TODO: Écrire votre code ici

    def update(self, maze):
        """Update Pacman's position and state"""
        # Update mouth animation
        self.mouth_timer += 1
        if self.mouth_timer >= 10:
            self.mouth_open = not self.mouth_open
            self.mouth_timer = 0
        
        # Get next position based on next_direction
        new_x, new_y, hitbox = self.get_next_position()

        # Check if there is collision with a wall
        if not maze.is_wall_collision(hitbox):
            self.direction = self.next_direction
            self.x = new_x
            self.y = new_y

    def get_next_position(self):
        """
        Get the next position based on direction

        The hitbox will be used to detect collisions before moving.
        Returns new_x, new_y, hitbox
        """
        new_x, new_y = self.x, self.y
        hitbox = None

        # TODO: Écrire votre code ici
        
        return new_x, new_y, hitbox
    
    def draw(self, screen):
        """Draw Pacman with mouth animation"""
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        radius = self.width // 2

        # TODO: Écrire votre code ici
        # Draw Pacman body

        # Draw Pacman eye
    
    def reset_position(self):
        """Reset Pacman to starting position"""
        self.x = self.start_x - self.width // 2
        self.y = self.start_y - self.height // 2
        self.direction = 0
        self.next_direction = 0