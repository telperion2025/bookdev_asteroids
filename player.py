import pygame

from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED,PLAYER_SPEED

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y, PLAYER_RADIUS)
        self.rotation = 0

    # in the Player class
    # Paste the triangle method below into your Player class. 
    # A player will look like a triangle, even though 
    # we'll use a circle to represent its hitbox. 
    # The math of drawing a triangle can be a bit tricky, 
    # so we've written the method for you

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # To draw the player, override the draw method of CircleShape. 
    # It should take the screen object as a parameter, 
    # and call pygame.draw.polygon(). 
    # It takes as inputs:
    # * The screen object
    # * A color (use "white")
    # * A list of points (use the list returned by a call 
    #   to the self.triangle() function)    
    # * A line width (use the one in your constants.py file)

    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),LINE_WIDTH)
    
    # dd a new rotate method to the Player class. 
    # It takes one argument: dt (I told you we'd use it!). 
    # When it's called, it should add PLAYER_TURN_SPEED * dt 
    # to the player's current rotation.

    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    # update method
    # call the rotate method with the dt argument. 
    # To go left instead of right when a is pressed, 
    # you'll need to reverse dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector