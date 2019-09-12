import pygame
import sys
import math
from random import random, randint
from pygame import Vector3
from particle import Particle

white = Vector3(255, 255, 255)
black = Vector3(0, 0, 0)
red = Vector3(255, 0, 0)


class Firework:
    def __init__(self, screen, width, height, gravity):
        self.screen = screen
        self.width = width
        self.height = height
        self.gravity = gravity

        self.firework = Particle(screen, Vector3(randint(0, width), height, 0), Vector3(0, randint(-16, -10), 0))
        self.exploded = False
        self.particles = []

    def update(self):
        if not self.exploded:
            self.firework.add_force(self.gravity)
            self.firework.update()
            self.exploded = self.firework.is_dead()
            if self.exploded:
                for i in range(300):
                    r = (random() * 360) * math.pi / 180
                    f = random() * 4
                    self.particles.append(Particle(self.screen, Vector3(self.firework.pos), Vector3(math.sin(r) * f, math.cos(r) * f, 0)))

        for i in range(len(self.particles)-1, -1, -1):
            self.particles[i].add_force(self.gravity)
            if self.particles[i].update_transparency(7):
                self.particles.pop(i)
            else:
                self.particles[i].update()

    def draw(self):
        if not self.exploded:
            self.firework.draw(white)
        for p in self.particles:
            p.draw(white)
