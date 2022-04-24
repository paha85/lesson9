class Diap():
    def __init__(self, a, b):
        self.__begin = a
        self.__end = b
        self.__length = self.__end - self.__begin
        self.__value = self.__begin - 1

    def __str__(self):
        return f'Диапазон длинной {self.__length} ({self.__begin} - {self.__end})'

    def __gt__(self, other):
        if self.__length > other.__length:
            return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        self.__value += 1
        if self.__value > self.__end:
            raise StopIteration
        return self.__value

    def my_method(self):
        pass

a = Diap(1, 5)
b = Diap(2, 10)
c = a + b

for i in b:
    print(i)