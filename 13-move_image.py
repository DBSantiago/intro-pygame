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
teal = pygame.Color(0, 128, 128)

my_color = (200, 90, 130)

codi_image = pygame.image.load("images/codi.png")
codi_image_rect = codi_image.get_rect()
codi_image_rect.center = (width // 2, height // 2)

font = pygame.font.Font("fonts/RussoOne-Regular.ttf", 72)
text_welcome = font.render("Welcome!", True, teal)
text_welcome_rect = text_welcome.get_rect()
text_welcome_rect.center = (width // 2, 60)


pygame.mixer.music.load(
    "sounds/1.-introduccion_sounds_Haggstrom.mp3")
pygame.mixer.music.set_volume(0.30)
pygame.mixer.music.play(-1, 0.0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYUP:
            print("Tecla liberada.")

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Evento mousedown.")

        if event.type == pygame.MOUSEBUTTONUP:
            print("Evento mouseup.")

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] or pressed[pygame.K_UP]:
        codi_image_rect.y -= 5

    if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
        codi_image_rect.x -= 5

    if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
        codi_image_rect.y += 5

    if pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
        codi_image_rect.x += 5

    if codi_image_rect.left < 0:
        codi_image_rect.left = 0

    if codi_image_rect.right > width:
        codi_image_rect.right = width

    if codi_image_rect.bottom > height:
        codi_image_rect.bottom = height

    if codi_image_rect.top < 0:
        codi_image_rect.top = 0

    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    print(mouse_pos_x, mouse_pos_y)

    #codi_image_rect.center = mouse_pos_x, mouse_pos_y

    surface.fill(black)
    surface.blit(codi_image, codi_image_rect)
    #surface.blit(text_welcome, text_welcome_rect)

    time = pygame.time.get_ticks() // 1000
    time_text = font.render(str(time), True, teal)
    time_rect = time_text.get_rect()
    time_rect.center = (width // 2, 60)
    surface.blit(time_text, time_rect)

    print(time)

    pygame.display.update()
