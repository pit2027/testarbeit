
class Person:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return (f'{self.__class__.__name__} {self.name}, salary {self.salary}, bonus {self.bonus} %,'
                f' total bonus {self.calculate_total_bonus()} rub')



class Cleaner(Person):
    def __init__(self, name):
        self.name = name
        self.salary = 15000
        self.bonus = 1



class Manager:
    def __init__(self, name):
        self.name = name
        self.salary = 45000
        self.bonus = 15

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f'Manager {self.name}, salary {self.salary}, bonus {self.bonus} %, total bonus {self.calculate_total_bonus()} rub'


class CEO:
    def __init__(self, name):
        self.name = name
        self.salary = 105000
        self.bonus = 100

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f'CEO {self.name}, salary {self.salary}, bonus {self.bonus} %, total bonus {self.calculate_total_bonus()} rub'


if __name__ == '__main__':
    masha = Cleaner('Maria Ivanovna')
    print(masha)
    grisha = Manager('Grigoriy Petrovich')
    print(grisha)
    ivan_palych = CEO('Ivan Pavlovich')
    print(ivan_palych)