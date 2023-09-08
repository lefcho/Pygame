import pygame


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