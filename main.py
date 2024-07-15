import pygame
import random

WIDTH = 1080  # ширина игрового окна
HEIGHT = 720  # высота игрового окна
FPS = 30  # частота кадров в секунду

def changeColor(tmp_color):
    colors = [RED, GREEN, BLUE, YELLOW, MAGENTA]

    int_colour = random.randint(0, 4)
    to_return = colors[int_colour]

    while tmp_color == to_return:
        colors = [RED, GREEN, BLUE, YELLOW, MAGENTA]

        int_colour = random.randint(0, 4)
        to_return = colors[int_colour]

    return to_return


def setColor():
    colors = [RED, GREEN, BLUE, YELLOW, MAGENTA]

    int_colour = random.randint(0, 4)
    to_return = colors[int_colour]
    return to_return


def checkForWin(x_coord, y_coord):
    if (x_coord + square_width >= x_death) and (y_coord + square_height >= y_death):
        return True # правый нижний
    elif (x_coord + square_width >= x_death) and (y_coord <= 0):
        return True # правый верхний
    elif (x_coord <= 0) and (y_coord + square_height >= y_death):
        return True # левый нижний
    elif (x_coord <= 0) and (y_coord <= 0):
        return True # левый верхний
    return False


if __name__ == '__main__':
    # создаем игру и окно
    pygame.init()
    pygame.mixer.init()  # для звука
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("DVD")
    clock = pygame.time.Clock()

    # Цвета (R, G, B)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    SECRET = (25, 0, 51)

    color = setColor()

    x = 30
    y = 30
    is_right = True
    is_down = True


    square_width = WIDTH / 10 * 1.5
    square_height = HEIGHT / 10 * 1.5


    x_death = WIDTH
    y_death = HEIGHT


    x_speed = 2
    y_speed = 2

    fps_winning_counter = 0
    is_winning = False

    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        if is_winning:
            fps_winning_counter += 1

        if fps_winning_counter == 30:
            is_winning = False
            fps_winning_counter = 0


        if is_winning:
            screen.fill(SECRET)
        else:
            screen.fill(BLACK)

        if checkForWin(x, y):
            is_winning = True

        if is_right:
            #вправо
            if x + square_width != x_death:
                x += x_speed
            else:
                is_right = False
                x -= x_speed
                color = changeColor(color)
        else:
            #влево
            if x != 0:
                x -= x_speed
            else:
                is_right = True
                x += x_speed
                color = changeColor(color)

        if is_down:
            #вниз
            if y + square_height != y_death:
                y += y_speed
            else:
                is_down = False
                y -= y_speed
                color = changeColor(color)

        else:
            #вверх
            if y != 0:
                y -= y_speed
            else:
                is_down = True
                y += y_speed
                color = changeColor(color)


        pygame.draw.rect(screen, color, pygame.Rect(x, y, square_width, square_height))
        pygame.display.flip()


    # Обновление
    # Визуализация (сборка)