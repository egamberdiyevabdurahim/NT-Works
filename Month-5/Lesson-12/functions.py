from database import execute_query
from models import to_do


def add_to_do(task: str):
    number = get_last_to_do()
    print(number)
    if number is None:
        number = 0
    else:
        number = number[3]
    query = to_do.insert().values(task=task, number=number+1)
    result = execute_query(query)
    return result.inserted_primary_key


def get_last_to_do():
    query = to_do.select().order_by(to_do.c.number.desc()).limit(1)
    result = execute_query(query)
    return result.fetchone()


def get_to_do(to_do_number: int):
    query = to_do.select().where(to_do.c.number == to_do_number)
    result = execute_query(query)
    return result.fetchone()


def update_to_do(to_do_id: int, to_do_number: int, task: str):
    query = to_do.update().where(to_do.c.number == to_do_number).values(task=task)
    result = execute_query(query)
    return result.rowcount


def completed_to_do(to_do_number: int):
    query = to_do.update().where(to_do.c.number == to_do_number).values(is_completed=True)
    result = execute_query(query)
    return result.rowcount


def update_number_to_do(to_do_num: int):
    new = to_do_num+1
    query = to_do.update().where(to_do.c.number == to_do_num).values(number=new)
    result = execute_query(query)
    return result.rowcount


def update_number_to_do2(to_do_num: int):
    query = to_do.update().where(to_do.c.number == to_do_num).values(number=to_do_num-1)
    result = execute_query(query)
    return result.rowcount


def change_number_to_do(to_do_num: int, number: int):
    for x in range(number, to_do_num+1):
        print(x)
        update_number_to_do(x)
    query = to_do.update().where(to_do.c.number == to_do_num).values(number=number)
    result = execute_query(query)
    return result.rowcount


def delete_to_do(to_do_number: int):
    query = to_do.delete().where(to_do.c.number == to_do_number)
    last_num = get_last_to_do()
    for x in range(to_do_number+1, last_num[3]+1):
        update_number_to_do(x)
    result = execute_query(query)
    return result.rowcount


def get_all():
    query = to_do.select()
    result = execute_query(query)
    return result.fetchall()


def run():
    print("1. Add a new Task\n"
          "2. Get a Task by Number\n"
          "3. Update a Task\n"
          "4. Mark a Task as Completed\n"
          "5. Change the Number of a Task\n"
          "6. Delete a Task\n"
          "7. Show All Tasks\n"
          "8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_to_do(task)
        print("Task added successfully!")

    elif choice == '2':
        to_do_number = int(input("Enter the task number: "))
        to_do_data = get_to_do(to_do_number)
        if to_do_data:
            print(f"Task: {to_do_data[1]}, Completed: {to_do_data[2]}")
        else:
            print("Task not found!")

    elif choice == '3':
        to_do_number = int(input("Enter the task number: "))
        task = input("Enter the new task: ")
        update_to_do(to_do_number, to_do_number, task)
        print("Task updated successfully!")

    elif choice == '4':
        to_do_number = int(input("Enter the task number: "))
        completed_to_do(to_do_number)
        print("Task marked as completed successfully!")

    elif choice == '5':
        to_do_num = int(input("Enter the task number: "))
        new_number = int(input("Enter the new number: "))
        change_number_to_do(to_do_num, new_number)
        print("Task number changed successfully!")

    elif choice == '6':
        to_do_number = int(input("Enter the task number: "))
        delete_to_do(to_do_number)
        print("Task deleted successfully!")

    elif choice == '7':
        all_tasks = get_all()
        for task in all_tasks:
            print(f"Task Number: {task[3]}, Task: {task[1]}, Completed: {task[2]}")

    elif choice == '8':
        print("Exiting...")
        return

    else:
        print("Invalid choice. Please try again!")
    run()


if __name__ == "__main__":
    run()