data, st = [], ''
n = input('Вводите числа/закончите ввод, нажав Enter ')
while n != '':
    data.append(n)
    n = input('Вводите числа/закончите ввод, нажав Enter ')
for i in range(len(data)-1):
    st += data[i]+'-'
st+=data[-1]
print(st)