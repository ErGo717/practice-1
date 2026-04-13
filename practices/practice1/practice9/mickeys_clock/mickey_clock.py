import os
from datetime import datetime
import pygame


def load_images():
    base_dir = os.path.dirname(__file__)
    images_dir = os.path.join(base_dir, "images")

    mickey = pygame.image.load(os.path.join(images_dir, "mickey.png")).convert_alpha()
    left_hand = pygame.image.load(os.path.join(images_dir, "left_hand.png")).convert_alpha()
    right_hand = pygame.image.load(os.path.join(images_dir, "right_hand.png")).convert_alpha()

    return mickey, left_hand, right_hand


def draw_rotated(screen, image, center, angle):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=center)
    screen.blit(rotated, rect)


def draw_clock(screen, mickey, left_hand, right_hand, center):
    now = datetime.now()

    minutes = now.minute + now.second / 60
    seconds = now.second

    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)

    bg_rect = mickey.get_rect(center=center)
    screen.blit(mickey, bg_rect)

    draw_rotated(screen, right_hand, center, minute_angle)
    draw_rotated(screen, left_hand, center, second_angle)