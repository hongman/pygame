import pygame ,sys, random
from constants import *
import SpriteSheet
from Item import Item

# Initilize Pygame
pygame.init()

# Set the width and height of the screen
screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )

# ./black.png에 마음에 드는 사진을 넣어보세요 !
background = pygame.image.load('./black.png')
background = pygame.transform.scale(background, (SCREEN_WIDTH,SCREEN_HEIGHT))


theClock = pygame.time.Clock()
isItem = False
ItemList = []
# 아래 10을 마음껏 바꿔보세요 !
max_cnt = 10
for i in range(0,max_cnt):
    ItemList.append(Item(0,0))

game_loop = True
game_loop_cnt = 0
# Main Loop
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
			
    if game_loop_cnt!=max_cnt:
        #ItemList[game_loop_cnt].change_rect(random.randint(0, SCREEN_WIDTH - ITEM_WIDTH), random.randint(0, SCREEN_HEIGHT - ITEM_HEIGHT))
        pass

	
    # Draw the background
    screen.blit(background,(0,0))
    
    # Draw & Update Items
    for i in range(0,game_loop_cnt):
        ItemList[i].update()
        screen.blit(ItemList[i].image, (ItemList[i].rect.x,ItemList[i].rect.y))
   
	

    # Gp ahead and upadate the screen with what we've drawn.
    pygame.display.flip()
    theClock.tick(3)
    if game_loop_cnt < max_cnt-1	:
        game_loop_cnt = game_loop_cnt + 1


# Quit
pygame.quit()
