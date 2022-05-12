import sys
import pygame

pygame.init()

# surface
width = 600
height = 500

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colors")

# colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(130, 20, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

pink = (200, 90, 130)

# rects
rect = pygame.Rect(100, 150, 120, 60)
rect.center = (width // 2, height // 2)

rect2 = (100, 100, 80, 40)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(black)

    pygame.draw.rect(surface, pink, rect)
    pygame.draw.rect(surface, green, rect2)
    pygame.draw.circle(surface, purple, (200, 300), 60)
    pygame.draw.line(surface, blue, (100, 100), (200, 300), 3)

    pygame.display.update()
