import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Add this line to properly close pygame
                return

        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()
