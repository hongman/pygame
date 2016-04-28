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
pygame.display.set_caption('my name is hongmin! hello!') # setup name  

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


#Section3(Add keyevent)

moveLeft=False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 5


#Section4(Add collision event and counting board)

getChickNum = 0 #for counting chicken removed
getPizzaNum = 0 #for counting pizza removed
scoreBoard = pygame.Rect(300,0,400,50) #positioning at (300,0), Width : 400 Height : 50 
basicfont = pygame.sysfont.SysFont("comicsansms", 40)


#############loop start#############
while True: #loop start  
    for event in pygame.event.get(): # handle event  
        if event.type == QUIT:       # select 'x' button  
            pygame.quit()            # pygame library exit  
            sys.exit()               # program exit
    #Section3(Add keyevent, this section must be within event loop) 
    
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = True
                moveLeft = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'):
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d'):
                moveRight = False
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s'):
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOWHEIGHT - player.height )
                player.left = random.randint(0, WINDOWWIDTH - player.width )              
        
    #Section2(Create player and others)
    
    windowSurface.fill((0,0,0)) # fill black before moving player
    windowSurface.blit(playerImage,player)     #create player

    for i in range(len(agooses)):
      windowSurface.blit(agooseImage,agooses[i])#create pizza

    for i in range(len(chicks)):
      windowSurface.blit(chickImage,chicks[i])#create chicken

    for i in range(len(pizzas)):
      windowSurface.blit(pizzaImage,pizzas[i])#create pizza
    
    #Section3(about keyevent)
    
    if moveDown and player.bottom < WINDOWHEIGHT:  #player.left and player.top is start point, so you can calculate this at (0,0) pixel
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0 :
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.left += MOVESPEED
    

        
    #Section4(Add collision event)
    
    for chicken in chicks[:]: 
        if player.colliderect(chicken): #if collision event         
            chicks.remove(chicken)
            getChickNum += 1 #count hamburger removed
    for pizza in pizzas[:]: 
        if player.colliderect(pizza): #if collision event 
            pizzas.remove(pizza)
            getPizzaNum += 1 #count hamburger removed
    for agoose in agooses[:]: 
        if player.colliderect(agoose): #if collision event 
            agooses.remove(agoose)
            getPizzaNum = 0 #all counting reset   
            getChickNum = 0
   

    #Section4(Creating counting board)
       
    pygame.draw.rect(windowSurface, (255,255,255), scoreBoard)
    scoreChickText = basicfont.render(str(getChickNum), True, (0,0,0))
    scorePizzaText = basicfont.render(str(getPizzaNum), True, (0,0,0))    
        
    if getChickNum == getPizzaNum:
        windowSurface.blit(scoreChickText, scoreBoard)
    elif getChickNum > getPizzaNum:
        windowSurface.blit(scorePizzaText, scoreBoard)
    else:
        windowSurface.blit(scoreChickText, scoreBoard)
   


    pygame.display.update()      # draw screen on loop  
    mainClock.tick(60) # setup loop speed per second 
