def Summing(num):
    if num == 1:
        return num
    else:
        return num+Summing(num-1)

print(Summing(int(input())))