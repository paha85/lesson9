class Road:
    def __init__(self, length=1000, width=10):
        self._length = length
        self._width = width

    def mass(self):
        return self._length * self._width * 25 * 5


if __name__ == "__main__":
    r = Road(5000, 20)
    print(f'Масса асфальта - {r.mass()//1000} тонн')
