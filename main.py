import pygame
import sys
import math
from random import random, randint
from pygame import Vector3
from particle import Particle

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
        for f in fireworks:
            f.add_force(gravity)
            f.update()
        if random() < 0.05:
            fireworks.append(Particle(screen, Vector3(randint(0, width), height, 0), Vector3(0, randint(-16, -10), 0)))

    # Draw
    screen.fill(black)

    for f in fireworks:
        f.draw()

    pygame.display.flip()
