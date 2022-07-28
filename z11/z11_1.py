class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def GetPerson(self):
        print(str('Информация о человеке', self.name)+', Возраст:', self.age)

class Student(Person):
    def __init__(self, name, age, form, school):
        self.name = name
        self.age = age
        self.form = form
        self.school = school
    def GetInfo(self):
        print('Информация об ученике\n',self.name,'- учащийся школы №', str(self.school)+',\n',str(self.form)+'-ого класса (', self.age,'лет)')

student = Student('Vasya', 14, 9, 123)
student.GetInfo()
man = Person('Yan', 32)
man.GetPerson()