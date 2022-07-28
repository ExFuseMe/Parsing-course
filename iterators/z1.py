a = [1, 3, 4, 5, 8]
iter_str = iter(a)
while True:
    try:
        i = next((iter_str))
        print(i)

    except StopIteration:
        break