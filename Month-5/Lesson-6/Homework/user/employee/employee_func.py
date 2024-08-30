from database_config.db_settings import execute_query
from utils.printer import employee_printer


def start_work(username: str):
    """
    Starts the work process for the given user.

    Args:
    username (str): The user's username.
    """
    queries = "SELECT * FROM employees WHERE username = %s"
    params = (username,)
    data_of = execute_query(query=queries, params=params, fetch="one")
    if data_of:
        queries = "SELECT max(id) FROM start_status GROUP BY id"
        params = (data_of.get('id'),)
        data = execute_query(query=queries, params=params, fetch="one")
        if data:
            queries = "SELECT * FROM start_status WHERE id = %s"
            params = (data.get('id'),)
            data = execute_query(query=queries, params=params, fetch="one")
            if data.get('status') is False:
                queries = "INSERT INTO start_status (status, employee_id) VALUES (%s, %s)"
                params = (True, data.get('employee_id'))
                execute_query(query=queries, params=params)
                print(f"Work started for {username}.")
                return True
            else:
                print(f"Work already started for {username}.")
                return False
        queries = "INSERT INTO start_status (status, employee_id) VALUES (%s, %s)"
        params = (True, data_of.get('employee_id'))
        execute_query(query=queries, params=params)
        print(f"Work started for {username}.")
        return True


def stop_work(username: str):
    """
    Stops the work process for the given user.

    Args:
    username (str): The user's username.
    """
    queries = "SELECT * FROM employees WHERE username = %s"
    params = (username,)
    data = execute_query(query=queries, params=params, fetch="one")
    if data:
        queries = "SELECT max(id) FROM start_status GROUP BY id"
        params = (data.get('id'),)
        data = execute_query(query=queries, params=params, fetch="one")
        if data:
            queries = "SELECT * FROM start_status id = %s"
            params = (data.get('id'),)
            data = execute_query(query=queries, params=params, fetch="one")
            if data.get('status') is True:
                queries = "UPDATE start_status SET status = %s WHERE employee_id = %s ORDER BY DESC id"
                params = (False, data.get('employee_id'))
                execute_query(query=queries, params=params)
                queries = "INSERT INTO end_status (start_id) VALUES (%s)"
                params = (data.get('id'),)
                print(f"Work stopped for {username}.\n")
                return True
            else:
                print(f"Work is not started for {username}.\n")
                return False


def show_my_data(username: str):
    """
    Shows the work data of the given user.

    Args:
    username (str): The user's username.
    """
    queries = "SELECT * FROM employees WHERE username = %s"
    params = (username,)
    data = execute_query(query=queries, params=params, fetch="one")
    if data:
        employee_printer(data)
        return True
    else:
        print(f"User {username} not found.")
        return False


def view_my_statistics(username: str):
    """
    Shows the work statistics of the given user.

    Args:
    username (str): The user's username.
    """
    queries = "SELECT * FROM employees WHERE username = %s"
    params = (username,)
    data = execute_query(query=queries, params=params, fetch="one")
    if data:
        queries = "SELECT * FROM start_status WHERE employee_id = %s ORDER BY DESC id"
        params = (data.get('id'),)
        data = execute_query(query=queries, params=params, fetch="all")
        if data:
            print(f"Work Statistics for {username}:")
            print("-" * 20)
            for start_data in data:
                print(f"Start ID: {start_data.get('id')}")
                print(f"Start Status: {start_data.get('status')}")
                print(f"Start Time: {start_data.get('time')}")
                if start_data.get('status') is False:
                    queries = "SELECT * FROM end_status WHERE start_id = %s ORDER BY DESC id"
                    params = (start_data.get('id'),)
                    end_data = execute_query(query=queries, params=params, fetch="one")
                    if end_data:
                        print(f"End ID: {end_data.get('id')}")
                        print(f"End Time: {end_data.get('time')}")
                        print("-" * 20)

                    else:
                        print("No end status found.")
                        print("-" * 20)


def change_password(username: str):
    """
    Changes the password of the given user.

    Args:
    username (str): The user's username.
    """
    current_password = input("Enter your current password: ")
    new_password = input("Enter your new password: ")
    confirm_password = input("Confirm your new password: ")

    queries = "SELECT password FROM employees WHERE username = %s AND password = %s"
    params = (username, current_password)
    data = execute_query(query=queries, params=params, fetch="one")
    if data:
        if new_password == confirm_password:
            queries = "UPDATE employees SET password = %s WHERE username = %s"
            params = (new_password, username)
            execute_query(query=queries, params=params)
            print("Password changed successfully!")
        else:
            print("Passwords do not match!")

    else:
        print("Invalid current password!")
