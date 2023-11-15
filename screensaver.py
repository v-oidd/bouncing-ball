import time
import random


COLUMNS = 40
ROWS = 15
VELOCITY = 100

VECTORS = (1, -1)
vector = [random.choice(VECTORS), random.choice(VECTORS)]
position = [random.randint(0, COLUMNS-1), random.randint(0, ROWS-1)]


class Colors:
    BLUE = '\033[94m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'


class Ball:
    BALL = f'{Colors.RED}X{Colors.END}'
    WIDTH = COLUMNS - 1
    LENGTH = ROWS - 1
    REFRESH_RATE = 1 / VELOCITY


class Screen:
    def __init__(self, screen, vector):
        self.screen = screen
        self.vector = vector

    def draw(self):
        print("\033c", end="")
        print('\n'.join('  '.join(row) for row in self.screen))

    def update_vector(self):
        x, y = position

        if x == 0 or x == Ball.WIDTH:
            self.vector[1] *= -1

        if y == 0 or y == Ball.LENGTH:
            self.vector[0] *= -1

        return self.vector


screen = [[f'{Colors.BLUE}*{Colors.END}' for _ in range(COLUMNS)] for _ in range(ROWS)]
ball_screen = Screen(screen, vector)

ball_screen.screen[position[1]][position[0]] = Ball.BALL

ball_screen.draw()

try:
    while True:

        vector = ball_screen.update_vector()

        ball_screen.screen[position[1]][position[0]] = f'{Colors.YELLOW}*{Colors.END}'
        position[1] += vector[0]
        position[0] += vector[1]
        ball_screen.screen[position[1]][position[0]] = Ball.BALL

        ball_screen.draw()

        time.sleep(Ball.REFRESH_RATE)

except KeyboardInterrupt:
    ball_screen.draw()
    print('Ended.')
