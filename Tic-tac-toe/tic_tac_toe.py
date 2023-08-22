import pygame
import os

pygame.display.set_caption("Tic-tac-toe")
SIDE = 700
FPS = 30
WIN = pygame.display.set_mode((SIDE, SIDE))
LINE_WIDTH = 60

WHITE = (255, 255, 255)
PAPER = pygame.image.load(os.path.join('Assets', 'paper_background.jpg'))
HORIZONTAL_LINE = pygame.image.load(os.path.join('Assets', "black_line.png"))
VERTICAL_LINE = pygame.transform.rotate(HORIZONTAL_LINE, 90)
SQUARE = pygame.image.load(os.path.join('Assets', 'square_frame.png'))
X_IMAGE = pygame.image.load(os.path.join('Assets', 'ttt_x.png'))
O_IMAGE = pygame.image.load(os.path.join('Assets', 'ttt_o.png'))


def draw_game(t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r, mouse_position):
    WIN.blit(PAPER, (0, 0))
    WIN.blit(VERTICAL_LINE, (SIDE / 3 - LINE_WIDTH / 2, 0))
    WIN.blit(VERTICAL_LINE, ((SIDE / 3) * 2 - LINE_WIDTH / 2, 0))
    WIN.blit(HORIZONTAL_LINE, (0, SIDE / 3 - LINE_WIDTH / 2))
    WIN.blit(HORIZONTAL_LINE, (0, (SIDE / 3) * 2 - LINE_WIDTH / 2))

    if mouse_position[0] < SIDE / 3 and mouse_position[1] < SIDE / 3:   #TOP_LEFT
        WIN.blit(SQUARE, (10, 10))
    elif mouse_position[0] < (SIDE / 3) * 2 and mouse_position[1] < SIDE / 3:   #TOP_MIDDLE
        WIN.blit(SQUARE, (12 + SIDE / 3, 10))
    elif (SIDE / 3) * 2 < mouse_position[0] < (SIDE / 3) * 3 and mouse_position[1] < SIDE / 3:   #TOP_RIGHt
        WIN.blit(SQUARE, (12 + SIDE / 3 * 2, 10))
    elif mouse_position[0] < SIDE / 3 and mouse_position[1] < SIDE / 3 * 2:   #MIDDLE_LEFT
        WIN.blit(SQUARE, (10, 12 + SIDE / 3))
    elif mouse_position[0] < SIDE / 3 and mouse_position[1] < SIDE / 3 * 3:   #BOTTOM_LEFT
        WIN.blit(SQUARE, (10, 12 + SIDE / 3 * 2))
    elif mouse_position[0] < SIDE / 3 * 2 and mouse_position[1] < SIDE / 3 * 2:   #MIDDLE_MIDDLE
        WIN.blit(SQUARE, (12 + SIDE / 3, 12 + SIDE / 3))
    elif mouse_position[0] < SIDE / 3 * 3 and mouse_position[1] < SIDE / 3 * 2:   #MIDDLE_RIGHT
        WIN.blit(SQUARE, (12 + SIDE / 3 * 2, 12 + SIDE / 3))
    elif mouse_position[0] < SIDE / 3 * 2 and mouse_position[1] < SIDE / 3 * 3:    #BOTTOM_MIDDLE
        WIN.blit(SQUARE, (SIDE / 3 + 12, 12 + SIDE / 3 * 2))
    elif mouse_position[0] < SIDE / 3 * 3 and mouse_position[1] < SIDE / 3 * 3:   #BOTTOM_RIGHT
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


def main():

    turn = 0
    clock = pygame.time.Clock()
    run = True

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
                run = False

        if mouse_pressed[0]:
            print(mouse_position)
            if mouse_position[0] < SIDE / 3 and mouse_position[1] < SIDE / 3 and not t_l:
                if turn % 2 == 0:
                    t_l = 'x'
                    turn += 1
                else:
                    t_l = 'o'
                    turn += 1
            elif SIDE / 3 < mouse_position[0] < (SIDE / 3) * 2 and mouse_position[1] < SIDE / 3 and not t_m:
                if turn % 2 == 0:
                    t_m = 'x'
                    turn += 1
                else:
                    t_m = 'o'
                    turn += 1
            elif (SIDE / 3) * 2 < mouse_position[0] < SIDE and mouse_position[1] < SIDE / 3 and not t_r:
                if turn % 2 == 0:
                    t_r = 'x'
                    turn += 1
                else:
                    t_r = 'o'
                    turn += 1
            elif mouse_position[0] < SIDE / 3 and SIDE / 3 < mouse_position[1] < SIDE / 3 * 2 and not m_l:
                if turn % 2 == 0:
                    m_l = 'x'
                    turn += 1
                else:
                    m_l = 'o'
                    turn += 1
            elif SIDE / 3 < mouse_position[0] < (SIDE / 3) * 2 and SIDE / 3 < mouse_position[1] < SIDE / 3 * 2 and not m_m:
                if turn % 2 == 0:
                    m_m = 'x'
                    turn += 1
                else:
                    m_m = 'o'
                    turn += 1
            elif SIDE / 3 * 2 < mouse_position[0] < SIDE and SIDE / 3 < mouse_position[1] < SIDE / 3 * 2 and not m_r:
                if turn % 2 == 0:
                    m_r = 'x'
                    turn += 1
                else:
                    m_r = 'o'
                    turn += 1
            elif mouse_position[0] < SIDE / 3 and SIDE / 3 * 2 < mouse_position[1] < SIDE and not b_l:
                if turn % 2 == 0:
                    b_l = 'x'
                    turn += 1
                else:
                    b_l = 'o'
                    turn += 1
            elif SIDE / 3 < mouse_position[0] < SIDE / 3 * 2 and SIDE / 3 * 2 < mouse_position[1] < SIDE and not b_m:
                if turn % 2 == 0:
                    b_m = 'x'
                    turn += 1
                else:
                    b_m = 'o'
                    turn += 1
            elif SIDE / 3 * 2 < mouse_position[0] < SIDE and SIDE / 3 * 2 < mouse_position[1] < SIDE and not b_r:
                if turn % 2 == 0:
                    b_r = 'x'
                    turn += 1
                else:
                    b_r = 'o'
                    turn += 1

        draw_game(t_l, t_m, t_r, m_l, m_m, m_r, b_l, b_m, b_r, mouse_position)
    pygame.quit()


if __name__ == "__main__":
    main()
