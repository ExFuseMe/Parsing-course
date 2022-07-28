a = [1,2,3,4,5, 6]
iter_str = iter(a)
while True:
    try:
        i = next((iter_str))
        print(i)

    except StopIteration:
        break