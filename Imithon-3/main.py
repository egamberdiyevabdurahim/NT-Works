from first import main as f1
from second import main as f2
from third import main as f3


while True:
    print("------------------------------------------------------------")
    print("Enter 1 for first exercise\nEnter 2 for second exercise\nEnter 3 for third exercise\nEnter 4 for Stop")
    print("------------------------------------------------------------")
    choose = input("Enter your choice: ")
    if choose == '1':
        message = True
        f1()
    elif choose == '2':
        message = True
        f2()
    elif choose == '3':
        message = True
        f3()
    elif choose == '4':
        print("Program Terminated!")
        break
