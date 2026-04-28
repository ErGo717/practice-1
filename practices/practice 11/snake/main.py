import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake - Practice 11")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 180, 0)
RED = (220, 50, 50)
ORANGE = (255, 165, 0)
PURPLE = (155, 89, 182)
DARK_RED = (150, 0, 0)
GRAY = (230, 230, 230)

LEVEL_SPEED = {
    1: 8,
    2: 11,
    3: 14,
}

FOOD_TYPES = [
    {"weight": 1, "color": RED, "ttl": 7000},
    {"weight": 2, "color": ORANGE, "ttl": 5000},
    {"weight": 3, "color": PURPLE, "ttl": 3500},
]


class Snake:
    def __init__(self):
        self.size = CELL_SIZE
        self.body = [(300, 200)]
        self.dx = self.size
        self.dy = 0
        self.grow_by = 0

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.dx, head_y + self.dy)
        self.body.insert(0, new_head)

        if self.grow_by > 0:
            self.grow_by -= 1
        else:
            self.body.pop()

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, GREEN, (x, y, self.size, self.size))

    def change_direction(self, dx, dy):
        # Do not allow direct reverse direction.
        if self.dx == -dx and self.dy == -dy:
            return
        self.dx = dx
        self.dy = dy


class Food:
    def __init__(self, snake):
        self.snake = snake
        self.position = (0, 0)
        self.weight = 1
        self.color = RED
        self.ttl = 7000
        self.spawn_time = 0
        self.respawn()

    def random_free_cell(self):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in self.snake.body:
                return (x, y)

    def respawn(self):
        food_type = random.choice(FOOD_TYPES)
        self.position = self.random_free_cell()
        self.weight = food_type["weight"]
        self.color = food_type["color"]
        self.ttl = food_type["ttl"]
        self.spawn_time = pygame.time.get_ticks()

    def expired(self):
        return pygame.time.get_ticks() - self.spawn_time >= self.ttl

    def time_left_seconds(self):
        left_ms = max(0, self.ttl - (pygame.time.get_ticks() - self.spawn_time))
        return left_ms / 1000

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))


def get_level(score):
    if score >= 10:
        return 3
    if score >= 5:
        return 2
    return 1


def reset_game():
    snake = Snake()
    food = Food(snake)
    score = 0
    level = 1
    game_over = False
    return snake, food, score, level, game_over


font_small = pygame.font.SysFont("Arial", 22)
font_big = pygame.font.SysFont("Arial", 46)
font_button = pygame.font.SysFont("Arial", 30)

restart_button = pygame.Rect(WIDTH // 2 - 85, HEIGHT // 2 + 50, 170, 50)

snake, food, score, level, game_over = reset_game()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0, CELL_SIZE)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(CELL_SIZE, 0)

            if game_over and event.key == pygame.K_r:
                snake, food, score, level, game_over = reset_game()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over and restart_button.collidepoint(event.pos):
                snake, food, score, level, game_over = reset_game()

    if not game_over:
        level = get_level(score)

        # Food disappears after some time.
        if food.expired():
            food.respawn()

        # Move snake first, then check collisions.
        snake.move()
        head_x, head_y = snake.body[0]

        # Wall collision.
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over = True

        # Self collision.
        if snake.body[0] in snake.body[1:]:
            game_over = True

        # Food collision: higher weight gives more score and more growth.
        if snake.body[0] == food.position:
            score += food.weight
            snake.grow_by += food.weight
            food.respawn()

        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)

        score_text = font_small.render(f"Score: {score}", True, BLACK)
        level_text = font_small.render(f"Level: {level}", True, BLACK)
        weight_text = font_small.render(f"Food weight: {food.weight}", True, BLACK)
        timer_text = font_small.render(f"Food timer: {food.time_left_seconds():.1f}s", True, BLACK)

        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 38))
        screen.blit(weight_text, (10, 66))
        screen.blit(timer_text, (10, 94))

    else:
        screen.fill(DARK_RED)

        game_over_text = font_big.render("Game Over", True, WHITE)
        score_text = font_big.render(f"Score: {score}", True, WHITE)
        level_text = font_big.render(f"Level: {level}", True, WHITE)
        hint_text = font_small.render("Press R or click Restart", True, WHITE)

        screen.blit(game_over_text, (WIDTH // 2 - 115, HEIGHT // 2 - 100))
        screen.blit(score_text, (WIDTH // 2 - 80, HEIGHT // 2 - 45))
        screen.blit(level_text, (WIDTH // 2 - 80, HEIGHT // 2))
        screen.blit(hint_text, (WIDTH // 2 - 100, HEIGHT // 2 + 110))

        pygame.draw.rect(screen, GRAY, restart_button, border_radius=10)
        pygame.draw.rect(screen, BLACK, restart_button, 2, border_radius=10)
        button_text = font_button.render("Restart", True, BLACK)
        screen.blit(button_text, (restart_button.x + 36, restart_button.y + 10))

    pygame.display.flip()
    clock.tick(LEVEL_SPEED[level])