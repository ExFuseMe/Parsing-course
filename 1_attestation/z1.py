def Multiplication(number):
    global data
    data *= float(number)

data = 1
n = input('Write all numbers with space(without ,)\n').split()
for el in n:
    Multiplication(el)
print(data)