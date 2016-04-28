import pygame ,sys
from constants2 import *
import PuppySpriteSheet
from Puppy import Puppy

# Initilize Pygame
pygame.init()

# Set the width and height of the screen
screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )

# Background image
background = pygame.image.load('./puppy_background.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH,SCREEN_HEIGHT))

# FlappyBird
puppy = Puppy()
theClock = pygame.time.Clock()


game_loop = True
# Main Loop
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            puppy.action()

    # Update the FlappyBird
    puppy.update()

    # Draw the background
    screen.blit(background,(0,0))
    
    # Draw the FlappyBird
    screen.blit(puppy.image, (puppy.rect.x,puppy.rect.y))

    # Gp ahead and upadate the screen with what we've drawn.
    pygame.display.flip()
    theClock.tick(8)


# Quit
pygame.quit()
