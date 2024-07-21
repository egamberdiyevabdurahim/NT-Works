
class CarDetail:
    def __init__(self, name):
        self.name = name


class Equipment(CarDetail):
    def __init__(self, name: str, kg: float, cost: float):
        super().__init__(name)
        self._kg = kg
        self.__cost = cost

    @property
    def get_kg(self):
        return self._kg

    def set_kg(self, kg: float):
        if kg > 0:
            self._kg = kg
        else:
            raise ValueError("KG 0 dan Katta Bo'lishi Kerak!")

    @property
    def get_cost(self):
        return self.__cost

    def set_cost(self, cost: float):
        if cost > 0:
            self.__cost = cost
        else:
            raise ValueError("Narxi 0 dan Katta Bo'lishi Kerak!")


class Worker(CarDetail):
    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name)
        self._age = age
        self.__salary = salary

    @property
    def get_age(self):
        return self._age

    def set_age(self, age: int):
        self._age += age

    @property
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary: float):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary 0 dan Katta Bo'lishi Kerak!")


def run():
    equ1 = Equipment("Engine", 10, 2000)
    equ2 = Equipment("Wheel", 20, 1500)

    worker1 = Worker("John Doe", 30, 5000)
    worker2 = Worker("Ali John", 20, 3000)

    print(f"Before: Equipment1: {equ1.name}, Kilo: {equ1.get_kg}, Narxi: {equ1.get_cost}")
    print(f"Before: Equipment2: {equ2.name}, Kilo: {equ2.get_kg}, Narxi: {equ2.get_cost}")

    print(f"Before: Worker1: {worker1.name}, Yosh: {worker1.get_age}, Salary: {worker1.get_salary}")
    print(f"Before: Worker2: {worker2.name}, Yosh: {worker2.get_age}, Salary: {worker2.get_salary}")

    equ1.set_kg(20)
    equ1.set_cost(3000)

    equ2.set_kg(15)
    equ2.set_cost(3000)

    worker1.set_age(2)
    worker1.set_salary(6000)

    worker2.set_age(1)
    worker2.set_salary(4000)

    print(f"After: Equipment1: {equ1.name}, Kilo: {equ1.get_kg}, Narxi: {equ1.get_cost}")
    print(f"After: Equipment2: {equ2.name}, Kilo: {equ2.get_kg}, Narxi: {equ2.get_cost}")

    print(f"After: Worker1: {worker1.name}, Yosh: {worker1.get_age}, Salary: {worker1.get_salary}")
    print(f"After: Worker2: {worker2.name}, Yosh: {worker2.get_age}, Salary: {worker2.get_salary}")
