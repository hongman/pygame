import pygame ,sys
from constants import *
import SpriteSheet
from Item import Item

# Initilize Pygame
pygame.init()

# Set the width and height of the screen
screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )

# Background image
background = pygame.image.load('./black.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH,SCREEN_HEIGHT))


theClock = pygame.time.Clock()
isItem = False
Item = Item(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
game_loop = True
# Main Loop
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        
    
    screen.blit(background,(0,0))
    
    
    screen.blit(Item.image, (Item.rect.x,Item.rect.y))
    Item.update()
	
    # 아래 빈칸에 따라쳐보세요.
    # pygame.display.flip()
    
    theClock.tick(3)


# Quit
pygame.quit()
