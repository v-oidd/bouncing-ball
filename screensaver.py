import time

COLUMNS = 40
ROWS = 15
DELAY = .1
vector = [1, -1]
position = [0, 0]


class Bcolors:
    BLUE = '\033[94m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'


class Ball:
    BALL = f'{Bcolors.RED}X{Bcolors.END}'
    WIDTH = COLUMNS - 1
    LENGTH = ROWS - 1

class Screen:
    def __init__(self, screen, vector):
        self.screen = screen
        self.vector = vector

    def draw(self):
        print('\n')
        for row in screen:
            print('  '.join(row))

    def update_vector(self):
        if position[0] == Ball.WIDTH:
            if position[1] == 0:
                self.vector = [1, -1]
            elif position[1] == Ball.LENGTH:
                self.vector = [-1, -1]
            else:
                if self.vector == [-1, 1]:
                    self.vector = [-1, -1]
                elif self.vector == [1, 1]:
                    self.vector = [1, -1]

        elif position[0] == 0:
            if position[1] == 0:
                self.vector = [1, 1]
            elif position[1] == Ball.LENGTH:
                self.vector = [-1, 1]
            else:
                if self.vector == [-1, -1]:
                    self.vector = [-1, 1]
                elif self.vector == [1, -1]:
                    self.vector = [1, 1]

        elif position[1] == 0:
            if self.vector == [-1, 1]:
                self.vector = [1, 1]
            elif self.vector == [-1, -1]:
                self.vector = [1, -1]

        elif position[1] == Ball.LENGTH:
            if self.vector == [1, 1]:
                self.vector = [-1, 1]
            elif self.vector == [1, -1]:
                self.vector = [-1, -1]

        return self.vector


screen = [[f'{Bcolors.BLUE}*{Bcolors.END}' for _ in range(COLUMNS)] for _ in range(ROWS)]
board = Screen(screen, vector)

board.screen[position[1]][position[0]] = Ball.BALL

board.draw()

try:
    while True:

        vector = board.update_vector()

        screen[position[1]][position[0]] = f'{Bcolors.YELLOW}*{Bcolors.END}'
        position[1] += vector[0]
        position[0] += vector[1]
        screen[position[1]][position[0]] = Ball.BALL

        board.draw()

        time.sleep(DELAY)
except KeyboardInterrupt:
    print('Ended.')
