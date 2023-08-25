import pygame
import os
import sys
pygame.mixer.init()
pygame.font.init()

pygame.display.set_caption("Tic-tac-toe")
SIDE = 700
FPS = 30
WIN = pygame.display.set_mode((SIDE, SIDE))
LINE_WIDTH = 60
END_MESSAGE_BG_HEIGHT = 120

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PAPER = pygame.image.load(os.path.join('Assets', 'paper_background.jpg'))
HORIZONTAL_LINE = pygame.image.load(os.path.join('Assets', "black_line.png"))
VERTICAL_LINE = pygame.transform.rotate(HORIZONTAL_LINE, 90)
SQUARE = pygame.image.load(os.path.join('Assets', 'square_frame.png'))
X_IMAGE = pygame.image.load(os.path.join('Assets', 'ttt_x1.png'))
O_IMAGE = pygame.image.load(os.path.join('Assets', 'ttt_o1.png'))
END_MESSAGE_BACKGROUND = pygame.Rect(0, SIDE / 2 - END_MESSAGE_BG_HEIGHT / 2, SIDE, END_MESSAGE_BG_HEIGHT)
DRAW_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'draw.mp3'))
WIN_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'win.mp3'))
TIE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'tie.wav'))
WINNER_FONT = pygame.font.SysFont('inkfree', 80)


