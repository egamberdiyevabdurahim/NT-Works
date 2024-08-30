from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def get_all_departments(company_id: int):
    """
    Returns all departments in the database.

    Returns:
    List[DictRow].
    """
    query = "SELECT * FROM departments WHERE company_id = %s"
    data = execute_query(query, (company_id,), fetch="one")

    return data


def get_id_from_username_query(username: str) -> DictRow:
    """
    Returns the ID of a user from their username.

    Args:
    username (str): The username of the user.

    Returns:
    DictRow.
    """
    print("usernams:", username)
    query = "SELECT id FROM company WHERE username = %s"
    data = execute_query(query, (username,), "one")
    print("1-data:", data)

    return data


def get_company_username(username: str):
    """
    Retrieves the company username of a user from the database.

    Args:
    username (str): The user's username.

    Returns:
    str: The company's username.
    """
    queries = "SELECT username FROM company WHERE username = %s"
    params = (username,)
    data = execute_query(query=queries, params=params, fetch="one")
    if data:
        return data.get('username')
    return None


def get_company_password(username: str, password: str) -> DictRow:
    """
    Retrieves the password of a user from the database.

    Args:
    username (str): The user's username.
    password (str): The user's password.

    Returns:
    str: The company's password.
    """
    queries = "SELECT password FROM company WHERE username = %s AND password = %s"
    params = (username, password)
    data = execute_query(query=queries, params=params, fetch="one")
    return data


def insert_company(name: str, username: str, password: str) -> None:
    """
    Inserts a new user into the database.

    Args:
    name (str): The user's name.
    username (str): The user's company username.
    password (str): The user's password.

    Returns:
    None.
    """
    # Insert the new user into the database
    queries = "INSERT INTO company (name, username, password) VALUES (%s, %s, %s)"
    params = (name, username, password)
    execute_query(query=queries, params=params)
    return None


def delete_company(username: str):
    """
    Deletes a company from the database.

    Args:
    username (str): The company's username.

    Returns:
    None.
    """
    # Delete the user from the database
    queries = "DELETE FROM company WHERE username = %s"
    params = (username,)
    execute_query(query=queries, params=params)
    return None


def get_all_companies():
    """
    Returns all companies in the database.

    Returns:
    List[DictRow].
    """
    query = "SELECT * FROM company"
    data = execute_query(query, fetch="all")

    return data


def get_all_company_employees():
    """
    Returns all employees in the company database.

    Returns:
    List[DictRow].
    """
    query = "SELECT * FROM employees"
    data = execute_query(query, fetch="all")

    return data


def get_company_employees(username: str):
    """
    Returns all employees in the specified company.

    Args:
    username (str): The company's username.

    Returns:
    List[DictRow].
    """
    id_of_company = get_id_from_username_query(username)
    if not id_of_company:
        return list()  # No employees found for this company.
    id_of_department = get_all_departments(id_of_company.get('id'))
    if not id_of_department:
        return list()  # No departments found for this company.

    datas = list()
    print(id_of_department)
    for department in id_of_department:
        print(department)
        queries = "SELECT * FROM employees WHERE department_id = %s"
        params = (department,)
        data = execute_query(query=queries, params=params, fetch="all")
        print(data)
        [datas.append(dat) for dat in data]
    print("datas", datas)

    return datas
