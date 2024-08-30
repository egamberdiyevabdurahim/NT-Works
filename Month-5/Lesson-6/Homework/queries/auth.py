from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def get_password(username: str, password: str) -> DictRow:
    """
    Retrieves the password of a user from the database.

    Args:
    username (str): The username of the user.
    password (str): The user's password.

    Returns:
    str: The user's password.
    """
    queries = "SELECT password FROM employees WHERE username = %s AND password = %s"
    params = (username, password)
    data = execute_query(query=queries, params=params, fetch="one")
    return data


def insert_user(first_name: str, last_name: str, username: str, password: str, department_id: int) -> None:
    """
    Inserts a new user into the database.

    Args:
    first_name (str): The user's first name.
    last_name (str): The user's last name.
    email (str): The user's email address.
    password (str): The user's password.
    department_id (int): The ID of the department the user belongs to.

    Returns:
    None.
    """
    # Insert the new user into the database
    queries = "INSERT INTO employees (first_name, last_name, username, password, department_id) VALUES (%s, %s, %s, %s, %s)"
    params = (first_name, last_name, username, password, department_id)
    execute_query(query=queries, params=params)
    return None


def get_username(username: str) -> DictRow:
    """
    Retrieves the email address of a user from the database.

    Args:
    email (str): The user's email address.

    Returns:
    str: The user's email address.
    """
    queries = "SELECT username FROM employees WHERE username = %s"
    params = (username,)
    data = execute_query(query=queries, params=params, fetch="one")
    return data


def get_employees_by_department_id(department_id):
    """
    Returns all employees in the specified department.

    Args:
    department_id (int): The ID of the department.

    Returns:
    DictRow
    """
    queries = "SELECT * FROM employees WHERE department_id = %s"
    params = (department_id,)
    data = execute_query(query=queries, params=params, fetch="all")
    return data


def update_first_name(employee_id: str, first_name: str):
    """
    Updates the first name of an employee in the database.

    Args:
    employee_id (str): The ID of the employee.
    first_name (str): The new first name.

    Returns:
    None.
    """
    queries = "UPDATE employees SET first_name = %s WHERE id = %s"
    params = (first_name, employee_id)
    execute_query(query=queries, params=params)
    return None


def update_last_name(employee_id: str, last_name: str):
    """
    Updates the last name of an employee in the database.

    Args:
    employee_id (str): The ID of the employee.
    last_name (str): The new last name.

    Returns:
    None.
    """
    queries = "UPDATE employees SET last_name = %s WHERE id = %s"
    params = (last_name, employee_id)
    execute_query(query=queries, params=params)
    return None


def update_department(employee_id: str, department_id: str):
    """
    Updates the department of an employee in the database.

    Args:
    employee_id (str): The ID of the employee.
    department_id (str): The new department ID.

    Returns:
    None.
    """
    queries = "UPDATE employees SET department_id = %s WHERE id = %s"
    params = (department_id, employee_id)
    execute_query(query=queries, params=params)
    return None


def get_all_employees(company_id):
    """
    Returns all employees in the specified company.

    Args:
    company_id (int): The ID of the company.

    Returns:
    DictRow
    """
    print(company_id)
    data_of_departments = execute_query("SELECT id FROM departments WHERE company_id = %s", (company_id,), "all")
    all_departments = []
    for data in data_of_departments:
        queries = "SELECT * FROM employees WHERE company_id = %s"
        params = (data.get("id"),)
        data = execute_query(query=queries, params=params, fetch="all")
        [all_departments.append(employee) for employee in data]

    return all_departments


def get_id(id_of_employee: str) -> int:
    """
    Returns the ID of an employee from their employee ID.

    Args:
    id_of_employee (str): The employee ID.

    Returns:
    int: The ID of the employee.
    """
    queries = "SELECT id FROM employees WHERE id = %s"
    params = (id_of_employee,)
    data = execute_query(query=queries, params=params, fetch="one")
    return data["id"]


def get_id_from_username(username_of_employee: str) -> int:
    """
    Returns the ID of an employee from their employee ID.

    Args:
    username_of_employee (str): The employee username.

    Returns:
    int: The ID of the employee.
    """
    queries = "SELECT id FROM employees WHERE username = %s"
    params = (username_of_employee,)
    data = execute_query(query=queries, params=params, fetch="one")
    print("data:", data)
    return data["id"]


def delete_employee(employee_id):
    """
    Deletes an employee from the database.

    Args:
    employee_id (str): The ID of the employee.

    Returns:
    None.
    """
    queries = "DELETE FROM employees WHERE id = %s"
    params = (employee_id,)
    execute_query(query=queries, params=params)
    return None