import time


COLUMNS = 40
ROWS = 15
DELAY = .02
vector = [1, -1]
position = [0, 0]


class bcolors:
    BLUE = '\033[94m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    END = '\033[0m'


class Data:
    BALL = f'{bcolors.RED}X{bcolors.END}'
    WIDTH = COLUMNS - 1
    LENGTH = ROWS - 1


def draw(screen):
    print('\n')
    for row in screen:
        print('  '.join(row))


screen = [
    [f'{bcolors.BLUE}*{bcolors.END}' for _ in range(COLUMNS)] for _ in range(ROWS)]
screen[position[1]][position[0]] = Data.BALL

draw(screen)

while True:

    if position[0] == Data.WIDTH:
        if position[1] == 0:
            vector = [1, -1]
        elif position[1] == Data.LENGTH:
            vector = [-1, -1]
        else:
            if vector == [-1, 1]:
                vector = [-1, -1]
            elif vector == [1, 1]:
                vector = [1, -1]

    elif position[0] == 0:
        if position[1] == 0:
            vector = [1, 1]
        elif position[1] == Data.LENGTH:
            vector = [-1, 1]
        else:
            if vector == [-1, -1]:
                vector = [-1, 1]
            elif vector == [1, -1]:
                vector = [1, 1]

    elif position[1] == 0:
        if vector == [-1, 1]:
            vector = [1, 1]
        elif vector == [-1, -1]:
            vector = [1, -1]

    elif position[1] == Data.LENGTH:
        if vector == [1, 1]:
            vector = [-1, 1]
        elif vector == [1, -1]:
            vector = [-1, -1]

    screen[position[1]][position[0]] = f'{bcolors.YELLOW}*{bcolors.END}'
    position[1] += vector[0]
    position[0] += vector[1]
    screen[position[1]][position[0]] = Data.BALL

    draw(screen)

    time.sleep(DELAY)
