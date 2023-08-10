import pygame


pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
main_surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT))

dragon_left = pygame.image.load("dragon.png")
dragon_left_rect = dragon_left.get_rect()
dragon_left_rect.topleft = (0, 0)

dragon_right = pygame.transform.flip(dragon_left, True, False)
dragon_right_rect = dragon_right.get_rect()
dragon_right_rect.topright = (WINDOW_WIDTH, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_surface.blit(dragon_left, dragon_left_rect)
    main_surface.blit(dragon_right, dragon_right_rect)
    pygame.display.update()

pygame.quit()