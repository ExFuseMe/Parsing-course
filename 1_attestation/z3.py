class Test(List):
    def __init__(self, data) -> None:
        self.data = data
    
    def __append__(self, number):
        new_list = ''
        for el in self.data:
            el = el** number
            new_list += str(el)+', '
            print(el)
a = Test([1, 2, 3, 4, 5])
print(a.append(2))