def IsSimple(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n
summ = 0
for i in range(10, 250):
    if IsSimple(i):
        summ += i
        print(i)
print(summ)