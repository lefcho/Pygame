import pygame
import os
import button
import sys

pygame.init()
pygame.mixer.init()
pygame.font.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
FPS = 30
FONT_SIZE = 30
FONT = pygame.font.SysFont('widelatin', FONT_SIZE)
GUESS_FONT = pygame.font.SysFont("widelatin", FONT_SIZE + 20)
WINNER_FONT = pygame.font.SysFont("widelatin", FONT_SIZE + 15)
ANSWER_FONT = pygame.font.SysFont("calibri", FONT_SIZE + 5)
SMALL_FONT = pygame.font.SysFont("widelatin", FONT_SIZE - 5)

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
END_MESSAGE_BG_HEIGHT = 286
END_MESSAGE_BG_WIDTH = 500

BLACK = (0, 0, 0)
GREEN = (82, 209, 50)

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
RESTART_IMG_UNSELECTED = pygame.image.load(os.path.join('Pictures', 'restart_img_unselected.png'))
RESTART_IMG_SELECTED = pygame.image.load(os.path.join('Pictures', 'restart_img_selected.png'))
WOODEN_SIGN_IMG = pygame.image.load(os.path.join('Pictures', 'Wooden Sign.png'))

HANGMAN_STAGE_1 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_1.png'))
HANGMAN_STAGE_2 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_2.png'))
HANGMAN_STAGE_3 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_3.png'))
HANGMAN_STAGE_4 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_4.png'))
HANGMAN_STAGE_5 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_5.png'))
HANGMAN_STAGE_6 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_6.png'))
HANGMAN_STAGE_7 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_7.png'))
HANGMAN_STAGE_8 = pygame.image.load(os.path.join('Pictures', 'hangman_stage_8.png'))
HANGMAN_STAGE_FINAL = pygame.image.load(os.path.join('Pictures', 'hangman_dead.png'))

START_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'revolver_cock.mp3'))
FIRE_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'shotgun-firing.mp3'))
TYPE_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'type-writing-single.mp3'))
BELL_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'church_bell.mp3'))
HAMMERING_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'hammering-nail.mp3'))
ROPE_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'rope-sound.mp3'))
DING_SOUND = pygame.mixer.Sound(os.path.join('Sounds', 'ding-sound.mp3'))

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
restart_button = button.Button(SCREEN_WIDTH / 2 - RESTART_IMG_SELECTED.get_width() / 2, 500, RESTART_IMG_UNSELECTED, RESTART_IMG_SELECTED)


def track_answers(password, guess, list_of_holders, used_letters_list, initiate, stage):
    x_position = 400
    list_of_matches = []
    password_list = []
    current_answer = ''
    for letter in password:
        password_list.append(letter)

    for _ in range(len(password)):
        if not initiate:
            let_hold = pygame.Rect(x_position, 150, LETTER_HOLDER_W, LETTER_HOLDER_H)
            x_position += LETTER_HOLDER_W + 7
            list_of_holders.append(let_hold)

    if guess in password_list:
        DING_SOUND.play()
        for char in password_list:
            if char == guess:
                list_of_matches.append(password_list.index(char))
                current_index = password_list.index(char)
                password_list[current_index] = " "
        for index in list_of_matches:
            lst_letter_and_x = [guess]
            current_x_pos = list_of_holders[index][0]
            lst_letter_and_x.append(current_x_pos)
            list_of_holders[index] = lst_letter_and_x
    elif guess:
        stage -= 1
        if stage == 8 or stage == 7:
            HAMMERING_SOUND.play()
        elif 0 <= stage < 7:
            ROPE_SOUND.play()

    for let_holder in list_of_holders:
        if isinstance(let_holder[0], str):
            pass
            letter = ANSWER_FONT.render(let_holder[0], True, BLACK)
            screen.blit(letter, (let_holder[1], 136))
            current_answer += let_holder[0]
        else:
            pygame.draw.rect(screen, BLACK, let_holder)

    initiate = True
    guess = ''
    return initiate, guess, used_letters_list, current_answer, stage


def draw_used_letters(used_letters, password, font, color, x, y):
    password_list = []
    for letter in password:
        password_list.append(letter)
    final_char_list = []
    for letter in used_letters:
        if letter not in password:
            final_char_list.append(letter)
    used_letters_text = font.render('Used letters: ' + " ".join(final_char_list), True, color)
    height = used_letters_text.get_height()

    strikes = 9 - len(final_char_list)
    strikes_text = font.render("Strikes  left: " + str(strikes), True, color)

    screen.blit(strikes_text, (x, y + height + 2))
    screen.blit(used_letters_text, (x, y))

    return strikes


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


