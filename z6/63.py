m, n = int(input('Введите количество элементов в массиве со строками')), int(input('Введите количество элементов в массиве с числами'))
nums = [int(input('Введите число №'+str(i+1))) for i in range(n)]
strs = [input('Введите строку №'+str(i+1)) for i in range(m)]
data = []
for i,j in zip(nums, strs):
    data.append({i: j})
print(data)