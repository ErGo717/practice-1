import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 700
TOOLBAR_HEIGHT = 95
CANVAS_Y = TOOLBAR_HEIGHT

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (225, 225, 225)
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

TOOLS = [
    "brush",
    "rect",
    "circle",
    "square",
    "right_triangle",
    "equilateral_triangle",
    "rhombus",
    "eraser",
]


class Painter:
    def __init__(self):
        self.tool = "brush"
        self.color = (0, 0, 0)
        self.brush_size = 5
        self.eraser_size = 22

        self.items = []

        self.mouse_down = False
        self.start_pos = None
        self.current_pos = None
        self.current_stroke = []

    def set_tool(self, tool):
        self.tool = tool
        self.mouse_down = False
        self.start_pos = None
        self.current_pos = None
        self.current_stroke = []

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

        if pos[1] < CANVAS_Y:
            self.mouse_down = False
            self.start_pos = None
            self.current_pos = None
            self.current_stroke = []
            return

        # Save brush stroke.
        if self.tool == "brush":
            if len(self.current_stroke) > 1:
                self.items.append({
                    "type": "brush",
                    "points": self.current_stroke[:],
                    "color": self.color,
                    "width": self.brush_size
                })

        # Save rectangle.
        elif self.tool == "rect":
            rect = self.make_rect(self.start_pos, pos)
            self.items.append({
                "type": "rect",
                "rect": rect,
                "color": self.color,
                "width": 3
            })

        # Save circle.
        elif self.tool == "circle":
            radius = self.make_radius(self.start_pos, pos)
            self.items.append({
                "type": "circle",
                "center": self.start_pos,
                "radius": radius,
                "color": self.color,
                "width": 3
            })

        # Save square.
        elif self.tool == "square":
            rect = self.make_square(self.start_pos, pos)
            self.items.append({
                "type": "square",
                "rect": rect,
                "color": self.color,
                "width": 3
            })

        # Save right triangle.
        elif self.tool == "right_triangle":
            points = self.make_right_triangle(self.start_pos, pos)
            self.items.append({
                "type": "polygon",
                "points": points,
                "color": self.color,
                "width": 3
            })

        # Save equilateral triangle.
        elif self.tool == "equilateral_triangle":
            points = self.make_equilateral_triangle(self.start_pos, pos)
            self.items.append({
                "type": "polygon",
                "points": points,
                "color": self.color,
                "width": 3
            })

        # Save rhombus.
        elif self.tool == "rhombus":
            points = self.make_rhombus(self.start_pos, pos)
            self.items.append({
                "type": "polygon",
                "points": points,
                "color": self.color,
                "width": 3
            })

        self.mouse_down = False
        self.start_pos = None
        self.current_pos = None
        self.current_stroke = []

    def make_rect(self, start, end):
        x1, y1 = start
        x2, y2 = end
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

    def make_radius(self, start, end):
        return int(math.hypot(end[0] - start[0], end[1] - start[1]))

    def make_square(self, start, end):
        x1, y1 = start
        x2, y2 = end

        side = max(abs(x2 - x1), abs(y2 - y1))
        x = x1 if x2 >= x1 else x1 - side
        y = y1 if y2 >= y1 else y1 - side

        return pygame.Rect(x, y, side, side)

    def make_right_triangle(self, start, end):
        rect = self.make_rect(start, end)
        return [
            (rect.left, rect.top),
            (rect.left, rect.bottom),
            (rect.right, rect.bottom),
        ]

    def make_equilateral_triangle(self, start, end):
        x1, y1 = start
        x2, y2 = end

        side = max(10, abs(x2 - x1))
        height = int((math.sqrt(3) / 2) * side)

        if x2 >= x1:
            left_x = x1
            right_x = x1 + side
        else:
            left_x = x1 - side
            right_x = x1

        direction = 1 if y2 >= y1 else -1

        top = ((left_x + right_x) // 2, y1)
        left = (left_x, y1 + direction * height)
        right = (right_x, y1 + direction * height)

        return [top, left, right]

    def make_rhombus(self, start, end):
        rect = self.make_rect(start, end)
        return [
            (rect.centerx, rect.top),
            (rect.right, rect.centery),
            (rect.centerx, rect.bottom),
            (rect.left, rect.centery),
        ]

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

            elif item["type"] in ["rect", "square"]:
                rect = item["rect"]
                if rect.inflate(self.eraser_size * 2, self.eraser_size * 2).collidepoint(pos):
                    keep = False

            elif item["type"] == "circle":
                cx, cy = item["center"]
                dist = math.hypot(cx - px, cy - py)
                if dist <= item["radius"] + self.eraser_size:
                    keep = False

            elif item["type"] == "polygon":
                xs = [p[0] for p in item["points"]]
                ys = [p[1] for p in item["points"]]
                bounds = pygame.Rect(min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys))
                if bounds.inflate(self.eraser_size * 2, self.eraser_size * 2).collidepoint(pos):
                    keep = False

            if keep:
                new_items.append(item)

        self.items = new_items

    def draw_saved_items(self, screen):
        for item in self.items:
            if item["type"] == "brush":
                if len(item["points"]) >= 2:
                    pygame.draw.lines(screen, item["color"], False, item["points"], item["width"])

            elif item["type"] in ["rect", "square"]:
                pygame.draw.rect(screen, item["color"], item["rect"], item["width"])

            elif item["type"] == "circle":
                pygame.draw.circle(screen, item["color"], item["center"], item["radius"], item["width"])

            elif item["type"] == "polygon":
                pygame.draw.polygon(screen, item["color"], item["points"], item["width"])

    def draw_preview(self, screen):
        if not self.mouse_down or not self.start_pos or not self.current_pos:
            return

        if self.tool == "brush" and len(self.current_stroke) >= 2:
            pygame.draw.lines(screen, self.color, False, self.current_stroke, self.brush_size)

        elif self.tool == "rect":
            pygame.draw.rect(screen, self.color, self.make_rect(self.start_pos, self.current_pos), 3)

        elif self.tool == "circle":
            pygame.draw.circle(
                screen,
                self.color,
                self.start_pos,
                self.make_radius(self.start_pos, self.current_pos),
                3,
            )

        elif self.tool == "square":
            pygame.draw.rect(screen, self.color, self.make_square(self.start_pos, self.current_pos), 3)

        elif self.tool == "right_triangle":
            pygame.draw.polygon(screen, self.color, self.make_right_triangle(self.start_pos, self.current_pos), 3)

        elif self.tool == "equilateral_triangle":
            pygame.draw.polygon(
                screen,
                self.color,
                self.make_equilateral_triangle(self.start_pos, self.current_pos),
                3,
            )

        elif self.tool == "rhombus":
            pygame.draw.polygon(screen, self.color, self.make_rhombus(self.start_pos, self.current_pos), 3)

        elif self.tool == "eraser":
            pygame.draw.circle(screen, DARK_GRAY, self.current_pos, self.eraser_size, 2)

    def draw(self, screen):
        self.draw_saved_items(screen)
        self.draw_preview(screen)