def draw_hangman(strikes):
    if strikes == 8:
        screen.blit(HANGMAN_STAGE_1, (15, 110))
    elif strikes == 7:
        screen.blit(HANGMAN_STAGE_2, (15, 110))
    elif strikes == 6:
        screen.blit(HANGMAN_STAGE_3, (15, 110))
    elif strikes == 5:
        screen.blit(HANGMAN_STAGE_4, (15, 110))
    elif strikes == 4:
        screen.blit(HANGMAN_STAGE_5, (15, 110))
    elif strikes == 3:
        screen.blit(HANGMAN_STAGE_6, (15, 110))
    elif strikes == 2:
        screen.blit(HANGMAN_STAGE_7, (15, 110))
    elif strikes == 1:
        screen.blit(HANGMAN_STAGE_8, (15, 110))
    elif strikes <= 0:
        screen.blit(HANGMAN_STAGE_FINAL, (15, 110))


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, BLACK)
    screen.blit(WOODEN_SIGN_IMG, (SCREEN_WIDTH - END_MESSAGE_BG_WIDTH, 165))
    screen.blit(draw_text, (SCREEN_WIDTH - END_MESSAGE_BG_WIDTH + (END_MESSAGE_BG_WIDTH - draw_text.get_width()) / 2,
                            SCREEN_HEIGHT / 2 - draw_text.get_height() / 2 - 60))


def main():
    win = False
    confirmed_guess = ''
    clock = pygame.time.Clock()
    run = True
    welcome_screen = True
    entering_password = False
    hanging_time = False
    ending_screen = False
    password = ''
    letter_guess = ''
    current_answer = ''
    list_of_holders = []
    used_letters_list = []
    stage = 9
    initiate = False
    while run:
        clock.tick(FPS)
        if welcome_screen:
            screen.blit(TITLE_BACKGROUND, (0, 0))

            if start_button.draw(screen):
                START_SOUND.play()
                entering_password = True
                welcome_screen = False

            if exit_button.draw(screen):
                run = False
                sys.exit()

        if entering_password:
            screen.blit(PASSWORD_BACKGROUND, (0, 0))
            draw_entering_password(password, FONT, BLACK, 380, 400)
            if exit_button.draw(screen):
                run = False
                sys.exit()

            if hang_button.draw(screen) and password:
                FIRE_SOUND.play()
                hanging_time = True
                entering_password = False

        if hanging_time:
            screen.blit(DESERT_BACKGROUND, (0, 0))
            initiate, confirmed_guess, used_letters_list, current_answer, stage =\
                (track_answers(password, confirmed_guess, list_of_holders, used_letters_list, initiate, stage))
            draw_entering_guess(letter_guess, GUESS_FONT, BLACK, 515, 400)
            strikes = draw_used_letters(used_letters_list, password, FONT, BLACK, 10, 10)
            draw_hangman(strikes)

            if confirm_button.draw(screen):
                if letter_guess not in used_letters_list:
                    confirmed_guess = letter_guess
                    used_letters_list.append(confirmed_guess)


            if strikes <= 0:
                win = False
                ending_screen = True
                hanging_time = False
            elif current_answer == password:
                win = True
                ending_screen = True
                hanging_time = False

            if exit_button.draw(screen):
                run = False
                sys.exit()

        if ending_screen:
            if not win:
                draw_winner("HANGED!")
                loser_text = SMALL_FONT.render('The password was: ', 1, BLACK)
                password_text = SMALL_FONT.render(password, 1, BLACK)
                pass_width = password_text.get_width()
                screen.blit(password_text, [(750 - (pass_width / 2)), 370])
                screen.blit(loser_text, (550, 300))
            else:
                draw_winner("SAVED!")

            if restart_button.draw(screen):
                BELL_SOUND.play()
                main()

            if exit_button.draw(screen):
                run = False
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                if entering_password:
                    TYPE_SOUND.play()
                    password += event.text.upper()
                elif hanging_time:
                    letter_guess = event.text.upper()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if entering_password:
                        TYPE_SOUND.play()
                        password = password[:-1]
                if event.key == (pygame.K_RETURN or pygame.K_KP_ENTER) and welcome_screen:
                    START_SOUND.play()
                    entering_password = True
                    welcome_screen = False
                if event.key == (pygame.K_RETURN or pygame.K_KP_ENTER) and password and entering_password:
                    FIRE_SOUND.play()
                    hanging_time = True
                    entering_password = False
                if event.key == (pygame.K_RETURN or pygame.K_KP_ENTER) and letter_guess and hanging_time:
                    if letter_guess not in used_letters_list:
                        confirmed_guess = letter_guess
                        used_letters_list.append(confirmed_guess)
                if event.key == (pygame.K_RETURN or pygame.K_KP_ENTER) and ending_screen:
                    BELL_SOUND.play()
                    main()

            if event.type == pygame.QUIT:
                run = False
                sys.exit()

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
