def counter():
    num = 1
    while num <= 250:
        yield num
        num += 1
for el in counter():
    print(el)