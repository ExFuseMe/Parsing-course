n = int(input())
data = []
for i in range(n):
    city = input()
    if city in data:
        print('No')
    else:
        data.append(city)