def draw_game(t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r, mouse_position):
    WIN.blit(PAPER, (0, 0))
    WIN.blit(VERTICAL_LINE, (SIDE / 3 - LINE_WIDTH / 2, 0))
    WIN.blit(VERTICAL_LINE, ((SIDE / 3) * 2 - LINE_WIDTH / 2, 0))
    WIN.blit(HORIZONTAL_LINE, (0, SIDE / 3 - LINE_WIDTH / 2))
    WIN.blit(HORIZONTAL_LINE, (0, (SIDE / 3) * 2 - LINE_WIDTH / 2))

    if mouse_position[0] < SIDE / 3 and mouse_position[1] < SIDE / 3 and not t_l:  # TOP_LEFT
        WIN.blit(SQUARE, (10, 10))
    elif mouse_position[0] < (SIDE / 3) * 2 and mouse_position[1] < SIDE / 3 and not t_m:   # TOP_MIDDLE
        WIN.blit(SQUARE, (12 + SIDE / 3, 10))
    elif (SIDE / 3) * 2 < mouse_position[0] < (SIDE / 3) * 3 and mouse_position[1] < SIDE / 3 and not t_r:   # TOP_RIGHt
        WIN.blit(SQUARE, (12 + SIDE / 3 * 2, 10))
    elif mouse_position[0] < SIDE / 3 and mouse_position[1] < SIDE / 3 * 2 and not m_l:   # MIDDLE_LEFT
        WIN.blit(SQUARE, (10, 12 + SIDE / 3))
    elif mouse_position[0] < SIDE / 3 and mouse_position[1] < SIDE / 3 * 3 and not b_l:   # BOTTOM_LEFT
        WIN.blit(SQUARE, (10, 12 + SIDE / 3 * 2))
    elif mouse_position[0] < SIDE / 3 * 2 and mouse_position[1] < SIDE / 3 * 2 and not m_m:   # MIDDLE_MIDDLE
        WIN.blit(SQUARE, (12 + SIDE / 3, 12 + SIDE / 3))
    elif mouse_position[0] < SIDE / 3 * 3 and mouse_position[1] < SIDE / 3 * 2 and not m_r:   # MIDDLE_RIGHT
        WIN.blit(SQUARE, (12 + SIDE / 3 * 2, 12 + SIDE / 3))
    elif mouse_position[0] < SIDE / 3 * 2 and mouse_position[1] < SIDE / 3 * 3 and not b_m:    # BOTTOM_MIDDLE
        WIN.blit(SQUARE, (SIDE / 3 + 12, 12 + SIDE / 3 * 2))
    elif mouse_position[0] < SIDE / 3 * 3 and mouse_position[1] < SIDE / 3 * 3 and not b_r:   # BOTTOM_RIGHT
        WIN.blit(SQUARE, (SIDE / 3 * 2 + 12, 12 + SIDE / 3 * 2))

    if t_l == 'x':
        WIN.blit(X_IMAGE, (10, 10))
    elif t_l == 'o':
        WIN.blit(O_IMAGE, (10, 10))
    if t_m == 'x':
        WIN.blit(X_IMAGE, (12 + SIDE / 3, 10))
    elif t_m == 'o':
        WIN.blit(O_IMAGE, (12 + SIDE / 3, 10))
    if t_r == 'x':
        WIN.blit(X_IMAGE, (12 + SIDE / 3 * 2, 10))
    elif t_r == 'o':
        WIN.blit(O_IMAGE, (12 + SIDE / 3 * 2, 10))
    if m_l == 'x':
        WIN.blit(X_IMAGE, (10, 12 + SIDE / 3))
    elif m_l == 'o':
        WIN.blit(O_IMAGE, (10, 12 + SIDE / 3))
    if m_m == 'x':
        WIN.blit(X_IMAGE, (12 + SIDE / 3, 12 + SIDE / 3))
    elif m_m == 'o':
        WIN.blit(O_IMAGE, (12 + SIDE / 3, 12 + SIDE / 3))
    if m_r == 'x':
        WIN.blit(X_IMAGE, (12 + SIDE / 3 * 2, 12 + SIDE / 3))
    elif m_r == 'o':
        WIN.blit(O_IMAGE, (12 + SIDE / 3 * 2, 12 + SIDE / 3))
    if b_l == 'x':
        WIN.blit(X_IMAGE, (10, 12 + SIDE / 3 * 2))
    elif b_l == 'o':
        WIN.blit(O_IMAGE, (10, 12 + SIDE / 3 * 2))
    if b_m == 'x':
        WIN.blit(X_IMAGE, (SIDE / 3 + 12, 12 + SIDE / 3 * 2))
    elif b_m == 'o':
        WIN.blit(O_IMAGE, (SIDE / 3 + 12, 12 + SIDE / 3 * 2))
    if b_r == 'x':
        WIN.blit(X_IMAGE, (SIDE / 3 * 2 + 12, 12 + SIDE / 3 * 2))
    elif b_r == 'o':
        WIN.blit(O_IMAGE, (SIDE / 3 * 2 + 12, 12 + SIDE / 3 * 2))

    pygame.display.update()


