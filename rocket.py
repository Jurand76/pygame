import pygame
from pygame.math import Vector2

class Rocket(object):

    def __init__(self, game):

        self.game = game
        size = self.game.screen.get_size()

        self.pos = Vector2(size[0]/2,size[1]/2)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)


    def add_force(self, force):
        self.acc += force
    def tick(self):
        # Input
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.add_force(Vector2(0,-2))
        if key[pygame.K_s]:
            self.add_force(Vector2(0,2))
        if key[pygame.K_a]:
            self.add_force(Vector2(-2, 0))
        if key[pygame.K_d]:
            self.add_force(Vector2(2, 0))
        # Physics
        self.vel *= .8
        self.vel -= Vector2(0,-1)
        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0


    def draw(self):
        points = [Vector2(0,-10), Vector2(5,5), Vector2(-5,5)]
        points = [Vector2(self.pos+p) for p in points]
        pygame.draw.polygon(self.game.screen,(0, 150, 255), points)

