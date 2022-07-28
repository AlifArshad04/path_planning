from time import sleep
from turtle import width
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


class Rover:
    def __init__(self, startpos, roverImg, width):
        self.m2p = 3779.52  # meter to pixels

        # rover dimentions
        self.w = width
        self.x = startpos[0]
        self.y = startpos[1]
        self.theta = 0
        self.vl = 0.01*self.m2p  # m/s
        self.vr = 0.01*self.m2p
        self.maxspeed = 0.02*self.m2p
        self.minspeed = 0.02*self.m2p

        # graphics
        self.img = pygame.image.load(roverImg)
        self.rotated = self.img
        self.rect = self.rotated.get_rect(center=(self.x, self.y))

    def draw(self, map):
        map.blit(self.rotated, self.rect)

    def move(self, event=None):
        if event is not None:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    self.vl += 0.001*self.m2p
                elif event.key == pygame.K_k:
                    self.vl -= 0.001*self.m2p
                elif event.key == pygame.K_l:
                    self.vr += 0.001*self.m2p
                elif event.key == pygame.K_j:
                    self.vr -= 0.001*self.m2p
        # setting movements
        self.x += ((self.vl+self.vr)/2)*math.cos(self.theta)*dt
        self.y -= ((self.vl+self.vr)/2)*math.cos(self.theta)*dt
        self.theta += (self.vr-self.vl)/self.w*dt

        self.rotated = pygame.transform.rotozoom(
            self.img, math.degrees(self.theta), 1)
        self.rect = self.rotated.get_rect(center=(self.x, self.y))


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

# the rover
rover = Rover(
    start, "/home/alif/Projects/path_planning/rover.png", 0.01*3779.52)

dt = 0
lasttime = pygame.time.get_ticks()

# simulation loop
while running:
    # activate quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        rover.move(event)

    dt = (pygame.time.get_ticks()-lasttime)/1000
    lasttime = pygame.time.get_ticks()
    pygame.display.update()
    envir.map.fill(envir.black)
    rover.move()
    rover.draw(envir.map)
