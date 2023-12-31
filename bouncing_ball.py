import random
import os
import time


os.system('color')

colors = {
    'blue': '\033[94m',
    'red': '\033[91m',
    'yellow': '\033[93m',
    'purple': '\033[95m',
    'green': '\033[92m',
    'white': '\u001b[37m',
    'end': '\033[0m'
}

settings = {
    'columns': 40,
    'rows': 15,
    'velocity': 20,
    'terminal_velocity': None,
    'acceleration': 1,
    'ball_symbol': '0',
    'empty_symbol': '1',
    'ball_color': colors['green'],
    'screen_color': colors['red'],
    'step': 1,
    'show_velocity': True,
    'alternating_velocity': {
        'on': True,
        'minimum': 15,
        'maximum': 250
    }
}

ball = {
    'ball': (settings['ball_color'] + settings['ball_symbol'] + colors['end']),
    'width': settings['columns'] - 1,
    'length': settings['rows'] - 1,
}

VECTORS = (1, -1)
position = [random.randint(0, ball['width']), random.randint(0, ball['length'])]
trail_colors = [ansi_code for ansi_code in colors.values() if ansi_code not in (settings['ball_color'], settings['screen_color'])] + [settings['screen_color']]


class Screen:
    def __init__(self):
        self.screen = [[(settings['screen_color'] + settings['empty_symbol'] + colors['end']) for _ in range(settings['columns'])] for _ in range(settings['rows'])]
        self.seen = [[0 for _ in range(settings['columns'])] for _ in range(settings['rows'])]
        self.vector = [random.choice(VECTORS), random.choice(VECTORS)]
        self.accelerate = True

    def draw(self):
        print("\033c", end="")
        print('\n'.join('  '.join(row) for row in self.screen))
        if settings['show_velocity']:
            print(f"velocity={settings['velocity']}")
    
    def update_velocity(self):
        if not settings['alternating_velocity']['on']:
            if settings['terminal_velocity'] is None or settings['velocity'] < settings['terminal_velocity']:
                settings['velocity'] += settings['acceleration']
            else:
                settings['velocity'] = settings['terminal_velocity']

        else:
            if settings['velocity'] >= settings['alternating_velocity']['maximum'] and self.accelerate:
                self.accelerate = False
            elif settings['velocity'] <= settings['alternating_velocity']['minimum'] and not self.accelerate or settings['velocity'] == 1:
                self.accelerate = True

            if self.accelerate:
                settings['velocity'] += settings['acceleration']
            else:
                settings['velocity'] -= settings['acceleration']

    def update_vector(self):
        x, y = position

        if x == 0 or x == ball['width']:
            self.update_velocity()
            self.vector[1] *= -1

        if y == 0 or y == ball['length']:
            self.update_velocity()
            self.vector[0] *= -1

        return self.vector
    
    def pause(self, duration):
        start_time = time.perf_counter()
        while True:
            elapsed_time = time.perf_counter() - start_time
            remaining_time = duration - elapsed_time
            if remaining_time <= 0:
                break
            if remaining_time > 0.02:
                time.sleep(max(remaining_time / 2, 0.0001))
            else:
                pass


ball_screen = Screen()
ball_screen.screen[position[1]][position[0]] = ball['ball']
ball_screen.draw()

pixel_count = 0

try:
    while True:

        vector = ball_screen.update_vector()

        pixel_color = trail_colors[(ball_screen.seen[position[1]][position[0]]) % len(trail_colors)]

        ball_screen.screen[position[1]][position[0]] = pixel_color + settings['empty_symbol'] + colors['end']
        ball_screen.seen[position[1]][position[0]] += 1

        position[1] += vector[0]
        position[0] += vector[1]
        ball_screen.screen[position[1]][position[0]] = ball['ball']

        if pixel_count % settings['step'] == 0:
            ball_screen.draw()
            
        pixel_count += 1 
        ball_screen.pause(1 / settings['velocity'])

except KeyboardInterrupt:
    ball_screen.draw()
    print('Stopped.')
