import sys

import pygame as pg
from pygame import mixer

from Color import Color
from Setting import Setting


def main():
    pitch = 4
    key_time = [[0 for _ in range(8)], [0 for _ in range(7)]]
    pitch_time = [0, 0]
    pg.init()
    mixer.init()
    pg.display.set_caption('Simple Sheet Music Maker')
    pg.display.set_icon(pg.image.load('assets/icon/favicon.ico'))
    font = pg.font.Font('assets/font/SpaceJaeger-BW2pn.otf', 24)
    surface = pg.display.set_mode((Setting.WIDTH, Setting.HEIGHT))
    surface.fill(Color.BACKGROUND)
    tools = ['file', 'save', 'play', 'stop', 'record', 'edit']
    t_keys = ['Q', 'W', 'E', 'R', 'T', 'Y']
    text = font.render('pitch', True, Color.WHITE, None)
    rect = text.get_rect()
    rect.center = (Setting.PITCH_X, Setting.PITCH_Y)
    surface.blit(text, rect)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_z:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\0\\1.mp3')
                        mixer.music.play()
                        key_time[0][0] = Setting.PRESS_TIME
                    case pg.K_x:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\0\\2.mp3')
                        mixer.music.play()
                        key_time[0][1] = Setting.PRESS_TIME
                    case pg.K_c:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\0\\3.mp3')
                        mixer.music.play()
                        key_time[0][2] = Setting.PRESS_TIME
                    case pg.K_v:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\0\\4.mp3')
                        mixer.music.play()
                        key_time[0][3] = Setting.PRESS_TIME
                    case pg.K_b:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\0\\5.mp3')
                        mixer.music.play()
                        key_time[0][4] = Setting.PRESS_TIME
                    case pg.K_n:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\0\\6.mp3')
                        mixer.music.play()
                        key_time[0][5] = Setting.PRESS_TIME
                    case pg.K_m:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\0\\7.mp3')
                        mixer.music.play()
                        key_time[0][6] = Setting.PRESS_TIME
                    case pg.K_s:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\1\\1.mp3')
                        mixer.music.play()
                        key_time[1][1] = Setting.PRESS_TIME
                    case pg.K_d:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\1\\2.mp3')
                        mixer.music.play()
                        key_time[1][2] = Setting.PRESS_TIME
                    case pg.K_g:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\1\\4.mp3')
                        mixer.music.play()
                        key_time[1][4] = Setting.PRESS_TIME
                    case pg.K_h:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\1\\5.mp3')
                        mixer.music.play()
                        key_time[1][5] = Setting.PRESS_TIME
                    case pg.K_j:
                        mixer.music.load(f'assets\\audio\\piano\\{pitch}\\1\\6.mp3')
                        mixer.music.play()
                        key_time[1][6] = Setting.PRESS_TIME
                    case pg.K_DOWN | pg.K_LEFT:
                        pitch = max(1, pitch - 1)
                        pitch_time[0] = Setting.PRESS_TIME
                    case pg.K_UP | pg.K_RIGHT:
                        pitch = min(7, pitch + 1)
                        pitch_time[1] = Setting.PRESS_TIME

        # Render Tools
        for i, tool in enumerate(tools):
            pg.draw.rect(surface, Color.BACKGROUND,
                         pg.Rect(Setting.TOOL_SPACE * i + Setting.TOOL_X - 5, Setting.TOOL_Y - 5, 60, 60))
            img = pg.transform.scale(pg.image.load(f'assets/image/{tool}.png').convert_alpha(), (50, 50))
            img.set_alpha(100)
            surface.blit(img, (Setting.TOOL_SPACE * i + Setting.TOOL_X, Setting.TOOL_Y))
            pg.draw.circle(surface, Color.WHITE,
                           (Setting.TOOL_SPACE * i + Setting.TOOL_X + 50, Setting.TOOL_Y + 45), 16, 0)
            text = font.render(t_keys[i], True, Color.BLACK, None)
            rect = text.get_rect()
            rect.center = (Setting.TOOL_SPACE * i + Setting.TOOL_X + 50, Setting.TOOL_Y + 45)
            surface.blit(text, rect)

        # Render Piano Keys
        w_keys = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        b_keys = ['A', 'S', 'D', 'F', 'G', 'H', 'J']
        for i in range(7):
            pg.draw.rect(surface, Color.PRESS_W if key_time[0][i] else Color.PIANO_W,
                         pg.Rect(64 * i + Setting.MARGIN_LEFT, 260, 60, 250))
            text = font.render(w_keys[i], True, Color.WHITE if key_time[0][i] else Color.BLACK, None)
            rect = text.get_rect()
            rect.center = (64 * i + Setting.MARGIN_LEFT + 30, 460)
            surface.blit(text, rect)
            if key_time[0][i]:
                key_time[0][i] -= 1
            if i == 0 or i == 3:
                continue
            pg.draw.rect(surface, Color.PRESS_B if key_time[1][i] else Color.PIANO_B,
                         pg.Rect(64 * i + Setting.MARGIN_LEFT - 20, 260, 40, 130))
            text = font.render(b_keys[i], True, Color.WHITE, None)
            rect = text.get_rect()
            rect.center = (64 * i + Setting.MARGIN_LEFT, 350)
            surface.blit(text, rect)
            if key_time[1][i]:
                key_time[1][i] -= 1

        # Render Pitch
        pg.draw.rect(surface, Color.BACKGROUND, pg.Rect(Setting.PITCH_X + 60, Setting.PITCH_Y - 15, 30, 30))
        text = font.render(str(pitch), True, Color.WHITE, None)
        rect = text.get_rect()
        rect.center = (Setting.PITCH_X + 75, Setting.PITCH_Y)
        surface.blit(text, rect)
        if pitch_time[0]:
            img = pg.transform.scale(pg.image.load('assets/image/left_on.png').convert_alpha(), (40, 40))
            pitch_time[0] -= 1
        else:
            img = pg.transform.scale(pg.image.load('assets/image/left.png').convert_alpha(), (40, 40))
        surface.blit(img, (Setting.PITCH_X - 105, Setting.PITCH_Y - 20))
        if pitch_time[1]:
            img = pg.transform.scale(pg.image.load('assets/image/right_on.png').convert_alpha(), (40, 40))
            pitch_time[1] -= 1
        else:
            img = pg.transform.scale(pg.image.load('assets/image/right.png').convert_alpha(), (40, 40))
        surface.blit(img, (Setting.PITCH_X + 105, Setting.PITCH_Y - 20))

        # Update
        pg.display.update()
        pg.time.Clock().tick(30)


if __name__ == '__main__':
    main()
