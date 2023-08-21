import os
import pygame

WIDTH, HEIGHT = 900, 500
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 40
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER_WIDTH = 10
BORDER = pygame.Rect((WIDTH / 2) - (BORDER_WIDTH / 2), 0, BORDER_WIDTH, HEIGHT)

BULLET_WIDTH = 10
BULLET_HEIGHT = 5
MAX_BULLETS = 10

FPS = 60
VEL = 5
BULLET_VEL = 7

YELLOW_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width + VEL < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y + VEL > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + yellow.height + VEL < HEIGHT - 15:
        yellow.y += VEL


def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x + VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y + VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    bullets_yellow = []
    bullets_red = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets_yellow) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + (yellow.height / 2) - (BULLET_HEIGHT / 2), BULLET_WIDTH, BULLET_HEIGHT)
                    bullets_yellow.append(bullet)

                if event.key == pygame.K_KP0 and len(bullets_red) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + (red.height / 2) - (BULLET_HEIGHT / 2), BULLET_WIDTH, BULLET_HEIGHT)
                    bullets_red.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()