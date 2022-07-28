class MyIter:
    def __init__(self, value):
        self.value = value
        self.index = 0

    def __next__(self):
        try:
            if self.index < len(self.value):
                char = self.value[self.index]
                self.index += 1
                return(char)
            else:
                raise StopIteration
        except StopIteration:
            return('There is no more symbols')

a = MyIter('qwerty')
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())