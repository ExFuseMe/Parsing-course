def main(a, b):
    try:
        a, b = int(a), int(b)
        if a > 0 and b > 0:
            print(a*b)
        else:
            class Error(Exception):
                print('Число меньше или = 0')
            raise Error("Число меньше или = 0")
    except ValueError:
        print("Вы ввели не число")