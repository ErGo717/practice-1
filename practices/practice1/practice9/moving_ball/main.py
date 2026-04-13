import pygame
from ball import draw_ball, move_ball

pygame.init()

WIDTH = 800
HEIGHT = 600

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")
clock = pygame.time.Clock()

radius = 25
step = 20
x = WIDTH // 2
y = HEIGHT // 2

running = True
move_delay = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if move_delay <= 0:
        if keys[pygame.K_UP]:
            x, y = move_ball(x, y, 0, -1, step, radius, WIDTH, HEIGHT)
            move_delay = 6
        elif keys[pygame.K_DOWN]:
            x, y = move_ball(x, y, 0, 1, step, radius, WIDTH, HEIGHT)
            move_delay = 6
        elif keys[pygame.K_LEFT]:
            x, y = move_ball(x, y, -1, 0, step, radius, WIDTH, HEIGHT)
            move_delay = 6
        elif keys[pygame.K_RIGHT]:
            x, y = move_ball(x, y, 1, 0, step, radius, WIDTH, HEIGHT)
            move_delay = 6

    if move_delay > 0:
        move_delay -= 1

    screen.fill(WHITE)
    draw_ball(screen, x, y, radius, RED)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()