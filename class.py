import datetime

class Person:
    def __init__(self, name, DOB):
        self.name = name
        self.DOB = datetime.date(DOB)

    @property
    def speak():
        print("hello")

    @property
    def walk():
        print("walking away")

teacher = Person('John', "23-10-93")
print(teacher.name)
print(teacher.DOB)