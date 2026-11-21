import pygame
import soundfile as sf
import math
pygame.init()

file = input()

data, sr = sf.read()




#creating and setting up the pygame window
screen_width=1280
screen_height=690
screen=pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

run = True
offset = 0
speed = 0.005

while run:
    dt = clock.tick(60)/1000
    

    #check if player closes the window
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    
    #fill the screen with black
    screen.fill((0, 0, 0))


    #draws the wave on screen
    for i in range(screen_width):
        pygame.draw.line(screen, (255, 255, 255), (i, data[int(i+offset)][0]*600+screen_height/2), (i+1, data[int(i+offset)+1][0]*600+screen_height/2), 2)


    offset += sr * dt * speed

    #update the screen
    pygame.display.update()

pygame.quit()
