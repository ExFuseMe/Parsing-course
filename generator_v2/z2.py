def counter():
    num = 1
    while num <= 200:
        if num % 2 != 0:
            num += 1
        else:
            num += 2
        if num % 5 == 0:
            yield num / 3
for el in counter():
    print(el)