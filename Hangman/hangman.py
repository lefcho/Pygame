import pygame
import button
import os


class Button:
    def __init__(self, x, y, image_unselected, image_selected, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image_unselected, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action


SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

start_img_unselected = pygame.image.load(os.path.join('Pictures', 'Start_game - unselected.png'))
start_img_selected = pygame.image.load(os.path.join('Pictures', 'Start_game - selected.png'))
exit_img_unselected = pygame.image.load(os.path.join('Pictures', 'Exit - unselected.png'))
exit_img_selected = pygame.image.load(os.path.join('Pictures', 'Exit - selected.png'))

start_button = Button(100, 200, start_img_unselected, start_img_selected, 0.8)
exit_button = Button(450, 200, exit_img_unselected, exit_img_selected, 0.8)

run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        print('START')
    if exit_button.draw(screen):
        print('EXIT')

    # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
