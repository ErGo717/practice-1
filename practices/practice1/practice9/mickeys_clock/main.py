import pygame
from mickey_clock import load_images, draw_clock

pygame.init()

WIDTH = 800
HEIGHT = 800
BG = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

mickey, left_hand, right_hand = load_images()
center = (WIDTH // 2, HEIGHT // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)
    draw_clock(screen, mickey, left_hand, right_hand, center)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()