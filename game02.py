import pygame
from pygame import Color
pygame.init()
clock = pygame.time.Clock()
size = (600, 400) # screen size
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game02') #title of screen
running = True
frame = 0
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    color = Color((255, 0, 255)) # create object color
    screen.fill(color)
    clock.tick(30)  # 30 frame per second
    pygame.display.flip()
    frame += 1
    print(frame)
