
class Jewelry:
    def __init__(self, name):
        self.name = name


class Gold(Jewelry):
    def __init__(self, name: str, gr: float, cost: float):
        super().__init__(name)
        self._gr = gr
        self.__cost = cost

    @property
    def get_gr(self):
        return self._gr

    def set_gr(self, gr: float):
        if gr > 0:
            self._gr = gr
        else:
            raise ValueError("Gram 0 dan Katta Bo'lishi Kerak!")

    @property
    def get_cost(self):
        return self.__cost

    def set_cost(self, cost: float):
        if cost > 0:
            self.__cost = cost
        else:
            raise ValueError("Narxi 0 dan Katta Bo'lishi Kerak!")


class Silver(Jewelry):
    def __init__(self, name: str, gr: float, cost: float):
        super().__init__(name)
        self._gr = gr
        self.__cost = cost

    @property
    def get_gr(self):
        return self._gr

    def set_gr(self, gr: float):
        if gr > 0:
            self._gr = gr
        else:
            raise ValueError("Gram 0 dan Katta Bo'lishi Kerak!")

    @property
    def get_cost(self):
        return self.__cost

    def set_cost(self, cost: float):
        if cost > 0:
            self.__cost = cost
        else:
            raise ValueError("Narxi 0 dan Katta Bo'lishi Kerak!")


class Worker(Jewelry):
    def __init__(self, name: str, age: int, salary: float):
        super().__init__(name)
        self._age = age
        self.__salary = salary

    @property
    def get_age(self):
        return self._age

    def set_age(self, age: int):
        if age > 0:
            self._age = age
        else:
            raise ValueError("Yosh 0 dan Katta Bo'lishi Kerak!")

    @property
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary: float):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary 0 dan Katta Bo'lishi Kerak!")


def run():
    gold1 = Gold("Turkiya", 10, 2000)
    gold2 = Gold("Detskiy", 5, 1000)

    silver1 = Silver("Uzb", 5, 500)
    silver2 = Silver("Turkiya", 7, 1000)

    worker1 = Worker("John Doe", 30, 5000)
    worker2 = Worker("Ali John", 20, 3000)

    print(f"Before: Gold1: {gold1.name}, Gram: {gold1.get_gr}, Narxi: {gold1.get_cost}")
    print(f"Before: Gold2: {gold2.name}, Gram: {gold2.get_gr}, Narxi: {gold2.get_cost}")

    print(f"Before: Silver1: {silver1.name}, Gram: {silver1.get_gr}, Narxi: {silver1.get_cost}")
    print(f"Before: Silver2: {silver2.name}, Gram: {silver2.get_gr}, Narxi: {silver2.get_cost}")

    print(f"Before: Worker1: {worker1.name}, Yosh: {worker1.get_age}, Salary: {worker1.get_salary}")
    print(f"Before: Worker2: {worker2.name}, Yosh: {worker2.get_age}, Salary: {worker2.get_salary}")


    gold1.set_gr(20)
    gold1.set_cost(3000)

    gold2.set_gr(15)
    gold1.set_cost(3000)


    silver1.set_gr(10)
    silver1.set_cost(2000)

    silver2.set_gr(9)
    silver2.set_cost(500)


    worker1.set_age(35)
    worker1.set_salary(6000)

    worker2.set_age(25)
    worker2.set_salary(4000)

    print(f"After: Gold1: {gold1.name}, Gram: {gold1.get_gr}, Narxi: {gold1.get_cost}")
    print(f"After: Gold2: {gold2.name}, Gram: {gold2.get_gr}, Narxi: {gold2.get_cost}")

    print(f"After: Silver1: {silver1.name}, Gram: {silver1.get_gr}, Narxi: {silver1.get_cost}")
    print(f"After: Silver2: {silver2.name}, Gram: {silver2.get_gr}, Narxi: {silver2.get_cost}")

    print(f"After: Worker1: {worker1.name}, Yosh: {worker1.get_age}, Salary: {worker1.get_salary}")
    print(f"After: Worker2: {worker2.name}, Yosh: {worker2.get_age}, Salary: {worker2.get_salary}")
