
class Farm:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    @property
    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age > 0:
            self.__age = age
        else:
            raise ValueError("Age 0 dan Katta Bo'lishi Kerak!")


class Animal(Farm):
    def __init__(self, name: str, age: int, kg: float):
        super().__init__(name, age)
        self._kg = kg

    @property
    def get_kg(self):
        return self._kg

    def set_kg(self, kg: float):
        if kg > 0:
            self._kg = kg
        else:
            raise ValueError("KG 0 dan Katta Bo'lishi Kerak!")


class Worker(Farm):
    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name, age)
        self._salary = salary

    @property
    def get_salary(self):
        return self._salary

    def set_salary(self, salary: float):
        if salary > 0:
            self._salary = salary
        else:
            raise ValueError("Salary 0 dan Katta Bo'lishi Kerak!")


def run():
    animal = Animal("Dog", 5, 10)
    animal2 = Animal("Cat", 4, 15)

    worker = Worker("John Doe", 30, 5000)
    worker2 = Worker("Alice Doe", 25, 4000)


    print(f"Before: Animal 1: {animal.name}, Age: {animal.get_age}, Kg: {animal.get_kg}")
    print(f"Before: Animal 2: {animal2.name}, Age: {animal2.get_age}, Kg: {animal2.get_kg}")

    print(f"Before: Worker 1: {worker.name}, Age: {worker.get_age}, Salary: {worker.get_salary}")
    print(f"Before: Worker 2: {worker2.name}, Age: {worker2.get_age}, Salary: {worker2.get_salary}")

    animal.set_age(6)
    animal.set_kg(12)

    animal2.set_age(3)
    worker2.set_age(26)

    worker.set_age(31)
    worker.set_salary(5500)

    worker2.set_age(30)
    worker2.set_salary(4500)

    print(f"After: Animal 1: {animal.name}, Age: {animal.get_age}, Kg: {animal.get_kg}")
    print(f"After: Animal 2: {animal2.name}, Age: {animal2.get_age}, Kg: {animal2.get_kg}")

    print(f"After: Worker 1: {worker.name}, Age: {worker.get_age}, Salary: {worker.get_salary}")
    print(f"After: Worker 2: {worker2.name}, Age: {worker2.get_age}, Salary: {worker2.get_salary}")
