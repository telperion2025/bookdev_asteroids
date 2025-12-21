import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# In main.py import the log_state function from the logger module 
# that you created in the last assignment:
from logger import log_state


def main():
    # Initialize pygame using the pygame.init() function at the beginning of your program.
    pygame.init()
    print(pygame.get_init())


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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
