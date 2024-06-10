import sys

import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""
    def __init__(self):
        """Initialize the game, and create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            #Watch the keyboard and mouse events.
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()
            #Redraw the screen during teach pass through loop
            self.screen.fill(self.bg_color)

            #Make ther most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make the game instance, and run the game
    ai =AlienInvasion()
    ai.run_game()
