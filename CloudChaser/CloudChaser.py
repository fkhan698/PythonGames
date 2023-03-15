import pygame
import random
import os

# initialize Pygame
pygame.init()

# set up the display
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background_image = pygame.image.load(os.path.join('TestGame/Assets', 'CloudChaser.png'))
background_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Dodger')

# set up the game clock
clock = pygame.time.Clock()

# set up the player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
player_x = WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2
player_y = WINDOW_HEIGHT - PLAYER_HEIGHT
player_speed = 5

# set up the blocks
BLOCK_WIDTH = 10
BLOCK_HEIGHT = 10
block_list = []
block_speed = 3

# 

# set up the score
score = 0
font = pygame.font.SysFont(None, 36)

# draw window

def draw_window():
    window.blit(background_image, (0,0))
    pygame.display.update()

# game loop
game_over = False
while not game_over:

    
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - PLAYER_WIDTH:
        player_x += player_speed
    
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < WINDOW_HEIGHT - PLAYER_HEIGHT:
        player_y += player_speed



    # update block positions
    for block in block_list:
        block.y += block_speed

        # check for collision with player
        if block.colliderect(pygame.Rect(player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT)):
            game_over = True

        # check for block going off screen
        if block.y > WINDOW_HEIGHT:
            block_list.remove(block)
            score += 1

    # clear the screen
    window.fill((255, 255, 255))

    # draw the player
    pygame.draw.rect(window, (0, 0, 25), (player_x, player_y, PLAYER_WIDTH, PLAYER_HEIGHT))

    # draw the blocks
    for block in block_list:
        pygame.draw.rect(window, (255, 0, 0), block)

    # draw the score
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    window.blit(score_text, (10, 10))


    # update the display
    draw_window()

    # tick the clock
    clock.tick(60)

# game over screen
game_over_font = pygame.font.SysFont(None, 72)
game_over_text = game_over_font.render('GAME OVER', True, (255, 0, 0))
window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.update()

# wait for 3 seconds before quitting
pygame.time.wait(3000)

# quit Pygame
pygame.quit()
