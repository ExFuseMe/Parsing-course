def F(data):
    s_chet = 0
    for i in range(0, len(data), 2):
        s_chet += data[i]
    return {'Сумма': sum(data), 'Разность max и min': max(data)-min(data), 'Сумма чётных элементов': s_chet}
data = []
n = input('Вводите числа/закончите ввод, нажав Enter ')
while n != '':
    data.append(int(n))
    n = input('Вводите числа/закончите ввод, нажав Enter ')
print(F(data))