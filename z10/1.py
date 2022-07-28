class Child():
    def __init__(self, name, surname, form):
        self.name = name
        self.surname = surname
        self.form = form
    def GetInfo(self):
        return self.name, self.surname, self.form
student = Child('Vasya', 'Pupkin', '1A')
data = int(input('1. Get name\n2.Get surname\n3.Get form\n4.Get all data\n'))
if data == 1:
    print(student.name)
elif data == 2:
    print(student.surname)
elif data == 3:
    print(student.form)
elif data == 4:
    print(student.GetInfo())