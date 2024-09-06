from psycopg2.extras import DictRow

from database_config.db_settings import execute_query


def create_user_query(role: int, first_name: str, last_name: str, email: str, password: str, age: int, company_id: int=None) -> None:
    """
    Creates a query for inserting a new user into the database.

    Args:
        role (int): The role of the user (e.g., 1 for admin, 2 for employee).
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        age (int): The age of the user.
        company_id (int, optional): The ID of the company the user belongs to. Defaults to None.
    """
    query = """
    INSERT INTO users (role, first_name, last_name, email, password, age, company_id)
    VALUES (%s, %s, %s, %s, %s, %s);
    """
    params = (role, first_name, last_name, email, password, age, company_id)
    execute_query(query, params)
    return None


def get_user_by_id_query(user_id: int) -> DictRow:
    """
    Creates a query for retrieving a user by their ID from the database.

    Args:
    user_id (int): The ID of the user.

    Returns:
    DictRow.
    """
    query = """
    SELECT * FROM users
    WHERE id = %s AND status = %s
    """
    params = (user_id, True)
    data = execute_query(query, params, fetch="one")
    return data


def get_user_by_email_query(email: str) -> DictRow:
    """
    Creates a query for retrieving a user by their email from the database.

    Args:
    email (str): The email address of the user.

    Returns:
    DictRow.
    """
    query = """
    SELECT * FROM users
    WHERE email = %s AND status = %s
    """
    params = (email, True)
    data = execute_query(query, params, fetch="one")
    return data


def update_user_query(user_id: int, role: int, first_name: str, last_name: str, email: str, password: str, age: int, company_id: int=None) -> None:
    """
    Creates a query for updating a user's information in the database.

    Args:
        user_id (int): The ID of the user.
        role (int): The role of the user (e.g., 1 for admin, 2 for employee).
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        age (int): The age of the user.
        company_id (int, optional): The ID of the company the user belongs to. Defaults to None.
    """
    query = """
    UPDATE users
    SET role = %s, first_name = %s, last_name = %s, email = %s, password = %s, company_id = %s, age = %s
    WHERE id = %s
    """
    params = (role, first_name, last_name, email, password, company_id, age, user_id)
    execute_query(query, params)
    return None


def delete_user_query(user_id: int) -> None:
    """
    Creates a query for deleting a user from the database.

    Args:
    user_id (int): The ID of the user.
    """
    query = """
    UPDATE users
    SET status = %s
    WHERE id = %s
    """
    params = (False, user_id)
    execute_query(query, params)
    return None


def get_all_users_query() -> list:
    """
    Creates a query for retrieving all users from the database.

    Returns:
    List[DictRow].
    """
    query = """
    SELECT * FROM users WHERE status = %s
    """
    data = execute_query(query, (True,), fetch="all")
    return data


def get_users_by_role_query(role: int) -> list:
    """
    Creates a query for retrieving users by their role from the database.

    Args:
    role (int): The role of the users (e.g., 1 for admin, 2 for employee).

    Returns:
        List[DictRow].
    """
    query = """
    SELECT * FROM users
    WHERE role = %s AND status = %s
    """
    params = (role, True)
    data = execute_query(query, params, fetch="all")
    return data


def get_users_by_first_name_query(first_name: str) -> list:
    """
    Creates a query for retrieving users by their first name from the database.

    Args:
    first_name (str): The first name of the users.

    Returns:
    List[DictRow].
    """
    query = """
    SELECT * FROM users
    WHERE first_name = %s AND status = %s
    """
    params = (first_name, True)
    data = execute_query(query, params, fetch="all")
    return data


def get_users_by_last_name_query(last_name: str) -> list:
    """
    Creates a query for retrieving users by their last name from the database.

    Args:
    last_name (str): The last name of the users.

    Returns:
    List[DictRow].
    """
    query = """
    SELECT * FROM users
    WHERE last_name = %s AND status = %s
    """
    params = (last_name, True)
    data = execute_query(query, params, fetch="all")
    return data


def get_users_by_age_query(age: int) -> list:
    """
    Creates a query for retrieving users by their age from the database.

    Args:
    age (int): The age of the users.

    Returns:
    List[DictRow].
    """
    query = """
    SELECT * FROM users
    WHERE age = %s AND status = %s
    """
    params = (age, True)
    data = execute_query(query, params, fetch="all")
    return data
