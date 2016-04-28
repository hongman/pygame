import pygame
from constants import *
import SpriteSheet

class Item(pygame.sprite.Sprite):

    def __init__(self,add_x,add_y):
        # Call the parent's constructor
        super().__init__()
        
        sprite_sheet = SpriteSheet.SpriteSheet('./item.png')
        
        self.animations = []

        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 100, 100)
        image = pygame.transform.scale(image, (ITEM_WIDTH,ITEM_HEIGHT))
        self.animations.append(image)
        image = sprite_sheet.get_image(100, 0, 100, 100)
        image = pygame.transform.scale(image, (ITEM_WIDTH,ITEM_HEIGHT))
        self.animations.append(image)
        image = sprite_sheet.get_image(200, 0, 100, 100)
        image = pygame.transform.scale(image, (ITEM_WIDTH,ITEM_HEIGHT))
        self.animations.append(image)

        # Set the animation frame
        self.animation_frame = 0

        # Set the image the player starts with
        self.image = self.animations[self.animation_frame]

        # Set a reference to image rect
        self.rect = self.image.get_rect()
        self.rect.x = add_x
        self.rect.y = add_y       


    def update(self):
        self.image = self.animations[self.animation_frame]
        self.animation_frame += 1
        self.animation_frame %= len(self.animations)
        
    def change_rect_y(self,y):
        self.rect.y=y
		
    def change_rect(self,x,y):
        self.rect.x=x
        self.rect.y=y
		
    def dead(self):
        pass
    
    def get_rect(self):
        return pygame.Rect(self.rect.x,self.rect.y,ITEM_WIDTH,ITEM_HEIGHT)
		

