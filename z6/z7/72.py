import os
import time

if os.name == 'nt':
    os.system('cls')

while True:
    os.system('cls')
    command = int(input('1. Редактор учеников\n'))
    if command == 1:
        command = int(input('1. Список учеников\n2. Изменить данные ученика\n3. Удалить ученика\n'))
        if command == 1:
            with open('z7\students.txt', 'r') as f:
                data = eval(f.read())
            for name, obj in data.items():
                print(name, obj)
        elif command == 2:
            with open('z7\students.txt', 'r') as file:
                data = file.read()
            if data:
                data = eval(data)
            else:
                data = {}
            student= input('Введите ученика: ')
            subject= input('Введите предмет')
            mark= input('Введите оценку: ')
            if student in data:
                data[student].update({subject: mark})
            else:
                data[student] = {subject: mark}
            with open('z7\students.txt', 'w') as file:
                file.write(str(data))
        elif command == 3:
            name = input('Введите имя ученика\n')
            with open('z7\students.txt', 'r') as f:
                data = eval(f.read())
            data2={}
            for id, obj in data.items():
                if id != name:
                    data2[id] = obj
                    with open('z7\students.txt', 'w') as file:
                        file.write(str(data2))
    time.sleep(1)
