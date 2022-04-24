'''
Все вокруг объекты
Класс - чертежь
Объект - конкретная вещь
Атрибут - цвет,  вторичное
'''

class Person:
    def __init__(self, name, phone, email, age):
        self.name = name
        self.phone = phone
        self.address = email
        self.age = age

    def print_info(self):
        print(f'Hi, my name is {self.name}, Im {self.age} years old.')

class Oldman(Person):
    def __init__(self, name, phone, email, age, hatcolour):
        super().__init__(name, phone, email, age)
        self.hatcolour = hatcolour

    def print_info(self):
        print(f'Hi felloes, my name is {self.name}, Im {self.age} years old.')


a_man = Person('Ivan', '8-999-765-43-21', 'Ivan@name.ru', 33)
a_man.print_info()


a_man.name = 'Igor'
a_man.print_info()

grandfather = Oldman('Serg', )