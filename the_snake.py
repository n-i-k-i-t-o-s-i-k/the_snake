import pygame
from random import randint

pygame.init()

SCR_WIDTH, SCR_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCR_WIDTH // GRID_SIZE
GRID_HEIGHT = SCR_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
WHITE = (255, 255, 255)

INITIAL_SPEED = 10
SPEED_INCREMENT = 5
MIN_SPEED = 10
MAX_SPEED = 25

scr = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
pygame.display.set_caption('Р—РјРµР№РєР°')

clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)

SCREEN_WIDTH = 0
SCREEN_HEIGHT = 0
screen = pygame.Surface((150, 150))


class GameObject():
    """
    Fake
    comment
    """

    position = (0, 0)
    body_color = (0, 0, 0)

    def __int__(self):
        """
        Fake
        comment
        """
        return 0

    def draw():
        """
        Fake
        comment
        """
        return 0


class Snake(GameObject):
    """
    РџСѓР±Р»РёС‡РЅС‹Р№ РєР»Р°СЃСЃ Snake
    РљР»Р°СЃСЃ РґР»СЏ РІР·Р°РёРјРѕРґРµР№СЃС‚РІРёСЏ СЃРѕ Р·РјРµР№РєРѕР№
    """

    position = (0, 0)
    body_color = (0, 0, 0)
    positions = [(0, 0), (0, 0), (0, 0)]
    direction = 'UP'

    def __init__(self):
        """
        РРЅРёС†РёР°Р»РёР·РёСЂСѓРµС‚ СЌРєР·РµРјРїР»СЏСЂ Р·РјРµР№РєРё.
        РЈСЃС‚Р°РЅР°РІР»РёРІР°РµС‚ РЅР°С‡Р°Р»СЊРЅС‹Рµ РїРѕР·РёС†РёРё, РЅР°РїСЂР°РІР»РµРЅРёРµ, С„Р»Р°Рі СЂРѕСЃС‚Р° Рё СЃС‡РµС‚.
        """
        self.positions = [
            (GRID_WIDTH // 2, GRID_HEIGHT // 2),
            (GRID_WIDTH // 2, GRID_HEIGHT // 2 + 1),
            (GRID_WIDTH // 2, GRID_HEIGHT // 2 + 2)
        ]
        self.direction = RIGHT
        self.grow = False
        self.score = 0

    def get_head_position():
        """
        Fake
        comment
        """
        return 0

    def reset():
        """
        Fake
        comment
        """
        return 0

    def move(self):
        """
        РџРµСЂРµРјРµС‰Р°РµС‚ Р·РјРµР№РєСѓ РІ РЅСѓР¶РЅРѕРј РЅР°РїСЂР°РІР»РµРЅРёРё. РџСЂРѕРІРµСЂСЏРµС‚ СЃС‚РѕР»РєРЅРѕРІРµРЅРёРµ СЃ СЃРѕР±РѕР№.
        Р•СЃР»Рё СЃС‚РѕР»РєРЅРѕРІРµРЅРёРµ РїСЂРѕРёР·РѕС€Р»Рѕ, РІРѕР·РІСЂР°С‰Р°РµС‚ False, РёРЅР°С‡Рµ True.
        """
        current_head = self.positions[0]
        x, y = self.direction
        a = (current_head[0] + x) % GRID_WIDTH
        b = (current_head[1] + y) % GRID_HEIGHT
        new_head = (a, b)

        if new_head in self.positions:
            return False
        else:
            self.positions.insert(0, new_head)
            if not self.grow:
                self.positions.pop()
            self.grow = False
            return True

    def update_direction(self, direction):
        """
        РР·РјРµРЅСЏРµС‚ РЅР°РїСЂР°РІР»РµРЅРёРµ РґРІРёР¶РµРЅРёСЏ Р·РјРµР№РєРё.
        РџР°СЂР°РјРµС‚СЂС‹: direction - РЅР°РїСЂР°РІР»РµРЅРёРµ РІ РІРёРґРµ РєРѕСЂС‚РµР¶Р° (dx, dy)
        """
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def draw(self):
        """
        Р”Р°РЅРЅР°СЏ С„СѓРЅРєС†РёСЏ РїСЂРµРґРЅР°Р·РЅР°С‡РµРЅР° РґР»СЏ
        РѕС‚СЂРёСЃРѕРІРєРё Р·РјРµР№РєРё РЅР° СЌРєСЂР°РЅРµ.
        """
        for pos in self.positions:
            rect = pygame.Rect(pos[0] * GRID_SIZE, pos[1] * GRID_SIZE,
                               GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(scr, SNAKE_COLOR, rect)
            pygame.draw.rect(scr, BORDER_COLOR, rect, 1)


class Apple(GameObject):
    """
    РџСѓР±Р»РёС‡РЅС‹Р№ РєР»Р°СЃСЃ Apple
    РћРїСЂРµРґРµР»СЏРµС‚ РїРѕРІРµРґРµРЅРёРµ СЏР±Р»РѕРєР° РІ РёРіСЂРµ.
    """

    position = (0, 0)
    body_color = (0, 0, 0)

    def __init__(self):
        """
        РРЅРёС†РёР°Р»РёР·РёСЂСѓРµС‚ СЌРєР·РµРјРїР»СЏСЂ СЏР±Р»РѕРєР°. РЈСЃС‚Р°РЅР°РІР»РёРІР°РµС‚ РЅР°С‡Р°Р»СЊРЅСѓСЋ РїРѕР·РёС†РёСЋ
        СЏР±Р»РѕРєР° СЃР»СѓС‡Р°Р№РЅС‹Рј РѕР±СЂР°Р·РѕРј РІ РїСЂРµРґРµР»Р°С… РёРіСЂРѕРІРѕРіРѕ РїРѕР»СЏ.
        """
        a = randint(0, GRID_WIDTH - 1)
        b = randint(0, GRID_HEIGHT - 1)
        self.position = (a, b)

    def draw(self):
        """
        Р”Р°РЅРЅР°СЏ С„СѓРЅРєС†РёСЏ РїСЂРµРґРЅР°Р·РЅР°С‡РµРЅР° РґР»СЏ
        РѕС‚СЂРёСЃРѕРІРєРё СЏР±Р»РѕРєР° РЅР° СЌРєСЂР°РЅРµ.
        """
        a = self.position[0] * GRID_SIZE
        b = self.position[1] * GRID_SIZE
        rect = pygame.Rect(a, b, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(scr, APPLE_COLOR, rect)
        pygame.draw.rect(scr, BORDER_COLOR, rect, 1)

    def randomize_position(self):
        """
        РЎР±СЂР°СЃС‹РІР°РµС‚ РїРѕР·РёС†РёСЋ СЏР±Р»РѕРєР° РЅР° РЅРѕРІСѓСЋ СЃР»СѓС‡Р°Р№РЅСѓСЋ РєРѕРѕСЂРґРёРЅР°С‚Сѓ.
        РЈСЃС‚Р°РЅР°РІР»РёРІР°РµС‚ РЅРѕРІСѓСЋ СЃР»СѓС‡Р°Р№РЅСѓСЋ РїРѕР·РёС†РёСЋ СЏР±Р»РѕРєР° РІ РїСЂРµРґРµР»Р°С… РёРіСЂРѕРІРѕРіРѕ РїРѕР»СЏ.
        """
        a = randint(0, GRID_WIDTH - 1)
        b = randint(0, GRID_HEIGHT - 1)
        self.position = (a, b)


def handle_keys(snake):
    """
    Р”Р°РЅРЅР°СЏ С„СѓРЅРєС†РёСЏ РїСЂРµРґРЅР°Р·РЅР°С‡РµРЅР° РґР»СЏ
    РѕРїСЂРµРґРµР»РµРЅРёСЏ СѓРїСЂР°РІР»РµРЅРёРµ РІ РёРіСЂРµ.
    """
    global speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key in (
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT
            ):
                direction_map = {
                    pygame.K_UP: UP,
                    pygame.K_DOWN: DOWN,
                    pygame.K_LEFT: LEFT,
                    pygame.K_RIGHT: RIGHT
                }
                snake.update_direction((direction_map[event.key]))
            elif event.key == pygame.K_q:
                speed = max(MIN_SPEED, speed - SPEED_INCREMENT)
            elif event.key == pygame.K_w:
                speed = min(MAX_SPEED, speed + SPEED_INCREMENT)


def game_over_scr(score, high_score):
    """
    Р”Р°РЅРЅР°СЏ С„СѓРЅРєС†РёСЏ РїСЂРµРґРЅР°Р·РЅР°С‡РµРЅР° РґР»СЏ
    РѕРїСЂРµРґРµР»РµРЅРёСЏ СЂР°Р±РѕС‚С‹ СЌРєСЂР°РЅР° РїРѕСЃР»Рµ СЃРјРµСЂС‚Рё
    """
    while True:
        scr.fill(BOARD_BACKGROUND_COLOR)

        game_over_text = font.render('Р’С‹ РїСЂРѕРёРіСЂР°Р»Рё!', True, WHITE)
        score_text = font.render(f'Р’Р°С€ СЂРµР·СѓР»СЊС‚Р°С‚: {score}', True, WHITE)
        high_score_text = font.render(f'Р РµРєРѕСЂРґ: {high_score}', True, WHITE)
        exit_text = font.render('ESC - РІС‹Р№С‚Рё', True, WHITE)
        continue_text = font.render('SPACE - РїСЂРѕРґРѕР»Р¶РёС‚СЊ', True, WHITE)

        scr.blit(game_over_text, (SCR_WIDTH // 2 - 50, SCR_HEIGHT // 2 - 50))
        scr.blit(score_text, (SCR_WIDTH // 2 - 70, SCR_HEIGHT // 2 - 28))
        scr.blit(high_score_text, (SCR_WIDTH // 2 - 35, SCR_HEIGHT // 2))
        scr.blit(exit_text, (SCR_WIDTH // 2 - 50, SCR_HEIGHT // 2 + 28))
        scr.blit(continue_text, (SCR_WIDTH // 2 - 90, SCR_HEIGHT // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_SPACE:
                    return


def main():
    """
    РћР±С‰РёР№ РєР»Р°СЃСЃ РёРіСЂС‹
    Р’Р·Р°РёРјРѕРґРµР№СЃС‚РІСѓРµС‚ СЃ РѕСЃС‚Р°Р»СЊРЅС‹РјРё РєР»Р°СЃСЃР°РјРё
    """
    global speed
    speed = INITIAL_SPEED
    snake = Snake()
    apple = Apple()
    high_score = 0

    while True:
        handle_keys(snake)

        if not snake.move():
            if snake.score > high_score:
                high_score = snake.score
            game_over_scr(snake.score, high_score)
            snake = Snake()
            apple.randomize_position()

        if snake.positions[0] == apple.position:
            snake.grow = True
            snake.score += 1
            apple.randomize_position()

        scr.fill(BOARD_BACKGROUND_COLOR)

        pygame.draw.rect(scr, BORDER_COLOR, (0, 0, SCR_WIDTH, SCR_HEIGHT), 2)

        snake.draw()
        apple.draw()

        score_text = font.render(f'РЎС‡РµС‚: {snake.score}', True, WHITE)
        scr.blit(score_text, (10, 10))
        speed_text = font.render(f'РЎРєРѕСЂРѕСЃС‚СЊ: {speed}', True, WHITE)
        scr.blit(speed_text, (10, 30))

        pygame.display.flip()
        clock.tick(speed)


if __name__ == "__main__":
    main()
