"""PyWeek Contest 2020 by GUVI"""
"""PySnake Game Created by J.KALIRAJ"""
"""GUVI ID : """


import pygame
import random

pygame.init()

gray= (180,180,180)
gray2= (200,200,200)
white= (255,255,255)
black= (0,0,0)
red = (244,0,6)
green = (0,155,0)

display_width = 800
display_height = 600
block_size =20
appleThickness = 30
FPS = 10

img = pygame.image.load('Files/Snakehead.png')
appleimg= pygame.image.load('Files/Apple.png')

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('PySnake 2020')
pygame.display.update()
pygame.display.set_icon(img)

clock = pygame.time.Clock()

smallfont= pygame.font.SysFont(None, 25)
medfont= pygame.font.SysFont(None, 50)
largefont= pygame.font.SysFont("comicsansms", 80)

def gameIntro():
    intro = True
    introimg = pygame.image.load('Files/introimg.png')
    gameDisplay.blit(introimg, (0,0))
    pygame.mixer.music.set_volume(0.1)
    menu_song = pygame.mixer.music.load("Files/menu.ogg")
    pygame.mixer.music.play(-1)
    while intro:
        #gameDisplay.fill(gray)
        #message_to_screen("PyWeek Contest 2020", red, -250, "medium")
        #message_to_screen("Welcome to PySnake", green, -150, "large")
        #message_to_screen("Press C to Continue", green, 150, "medium")
        #message_to_screen("Press H to Help", green, 180, "medium")
        #message_to_screen("Press Q to Quit", red, 210, "medium")
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_e:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_p:
                    intro = False
                    pygame.mixer.music.stop()
                    ready = pygame.mixer.Sound('Files/getready.ogg')
                    ready.play()
                    gameDisplay.fill(black)
                    message_to_screen("Get Ready!", green, 50, "medium")
                    pygame.display.update()
                    pygame.time.wait(3000)
                    
                    gameLoop()
                elif event.key == pygame.K_h:
                    helper()
            if event.type == pygame.QUIT :
                pygame.quit
                quit()
        
        pygame.display.update()
        clock.tick(5)
    

def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, red)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def helper():
    helpmenu = True
    gameDisplay.fill(white)
    message_to_screen("GAMEPLAY", red, -210, "medium")
    message_to_screen("* The objective of the game is to eat red apples", green, -170)
    message_to_screen("* The more apples you eat, the longer you become", green, -140)
    message_to_screen("* You will lose if you collide with yourself or the edges", green, -110)
    message_to_screen("CONTROLS", red, -20, "medium")
    message_to_screen("* Use Arrow keys for Movement/Direction", green, 10)
    message_to_screen("* Press ESCAPE key for Pause", green, 40)
    message_to_screen("* Press C to Continue, Q to Quit", green, 70)
    message_to_screen("Press B to Back",black, 250, "medium")
    draw_text(gameDisplay,"Credits : PyWeek Contest 2020 GUVI TEAM & NEC COLLAGE KOVILPATTI" , 14, 400, 580)
    
    pygame.display.update()
    while helpmenu:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_b:
                    gameIntro()
                    intro = True
            if event.type == pygame.QUIT :
                pygame.quit
                quit()

def pause():
    paused = True
    message_to_screen("Paused", black, -50, "large")
    message_to_screen("Press C to continue or Q to quit ", black, 20)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_c:
                    paused = False
            if event.type == pygame.QUIT :
                pygame.quit
                quit()

        clock.tick(5)

def score(score):
    img1 = pygame.image.load('Files/score.jpg')
    gameDisplay.blit(img1, (10,-10))
    draw_text(gameDisplay,str(score) , 30, 180, 5)
    global finalscore
    finalscore=str(score)
    myscore=int(score)
    global level
    level = 1
                 
    if myscore >= 50:
        level = level +1
    if myscore >= 100:
        level = level +1
    if myscore >= 200:
        level = level +1
    if myscore >= 500:
        level = level +1
    img1 = pygame.image.load('Files/level.jpg')
    gameDisplay.blit(img1, (600,-5))
    draw_text(gameDisplay,str(level) , 30, 750, 5)

def apple(applex, appley):
    gameDisplay.blit(appleimg, (applex, appley))
    
def randAppleGen():
    randapple_y = round(random.randrange(30,display_height - appleThickness))
    randapple_x = round(random.randrange(30,display_width - appleThickness))
    return randapple_x, randapple_y

def snake(snakeList, block_size):

    if direction == 'right':
        head= pygame.transform.rotate(img, 270)
    if direction == 'left':
        head= pygame.transform.rotate(img, 90)
    if direction == 'up':
        head= pygame.transform.rotate(img, 0)
    if direction == 'down':
        head= pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

    for XnY in snakeList[:-1] :
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_Objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color,y_displace =0, size = "small"):
    
    textSurf, textRect = text_Objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf,textRect)
    
def gameLoop():
    menu_song = pygame.mixer.music.load("Files/menu.ogg")
    pygame.mixer.music.play(-1)
    global direction
    global mode
    direction = 'right'
    gameExit= False
    gameOver= False
    snakeList = []
    snakeLength = 1
    growthperapple =1
    snakeSpeed = block_size
    
    lead_x = display_width/2
    lead_y = display_height/2
    lead_xchange= snakeSpeed
    lead_ychange= 0
    randapple_x, randapple_y = randAppleGen()
    
    while not gameExit:
        if gameOver == True:
            #gameDisplay.fill(white)
            pygame.mixer.music.pause()
            ready = pygame.mixer.Sound('Files/gameover.wav')
            ready.play()
            img1 = pygame.image.load('Files/gameover.jpg')
            gameDisplay.blit(img1, (0,0))
            draw_text(gameDisplay,finalscore , 30, 430, 340)
            pygame.display.update()
        while gameOver == True:
                        
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                        pygame.quit
                        quit()
                    elif event.key == pygame.K_c:
                        gameLoop()
                if event.type == pygame.QUIT :
                    gameOver = False
                    gameExit = True
                    pygame.quit
                    quit()

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT :
                gameExit = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RIGHT:
                    lead_xchange = snakeSpeed
                    lead_ychange = 0
                    direction= 'right'
                if event.key == pygame.K_LEFT:
                    lead_xchange = -snakeSpeed
                    lead_ychange = 0
                    direction= 'left'
                if event.key == pygame.K_DOWN:
                    lead_ychange = snakeSpeed
                    lead_xchange = 0
                    direction= 'down'
                if event.key == pygame.K_UP:
                    lead_ychange = -snakeSpeed
                    lead_xchange = 0
                    direction= 'up'
                if event.key == pygame.K_ESCAPE:
                    pause()
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_xchange
        lead_y += lead_ychange

        if lead_x >= randapple_x and lead_x < randapple_x +appleThickness or lead_x + block_size > randapple_x and lead_x + block_size < randapple_x + appleThickness:
            
            if lead_y >= randapple_y and lead_y <randapple_y +appleThickness or lead_y + block_size > randapple_y and lead_y + block_size < randapple_y + appleThickness:
                randapple_x, randapple_y = randAppleGen()
                snakeLength += growthperapple
                
        gameDisplay.fill(white)
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) >(snakeLength):
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead :
                gameOver = True

        apple(randapple_x,randapple_y)
        snake(snakeList, block_size)
        score((snakeLength-1)*10)
        pygame.display.update()
        clock.tick(FPS)
        
gameIntro()

pygame.quit
quit()
