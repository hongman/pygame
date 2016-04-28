# -*- coding: utf-8 -*-
import pygame, sys, random
from pygame.locals import *  
  
pygame.init() #pygame initialize  

mainClock = pygame.time.Clock() # for control pygame loop speed per second

#############default value setup#############

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
#before display setup, you can use variable for 'tuple'
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # setup window size  
pygame.display.set_caption('pizza chicken baby baㄴㄴㄴby') # setup name  


#############loop start#############
while True: #loop start  
    for event in pygame.event.get(): # handle event  
        if event.type == QUIT:       # select 'x' button  
            pygame.quit()            # pygame library exit  
            sys.exit()               # program exit

    pygame.display.update()      # draw screen on loop  
    mainClock.tick(60) # setup loop speed per second 