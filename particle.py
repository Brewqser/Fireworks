import pygame
import sys
import math
from pygame import Vector3

white = Vector3(255, 255, 255)
black = Vector3(0, 0, 0)
red = Vector3(255, 0, 0)


class Particle:
    def __init__(self, screen, pos=Vector3(0, 0, 0), vel=Vector3(0, 0, 0), col=white):
        self.screen = screen
        self.pos = pos
        self.vel = vel
        self.acc = Vector3(0, 0, 0)
        self.col = col

    def add_force(self, force):
        self.vel += force

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self):
        pygame.draw.circle(self.screen, self.col, (int(self.pos[0]), int(self.pos[1])), 6)
