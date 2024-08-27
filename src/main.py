import pygame, os, sys,random

# init/window config
pygame.init()
WIDTH, HEIGHT = 1280, 720
FONT = pygame.font.SysFont('consolas',int(WIDTH/20))
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong!')
CLOCK = pygame.time.Clock()

# Paddles

player = pygame.Rect(WIDTH-110,HEIGHT/2-50,10,100)
opponent = pygame.Rect(110,HEIGHT/2-50,10,100)
player_score, opponent_score = 0, 0

# Ball

ball = pygame.Rect(WIDTH/2-10,HEIGHT/2-10,20,20)
x_speed,y_speed = 1, 1

while True:

# Control/Action config
    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_UP]:
        if player.top > 0 :
            player.top -= 2
    if key_pressed[pygame.K_DOWN]:
        if player.bottom < HEIGHT:
            player.bottom += 2
    if key_pressed[pygame.K_w]:
        if player.top > 0 :
            player.top -= 2
    if key_pressed[pygame.K_s]:
        if player.bottom < HEIGHT:
            player.bottom += 2

# QUIT window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    

# ball and player config
    if ball.y >= HEIGHT:
        y_speed = -1
    if ball.y <= 0:
        y_speed = 1

    if ball.x <= 0:
        player_score += 1
        ball.center = (WIDTH/2,HEIGHT/2)
        x_speed,y_speed = random.choice([1,-1]),random.choice([1,-1])

    if ball.x >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH/2,HEIGHT/2)
        x_speed,y_speed = random.choice([1,-1]),random.choice([1,-1])

    if player.x - ball.width <= ball.x <= player.x and ball.y in range(player.top-ball.width,player.bottom+ball.width):
        x_speed = -1
    
    if opponent.x - ball.width <= ball.x <= opponent.x and ball.y in range(opponent.top-ball.width,opponent.bottom+ball.width):
        x_speed =  1


# ball speed on SCREEN
    ball.x += x_speed * 2
    ball.y += y_speed * 2


# opponent ai 
    if opponent.y < ball.y:
        opponent.top += 1 
    if opponent.bottom > ball.y:
        opponent.bottom -= 1




    player_score_text = FONT.render(str(player_score),True,"#778da9")
    opponent_score_text = FONT.render(str(opponent_score),True,"#778da9")

 


#SCREEN config
    SCREEN.fill("#e0e1dd")

    pygame.draw.rect(SCREEN,"#415a77",player)
    pygame.draw.rect(SCREEN,"#415a77",opponent)
    pygame.draw.circle(SCREEN,"#778da9",ball.center,10)

    SCREEN.blit(player_score_text,(WIDTH/2+50,50))
    SCREEN.blit(opponent_score_text,(WIDTH/2-50,50))

    icon_image = pygame.image.load('Pong\src\main.py')
    pygame.display.set_icon(icon_image)

    pygame.display.update()
    CLOCK.tick(300)
