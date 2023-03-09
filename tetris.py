import pygame
import time

WIDTH = 800
HEIGHT = 600
FPS = 200

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (250, 250, 0)

cup_h = 20
cup_w = 10
block = 20
side_margin = int((WIDTH - cup_w * block) / 2)
top_margin = HEIGHT - (cup_h * block) - 5


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
# all_sprites = pygame.sprite.Group()

times_n_r_font = pygame.font.SysFont("Times New Roman", 20)
big_font = pygame.font.SysFont("Times New Roman", 45)
pause_text = big_font.render("Pause", True, WHITE)
settings_text = big_font.render("Settings", True, WHITE)
text_quit_b = times_n_r_font.render("Quit", True, WHITE)
text_pause_b = times_n_r_font.render("Pause", True, WHITE)

colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0))
figures = {'S': [['ooooo',
                  'ooooo',
                  'ooxxo',
                  'oxxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'oooxo',
                  'ooooo']],
           'Z': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'oxooo',
                  'ooooo']],
           'J': [['ooooo',
                  'oxooo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxxo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oooxo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'oxxoo',
                  'ooooo']],
           'L': [['ooooo',
                  'oooxo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxoo',
                  'ooxxo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'oxooo',
                  'ooooo'],
                 ['ooooo',
                  'oxxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo']],
           'I': [['ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'xxxxo',
                  'ooooo',
                  'ooooo']],
           'O': [['ooooo',
                  'ooooo',
                  'oxxoo',
                  'oxxoo',
                  'ooooo']],
           'T': [['ooooo',
                  'ooxoo',
                  'oxxxo',
                  'ooooo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'ooxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooooo',
                  'oxxxo',
                  'ooxoo',
                  'ooooo'],
                 ['ooooo',
                  'ooxoo',
                  'oxxoo',
                  'ooxoo',
                  'ooooo']]}


class Figure():
    def __init__(self, shape, rotation, color, x=0, y=3):
        self.shape = shape
        self.rotation = rotation
        self.color = color
        self.x = x
        self.y = y

    def get_table(self):
        return figures[self.shape][self.rotation]

    def get_color(self):
        return self.color
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, other):
        self.x = other
        
    def set_y(self, other):
        self.y = other

    def get_rotation(self):
        return self.rotation

    def set_rotation(self, other):
        self.rotation = other

    def get_shape(self):
        return self.shape


def pause(screen):
    pygame.draw.rect(screen, GREY, [0, 0, 800, 600])
    screen.blit(pause_text, (WIDTH/2 - 40, 30))
    text_continue = times_n_r_font.render("Continue", True, BLUE)
    pygame.draw.rect(screen, GREEN, [WIDTH / 2 - 90, HEIGHT / 2 - 100, 200, 70])
    screen.blit(text_continue, (WIDTH / 2 - 20, HEIGHT / 2 - 80))
    pygame.draw.rect(screen, RED, [WIDTH - 100, HEIGHT - 50, 80, 30])
    screen.blit(text_quit_b, (WIDTH - 60, HEIGHT - 50))
    text_settings = times_n_r_font.render("Settings", True, BLUE)
    pygame.draw.rect(screen, YELLOW, [WIDTH / 2 - 90, HEIGHT / 2, 200, 70])
    screen.blit(text_settings, (WIDTH / 2 - 20, HEIGHT / 2 + 20))

def play():
    global pause_active
    pause_active = False

