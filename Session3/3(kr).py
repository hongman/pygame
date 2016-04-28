# -*- coding: utf-8 -*-
import pygame, sys, random
from pygame.locals import *  
  
pygame.init() #pygame 시작

mainClock = pygame.time.Clock() # pygame의 속도를 조절 하기 위한 clock 선언 부분

#############기본 값 설정 부분#############

WINDOWWIDTH = 1024
WINDOWHEIGHT = 768
#화면 크기 설정에는 python의 'tuple' 자료형을 넣으셔야 합니다. 
#tuple 자료 : https://wikidocs.net/15
windowSurface = pygame.display.set_mode( (WINDOWWIDTH, WINDOWHEIGHT) ) #(값, 값) 이 tuple 자료형 입니다.  
pygame.display.set_caption('가나다라마바사') # 게임 이름 설정  


#Section2('플레이어' 및 게임의 다른 개체들 생성을 위한 정의 부분)
player = pygame.Rect(200,400,150,150) #사각형(rect) 개체의 기본 설정 부분(세로 시작 위치, 가로 시작 위치, 개체의 가로 폭, 개체의 세로 폭)

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

#Section2('플레이어' 및 게임의 다른 개체들의 이미지 변경 및 크기 조절 부분)
playerImage= pygame.image.load('junggi.png') #이미지를 바꾸시고 싶으시면 프로젝트 폴더에 사진을 추가하신 뒤, 파일명과 확장자를 바꿔주세요.
playerImage = pygame.transform.scale(playerImage, (150,150)) #위에서 만든 개체의 크기완 다르게, 사각형위에 보여질 이미지의 크기를 설정합니다.
agooseImage = pygame.image.load('agoose.png') 
agooseImage= pygame.transform.scale(agooseImage, (80,80)) 
chickImage = pygame.image.load('chicken.png') 
chickImage= pygame.transform.scale(chickImage, (80,40)) 
pizzaImage = pygame.image.load('pizza.png') 
pizzaImage= pygame.transform.scale(pizzaImage, (60,60)) 


#Section3(키 이벤트 추가를 위한 기본 정의)
moveLeft=False #컴퓨터에선 False는 0, True는 1의 값을 가집니다. 왼쪽에 대한 키 움직임을 위해 변수를 미리 0으로 정의해 놓은 것입니다.
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 5

while True: #loop start  
    
    for event in pygame.event.get(): # handle event  
        if event.type == QUIT:       # select 'x' button  
            pygame.quit()            # pygame 라이브러리를 종료합니다  
            sys.exit()               # 프로그램을 종료합니다.
    #Section3(키 이벤트에 대한 설정을 추가하는 부분, event for문 안에 꼭 넣어주셔야 합니다!)
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'): #만약 a키를 누르거나 왼쪽 방향 키를 눌렀다면~
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
    windowSurface.fill((0,0,0)) # 플레이어가 지나간 자리의 자취를 없애는 부분입니다. 화면이 지속적으로 업데이트 되므로 배경색과 맞추어 그 자취를 없애줍니다.
    windowSurface.blit(playerImage,player)     #플레이어 생성

    for i in range(len(agooses)):
      windowSurface.blit(agooseImage,agooses[i])#agoose 생성

    for i in range(len(chicks)):
      windowSurface.blit(chickImage,chicks[i])#치킨 생성

    for i in range(len(pizzas)):
      windowSurface.blit(pizzaImage,pizzas[i])#피자 생성

    #Section3(키 이벤트에 대한 설정을 추가하는 부분, event for문 안에 꼭 넣어주셔야 합니다!)                       
    if moveDown and player.bottom < WINDOWHEIGHT:  #캐릭터가 화면 크기의 경계 부분에 접근할 때 어떻게 해줄지에 관한 부분입니다. 
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0 :
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.left += MOVESPEED


    pygame.display.update()      # 루프를 돌면서 계속 화면을 갱신해줍니다.  
    mainClock.tick(60) # 기본 설정에서 해주었던 루프의 시간을 초당 60번 돌게 설정합니다.
