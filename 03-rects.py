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
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

my_color = (200, 90, 130)

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

    pygame.draw.rect(surface, my_color, rect)
    pygame.draw.rect(surface, green, rect2)

    pygame.display.update()
