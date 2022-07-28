a,b = int(input('Write number a\n')), int(input('Write number b\n'))
s, k = 0, 0
for i in range(a, b):
    if i % 3 == 0:
        s += i
        k += 1
print(s/k)