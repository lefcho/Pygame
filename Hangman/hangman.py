import pygame
import os

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

start_img_unselected = pygame.image.load(os.path.join('Pictures', 'Start_game-selected.png'))
start_img_selected = pygame.image.load(os.path.join('Pictures', 'Start_game - selected.png'))
exit_img_unselected = pygame.image.load(os.path.join('Pictures', 'Exit-unselected.png'))
exit_img_selected = pygame.image.load(os.path.join('Pictures', 'Exit - selected.png'))


class Button:
    def __init__(self, x, y, image_unselected, image_selected,):
        self.image = image_unselected
        self.rect = self.image.get_rect()
        self.x_pos = x
        self.y_pos = y
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        surface.blit(self.image, (self.x_pos, self.y_pos))
        return action


start_button = Button(100, 200, start_img_unselected, start_img_selected)
exit_button = Button(0, 0, exit_img_unselected, exit_img_selected)


def main():
    run = True
    while run:

        screen.fill((202, 228, 241))

        if start_button.draw(screen):
            print('START')
        if exit_button.draw(screen):
            print('exiT')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
