class Test(list):
    def __init__(self, data) -> None:
        self.data = data
    
    def append(self):
        self.data.pop()
        return self.data
a = Test([1, 2, 3, 4, 5])
print(a.append())