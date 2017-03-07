import pygame
import time
import random
pygame.init()
white=(0,110,0)
red=(255,0,0)
black=(0,0,0)
c=(200,0,200)
width = 800
height = 600
blocksize = 10
fps = 30
a=0
gamedisplay=pygame.display.set_mode((width,height))
number = pygame.font.Font(None,100)
font = pygame.font.SysFont(None,25)
clock=pygame.time.Clock()


def message(msg,color):
    screen_text = font.render(msg,True,color)
    gamedisplay.blit(screen_text,[width/2-80,height/2])
def creator(msg,color):
    screen_text = font.render(msg,True,color)
    gamedisplay.blit(screen_text,[width/2-40,height/2+25])
def score(msg,color):
    screen_text = font.render(msg,True,color)
    gamedisplay.blit(screen_text,[width/2,height/2-30])   
def snake(blocksize,snakelist):
    for xny in snakelist:
        pygame.draw.rect(gamedisplay,black,[xny[0],xny[1],blocksize,blocksize])
    
def gameloop():
    gameexit = False
    gameover = False
    x=width/2
    y=height/2
    x1=0
    y1=0
    a=0
    snakelist = []
    snakelength = 1
    rx = round(random.randrange(0,width-blocksize)/10.0)*10.0
    ry = round(random.randrange(0,height-blocksize)/10.0)*10.0
    while not gameexit:
        while gameover == True:
            gamedisplay.fill(black)
            score("SCORE: "+str(a),red)
            message("Press c to playagain and q to quit",red)
            creator("MILAN RPODUCTION",c)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameexit = True
                    gameover = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameexit = True
                        gameover = False
                    if event.key == pygame.K_c:
                        gameloop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1= -blocksize
                    y1=0
                elif event.key == pygame.K_RIGHT:
                    x1= blocksize
                    y1=0
                elif event.key == pygame.K_UP:
                    y1= -blocksize
                    x1=0
                elif event.key == pygame.K_DOWN:
                    y1= blocksize
                    x1=0
        if x>=width or x<0 or y>=height or y<0:
            gameover = True      
        x+=x1
        y+=y1
        pygame.display.set_caption('score: '+str(a))
        gamedisplay.fill(white)
        pygame.draw.rect(gamedisplay,red,[rx,ry,blocksize,blocksize])
        snakehead = []
        snakehead.append(x)
        snakehead.append(y)
        snakelist.append(snakehead)
        if len(snakelist)>snakelength:
            del snakelist[0]
        for segment in snakelist[:-1]:
            if segment == snakehead:
                gameover = True
        snake(blocksize,snakelist)
        pygame.display.update()
        if x == rx and y == ry:
            rx = round(random.randrange(0,width-blocksize)/10.0)*10.0
            ry = round(random.randrange(0,height-blocksize)/10.0)*10.0
            snakelength+=1
            a+=5
        clock.tick(fps)
    pygame.quit()
    quit()
gameloop()


