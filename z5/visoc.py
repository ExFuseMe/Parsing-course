def F(n):
    if n % 4 != 0:
            return('Не високосный')
    else:
        if n % 100 != 0:
            return('Високосный')
        else:
            if n % 400 == 0:
                return('Високосный')
            else:
                return('Не високосный')
print(F(n = int(input())))
