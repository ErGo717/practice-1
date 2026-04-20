import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Snake")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
GOLD = (255, 215, 0)
BLUE = (0, 183, 235)
DARK_RED = (160, 0, 0)
GRAY = (230, 230, 230)

LEVEL_COLORS = {
    1: WHITE,
    2: GOLD,
    3: BLUE
}

LEVEL_SPEED = {
    1: 8,   # slower
    2: 12,  # medium
    3: 16   # faster
}

font_small = pygame.font.SysFont("Georgia", 20)
font_big = pygame.font.SysFont(None, 50)
font_button = pygame.font.SysFont(None, 35)

restart_button = pygame.Rect(WIDTH // 2 - 90, HEIGHT // 2 + 40, 180, 50)


class Snake:
    def __init__(self):
        self.size = CELL_SIZE
        self.body = [(300, 200)]
        self.dx = self.size
        self.dy = 0
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.dx, head_y + self.dy)

        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0], segment[1], self.size, self.size))

    def change_direction(self, dx, dy):
        if self.dx == -dx and self.dy == -dy:
            return
        self.dx = dx
        self.dy = dy


def generate_food(snake):
    while True:
        x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
        y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE

        if (x, y) not in snake.body:
            return (x, y)


def get_level(score):
    if score >= 10:
        return 3
    elif score >= 5:
        return 2
    return 1


def reset_game():
    snake = Snake()
    food_pos = generate_food(snake)
    score = 0
    level = 1
    game_over = False
    return snake, food_pos, score, level, game_over


snake, food_pos, SCORE, LEVEL, game_over = reset_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -snake.size)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, snake.size)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-snake.size, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(snake.size, 0)

            if game_over and event.key == pygame.K_r:
                snake, food_pos, SCORE, LEVEL, game_over = reset_game()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and restart_button.collidepoint(event.pos):
                snake, food_pos, SCORE, LEVEL, game_over = reset_game()

    if not game_over:
        LEVEL = get_level(SCORE)

        # move first
        snake.move()
        head_x, head_y = snake.body[0]

        # wall collision
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over = True

        # self collision
        if snake.body[0] in snake.body[1:]:
            game_over = True

        # food collision
        if snake.body[0] == food_pos:
            snake.grow = True
            food_pos = generate_food(snake)
            SCORE += 1

        # draw game
        screen.fill(LEVEL_COLORS[LEVEL])
        snake.draw(screen)
        pygame.draw.rect(screen, RED, (food_pos[0], food_pos[1], snake.size, snake.size))

        score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
        level_text = font_small.render(f"Level: {LEVEL}", True, BLACK)
        speed_text = font_small.render(f"Speed: {LEVEL_SPEED[LEVEL]}", True, BLACK)

        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 35))
        screen.blit(speed_text, (10, 60))

    else:
        screen.fill(DARK_RED)

        game_over_text = font_big.render("Game Over!", True, WHITE)
        score_text = font_big.render(f"Score: {SCORE}", True, WHITE)
        level_text = font_big.render(f"Level: {LEVEL}", True, WHITE)

        screen.blit(game_over_text, (WIDTH // 2 - 120, HEIGHT // 2 - 100))
        screen.blit(score_text, (WIDTH // 2 - 85, HEIGHT // 2 - 40))
        screen.blit(level_text, (WIDTH // 2 - 85, HEIGHT // 2))

        pygame.draw.rect(screen, GRAY, restart_button, border_radius=10)
        pygame.draw.rect(screen, BLACK, restart_button, 2, border_radius=10)

        restart_text = font_button.render("Restart", True, BLACK)
        screen.blit(restart_text, (restart_button.x + 45, restart_button.y + 12))

        hint_text = font_small.render("Press R or click Restart", True, WHITE)
        screen.blit(hint_text, (WIDTH // 2 - 95, HEIGHT // 2 + 100))

    pygame.display.flip()
    clock.tick(LEVEL_SPEED[LEVEL])
    