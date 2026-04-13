import os
import pygame
from player import (
    get_tracks,
    play_track,
    stop_track,
    next_track,
    prev_track,
    current_track_name,
    current_position,
)

pygame.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500

BLACK = (30, 30, 30)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
GREEN = (100, 220, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

font1 = pygame.font.SysFont("Arial", 32, bold=True)
font2 = pygame.font.SysFont("Arial", 24)
font3 = pygame.font.SysFont("Arial", 20)

music_folder = os.path.join(os.path.dirname(__file__), "music")
tracks = get_tracks(music_folder)

current_index = 0
is_playing = False

TRACK_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(TRACK_END)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == TRACK_END:
            if len(tracks) > 0 and is_playing:
                current_index = next_track(current_index, tracks)
                play_track(tracks, current_index)

        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_p, pygame.K_SPACE):
                if len(tracks) > 0:
                    play_track(tracks, current_index)
                    is_playing = True

            elif event.key in (pygame.K_s, pygame.K_DOWN):
                stop_track()
                is_playing = False

            elif event.key in (pygame.K_n, pygame.K_RIGHT):
                if len(tracks) > 0:
                    current_index = next_track(current_index, tracks)
                    play_track(tracks, current_index)
                    is_playing = True

            elif event.key in (pygame.K_b, pygame.K_LEFT):
                if len(tracks) > 0:
                    current_index = prev_track(current_index, tracks)
                    play_track(tracks, current_index)
                    is_playing = True

            elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                running = False

    screen.fill(BLACK)

    title = font1.render("Music Player", True, WHITE)
    controls = font2.render("P/SPACE=Play  S/DOWN=Stop  N/RIGHT=Next  B/LEFT=Back  Q/ESC=Quit", True, GRAY)

    screen.blit(title, (30, 20))
    screen.blit(controls, (30, 70))

    if len(tracks) == 0:
        text = font2.render("Add mp3/wav/ogg files to music_player/music", True, WHITE)
        screen.blit(text, (30, 140))
    else:
        now_text = font2.render("Current: " + current_track_name(tracks, current_index), True, GREEN)
        pos_text = font2.render("Position: " + current_position(), True, WHITE)

        screen.blit(now_text, (30, 140))
        screen.blit(pos_text, (30, 180))

        y = 250
        for i in range(len(tracks)):
            name = current_track_name(tracks, i)

            if i == current_index:
                line = "-> " + name
            else:
                line = "   " + name

            text = font3.render(line, True, WHITE)
            screen.blit(text, (50, y))
            y += 30

    pygame.display.flip()
    clock.tick(60)

pygame.quit()