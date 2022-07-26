import pygame
import math


class Envir:
    def __init__(self, dimentions):
        # colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)
        self.yel = (255, 255, 0)

        # map dimentions
        self.hight = dimentions[0]
        self.width = dimentions[1]

        # window setting
        pygame.display.set_caption("Differential rover drive")
        self.map = pygame.display.set_mode((self.width, self.hight))


# initialisation
pygame.init()

# start position
start = (200, 200)

# dimnetions
dims = (800, 1200)

# running or not
running = True

# the envir
envir = Envir(dims)


# simulation loop
while running:
    # activate quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    envir.map.fill(envir.black)
