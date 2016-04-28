import pygame
from constants2 import *
import PuppySpriteSheet

class Puppy(pygame.sprite.Sprite):
    

    def __init__(self):
        # Call the parent's constructor
        super().__init__()
        
        sprite_sheet = PuppySpriteSheet.PuppySpriteSheet('./char.png')
        
        self.animations = []

        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 100, 127)
        #image = pygame.transform.scale(image, (75,94))
        self.animations.append(image)
        image = sprite_sheet.get_image(100, 0, 100, 127)
        #image = pygame.transform.scale(image, (75,94))
        self.animations.append(image)
        image = sprite_sheet.get_image(200, 0, 100, 127)
        #image = pygame.transform.scale(image, (75,94))
        self.animations.append(image)
        image = sprite_sheet.get_image(100, 0, 100, 127)
        #image = pygame.transform.scale(image, (75,94))
        self.animations.append(image)

        # Set the animation frame
        self.animation_frame = 0

        # Set the image the player starts with
        self.image = self.animations[self.animation_frame]

        # Set a reference to image rect
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2        

        # 
        self.moveable = False
        self.actionable = False
        self.isDead = False
        # 
        self.jump = 0.0
        

    def update(self):
        if self.actionable:
            self.image = self.animations[self.animation_frame]
            self.animation_frame += 1
            self.animation_frame %= len(self.animations)


    def action(self):
        self.moveable = True
        self.actionable = True

