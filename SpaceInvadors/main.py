import pygame
import os
pygame.font.init()
#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WIDTH, HEIGHT = 900, 500
#Values
border = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
space_heigh, space_width = 55, 40
FPS = 60
VEL = 5
BULLET_VEL = 7
max_bullets = 10
#screen
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boom Boom!!!!!")
#Images
yellow_spaceship = pygame.image.load(os.path.join("Assets", 'spaceship_yellow.png'))
yellow_ship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship, (space_heigh, space_width)), 90)
red_spaceship = pygame.image.load(os.path.join("Assets", 'spaceship_red.png'))
red_ship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (space_heigh, space_width)), 270)
background = pygame.transform.scale(pygame.image.load(os.path.join('Assets', "space.png")), (WIDTH, HEIGHT))
#Event
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2
#Fonts and strs
winner_font = pygame.font.SysFont('comicsans', 100)
health_font = pygame.font.SysFont('comicsans', 40)
credit = 'Game Made By Mohab Gabber (Fuck You)'
credit_font = pygame.font.SysFont('comicsans', 50)
#functions
def draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(background, (0, 0))
    pygame.draw.rect(WIN, BLACK, border)
    red_health_text = health_font.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = health_font.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 20))
    WIN.blit(yellow_health_text, (10, 20))
    WIN.blit(yellow_ship, (yellow.x, yellow.y))
    WIN.blit(red_ship, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()
def draw_winner(text, credit):
    text_draw = winner_font.render(text, 1, WHITE)
    credits = credit_font.render(credit, 1, RED)
    WIN.blit(credits, (WIDTH/2 - credits.get_width()/2, HEIGHT/2 - credits.get_height()/2 + 70))
    WIN.blit(text_draw, (WIDTH/2 - text_draw.get_width()/2, HEIGHT/2 - text_draw.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < border.x : #right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #up
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: #down
        yellow.y += VEL
def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > border.x + border.width: #left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < 900: #right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT: #down
        red.y += VEL
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)
def main():
    red = pygame.Rect(700, 300, space_width, space_heigh)
    yellow = pygame.Rect(100, 300, space_width, space_heigh)
    clock = pygame.time.Clock()
    running = True
    red_health = 10
    yellow_health = 10
    yellow_bullets = []
    red_bullets = []
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width - 7, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
            if event.type == red_hit:
                red_health -= 1
            if event.type == yellow_hit:
                yellow_health -= 1
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins Bitches"
        if yellow_health <= 0:
            winner_text = "Red Wins Bitches"
        if winner_text != "":
            draw_winner(winner_text, credit)
            break
        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)
        draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)
    main()
if __name__ == "__main__":
    main()
