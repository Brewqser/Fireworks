import pygame
import sys
import math
from random import random, randint
from pygame import Vector3
from firework import Firework

pygame.init()
width, height = 1600, 800
cx, cy = width // 2, height // 2
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

white = Vector3(255, 255, 255)
black = Vector3(0, 0, 0)
red = Vector3(255, 0, 0)

tps = 60.0
tps_dt = 0

fireworks = []
gravity = Vector3(0, 0.2, 0)

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
        for i in range(len(fireworks)-1, -1, -1):
            fireworks[i].update()
        if random() < 0.05:
            fireworks.append(Firework(screen, width, height, gravity))

    # Draw
    screen.fill(black)

    for f in fireworks:
        f.draw()

    pygame.display.flip()
