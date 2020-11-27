import pygame
import time
import random

size = [600, 400]  # указываем размер
green = (0, 255, 0)  # цвет змейки
black = (0, 0, 0)  # цвет фона
red = (255, 0, 0)  # Цвета текста
blue = (0, 0, 255)  # цвет еды
white = (255, 255, 255) # цвет результата

x1 = 300  # где спавнится змейка
y1 = 300  #

snake_block = 10  # длина змейки
delta = [0, 0]  # смещение по координатам

snake_List = []  # список координат
Length_of_snake = 1  # длина змейки

foodx = round(random.randrange(0, size[0] - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, size[1] - snake_block) / 10.0) * 10.0

clock = pygame.time.Clock()  # нужно для FPS

pygame.init()  # включаем pygame

screen = pygame.display.set_mode(size)  # задаем окно с размером
pygame.display.set_caption('Змейка by Кодиум')  # имя окна
def save(point):
    max_point = 0
    a = open('point.txt', "r")
    for line in a:
        max_point = line
    a.close

    if point > int(max_point):
        f = open("point_txt", "w")
        f.write(str(point))
        f.close()



def print_point(point):
    value =point_style.render("point: " + str(point), True, white)
    screen.blit(value, [5, 5])

# ------Рисование змейки--------
def print_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

    if len(snake_list) > 1:  # окрашивание головы в красный цвет
        k = len(snake_list)
        pygame.draw.rect(screen, red, [snake_list[k - 1][0], snake_list[k - 1][1], snake_block, snake_block])


# -------Диалоги----------
font_style = pygame.font.SysFont(None, 50)  # подключили стандартный шрифт
point_style = pygame.font.SysFont(None, 20) #


def message(text, color):
    mes = font_style.render(text, True, color)  # создаем сам текст
    screen.blit(mes, [size[0] / 2, size[1] / 2])  # отображаем текст


# -----------------

def key_down(event):
    if event.key == pygame.K_LEFT:  # нажата клавиша влево
        delta = [-snake_block, 0]  # смещение по X
    if event.key == pygame.K_RIGHT:
        delta = [snake_block, 0]
    if event.key == pygame.K_UP:  # нажата клавиша вверх
        delta = [0, -snake_block]  # смещение по Y
    if event.key == pygame.K_DOWN:
        delta = [0, snake_block]
    return (delta)  # возвращаем список смещений


game_over = False

while game_over == False:  # пока игра не закончилась
    for event in pygame.event.get():  # получаем события сейчас
        if event.type == pygame.QUIT:  # закрытие окна
            pygame.quit()
        if event.type == pygame.KEYDOWN:  # если клавиша нажата
            delta = key_down(event)

    if x1 >= size[0] or x1 < 0 or y1 >= size[1] or y1 < 0:  # условия конца игры
        game_over = True

    x1 += delta[0]
    y1 += delta[1]
    screen.fill((0, 0, 0))

    # спавн еды
    pygame.draw.rect(screen, blue, [foodx, foody, snake_block, snake_block])
    # спавн змейки
    pygame.draw.rect(screen, green, [x1, y1, snake_block, snake_block])

    snake_Head = []  # список головы змейки
    snake_Head.append(x1)  # кладем координату головы
    snake_Head.append(y1)
    snake_List.append(snake_Head)  # добавляем координаты в snake_List
    if len(snake_List) > Length_of_snake:  # удаляем первый элемент  в SnakeList
        del snake_List[0]

    # рисуем змейку
    print_snake(snake_List)
    print_point(Length_of_snake - 1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        print("Yummy!!")
        foodx = round(random.randrange(0, size[0] - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, size[1] - snake_block) / 10.0) * 10.0
        Length_of_snake += 1  # увеличиваем длину
        save(Length_of_snake -1)

    clock.tick(20)

message("Проиграл :( ", red)
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()
