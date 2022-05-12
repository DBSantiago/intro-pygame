import sys
import pygame

pygame.init()

width = 800
height = 800

surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colors")

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

my_color = (200, 90, 130)

codi_image = pygame.image.load("intro-pygame/images/codi.png")
codi_image_rect = codi_image.get_rect()
codi_image_rect.center = (width // 2, height // 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill(my_color)
    surface.blit(codi_image, codi_image_rect)
    pygame.display.update()
