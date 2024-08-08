from first.first import main as m_1
from first.second import main as m_2
from second.main import main as m_3
from third.main import main as m_4
from third.main import command, error, enter


def main():
    print(command+"Enter 1 for first exercise\n"
          "Enter 2 for first ver - 2 exercise\n"
          "Enter 3 for second exercise\n"
          "Enter 4 for third exercise")
    choosing = input(enter+"Enter: ")

    if choosing == '1':
        m_1()
    elif choosing == '2':
        m_2()
    elif choosing == '3':
        m_3()
    elif choosing == '4':
        m_4()
    else:
        print(error+"Invalid input, please try again.")


if __name__ == '__main__':
    main()