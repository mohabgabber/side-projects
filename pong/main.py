import pygame, sys, random
def movement():
    global ball_x, ball_y, score1, score2, score_time
    ball.x += ball_x
    ball.y += ball_y
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_y *= -1
    if ball.left <= 0:
        score1 += 1
        score_time = pygame.time.get_ticks()
    if ball.right >= WIDTH:
        score2 += 1
        score_time = pygame.time.get_ticks()
    if ball.colliderect(player1) and ball_x > 0:
        if abs(ball.right - player1.left) < 10:
            ball_x *= -1
        elif abs(ball.bottom - player1.top) < 10 and ball_y > 0:
            ball_y *= -1
        elif abs(ball.top - player1.bottom) < 10 and ball_y > 0:
            ball_y *= -1

    if ball.colliderect(player2) and ball_x < 0:
        if abs(ball.left - player2.right) < 10:
            ball_x *= -1
        elif abs(ball.bottom - player2.top) < 10 and ball_y > 0:
            ball_y *= -1
        elif abs(ball.top - player2.bottom) < 10 and ball_y > 0:
            ball_y *= -1
def ballreset():
    global ball_x, ball_y, score_time
    current_time = pygame.time.get_ticks()
    ball.center = (WIDTH/2,HEIGHT/2)
    if current_time - score_time < 700:
        number_three = scorefont.render("3",False,LIGHTGREY)
        screen.blit(number_three,(WIDTH/2 - 10, HEIGHT/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = scorefont.render("2",False,LIGHTGREY)
        screen.blit(number_two,(WIDTH/2 - 10, HEIGHT/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = scorefont.render("1",False,LIGHTGREY)
        screen.blit(number_one,(WIDTH/2 - 10, HEIGHT/2 + 20))
    if current_time - score_time < 2100:
        ball_x, ball_y = 0,0
    else:
        ball_x = 7 * random.choice((1,-1))
        ball_y = 7 * random.choice((1,-1))
        score_time = None



#initializing
pygame.init()
#FPS
Clock = pygame.time.Clock()
FPS = 60
WIDTH = 1000
#Screen And Screen Caption
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONGO PONGO")
#Shapes
ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 -15,30,30)
player1 = pygame.Rect(WIDTH - 20, HEIGHT/2 - 70, 10, 140)
player2 = pygame.Rect(10, HEIGHT/2 - 70, 10, 140)
#COLORS
BG = pygame.Color("grey12")
LIGHTGREY = (200,200,200)
#score, timer
score1 = 0
score2 = 0
scorefont = pygame.font.Font("freesansbold.ttf", 40)
score_time = True
#movement
ball_x = 7 * random.choice((1,-1))
ball_y = 7 * random.choice((1,-1))
players1 = 0
players = 0
#song
#sound = pygame.mixer.Sound("song.mp3")
#pygame.mixer.Sound.play(sound)
def draw():
    screen.fill(BG)
    player_score1 = scorefont.render(f'{score1}',False,LIGHTGREY)
    screen.blit(player_score1, (530,335))
    player_score2 = scorefont.render(f'{score2}',False,LIGHTGREY)
    screen.blit(player_score2, (450,335))
    pygame.draw.rect(screen,LIGHTGREY,player1)
    pygame.draw.rect(screen,LIGHTGREY,player2)
    pygame.draw.ellipse(screen,LIGHTGREY,ball)
    pygame.draw.aaline(screen,LIGHTGREY, (WIDTH/2,0), (WIDTH/2,HEIGHT))
while True:
    #Event Listening
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                players += 7
            if event.key == pygame.K_UP:
                players -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                players -= 7
            if event.key == pygame.K_UP:
                players += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                players1 += 7
            if event.key == pygame.K_w:
                players1 -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                players1 -= 7
            if event.key == pygame.K_w:
                players1 += 7



    movement()
    player1.y += players
    player2.y += players1
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT
    draw()
    if score_time:
        ballreset()

     #updating the screen
    pygame.display.flip()
    Clock.tick(FPS)
