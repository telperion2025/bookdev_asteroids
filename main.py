import pygame
import sys

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# In main.py import the log_state function from the logger module 
# that you created in the last assignment
from logger import log_event, log_state

def main():
    # Initialize pygame using the pygame.init() function at the beginning of your program.
    pygame.init()
    
    # Before the game loop starts, create two new empty groups in main.py:
    #   updatable – this will hold all the objects that can be updated
    #   drawable – this will hold all the objects that can be drawn
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
                                                    
    # This checks whether pygame has been properly initialised
    # print(pygame.get_init())

    # After initializing pygame, but before the game loop starts, create
    # A new clock object using pygame.time.Clock.
    clock = pygame.time.Clock()
    # A dt variable set to 0
    dt = 0

    # Use pygame's display.set_mode function to get a new instance of GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Add the Player class to the updatable and drawable groups 
    # before the player object instance is created
    # Do the same for asteroids
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    # instantiate a Player object. You can pass these values 
    # to the constructor to spawn it in the middle of the screen
    # x = SCREEN_WIDTH / 2
    # y = SCREEN_HEIGHT / 2
    ship = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    # Create the game loop
    # Use an infinite while loop for the game loop. At each iteration, it should:
    #   1.  Call log_state() – no arguments needed.
    #   2.  Use the screen's .fill method to fill the screen with a solid "black" color 
    #       (you can literally just pass the string "black" to the method).
    #   3.  Use pygame's display.flip() method to refresh the screen. 
    #       Be sure to call this last!

    while True:
        log_state()

        # Insert event "pump" within infinite loop
        # essential in Mac OS
        # This will check if the user has closed the window, 
        # and exit the game loop if they do. 
        # It will make the window's close button actually work

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # screen is an instance of the object Surface
        # fill() is a method of Surface
        screen.fill("black")

        # Hook the update method into the game loop by calling 
        # it on the updatable group of objects each frame before rendering
        updatable.update(dt)

        # After the "update" step in your game loop, 
        # iterate over all the objects in your asteroids group. 
        # Check if any of them collide with the player. 
        # If a collision is detected:
        #   Call log_event("player_hit").
        #   Print Game over! to the console.
        #   End the game immediately with sys.exit(). 
        #   (Don't forget to import sys!)

        for rock in asteroids:
            if rock.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for rock in asteroids:
            for missile in shots:
                if rock.collides_with(missile):
                    log_event("asteroid_shot")
                    rock.split()
                    missile.kill()

        # we need to re-render the player on the screen each frame, 
        # meaning inside our game loop. Use the player.draw(screen)
        # method we just added to do so.

        # You can iterate over objects in a group just like
        # any other collection in Python:
        # e.g.
        #   for thing in group:
        #       thing.do_something(some_value)
        ##
        # Loop over all "drawables" and .draw() them individually.
        for drawing in drawable:
            drawing.draw(screen)
        
        # display.flip() isn't really a method
        # instead its a function imported from the pygame "module"
        # (at least, that's how I understand it at the moment)
        pygame.display.flip()

        # At the end of each iteration of the game loop, 
        # call the .tick() method on the clock object, 
        # and pass it 60. 
        # It will pause the game loop until 1/60th of a second has passed.
        dt = clock.tick(60) / 1000
        
        # we need to re-render the player on the screen each frame, 
        # meaning inside our game loop. Use the player.draw(screen)
        # method we just added to do so.
        ship.draw(screen)


    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
