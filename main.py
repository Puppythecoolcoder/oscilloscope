import pygame
import soundfile as sf
import math
pygame.init()

print("Welcome to my oscilloscope.\n Keybinds:\n Space key: stop\n Right key: forward \n Left key: backward")


file = input(r"Enter the file: ")

data, sr = sf.read(file)

#creating and setting up the pygame window
screen_width=1280
screen_height=690
screen=pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

run = True
offset = 0
speed = 1
paused = False

t = 0

while run:
    dt = clock.tick(60)/1000
    

    #check if player closes the window
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    
    #fill the screen with black
    screen.fill((0, 0, 0))

    #detect key press
    key = pygame.key.get_pressed()

    if (key[pygame.K_SPACE]):
        if t==5:
            if paused == True:
                paused = False
                t = 0
            else:
                paused = True
                t = 0

    if (key[pygame.K_RIGHT]):
        offset+=100

    if (key[pygame.K_LEFT] and offset>100):
        offset-=100


    #draws the wave on screen

    pygame.draw.line(screen, (240, 0, 0), (0, screen_height/2), (screen_width, screen_height/2), 2)

    for i in range(screen_width):
        pygame.draw.line(screen, (255, 255, 255), (i, data[int(i+offset)][0]*600+screen_height/2), (i+1, data[int(i+offset)+1][0]*600+screen_height/2), 1)

    
    if not paused:
        offset += sr * dt * speed

    #update the screen
    pygame.display.update()
    t+=1

pygame.quit()
