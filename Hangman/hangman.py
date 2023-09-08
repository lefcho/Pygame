import pygame
import os
import button

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
FPS = 30
EXIT_BUTTON_W = 120
EXIT_BUTTON_H = 43
START_BUTTON_W = 300
START_BUTTON_H = 169

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hangman')
TITLE_BACKGROUND = pygame.image.load(os.path.join('Pictures', 'background_with_title.png'))
start_img_unselected = pygame.image.load(os.path.join('Pictures', 'Start_game - unselected.png'))
start_img_selected = pygame.image.load(os.path.join('Pictures', 'Start_game - selected.png'))
exit_img_unselected = pygame.image.load(os.path.join('Pictures', 'Exit - unselected.png'))
exit_img_selected = pygame.image.load(os.path.join('Pictures', 'Exit - selected.png'))

start_button = (button.Button
                (SCREEN_WIDTH / 2 - START_BUTTON_W / 2, SCREEN_HEIGHT / 2 - START_BUTTON_H / 2 - 90,
                 start_img_unselected, start_img_selected))
exit_button = button.Button(SCREEN_WIDTH - EXIT_BUTTON_W - 10, 10, exit_img_unselected, exit_img_selected)


def main():
    clock = pygame.time.Clock()
    run = True
    game_started = False
    while run:
        clock.tick(FPS)

        if not game_started:
            screen.blit(TITLE_BACKGROUND, (0, 0))

            if start_button.draw(screen):
                game_started = True
                print('START')

        if exit_button.draw(screen):
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
