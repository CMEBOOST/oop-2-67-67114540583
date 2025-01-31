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
    magenta = Color((255, 0, 255)) # create object color
    black = Color((0, 0, 0))
    rect = pygame.Rect(20, 50, 200, 300)
    screen.fill(black)
    pygame.draw.rect(screen, magenta, rect)
    clock.tick(30)  # 30 frame per second
    pygame.display.flip()
    frame += 1
    print(frame)
