# pip install easygui - Message Box


import pygame
import sys
import random
import easygui

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

snake_block = 10
snake_speed = 15

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'

food_pos = [random.randrange(1, (width//snake_block)) * snake_block,
            random.randrange(1, (height//snake_block)) * snake_block]

score = 0

font = pygame.font.SysFont(None, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'


    if direction == 'UP':
        snake_pos[1] -= snake_block
    elif direction == 'DOWN':
        snake_pos[1] += snake_block
    elif direction == 'LEFT':
        snake_pos[0] -= snake_block
    elif direction == 'RIGHT':
        snake_pos[0] += snake_block

    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        easygui.msgbox(f"Game Over\nYour score: {score}", "Snake Game")
        pygame.quit()
        sys.exit()

    for segment in snake_body[1:]:
        if snake_pos == segment:
            easygui.msgbox(f"Game Over\nYour score: {score}", "Snake Game")
            pygame.quit()
            sys.exit()

    if snake_pos == food_pos:
        score += 1
        food_pos = [random.randrange(1, (width//snake_block)) * snake_block,
                    random.randrange(1, (height//snake_block)) * snake_block]
    else:
        snake_body.pop()

    snake_body.insert(0, list(snake_pos))

    screen.fill(black)

    for segment in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(segment[0], segment[1], snake_block, snake_block))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_block, snake_block))

    score_text = font.render("Score: " + str(score), True, green)
    screen.blit(score_text, (width - 120, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(snake_speed)
