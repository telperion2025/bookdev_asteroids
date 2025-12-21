import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# In main.py import the log_state function from the logger module 
# that you created in the last assignment:
from logger import log_state


def main():
    # Initialize pygame using the pygame.init() function at the beginning of your program.
    pygame.init()
    
    # This checks whether pygame has been properly initialised
    # print(pygame.get_init())

    # After initializing pygame, but before the game loop starts, create
    # A new clock object using pygame.time.Clock.
    clock = pygame.time.Clock()
    # A dt variable set to 0
    dt = 0




    # Use pygame's display.set_mode function to get a new instance of GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

        # display.flip() isn't really a method
        # instead its a function imported from the pygame "module"
        # (at least, that's how I understand it at the moment)
        pygame.display.flip()

        # At the end of each iteration of the game loop, 
        # call the .tick() method on the clock object, 
        # and pass it 60. 
        # It will pause the game loop until 1/60th of a second has passed.
        dt = clock.tick(60) / 1000
        
 

    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
