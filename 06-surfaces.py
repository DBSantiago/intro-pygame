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
teal = pygame.Color(0, 128, 128)

pink = (200, 90, 130)

# rects
rect = pygame.Rect(100, 150, 120, 60)
rect.center = (width // 2, height // 2)

rect2 = (100, 100, 80, 40)

surface2 = pygame.Surface((200, 200))
surface2.fill((162, 162, 162))

rect_surface2 = surface2.get_rect()
rect_surface2.center = (width // 2, height // 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(black)

    pygame.draw.polygon(surface, teal, ((146, 0), (291, 106),
                        (236, 277), (56, 277), (0, 106)))  # pentagono

    pygame.draw.rect(surface, pink, rect)
    pygame.draw.rect(surface, green, rect2)
    pygame.draw.circle(surface, purple, (200, 300), 60)
    pygame.draw.line(surface, blue, (100, 100), (200, 300), 3)

    pygame.draw.polygon(
        surface, white, ((0, 400), (100, 300), (200, 400)))  # triangulo

    surface.blit(surface2, rect_surface2)

    pygame.draw.rect(surface2, red, rect2)

    pygame.display.update()
