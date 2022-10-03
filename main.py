import pygame
import random

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

snake_block = 10

frame_rate = 60
clock = pygame.time.Clock()

font_style1 = pygame.font.SysFont(None, 70)
font_style2 = pygame.font.SysFont(None, 40)



def message1(text, color):
    mesg1 = font_style1.render(text, True, color)
    window.blit(mesg1, [window_width/3, window_height/3])


def message2(text, color):
    mesg2 = font_style2.render(text, True, color)
    window.blit(mesg2, [window_width/4, window_height/2])

def message3(text, color):
    mesg2 = font_style2.render(text, True, color)
    window.blit(mesg2, [10, 10])

def snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(window, (0, 255, 0), [
                         i[0], i[1], snake_block, snake_block])


pygame.display.set_caption("Snake with Pygame")


def game_loop():

    snake_x = window_width/2
    snake_y = window_height/2

    snake_x_change = 0
    snake_y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    game_over = False
    game_close = False

    score=0

    while not game_over:
        
        while game_close == True:

            message1("NOOB", (255, 255, 0))
            message2("Press:  C to PLAY AGAIN   or   Q to QUIT", (255, 255, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_x_change = 0
                    snake_y_change = -snake_block
                if event.key == pygame.K_DOWN:
                    snake_x_change = 0
                    snake_y_change = snake_block
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block
                    snake_y_change = 0
                if event.key == pygame.K_RIGHT:
                    snake_x_change = +snake_block
                    snake_y_change = 0

        if snake_x > window_width or snake_x < 0 or snake_y > window_height or snake_y < 0:
            game_close = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (255, 0, 0), [
                         food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        message3(f"Score:{score}",(255, 255, 0))
        pygame.display.update()

        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            score+=1
            length_of_snake += 1

        clock.tick(20)

    pygame.quit()

    quit()


game_loop()
