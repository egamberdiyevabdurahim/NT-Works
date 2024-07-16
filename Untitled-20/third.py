class Vehicle:
    def engine(self):
        raise NotImplementedError("BU Parent Claass Niki Bunda Ishlamaydi.")

    def move(self):
        raise NotImplementedError("BU Parent Claass Niki Bunda Ishlamaydi.")


class Car(Vehicle):
    def engine(self):
        return "Mashina Dvigateli Ishga Tushdi."

    def move(self):
        return "Mashina Harakatlanmoqda..."


class Motorbike(Vehicle):
    def engine(self):
        return "Mototsikl Dvigateli Ishga Tushdi."

    def move(self):
        return "Mototsikl Harakatlanmoqda..."


# Usage
vehicles = [Car(),
            Motorbike()]
