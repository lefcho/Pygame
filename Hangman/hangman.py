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

EXIT_BUTTON_W = 120
EXIT_BUTTON_H = 43
START_BUTTON_W = 300
START_BUTTON_H = 169

BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hangman')
TITLE_BACKGROUND = pygame.image.load(os.path.join('Pictures', 'background_with_title.png'))
PASSWORD_BACKGROUND = pygame.image.load(os.path.join('Pictures', 'password_background.png'))
START_IMG_UNSELECTED = pygame.image.load(os.path.join('Pictures', 'Start_game - unselected.png'))
START_IMG_SELECTED = pygame.image.load(os.path.join('Pictures', 'Start_game - selected.png'))
EXIT_IMG_UNSELECTED = pygame.image.load(os.path.join('Pictures', 'Exit - unselected.png'))
EXIT_IMG_SELECTED = pygame.image.load(os.path.join('Pictures', 'Exit - selected.png'))

start_button = (button.Button
                (SCREEN_WIDTH / 2 - START_BUTTON_W / 2, SCREEN_HEIGHT / 2 - START_BUTTON_H / 2 - 90,
                 START_IMG_UNSELECTED, START_IMG_SELECTED))
exit_button = button.Button(SCREEN_WIDTH - EXIT_BUTTON_W - 10, 10, EXIT_IMG_UNSELECTED, EXIT_IMG_SELECTED)


def draw_entering_password(password, font, pass_color, x, y):
    text = font.render(password, True, pass_color)
    text = pygame.transform.rotate(text, 20)
    width = text.get_width()
    height = text.get_height()
    screen.blit(text, [(x - (width / 2)), y - (height / 2)])


def main():
    clock = pygame.time.Clock()
    run = True
    game_started = False
    password = ''
    while run:
        clock.tick(FPS)
        if not game_started:
            screen.blit(TITLE_BACKGROUND, (0, 0))

            if start_button.draw(screen):
                game_started = True

            if exit_button.draw(screen):
                run = False

        if game_started:
            screen.blit(PASSWORD_BACKGROUND, (0, 0))
            draw_entering_password(password, FONT, BLACK, 380, 400)
            if exit_button.draw(screen):
                run = False

        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                if game_started:
                    password += event.text

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if game_started:
                        password = password[:-1]

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