def keep_score(mouse_pressed, mouse_position, t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r, turn):
    if mouse_pressed[0]:
        if mouse_position[0] < SIDE / 3 and mouse_position[1] < SIDE / 3 and not t_l:
            if turn % 2 == 0:
                t_l = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                t_l = 'o'
                turn += 1
                DRAW_SOUND.play()
        elif SIDE / 3 < mouse_position[0] < (SIDE / 3) * 2 and mouse_position[1] < SIDE / 3 and not t_m:
            if turn % 2 == 0:
                t_m = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                t_m = 'o'
                turn += 1
                DRAW_SOUND.play()
        elif (SIDE / 3) * 2 < mouse_position[0] < SIDE and mouse_position[1] < SIDE / 3 and not t_r:
            if turn % 2 == 0:
                t_r = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                t_r = 'o'
                turn += 1
                DRAW_SOUND.play()
        elif mouse_position[0] < SIDE / 3 and SIDE / 3 < mouse_position[1] < SIDE / 3 * 2 and not m_l:
            if turn % 2 == 0:
                m_l = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                m_l = 'o'
                turn += 1
                DRAW_SOUND.play()
        elif SIDE / 3 < mouse_position[0] < (SIDE / 3) * 2 and SIDE / 3 < mouse_position[1] < SIDE / 3 * 2 and not m_m:
            if turn % 2 == 0:
                m_m = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                m_m = 'o'
                turn += 1
                DRAW_SOUND.play()
        elif SIDE / 3 * 2 < mouse_position[0] < SIDE and SIDE / 3 < mouse_position[1] < SIDE / 3 * 2 and not m_r:
            if turn % 2 == 0:
                m_r = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                m_r = 'o'
                turn += 1
                DRAW_SOUND.play()
        elif mouse_position[0] < SIDE / 3 and SIDE / 3 * 2 < mouse_position[1] < SIDE and not b_l:
            if turn % 2 == 0:
                b_l = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                b_l = 'o'
                turn += 1
                DRAW_SOUND.play()
        elif SIDE / 3 < mouse_position[0] < SIDE / 3 * 2 and SIDE / 3 * 2 < mouse_position[1] < SIDE and not b_m:
            if turn % 2 == 0:
                b_m = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                b_m = 'o'
                turn += 1
                DRAW_SOUND.play()
        elif SIDE / 3 * 2 < mouse_position[0] < SIDE and SIDE / 3 * 2 < mouse_position[1] < SIDE and not b_r:
            if turn % 2 == 0:
                b_r = 'x'
                turn += 1
                DRAW_SOUND.play()
            else:
                b_r = 'o'
                turn += 1
                DRAW_SOUND.play()
    return t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r, turn


def check_winner(t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r):
    x_wins = False
    o_wins = False
    if t_l == t_m == t_r:
        if t_l == 'x':
            x_wins = True
        elif t_l == 'o':
            o_wins = True
    if m_l == m_m == m_r:
        if m_l == 'x':
            x_wins = True
        elif m_l == 'o':
            o_wins = True
    if b_l == b_m == b_r:
        if b_l == 'x':
            x_wins = True
        elif b_l == 'o':
            o_wins = True
    if t_l == m_l == b_l:
        if t_l == 'x':
            x_wins = True
        elif t_l == 'o':
            o_wins = True
    if t_m == m_m == b_m:
        if t_m == 'x':
            x_wins = True
        elif t_m == 'o':
            o_wins = True
    if t_r == m_r == b_r:
        if t_r == 'x':
            x_wins = True
        elif t_r == 'o':
            o_wins = True
    if t_l == m_m == b_r:
        if t_l == 'x':
            x_wins = True
        elif t_l == 'o':
            o_wins = True
    if t_r == m_m == b_l:
        if t_r == 'x':
            x_wins = True
        elif t_r == 'o':
            o_wins = True

    return x_wins, o_wins


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    pygame.draw.rect(WIN, BLACK, END_MESSAGE_BACKGROUND)
    WIN.blit(draw_text, (SIDE / 2 - draw_text.get_width() / 2, SIDE / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    mouse_pressed = (False, False, False)
    o_wins = False
    x_wins = False
    turn = 0
    clock = pygame.time.Clock()
    run = True
    restart = True

    t_l = ''
    t_m = ''
    t_r = ''
    m_l = ''
    m_m = ''
    m_r = ''
    b_l = ''
    b_m = ''
    b_r = ''

    while run:
        clock.tick(FPS)
        mouse_position = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                sys.exit()

        if restart and mouse_pressed[0]:
            restart = False
            continue

        t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r, turn = keep_score(
            mouse_pressed, mouse_position, t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r, turn)

        x_wins, o_wins = check_winner(t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r)

        draw_game(t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r, mouse_position)

        win_txt = ''
        if x_wins:
            WIN_SOUND.play()
            win_txt = "X-player WINS!"

        elif o_wins:
            WIN_SOUND.play()
            win_txt = "O-player WINS!"

        elif turn >= 9:
            TIE_SOUND.play()
            win_txt = 'DRAW!'

        if win_txt != '':
            draw_winner(win_txt)
            break

    main()


if __name__ == "__main__":
    main()
