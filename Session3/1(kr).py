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

while True: #loop start  
    
    for event in pygame.event.get(): # handle event  
        if event.type == QUIT:       # select 'x' button  
            pygame.quit()            # pygame 라이브러리를 종료합니다  
            sys.exit()               # 프로그램을 종료합니다.

    pygame.display.update()      # 루프를 돌면서 계속 화면을 갱신해줍니다.  
    mainClock.tick(60) # 기본 설정에서 해주었던 루프의 시간을 초당 60번 돌게 설정합니다.
