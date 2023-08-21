import os
import pygame
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 40
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('ebrima', 100)
HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
WIN_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'win.mp3'))

BORDER_WIDTH = 10
BORDER = pygame.Rect((WIDTH // 2) - (BORDER_WIDTH // 2), 0, BORDER_WIDTH, HEIGHT)

BULLET_WIDTH = 10
BULLET_HEIGHT = 5
MAX_BULLETS = 6
SHIP_HP = 10

FPS = 60
VEL = 5
BULLET_VEL = 10

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMG = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))


def draw_window(red, yellow, bullets_yellow, bullets_red, red_hp, yellow_hp):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_hp_txt = HEALTH_FONT.render("HP: " + str(red_hp), 1, WHITE)
    yellow_hp_txt = HEALTH_FONT.render("HP: " + str(yellow_hp), 1, WHITE)
    WIN.blit(red_hp_txt, (WIDTH - red_hp_txt.get_width() - 10, 10))
    WIN.blit(yellow_hp_txt, (10, 10))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in bullets_red:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in bullets_yellow:
        pygame.draw.rect(WIN, YELLOW, bullet)

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


def handle_bullets(bullets_red, bullets_yellow, red, yellow):
    for bullet in bullets_yellow:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            bullets_yellow.remove(bullet)
        elif bullet.x > WIDTH:
            bullets_yellow.remove(bullet)
    for bullet in bullets_red:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            bullets_red.remove(bullet)
        elif bullet.x < 0:
            bullets_red.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():

    print(pygame.font.get_fonts())

    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    bullets_yellow = []
    bullets_red = []
    yellow_hp = SHIP_HP
    red_hp = SHIP_HP

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(bullets_yellow) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + (yellow.height // 2) - (BULLET_HEIGHT // 2), BULLET_WIDTH, BULLET_HEIGHT)
                    bullets_yellow.append(bullet)
                    FIRE_SOUND.play()

                if event.key == pygame.K_KP0 and len(bullets_red) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + (red.height // 2) - (BULLET_HEIGHT // 2), BULLET_WIDTH, BULLET_HEIGHT)
                    bullets_red.append(bullet)
                    FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_hp -= 1
                HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_hp -= 1
                HIT_SOUND.play()
        win_txt = ''
        if red_hp <= 0:
            WIN_SOUND.play()
            win_txt = "Yellow Wins!"

        if yellow_hp <= 0:
            WIN_SOUND.play()
            win_txt = "Red Wins!"

        if win_txt != '':
            draw_winner(win_txt)
            break

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        handle_bullets(bullets_red, bullets_yellow, red, yellow)
        draw_window(red, yellow, bullets_yellow, bullets_red, red_hp, yellow_hp)
    main()


if __name__ == "__main__":
    main()