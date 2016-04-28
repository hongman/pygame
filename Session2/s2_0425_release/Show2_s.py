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
ItemList = []
max_cnt = 5
for i in range(0,max_cnt):
    ItemList.append(Item(0,0))

game_loop = True
game_loop_cnt = 1

# Main Loop
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
			
    if game_loop_cnt!=0:
        ItemList[game_loop_cnt].change_rect_y(game_loop_cnt*100)
	
    # Draw the background
    screen.blit(background,(0,0))
    
    # Draw Items
    for i in range(0,game_loop_cnt):
        #ItemList[i].update()
        #screen.blit(ItemList[i].image, (ItemList[i].rect.x,ItemList[i].rect.y))
        
        
        pass
        
    


		
    # Gp ahead and upadate the screen with what we've drawn.
    pygame.display.flip()
    theClock.tick(3)
    if game_loop_cnt < max_cnt-1	:
        game_loop_cnt = game_loop_cnt + 1


# Quit
pygame.quit()
