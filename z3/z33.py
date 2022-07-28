import random
print(list(set([random.randint(1, 100) for i in range(10)])& set([random.randint(1, 100) for i in range(10)])))