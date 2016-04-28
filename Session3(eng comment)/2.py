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
pygame.display.set_caption('my name is hongmiㄴㄴㄴn! hello!') # setup name  


#Section2(Create player and others)

player = pygame.Rect(200,400,150,150) #default player position and size

AGOOSESIZE = 80
agooses = []
for i in range(0,5):
     agooses.append( pygame.Rect( random.randint(0, WINDOWWIDTH - AGOOSESIZE), random.randint(0, WINDOWHEIGHT - AGOOSESIZE), AGOOSESIZE, AGOOSESIZE) )

CHICKSIZE = 60
chicks = []
for i in range(0,20):
     chicks.append( pygame.Rect( random.randint(0, WINDOWWIDTH - CHICKSIZE), random.randint(0, WINDOWHEIGHT - CHICKSIZE), CHICKSIZE + 20, CHICKSIZE - 20) )

PIZZASIZE = 60
pizzas = []
for i in range(0,20):
     pizzas.append( pygame.Rect( random.randint(0, WINDOWWIDTH - PIZZASIZE), random.randint(0, WINDOWHEIGHT - PIZZASIZE), PIZZASIZE, PIZZASIZE) )




#Section2(Create player and others)
         
playerImage= pygame.image.load('junggi.png') #customize image
playerImage = pygame.transform.scale(playerImage, (150,150)) #customize image size
agooseImage = pygame.image.load('agoose.png') #customize image
agooseImage= pygame.transform.scale(agooseImage, (80,80)) #customize image size
chickImage = pygame.image.load('chicken.png') #customize image
chickImage= pygame.transform.scale(chickImage, (80,40)) #customize image size
pizzaImage = pygame.image.load('pizza.png') #customize image
pizzaImage= pygame.transform.scale(pizzaImage, (60,60)) #customize image size



#############loop start#############
while True: #loop start  
    for event in pygame.event.get(): # handle event  
        if event.type == QUIT:       # select 'x' button  
            pygame.quit()            # pygame library exit  
            sys.exit()               # program exit
    
    #Section2(Create player and others)
    
    windowSurface.fill((0,0,0)) # fill black before moving player
    windowSurface.blit(playerImage,player)     #create player

    for i in range(len(agooses)):
      windowSurface.blit(agooseImage,agooses[i])#create pizza

    for i in range(len(chicks)):
      windowSurface.blit(chickImage,chicks[i])#create chicken

    for i in range(len(pizzas)):
      windowSurface.blit(pizzaImage,pizzas[i])#create pizza
    
    pygame.display.update()      # draw screen on loop  
    mainClock.tick(60) # setup loop speed per second 
