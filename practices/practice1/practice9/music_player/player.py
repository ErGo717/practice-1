import os
import pygame


def get_tracks(folder):
    tracks = []

    if not os.path.exists(folder):
        return tracks

    for name in os.listdir(folder):
        low = name.lower()
        if low.endswith(".mp3") or low.endswith(".wav") or low.endswith(".ogg"):
            tracks.append(os.path.join(folder, name))

    tracks.sort()
    return tracks


def play_track(tracks, index):
    if len(tracks) == 0:
        return

    pygame.mixer.music.load(tracks[index])
    pygame.mixer.music.play()


def stop_track():
    pygame.mixer.music.stop()


def next_track(index, tracks):
    if len(tracks) == 0:
        return 0
    return (index + 1) % len(tracks)


def prev_track(index, tracks):
    if len(tracks) == 0:
        return 0
    return (index - 1) % len(tracks)


def current_track_name(tracks, index):
    if len(tracks) == 0:
        return "No tracks"
    return os.path.basename(tracks[index])


def current_position():
    pos = pygame.mixer.music.get_pos()

    if pos < 0:
        return "00:00"

    seconds = pos // 1000
    minutes = seconds // 60
    seconds = seconds % 60

    return f"{minutes:02}:{seconds:02}"