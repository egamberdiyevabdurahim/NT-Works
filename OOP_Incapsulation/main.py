from first import run as f_r
from second import run as s_r
from third import run as t_r


print("1) Running First\n2) Running Second\n3) Running Third\n4) Stop")

while True:
    choosing = input("Enter: ")
    if choosing == "1":
        f_r()
    elif choosing == "2":
        s_r()
    elif choosing == "3":
        t_r()
    elif choosing == "4":
        break
    else:
        print("Invalid Input, Please Try Again!")