def settings(screen):
    pygame.draw.rect(screen, GREY, [0, 0, 800, 600])
    screen.blit(settings_text, (WIDTH / 2 - 60, 30))
    global extra_speed
    speed_text = big_font.render("Extra speed: " + str(int(extra_speed*100//1)/100) + "(max: 1)", True, WHITE)
    screen.blit(speed_text, (WIDTH / 2 - 200, 150))
    pygame.draw.rect(screen, YELLOW, [WIDTH / 2 - 90, HEIGHT / 2 - 50, 200, 70])
    pygame.draw.rect(screen, YELLOW, [WIDTH / 2 - 90, HEIGHT / 2 + 50, 200, 70])
    text_faster = times_n_r_font.render("Faster", True, BLUE)
    text_slower = times_n_r_font.render("Slower", True, BLUE)
    screen.blit(text_faster, (WIDTH / 2 - 15, HEIGHT / 2 - 30))
    screen.blit(text_slower, (WIDTH / 2 - 15, HEIGHT / 2 + 70))
    pygame.draw.rect(screen, RED, [WIDTH - 100, HEIGHT - 50, 80, 30])
    screen.blit(text_quit_b, (WIDTH - 60, HEIGHT - 50))
    pygame.draw.rect(screen, GREEN, [WIDTH - 100, 30, 80, 30])
    screen.blit(text_pause_b, (WIDTH - 80, 30))


def create_cup(): # создание стакана
    cup = []
    for i in range(cup_h):
        cup.append([None] * cup_w)
    return cup


def in_cup(x, y): # проверка, находится ли объект внутри стакана
    if 0 > x or x > cup_h-1 or 0 > y or y > cup_w-1:
        return False
    else:
        return True


def fig_in_cup(cup, fig, x_0 = 0, y_0 = 7): # можно ли разместить фигуру в чашке в данном месте
    a = [0, 0]
    for i in range(5):
        for j in range(5):
            if fig.get_table()[i][j] == 'x':
                # print(i, x_0, j, y_0)
                if not in_cup(i+x_0, j+y_0):
                    # print('not', i+x_0, j+y_0)
                    return False
                # print(1)
                if cup[i+x_0][j+y_0] != None:
                    # print('a')
                    return False
    return True


def is_line_ready(cup, x): # собрана ли целая линия из блоков
    for i in range(len(cup[x])):
        if cup[x][i] == None:
            return False
    return True


def delete_line(cup): # удаляет собранные линии, возвращает количество удалённых линий
    score = 0
    for i in range(len(cup)):
        if is_line_ready(cup, i):
            cup.pop(i)
            cup.insert(0, [None] * cup_w)
            score += 1
    return score


def add_to_cup(cup, fig, x_0, y_0): # помещает фигуру в чашку
    for x in range(5):
        for y in range(5):
            if fig.get_table()[x][y] == 'x':
                # print(x_0 + x, x, x_0, y_0 + y, y, y_0)
                cup[x_0 + x][y_0 + y] = fig.get_color()


def get_new_figure(): # генерация новой фигуры
    import random
    shape = random.choice(list(figures.keys()))
    rotation = random.randint(0, len(figures[shape]) - 1)
    color = random.randint(0, len(colors) - 1)
    fig = Figure(shape, rotation, color)
    return fig


def calc_speed(points): # вычисление скорости игры
    global extra_speed
    level = int(points / 10)
    fall_speed = 0.27 - (level * 0.02)
    return level, fall_speed


# блок отрисовки элементов интерфейса
def convert_to_pixels(block_x, block_y):
    return side_margin + (block_y * block), top_margin + (block_x * block)


def draw_block(block_x, block_y, color, pixelx=None, pixely=None):
    # отрисовка квадратных блоков, из которых состоят фигуры
    if color == None:
        return
    if pixelx == None and pixely == None:
        pixelx, pixely = convert_to_pixels(block_x, block_y)
    pygame.draw.rect(screen, colors[color], [pixelx, pixely, block, block])


def draw_cup(cup):
    # граница игрового поля-стакана
    pygame.draw.rect(screen, WHITE, [side_margin - 4, top_margin - 4, (cup_w * block) + 8, (cup_h * block) + 8], 5)

    # фон игрового поля
    pygame.draw.rect(screen, BLACK, (side_margin, top_margin, block * cup_w, block * cup_h))
    for x in range(cup_h):
        for y in range(cup_w):
            draw_block(x, y, cup[x][y])


def draw_info(points, level):
    pointsSurf = times_n_r_font.render('Счёт: {0}'.format(points), True, WHITE)
    pointsRect = pointsSurf.get_rect()
    pointsRect.topleft = (WIDTH - 550, 180)
    screen.blit(pointsSurf, pointsRect)

    levelSurf = times_n_r_font.render('Уровень: {0}'.format(level), True, WHITE)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WIDTH - 550, 250)
    screen.blit(levelSurf, levelRect)

    #pausebSurf = times_n_r_font.render('Пауза: пробел', True, WHITE)
    #pausebRect = pausebSurf.get_rect()
    #pausebRect.topleft = (WIDTH - 550, 420)
    #screen.blit(pausebSurf, pausebRect)

    #escbSurf = times_n_r_font.render('Выход: Esc', True, WHITE)
    #escbRect = escbSurf.get_rect()
    #escbRect.topleft = (WIDTH - 550, 450)
    #screen.blit(escbSurf, escbRect)


def draw_curent_fig(fig, pixelx=None, pixely=None):
    fig_to_draw = fig.get_table()
    if pixelx == None and pixely == None:
        pixelx, pixely = convert_to_pixels(0, 3)

    # отрисовка элементов фигур
    for x in range(5):
        for y in range(5):
            if fig_to_draw[y][x] != 'o':
                draw_block(pixelx, pixely, fig.get_color(), pixelx + (x * block), pixely + (y * block))


def draw_next_fig(fig):  # превью следующей фигуры
    pygame.draw.rect(screen, BLACK, (WIDTH - 150, 250, block * 5, block * 5))
    nextSurf = times_n_r_font.render('Следующая:', True, WHITE)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WIDTH - 150, 180)
    screen.blit(nextSurf, nextRect)
    draw_curent_fig(fig, pixelx=WIDTH - 150, pixely=230)


# cup = create_cup()
# fig_1 = get_new_figure()
# for i in range(len(cup)):
#     print(*cup[i])
# print(1)
# add_to_cup(cup, fig_1, 1, 1)
# for i in range(len(cup)):
#     print(*cup[i])
# print(fig_in_cup(cup, fig_1, 2, 1))
def runTetris(screen):
    global pause_active
    global running
    global settings_active
    global extra_speed
    mouse_pos = pygame.mouse.get_pos()
    cup = create_cup()
    last_move_down = time.time()
    last_side_move = time.time()
    last_fall = time.time()
    going_down = False
    going_left = False
    going_right = False
    points = 0
    global WIDTH
    global HEIGHT
    level, fall_speed = calc_speed(points)
    fallingFig = get_new_figure()
    nextFig = get_new_figure()

    while running:
        if not pause_active:
            pygame.display.flip()
        if fallingFig == None:
            # если нет падающих фигур, генерируем новую
            fallingFig = nextFig
            nextFig = get_new_figure()
            last_fall = time.time()

            if not fig_in_cup(cup, fallingFig):
                pause_active = True
                pause(screen)
                # если на игровом поле нет свободного места - игра закончена

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if pause_active:
                    last_fall = time.time()
                    last_move_down = time.time()
                    last_side_move = time.time()
                elif event.key == pygame.K_LEFT:
                    going_left = False
                elif event.key == pygame.K_RIGHT:
                    going_right = False
                elif event.key == pygame.K_DOWN:
                    going_down = False

            elif event.type == pygame.KEYDOWN:
                # перемещение фигуры вправо и влево
                if event.key == pygame.K_LEFT and fig_in_cup(cup, fallingFig, fallingFig.get_x(), fallingFig.get_y()-1):
                    y_1 = fallingFig.get_y()
                    fallingFig.set_y(y_1 - 1)
                    going_left = True
                    going_right = False
                    last_side_move = time.time()

                elif event.key == pygame.K_RIGHT and fig_in_cup(cup, fallingFig, fallingFig.get_x(), fallingFig.get_y()+1):
                    y_1 = fallingFig.get_y()
                    fallingFig.set_y(y_1 + 1)
                    going_right = True
                    going_left = False
                    last_side_move = time.time()

                # поворачиваем фигуру, если есть место
                elif event.key == pygame.K_UP:
                    fallingFig.set_rotation((fallingFig.get_rotation() + 1) % len(figures[fallingFig.get_shape()]))
                    if not fig_in_cup(cup, fallingFig, fallingFig.get_x(), fallingFig.get_y()):
                        fallingFig.set_rotation((fallingFig.get_rotation() - 1) % len(figures[fallingFig.get_shape()]))

                # ускоряем падение фигуры
                elif event.key == pygame.K_DOWN:
                    going_down = True
                    if fig_in_cup(cup, fallingFig, fallingFig.get_x()+1, fallingFig.get_y()):
                        x_1 = fallingFig.get_x()
                        fallingFig.set_x(x_1 + 1)
                    last_move_down = time.time()

                # мгновенный сброс вниз
                elif event.key == pygame.K_RETURN:
                    going_down = False
                    going_left = False
                    going_right = False
                    for i in range(1, cup_h):
                        if not fig_in_cup(cup, fallingFig, fallingFig.get_x()+i, fallingFig.get_y()):
                            break
                        x_1 = fallingFig.get_x()
                        fallingFig.set_x(x_1 + i - 1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH - 100 <= mouse_pos[0] <= WIDTH - 20 and HEIGHT - 50 <= mouse_pos[1] <= HEIGHT - 20:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH - 100 <= mouse_pos[0] <= WIDTH - 20 and 30 <= mouse_pos[1] <= 60:
                    pause(screen)
                    pygame.display.flip()
                    pause_active = True
                    settings_active = False
            if event.type == pygame.MOUSEBUTTONDOWN and pause_active:
                if WIDTH / 2 - 90 <= mouse_pos[0] <= WIDTH / 2 + 110 and HEIGHT / 2 - 100 <= mouse_pos[1] <= HEIGHT / 2 - 30:
                    play()
                    pygame.display.flip()
                if WIDTH / 2 - 90 <= mouse_pos[0] <= WIDTH / 2 + 110 and HEIGHT / 2 <= mouse_pos[1] <= HEIGHT / 2 + 70:
                    settings(screen)
                    pygame.display.flip()
                    settings_active = True
            if event.type == pygame.MOUSEBUTTONDOWN and settings_active:
                if WIDTH / 2 - 90 <= mouse_pos[0] <= WIDTH / 2 + 110 and HEIGHT / 2 - 50 <= mouse_pos[1] <= HEIGHT / 2 + 20:
                    extra_speed = min(extra_speed + 0.01, 1)
                    settings(screen)
                    pygame.display.flip()
                if WIDTH / 2 - 90 <= mouse_pos[0] <= WIDTH / 2 + 110 and HEIGHT / 2 + 50 <= mouse_pos[1] <= HEIGHT / 2 + 120:
                    extra_speed = max(extra_speed - 0.01, 0)
                    settings(screen)
                    pygame.display.flip()
        # управление падением фигуры при удержании клавиш
        if (going_left or going_right) and time.time() - last_side_move > cup_w:
            if going_left and fig_in_cup(cup, fallingFig, fallingFig.get_x(), fallingFig.get_y()-1):
                y_1 = fallingFig.get_y()
                fallingFig.set_y(y_1 - 1)
            elif going_right and fig_in_cup(cup, fallingFig, fallingFig.get_x(), fallingFig.get_y()+1):
                y_1 = fallingFig.get_y()
                fallingFig.set_y(y_1 + 1)
            last_side_move = time.time()

        if going_down and time.time() - last_move_down > cup_h and fig_in_cup(cup, fallingFig, fallingFig.get_x()+1, fallingFig.get_y()):
            x_1 = fallingFig.get_x()
            fallingFig.set_x(x_1 + 1)
            last_move_down = time.time()

        if time.time() - last_fall > fall_speed:  # свободное падение фигуры
            if not fig_in_cup(cup, fallingFig, fallingFig.get_x()+1, fallingFig.get_y()):  # проверка "приземления" фигуры
                print(fallingFig.get_x()+1, fallingFig.get_y(), 'pause')
                add_to_cup(cup, fallingFig, fallingFig.get_x(), fallingFig.get_y())  # фигура приземлилась, добавляем ее в содержимое стакана
                points += delete_line(cup)
                print(points)
                level, fall_speed = calc_speed(points) #if not pause_active else 0, 0
                fallingFig = None
            else:  # фигура пока не приземлилась, продолжаем движение вниз
                # print(fallingFig.get_x() + 1, fallingFig.get_y())
                x_1 = fallingFig.get_x()
                fallingFig.set_x(x_1+1)
                last_fall = time.time()

        # рисуем окно игры со всеми надписями
        #drawTitle()
        draw_cup(cup)
        draw_info(points, level)
        draw_next_fig(nextFig)
        if fallingFig != None:
            x_1, y_1 = convert_to_pixels(fallingFig.get_x(), fallingFig.get_y())
            draw_curent_fig(fallingFig, x_1, y_1)
        if not pause_active:
            pygame.display.update()
        clock.tick(FPS)


def checkKeys():
    #quitGame()

    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP]):
        if event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None


# def showText(text):
    # titleSurf, titleRect = txtObjects(text, big_font, title_color)
    # titleRect.center = (int(window_w / 2) - 3, int(window_h / 2) - 3)
    # display_surf.blit(titleSurf, titleRect)
    #
    # pressKeySurf, pressKeyRect = txtObjects('Нажмите любую клавишу для продолжения', basic_font, title_color)
    # pressKeyRect.center = (int(window_w / 2), int(window_h / 2) + 100)
    # display_surf.blit(pressKeySurf, pressKeyRect)

    # while checkKeys() == None:
    #     pygame.display.update()
    #     clock.tick()


running = True
pause_active = False
settings_active = False
extra_speed = 0
while running:
    clock.tick(FPS)
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREY, [WIDTH - 100, HEIGHT - 50, 80, 30])
    screen.blit(text_quit_b, (WIDTH - 60, HEIGHT - 50))
    pygame.draw.rect(screen, GREY, [WIDTH - 100, 30, 80, 30])
    screen.blit(text_pause_b, (WIDTH - 80, 30))
    runTetris(screen)
