import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((300, 400))

white = (255, 255, 255)
green = (0, 255, 0)
black = (0,0,0)
font = pg.font.Font('freesansbold.ttf', 50)
fontf = pg.font.Font('freesansbold.ttf', 30)

goal_state = [[1,4,7],[2,5,8],[3,6,0]]

def get_state():
    b_nums = []
    while (len(b_nums) != 9):
        num = random.randint(0, 8)
        if num not in b_nums:
            b_nums.append(num)

    state = [b_nums[i:i + 3] for i in range(0, 9, 3)]
    return state


puzzle = get_state()


def get_blankcords():
    global puzzle
    for i, j in enumerate(puzzle):
        if 0 in j:
            return i, j.index(0)


x, y = get_blankcords()
print(x, y)


def makeMove(move):
    global puzzle
    x, y = get_blankcords()
    if move == pg.K_UP and y > 0:
        puzzle[x][y], puzzle[x][y - 1] = puzzle[x][y - 1], puzzle[x][y]
    elif move == pg.K_DOWN and y < 2:
        puzzle[x][y], puzzle[x][y + 1] = puzzle[x][y + 1], puzzle[x][y]
    elif move == pg.K_LEFT and x > 0:
        puzzle[x][y], puzzle[x - 1][y] = puzzle[x - 1][y], puzzle[x][y]
    elif move == pg.K_RIGHT and x < 2:
        puzzle[x][y], puzzle[x + 1][y] = puzzle[x + 1][y], puzzle[x][y]


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

        elif event.type == pg.KEYDOWN:
            print(puzzle)
            makeMove(event.key)

    for i in range(3):
        color = white
        txt_color = black
        for j in range(3):
            color = white
            txt_color = black
            if puzzle[i][j] == 0:
                color = green
                txt_color = green
            pg.draw.rect(screen, color, [i * 100, j * 100, 99, 99])
            num = font.render(str(puzzle[i][j]), True, txt_color)
            screen.blit(num, (i * 100 + 30, j * 100 + 10))


    if goal_state == puzzle:
        text = fontf.render('Puzzle Solved !!',True,white)
        textRect = text.get_rect()
        textRect.center = (150,350)
        screen.blit(text,textRect)


    pg.display.update()
