import pygame
import sys
import math

pygame.init()
width, height = 1600, 800
cx, cy = width // 2, height // 2
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

tps = 60.0
tps_dt = 0

while True:
    dt = clock.tick() / 1000.0

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Tick ( update )
    tps_dt += dt
    while tps_dt > 1 / tps:
        tps_dt -= 1 / tps

    # Draw
    screen.fill(white)



    pygame.display.flip()