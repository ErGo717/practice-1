import pygame
import sys
from pygame.locals import *
import random
import time

# -------------------- INIT --------------------
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# -------------------- COLORS --------------------
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
ORANGE = (255, 165, 0)
PURPLE = (160, 32, 240)

# -------------------- GAME SETTINGS --------------------
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Enemy speed logic:
# enemy becomes faster every N collected coin points
BASE_ENEMY_SPEED = 5
ENEMY_SPEED = BASE_ENEMY_SPEED
COINS_FOR_SPEED_UP = 5
SPEED_STEP = 1

# Regular score = how many enemies passed the player
SCORE = 0

# Coin score = how many coin points player collected
COIN_SCORE = 0

# Coin falling speed
COIN_SPEED = 5

# Different coin weights
COIN_VALUES = [1, 2, 3]

# -------------------- FONTS --------------------
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
font_coin = pygame.font.SysFont("Verdana", 22, bold=True)
game_over = font.render("Game Over", True, BLACK)

# -------------------- LOAD ASSETS --------------------
background = pygame.image.load("AnimatedStreet.png")

# Create screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer - Practice 11")

# Load sounds once
try:
    coin_sound = pygame.mixer.Sound("chieuk-coin-257878.mp3")
except pygame.error:
    coin_sound = None

try:
    crash_sound = pygame.mixer.Sound("tunetank.com_metal-crash-and-debris.wav")
except pygame.error:
    crash_sound = None


# -------------------- CLASSES --------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, ENEMY_SPEED)

        # If enemy goes off screen, player gets 1 score point
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player inside the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("coin.png")
        self.image = None
        self.rect = None
        self.value = 1
        self.color = GOLD
        self.reset()

    def reset(self):
        # Random weight for coin: 1, 2 or 3
        self.value = random.choice(COIN_VALUES)

        # Different colors by weight
        if self.value == 1:
            self.color = GOLD
            size = 50
        elif self.value == 2:
            self.color = ORANGE
            size = 60
        else:
            self.color = PURPLE
            size = 70

        # Different size by weight
        self.image = pygame.transform.scale(self.original_image, (size, size))
        self.rect = self.image.get_rect()

        # Spawn near the top
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), -20)

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)

        # If coin goes off screen, respawn it
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def earn_point(self):
        global COIN_SCORE
        COIN_SCORE += self.value
        self.reset()

    def draw(self, surface):
        # Draw coin image
        surface.blit(self.image, self.rect)

        # Draw coin value on the coin
        value_text = font_coin.render(str(self.value), True, BLACK)
        text_rect = value_text.get_rect(center=self.rect.center)
        surface.blit(value_text, text_rect)


# -------------------- SPRITES --------------------
P1 = Player()
E1 = Enemy()
COIN = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(COIN)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(COIN)


# -------------------- HELPER --------------------
def update_enemy_speed():
    global ENEMY_SPEED
    # Increase enemy speed every N coin points
    ENEMY_SPEED = BASE_ENEMY_SPEED + (COIN_SCORE // COINS_FOR_SPEED_UP) * SPEED_STEP


# -------------------- GAME LOOP --------------------
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update speed based on collected coin points
    update_enemy_speed()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Draw texts
    scores = font_small.render(str(SCORE), True, BLACK)
    score_text = font_small.render("Score", True, BLACK)

    coin_scores = font_small.render(str(COIN_SCORE), True, BLACK)
    coin_text = font_small.render("Coins", True, BLACK)

    speed_text = font_small.render(f"Enemy speed: {ENEMY_SPEED}", True, BLACK)
    info_text = font_small.render(f"+1 speed every {COINS_FOR_SPEED_UP} coins", True, BLACK)

    DISPLAYSURF.blit(scores, (10, 25))
    DISPLAYSURF.blit(score_text, (5, 0))

    DISPLAYSURF.blit(coin_scores, (340, 25))
    DISPLAYSURF.blit(coin_text, (335, 0))

    DISPLAYSURF.blit(speed_text, (120, 0))
    DISPLAYSURF.blit(info_text, (95, 25))

    # Move and draw sprites
    P1.move()
    E1.move()
    COIN.move()

    DISPLAYSURF.blit(P1.image, P1.rect)
    DISPLAYSURF.blit(E1.image, E1.rect)
    COIN.draw(DISPLAYSURF)

    # -------------------- COIN COLLISION --------------------
    if pygame.sprite.spritecollideany(P1, coins):
        COIN.earn_point()

        if coin_sound:
            coin_sound.play()

    # -------------------- ENEMY COLLISION --------------------
    if pygame.sprite.spritecollideany(P1, enemies):
        if crash_sound:
            crash_sound.play()

        time.sleep(0.5)

        final_score_text = font.render(f"Score: {SCORE}", True, BLACK)
        final_coin_score = font.render(f"Coins: {COIN_SCORE}", True, BLACK)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 180))
        DISPLAYSURF.blit(final_score_text, (45, 270))
        DISPLAYSURF.blit(final_coin_score, (45, 350))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)