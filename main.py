import pygame
import sys
from rocket import Rocket


class Game(object):
    def __init__(self):
        # Configuration
        self.max_fps = 40
        self.box = pygame.Rect(10, 10, 50, 50)

        # Initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.fps_clock = pygame.time.Clock()
        self.fps_delta = 0.0
        self.player = Rocket(self)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # Ticking
            self.fps_delta += self.fps_clock.tick() / 1000.0
            while self.fps_delta > 1 / self.max_fps:
                self.tick()
                self.fps_delta -= 1 / self.max_fps

            # Rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):
        keys = pygame.key.get_pressed()
        self.player.tick()

    def draw(self):
        self.player.draw()


if __name__ == "__main__":
    Game()
