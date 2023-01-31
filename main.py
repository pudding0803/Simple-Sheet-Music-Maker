import sys

import pygame as pg
from winsound import Beep

FREQUENCY = [
    [16.352, 18.354, 20.602, 21.827, 24.5, 27.5, 30.868, 17.324, 19.445, 23.125, 25.957, 29.135],
    [32.703, 36.708, 41.203, 43.654, 48.999, 55, 61.735, 34.648, 38.891, 46.249, 51.913, 58.27],
    [65.406, 73.416, 82.407, 87.307, 97.999, 110, 123.47, 69.296, 77.782, 92.499, 103.83, 116.54],
    [130.81, 146.83, 164.81, 174.61, 196, 220, 246.94, 138.59, 155.56, 185, 207.65, 233.08],
    [261.63, 293.66, 329.63, 349.23, 392, 440, 493.88, 277.18, 311.13, 369.99, 415.3, 466.16],
    [523.25, 587.33, 659.26, 698.46, 783.99, 880, 987.77, 554.37, 622.25, 739.99, 830.61, 932.33],
    [1046.5, 1174.7, 1318.5, 1396.9, 1568, 1760, 1975.5, 1108.7, 1244.5, 1480, 1661.2, 1864.7],
    [2093, 2349.3, 2637, 2793.8, 3136, 3520, 3951.1, 2217.5, 2489, 2960, 3322.4, 3729.3],
    [4186, 4698.6, 5274, 5587.7, 6271.9, 7040, 7902.1, 4434.9, 4978, 5919.9, 6644.9, 7458.6],
    [8372, 9397.3, 10548, 11175, 12544, 14080, 15804, 8869.8, 9956.1, 11840, 13290, 14917]
]


def main():
    pitch = 5
    pg.init()
    display = pg.display.set_mode((300, 300))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_z: Beep(int(FREQUENCY[pitch][0]), 250)
                    case pg.K_x: Beep(int(FREQUENCY[pitch][1]), 250)
                    case pg.K_c: Beep(int(FREQUENCY[pitch][2]), 250)
                    case pg.K_v: Beep(int(FREQUENCY[pitch][3]), 250)
                    case pg.K_b: Beep(int(FREQUENCY[pitch][4]), 250)
                    case pg.K_n: Beep(int(FREQUENCY[pitch][5]), 250)
                    case pg.K_m: Beep(int(FREQUENCY[pitch][6]), 250)
                    case pg.K_s: Beep(int(FREQUENCY[pitch][7]), 250)
                    case pg.K_x: Beep(int(FREQUENCY[pitch][8]), 250)
                    case pg.K_g: Beep(int(FREQUENCY[pitch][9]), 250)
                    case pg.K_h: Beep(int(FREQUENCY[pitch][10]), 250)
                    case pg.K_j: Beep(int(FREQUENCY[pitch][11]), 250)
                    case pg.K_COMMA: pitch -= 1
                    case pg.K_PERIOD: pitch += 1
            # frequency = 500
            # duration = 2000
            # Beep(frequency, duration)


if __name__ == '__main__':
    main()
