import pygame
from pygame import Color
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
size = (600, 400) # screen size
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Game02') #title of screen
running = True
sheet = pygame.image.load('spritesheet.png')

x, y = 20, 40
frame = 0
speed = 2
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        # if e.type == KEYDOWN:
        #     if e.key in [K_a, K_LEFT]:  x += speed
        #     elif e.key in [K_d, K_RIGHT]:  x -= speed
        #     elif e.key in [K_s, K_DOWN]:  y -= speed
        #     elif e.key in [K_w, K_UP]:  y += speed
    keys = pygame.key.get_pressed()
    if keys[K_a] or keys[K_LEFT]:  x += speed
    elif keys[K_d] or keys[K_RIGHT]:  x -= speed
    elif keys[K_s] or keys[K_DOWN]:  y -= speed
    elif keys[K_w] or keys[K_UP]:  y += speed
    screen.fill((0, 0, 0))
    screen.blit(sheet, (x, y))
    clock.tick(30)  # 30 frame per second
    pygame.display.flip()
    # frame += 1
    # print(frame)
