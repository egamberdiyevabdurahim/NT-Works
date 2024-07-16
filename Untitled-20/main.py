from first import products
from second import animals
from third import vehicles


print("1) Running First File\n"
      "2) Running Second File\n"
      "3) Running Third File\n"
      "4) Stop")

while True:
    choice = input("Enter: ")
    if choice == "1":
        for product in products:
            print(product.get_info())
            print(product.get_price())

    elif choice == "2":
        for animal in animals:
            print(animal.move())
            print(animal.move())

    elif choice == "3":
        for vehicle in vehicles:
            print(vehicle.engine())
            print(vehicle.move())

    elif choice == "4":
        break