def draw_toolbar(screen, font, painter, tool_buttons, color_buttons, clear_button):
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))
    pygame.draw.line(screen, DARK_GRAY, (0, TOOLBAR_HEIGHT - 1), (WIDTH, TOOLBAR_HEIGHT - 1), 2)

    for tool_name, rect in tool_buttons:
        fill = LIGHT_BLUE if painter.tool == tool_name else WHITE
        pygame.draw.rect(screen, fill, rect, border_radius=8)
        pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
        label = font.render(tool_name, True, BLACK)
        screen.blit(label, (rect.x + 6, rect.y + 8))

    for color_value, rect in color_buttons:
        pygame.draw.rect(screen, color_value, rect)
        border = 4 if painter.color == color_value else 2
        pygame.draw.rect(screen, BLACK, rect, border)

    preview_rect = pygame.Rect(865, 18, 40, 40)
    pygame.draw.rect(screen, painter.color, preview_rect)
    pygame.draw.rect(screen, BLACK, preview_rect, 2)

    label = font.render("Color", True, BLACK)
    screen.blit(label, (858, 60))

    pygame.draw.rect(screen, (255, 210, 210), clear_button, border_radius=8)
    pygame.draw.rect(screen, BLACK, clear_button, 2, border_radius=8)
    clear_text = font.render("CLEAR", True, BLACK)
    screen.blit(clear_text, (clear_button.x + 10, clear_button.y + 8))


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Paint - Practice 11")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    painter = Painter()

    tool_buttons = []
    x = 10
    for tool_name in TOOLS:
        rect = pygame.Rect(x, 15, 105, 34)
        tool_buttons.append((tool_name, rect))
        x += 110

    color_buttons = []
    color_x = 15
    for color in COLORS:
        color_buttons.append((color, pygame.Rect(color_x, 58, 28, 28)))
        color_x += 33

    clear_button = pygame.Rect(920, 20, 70, 35)

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
                    painter.set_tool("square")
                elif event.key == pygame.K_5:
                    painter.set_tool("right_triangle")
                elif event.key == pygame.K_6:
                    painter.set_tool("equilateral_triangle")
                elif event.key == pygame.K_7:
                    painter.set_tool("rhombus")
                elif event.key == pygame.K_8:
                    painter.set_tool("eraser")
                elif event.key == pygame.K_BACKSPACE:
                    painter.items.clear()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                clicked_ui = False

                for tool_name, rect in tool_buttons:
                    if rect.collidepoint(pos):
                        painter.set_tool(tool_name)
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

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                painter.on_mouse_up(event.pos)

        screen.fill(WHITE)
        draw_toolbar(screen, font, painter, tool_buttons, color_buttons, clear_button)
        painter.draw(screen)

        info = font.render(
            "1 brush | 2 rect | 3 circle | 4 square | 5 right triangle | 6 equilateral | 7 rhombus | 8 eraser",
            True,
            BLACK,
        )
        clear_info = font.render("Backspace = clear all", True, BLACK)
        screen.blit(info, (10, HEIGHT - 45))
        screen.blit(clear_info, (10, HEIGHT - 22))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()