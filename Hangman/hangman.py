import pygame
import os

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
FPS = 30
EXIT_BUTTON_W = 120
EXIT_BUTTON_H = 43
START_BUTTON_W = 300
START_BUTTON_H = 169

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hangman')

start_img_unselected = pygame.image.load(os.path.join('Pictures', 'Start_game - unselected.png'))
start_img_selected = pygame.image.load(os.path.join('Pictures', 'Start_game - selected.png'))
exit_img_unselected = pygame.image.load(os.path.join('Pictures', 'Exit - unselected.png'))
exit_img_selected = pygame.image.load(os.path.join('Pictures', 'Exit - selected.png'))


class Button:
    def __init__(self, x, y, image_unselected, image_selected,):
        self.unselected_image = image_unselected
        self.selected_image = image_selected
        self.x_pos = x
        self.y_pos = y
        self.rect = self.selected_image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            surface.blit(self.selected_image, (self.x_pos, self.y_pos))
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        else:
            surface.blit(self.unselected_image, (self.x_pos, self.y_pos))
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action


start_button = (Button
                (SCREEN_WIDTH / 2 - START_BUTTON_W / 2, SCREEN_HEIGHT / 2 - START_BUTTON_H / 2,
                 start_img_unselected, start_img_selected))
exit_button = Button(SCREEN_WIDTH - EXIT_BUTTON_W - 10, 10, exit_img_unselected, exit_img_selected)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        screen.fill((202, 228, 241))

        if exit_button.draw(screen):
            run = False
        if start_button.draw(screen):
            print('START')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
