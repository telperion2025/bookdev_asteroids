import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    # Override the draw() method to draw the asteroid 
    # using the pygame.draw.circle function. It accepts:
    #   The "surface" to draw on (the screen object)
    #   The color of the circle ("white")
    #   Its own position as the center
    #   Its own radius
    #   The width of the line to draw the circle (use LINE_WIDTH from constants.py)    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    # Override the update() method so that it moves 
    # in a straight line at constant speed. 
    # On each frame, it should add (self.velocity * dt) 
    # to its position 
    # (get self.velocity from its parent class, CircleShape).
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            
            new_vector1 = self.velocity.rotate(angle)
            new_vector2 = self.velocity.rotate(-angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = new_vector1 * 1.2
            asteroid2.velocity = new_vector2 * 1.2


