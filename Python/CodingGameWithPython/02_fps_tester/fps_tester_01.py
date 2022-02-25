#!/usr/bin/env python3
import sys
import pygame
from pygame.locals import QUIT

# --------------------------------------------------
pygame.init()
SURFACE = pygame.display.set_mode((400, 300))


# --------------------------------------------------
def main():
    """ Main function starts here """
    sys_font = pygame.font.SysFont(None, 36)
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        counter += 1
        SURFACE.fill((0, 0, 0))
        count_image = sys_font.render("Count is {}".format(counter), True, (255, 255, 255))
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()

        
# --------------------------------------------------
if __name__ == '__main__':
    main()
