# import differnt libs
import os, time, numpy, random

# generate current list and winning
numbers = [i for i in range(1, 16)]
numbers.append('*')
WinPosition = numpy.array_split(numbers, 4)
for i in range(len(WinPosition)):
    WinPosition[i] = list(WinPosition[i])
random.shuffle(numbers)
PlayGround = numpy.array_split(numbers, 4)
# Here's a tip: delete comment to easier checking my homework
# PlayGround = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '*', '15']]
for i in range(len(PlayGround)):
    PlayGround[i] = list(PlayGround[i])

# clear console with cls
if os.name == 'nt':
    os.system('cls')
# game logic
while PlayGround != WinPosition:
    os.system('cls')
    # print Playground
    for el in PlayGround:
        print(el)
    # Get all data
    x1, y1 = int(input('Введите строку числа: ')), int(input('Введите колонку числа: '))
    x2, y2 = int(input('Введите строку пустой клетки: ')), int(input('Введите колонку пустой клетки: '))
    # mfin conditions
    if PlayGround[x2][y2] == '*':
        if (abs(x1-x2) == 1 and abs(y1-y2) == 0) or (abs(x1-x2) == 0 and abs(y1-y2) == 1):
            PlayGround[x1][y1], PlayGround[x2][y2] = PlayGround[x2][y2], PlayGround[x1][y1]
        else:
            print('Нельзя двигать сюда')
    else:
        print('Это не пустая клетка')
    # time.sleep needs to see messages
    time.sleep(0.5)
# user wins
print('Вы победили')
for el in PlayGround:
    print(el)