import pygame
import os
import button

pygame.init()
pygame.mixer.init()
pygame.font.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
FPS = 30
FONT_SIZE = 30
FONT = pygame.font.SysFont('widelatin', FONT_SIZE)
GUESS_FONT = pygame.font.SysFont("widelatin", FONT_SIZE + 20)
ANSWER_FONT = pygame.font.SysFont("calibri", FONT_SIZE + 5)

EXIT_BUTTON_W = 120
EXIT_BUTTON_H = 43
START_BUTTON_W = 300
START_BUTTON_H = 169
HANG_BUTTON_W = 350
HANG_BUTTON_H = 83
LETTER_HOLDER_W = 25
LETTER_HOLDER_H = 5
CONFIRM_BUTTON_W = 350
CONFIRM_BUTTON_H = 58

BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hangman')
TITLE_BACKGROUND = pygame.image.load(os.path.join('Pictures', 'background_with_title.png'))
PASSWORD_BACKGROUND = pygame.image.load(os.path.join('Pictures', 'password_background.png'))
DESERT_BACKGROUND = pygame.image.load(os.path.join('Pictures', 'desert_bg.png'))
START_IMG_UNSELECTED = pygame.image.load(os.path.join('Pictures', 'Start_game - unselected.png'))
START_IMG_SELECTED = pygame.image.load(os.path.join('Pictures', 'Start_game - selected.png'))
EXIT_IMG_UNSELECTED = pygame.image.load(os.path.join('Pictures', 'Exit - unselected.png'))
EXIT_IMG_SELECTED = pygame.image.load(os.path.join('Pictures', 'Exit - selected.png'))
HANG_IMG_UNSELECTED = pygame.image.load(os.path.join('Pictures', 'Hang_button - unselected.png'))
HANG_IMG_SELECTED = pygame.image.load(os.path.join('Pictures', 'Hang_button - selected.png'))
CONFIRM_IMG_UNSELECTED = pygame.image.load(os.path.join('Pictures', 'confirm_unselected.png'))
CONFIRM_IMG_SELECTED = pygame.image.load(os.path.join('Pictures', 'confirm_selected.png'))


HANGMAN_STAGE_1 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_1.png'))
HANGMAN_STAGE_2 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_2.png'))
HANGMAN_STAGE_3 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_3.png'))
HANGMAN_STAGE_4 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_4.png'))
HANGMAN_STAGE_5 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_5.png'))
HANGMAN_STAGE_6 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_6.png'))
HANGMAN_STAGE_7 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_7.png'))
HANGMAN_STAGE_8 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_8.png'))
HANGMAN_STAGE_FINAL = pygame.image.load(os.path.join('Pictures', 'hangman_dead.png'))

start_button = (button.Button
                (SCREEN_WIDTH / 2 - START_BUTTON_W / 2, SCREEN_HEIGHT / 2 - START_BUTTON_H / 2 - 90,
                 START_IMG_UNSELECTED, START_IMG_SELECTED))
exit_button = (button.Button
               (SCREEN_WIDTH - EXIT_BUTTON_W - 10, 10, EXIT_IMG_UNSELECTED, EXIT_IMG_SELECTED))
hang_button = (button.Button
               (SCREEN_WIDTH - HANG_BUTTON_W - 10, SCREEN_HEIGHT - HANG_BUTTON_H - 10,
                HANG_IMG_UNSELECTED, HANG_IMG_SELECTED))
confirm_button = (button.Button
                  (SCREEN_WIDTH / 2 - CONFIRM_BUTTON_W / 2, 500,
                   CONFIRM_IMG_UNSELECTED, CONFIRM_IMG_SELECTED))


def track_answers(password, guess, list_of_holders, initiate):
    x_position = 400
    list_of_matches = []
    password_list = []
    for letter in password:
        password_list.append(letter)

    for _ in range(len(password)):
        if not initiate:
            let_hold = pygame.Rect(x_position, 150, LETTER_HOLDER_W, LETTER_HOLDER_H)
            x_position += LETTER_HOLDER_W + 7
            list_of_holders.append(let_hold)

    if guess in password_list:
        for char in password_list:
            if char == guess:
                list_of_matches.append(password_list.index(char))
                current_index = password_list.index(char)
                password_list[current_index] = " "
                print(list_of_matches)
        for index in list_of_matches:
            lst_letter_and_x = [guess]
            current_x_pos = list_of_holders[index][0]
            lst_letter_and_x.append(current_x_pos)
            list_of_holders[index] = lst_letter_and_x

    for let_holder in list_of_holders:
        print(let_holder)
        print(list_of_holders)
        if isinstance(let_holder[0], str):
            pass
            letter = ANSWER_FONT.render(let_holder[0], True, BLACK)
            screen.blit(letter, (let_holder[1], 136))
        else:
            pygame.draw.rect(screen, BLACK, let_holder)

    initiate = True
    guess = ''
    return initiate, guess


def draw_entering_password(password, font, pass_color, x, y):
    text = font.render(password, True, pass_color)
    text = pygame.transform.rotate(text, 20)
    width = text.get_width()
    height = text.get_height()
    screen.blit(text, [(x - (width / 2)), y - (height / 2)])


def draw_entering_guess(password, font, pass_color, x, y):
    text = font.render(password, True, pass_color)
    width = text.get_width()
    height = text.get_height()
    screen.blit(text, [(x - (width / 2)), y - (height / 2)])


def main():
    confirmed_guess = ''
    clock = pygame.time.Clock()
    run = True
    entering_password = False
    hanging_time = False
    password = ''
    letter_guess = ''
    list_of_holders = []
    initiate = False
    while run:
        clock.tick(FPS)
        if not entering_password:
            screen.blit(TITLE_BACKGROUND, (0, 0))

            if start_button.draw(screen):
                entering_password = True

            if exit_button.draw(screen):
                run = False

        if entering_password and not hanging_time:
            screen.blit(PASSWORD_BACKGROUND, (0, 0))
            draw_entering_password(password, FONT, BLACK, 380, 400)
            if exit_button.draw(screen):
                run = False

            if hang_button.draw(screen) and password:
                hanging_time = True
                entering_password = False

        if hanging_time:
            screen.blit(DESERT_BACKGROUND, (0, 0))
            screen.blit(HANGMAN_STAGE_FINAL, (15, 110))
            initiate, confirmed_guess = track_answers(password, confirmed_guess, list_of_holders, initiate)
            draw_entering_guess(letter_guess, GUESS_FONT, BLACK, 515, 400)

            if confirm_button.draw(screen):
                print('sca')

            if exit_button.draw(screen):
                run = False

        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                if entering_password:
                    password += event.text.upper()
                elif hanging_time:
                    letter_guess = event.text.upper()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if entering_password:
                        password = password[:-1]
                if event.key == (pygame.K_RETURN or pygame.K_KP_ENTER) and password and entering_password:
                    hanging_time = True
                    entering_password = False
                if event.key == (pygame.K_RETURN or pygame.K_KP_ENTER) and letter_guess and hanging_time:
                    confirmed_guess = letter_guess

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
