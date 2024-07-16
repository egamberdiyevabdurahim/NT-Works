class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self):
        raise NotImplementedError("BU Parent Claass Niki Bunda Ishlamaydi.")

    def move(self):
        raise NotImplementedError("BU Parent Claass Niki Bunda Ishlamaydi.")


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def sound(self):
        return f"{self.name} 'Meow' dedi"

    def move(self):
        return f"{self.name} Harakatlanmqda..."


class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def sound(self):
        return f"{self.name} Vou dedi"

    def move(self):
        return f"{self.name} Harakatlanmqda..."


# Usage
animals = [Cat('Muiza'),
           Dog('Ruster')]
