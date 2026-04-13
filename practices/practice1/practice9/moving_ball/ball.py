import pygame


def draw_ball(screen, x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)


def move_ball(x, y, dx, dy, step, radius, width, height):
    new_x = x + dx * step
    new_y = y + dy * step

    if radius <= new_x <= width - radius:
        x = new_x

    if radius <= new_y <= height - radius:
        y = new_y

    return x, y