import pygame
from constants2 import *

class PuppySpriteSheet(object):
    
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        # Create a new blank image
        image = pygame.Surface([width,height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0,0), (x,y,width,height))

        # Assuming blank works as the transparent color
        image.set_colorkey(YELLOW)

        # Return the imagei
        return image
	
