import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 700
TOOLBAR_HEIGHT = 90
CANVAS_Y = TOOLBAR_HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (70, 70, 70)
LIGHT_BLUE = (180, 220, 255)

COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 180, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (128, 0, 128),
    (0, 255, 255),
    (255, 105, 180),
    (139, 69, 19),
]

TOOLS = ["brush", "rect", "circle", "eraser"]


class Painter:
    def __init__(self):
        self.tool = "brush"
        self.color = (0, 0, 0)
        self.brush_size = 6
        self.eraser_size = 22

        self.items = []  # saved objects

        self.mouse_down = False
        self.start_pos = None
        self.current_pos = None

        self.current_stroke = []

    def set_tool(self, tool):
        self.tool = tool
        self.current_stroke = []
        self.start_pos = None
        self.current_pos = None

    def set_color(self, color):
        self.color = color

    def on_mouse_down(self, pos):
        if pos[1] < CANVAS_Y:
            return

        self.mouse_down = True
        self.start_pos = pos
        self.current_pos = pos

        if self.tool == "brush":
            self.current_stroke = [pos]

        elif self.tool == "eraser":
            self.erase_at(pos)

    def on_mouse_move(self, pos):
        self.current_pos = pos

        if not self.mouse_down:
            return

        if pos[1] < CANVAS_Y:
            return

        if self.tool == "brush":
            self.current_stroke.append(pos)

        elif self.tool == "eraser":
            self.erase_at(pos)

    def on_mouse_up(self, pos):
        if not self.mouse_down:
            return

        self.mouse_down = False

        if pos[1] < CANVAS_Y:
            self.start_pos = None
            self.current_pos = None
            self.current_stroke = []
            return

        if self.tool == "brush":
            if len(self.current_stroke) > 1:
                self.items.append({
                    "type": "brush",
                    "points": self.current_stroke[:],
                    "color": self.color,
                    "size": self.brush_size
                })
            self.current_stroke = []

        elif self.tool == "rect" and self.start_pos:
            rect = self.make_rect(self.start_pos, pos)
            self.items.append({
                "type": "rect",
                "rect": rect,
                "color": self.color,
                "width": 3
            })

        elif self.tool == "circle" and self.start_pos:
            radius = self.make_radius(self.start_pos, pos)
            if radius > 0:
                self.items.append({
                    "type": "circle",
                    "center": self.start_pos,
                    "radius": radius,
                    "color": self.color,
                    "width": 3
                })

        self.start_pos = None
        self.current_pos = None

    def make_rect(self, start, end):
        x1, y1 = start
        x2, y2 = end
        x = min(x1, x2)
        y = min(y1, y2)
        w = abs(x2 - x1)
        h = abs(y2 - y1)
        return pygame.Rect(x, y, w, h)

    def make_radius(self, start, end):
        x1, y1 = start
        x2, y2 = end
        return int(math.hypot(x2 - x1, y2 - y1))

    def erase_at(self, pos):
        px, py = pos
        new_items = []

        for item in self.items:
            keep = True

            if item["type"] == "brush":
                for x, y in item["points"]:
                    if math.hypot(x - px, y - py) <= self.eraser_size:
                        keep = False
                        break

            elif item["type"] == "rect":
                rect = item["rect"]
                if rect.inflate(self.eraser_size * 2, self.eraser_size * 2).collidepoint(pos):
                    keep = False

            elif item["type"] == "circle":
                cx, cy = item["center"]
                radius = item["radius"]
                dist = math.hypot(cx - px, cy - py)
                if abs(dist - radius) <= self.eraser_size or dist < radius:
                    keep = False

            if keep:
                new_items.append(item)

        self.items = new_items

    def draw(self, screen):
        # draw saved items
        for item in self.items:
            if item["type"] == "brush":
                points = item["points"]
                if len(points) >= 2:
                    pygame.draw.lines(screen, item["color"], False, points, item["size"])
                elif len(points) == 1:
                    pygame.draw.circle(screen, item["color"], points[0], item["size"] // 2)

            elif item["type"] == "rect":
                pygame.draw.rect(screen, item["color"], item["rect"], item["width"])

            elif item["type"] == "circle":
                pygame.draw.circle(screen, item["color"], item["center"], item["radius"], item["width"])

        # preview while drawing
        if self.mouse_down:
            if self.tool == "brush" and len(self.current_stroke) >= 2:
                pygame.draw.lines(screen, self.color, False, self.current_stroke, self.brush_size)

            elif self.tool == "rect" and self.start_pos and self.current_pos:
                rect = self.make_rect(self.start_pos, self.current_pos)
                pygame.draw.rect(screen, self.color, rect, 3)

            elif self.tool == "circle" and self.start_pos and self.current_pos:
                radius = self.make_radius(self.start_pos, self.current_pos)
                pygame.draw.circle(screen, self.color, self.start_pos, radius, 3)

            elif self.tool == "eraser" and self.current_pos:
                pygame.draw.circle(screen, DARK_GRAY, self.current_pos, self.eraser_size, 2)


def draw_toolbar(screen, font, painter, tool_buttons, color_buttons, clear_button):
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, DARK_GRAY, (0, TOOLBAR_HEIGHT - 1), (WIDTH, TOOLBAR_HEIGHT - 1), 2)

    # tool buttons
    for tool, rect in tool_buttons.items():
        color = LIGHT_BLUE if painter.tool == tool else WHITE
        pygame.draw.rect(screen, color, rect, border_radius=8)
        pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
        text = font.render(tool, True, BLACK)
        screen.blit(text, (rect.x + 10, rect.y + 10))

    # color buttons
    for color_value, rect in color_buttons:
        pygame.draw.rect(screen, color_value, rect)
        border = 4 if painter.color == color_value else 2
        pygame.draw.rect(screen, BLACK, rect, border)

    # selected color preview
    preview_rect = pygame.Rect(780, 15, 50, 50)
    pygame.draw.rect(screen, painter.color, preview_rect)
    pygame.draw.rect(screen, BLACK, preview_rect, 2)

    label = font.render("Selected", True, BLACK)
    screen.blit(label, (770, 68))

    # clear button
    pygame.draw.rect(screen, (255, 200, 200), clear_button, border_radius=8)
    pygame.draw.rect(screen, BLACK, clear_button, 2, border_radius=8)
    clear_text = font.render("CLEAR", True, BLACK)
    screen.blit(clear_text, (clear_button.x + 12, clear_button.y + 10))


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Better Paint")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    painter = Painter()

    tool_buttons = {
        "brush": pygame.Rect(15, 18, 100, 40),
        "rect": pygame.Rect(125, 18, 100, 40),
        "circle": pygame.Rect(235, 18, 100, 40),
        "eraser": pygame.Rect(345, 18, 100, 40),
    }

    color_buttons = []
    start_x = 470
    for i, color in enumerate(COLORS):
        rect = pygame.Rect(start_x + i * 28, 22, 24, 24)
        color_buttons.append((color, rect))

    clear_button = pygame.Rect(860, 18, 110, 40)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                elif event.key == pygame.K_1:
                    painter.set_tool("brush")
                elif event.key == pygame.K_2:
                    painter.set_tool("rect")
                elif event.key == pygame.K_3:
                    painter.set_tool("circle")
                elif event.key == pygame.K_4:
                    painter.set_tool("eraser")

                elif event.key == pygame.K_LEFTBRACKET:
                    painter.brush_size = max(1, painter.brush_size - 1)
                    painter.eraser_size = max(5, painter.eraser_size - 2)

                elif event.key == pygame.K_RIGHTBRACKET:
                    painter.brush_size += 1
                    painter.eraser_size += 2

                elif event.key == pygame.K_BACKSPACE:
                    painter.items.clear()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = event.pos

                    clicked_ui = False

                    for tool, rect in tool_buttons.items():
                        if rect.collidepoint(pos):
                            painter.set_tool(tool)
                            clicked_ui = True
                            break

                    if not clicked_ui:
                        for color_value, rect in color_buttons:
                            if rect.collidepoint(pos):
                                painter.set_color(color_value)
                                clicked_ui = True
                                break

                    if not clicked_ui and clear_button.collidepoint(pos):
                        painter.items.clear()
                        clicked_ui = True

                    if not clicked_ui:
                        painter.on_mouse_down(pos)

            elif event.type == pygame.MOUSEMOTION:
                painter.on_mouse_move(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    painter.on_mouse_up(event.pos)

        screen.fill(WHITE)

        draw_toolbar(screen, font, painter, tool_buttons, color_buttons, clear_button)
        painter.draw(screen)

        info1 = font.render("Keys: 1-brush  2-rect  3-circle  4-eraser", True, BLACK)
        info2 = font.render("[- / ]+] size   Backspace-clear", True, BLACK)
        screen.blit(info1, (15, HEIGHT - 55))
        screen.blit(info2, (15, HEIGHT - 28))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()