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
        self.transparency = 255

    def add_force(self, force):
        self.vel += force

    def is_dead(self):
        return self.vel[1] > 0

    def update_transparency(self, t):
        self.transparency -= t
        if self.transparency < 0:
            return True
        return False

    def update(self):
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

    def draw(self, color):
        if color != white:
            pygame.draw.circle(self.screen, (color[0], color[1], color[2], self.transparency), (int(self.pos[0]), int(self.pos[1])), 6)
        else:
            # print  (self.col[0], self.col[1], self.col[2], self.transparency)
            pygame.draw.circle(self.screen, (self.col[0], self.col[1], self.col[2], self.transparency), (int(self.pos[0]), int(self.pos[1])), 3)
