from colorama import Fore, init


init(autoreset=True)

error = Fore.RED
enter = Fore.CYAN
re_enter = Fore.MAGENTA
success = Fore.LIGHTGREEN_EX
prints = Fore.YELLOW
command = Fore.LIGHTCYAN_EX


def closure(num):
    def function(a, b):
        if a + b < num:
            return (a + b) * num
        elif a + b > num:
            return (a + b) / num
        else:
            return a + b
    return function


def main():
    while True:
        num = input(enter+"Enter a number for closure: ")
        while not num.isdigit():
            print(error+"Invalid input. Please enter a number.\n"
                  "stop for Exit")
            num = input(re_enter+"Re-Enter a number for closure: ")
            if num.lower() == "stop":
                return
        closure_func = closure(int(num))
        a = input(enter+"Enter first number for function: ")
        while not a.isdigit():
            print(error+"Invalid input. Please enter a number.\n"
                  "stop for Exit")
            a = input(re_enter+"Re-Enter first number for function: ")
            if a.lower() == "stop":
                return
        b = input(enter+"Enter second number for function: ")
        while not b.isdigit():
            print(error+"Invalid input. Please enter a number.\n"
                  "stop for Exit")
            b = input(re_enter+"Re-Enter second number for function: ")
            if b.lower() == "stop":
                return
        result = closure_func(int(a), int(b))
        print(success+f"Result: {result}")

        choice = input(command+"Do you want to continue? (y/n): ")
        if choice.lower() != "y":
            break
