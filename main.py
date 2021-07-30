class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if self.capacity - self.count >= v:
            return True
        else:
            return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        if MoneyBox.can_add(self, v) == True:
            self.count += v
            return self.count
        else:
            return False
        # положить v монет в копилку

if __name__ == "__main__":
    kopilka = MoneyBox(10)
    print(kopilka.count)
    print(kopilka.can_add(10))
    print(kopilka.add(10))
    print(kopilka.count)