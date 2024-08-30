from psycopg2.extras import DictRow

from database_config.db_settings import execute_query

from .for_company import get_id_from_username_query


def get_id_department_from_name_query(name: str, company_id: str) -> DictRow:
    """
    Returns the ID of a department.

    Args:
    name (str): The department's name.

    Returns:
    DictRow.
    """
    query = "SELECT id FROM departments WHERE name = %s AND company_id = %s"
    data = execute_query(query, (name, company_id), "one")

    return data


def get_department_name(name: str, company_id: str):
    """
    Retrieves the department name of a user from the database.

    Args:
    name (str): The user's name.

    Returns:
    str: The department's name.
    """
    query = "SELECT id FROM departments WHERE name = %s AND company_id = %s"
    data = execute_query(query, (name, company_id), "one")

    return data


def insert_department(name: str, company_id: int):
    """
    Inserts a new department into the database.

    Args:
    name (str): The department's name.
    company_id (str): The ID of the company the department belongs to.

    Returns:
    None.
    """
    # Insert the new department into the database
    queries = "INSERT INTO departments (name, company_id) VALUES (%s, %s)"
    params = (name, company_id)
    execute_query(query=queries, params=params)

    return None


def delete_department(id_of_department: str):
    """
    Deletes a department from the database.

    Args:
    name (str): The department's name.

    Returns:
    None.
    """
    # Delete the department from the database
    queries = "DELETE FROM departments WHERE id = %s"
    params = (id_of_department,)
    execute_query(query=queries, params=params)

    return None


def get_all_departments(company_id: int):
    """
    Returns all departments in the database.

    Returns:
    List[DictRow].
    """
    query = "SELECT * FROM departments WHERE company_id = %s"
    data = execute_query(query, (company_id,), fetch="all")

    return data


def get_department_employees(name: str, username: str):
    """
    Returns all employees in the specified department.

    Args:
    name (str): The department's name.

    Returns:
    List[DictRow].
    """
    company_id = get_id_from_username_query(username)
    id_of_department = get_id_department_from_name_query(name, str(company_id))
    queries = "SELECT * FROM employees WHERE department_id = %s"
    params = (id_of_department,)
    data = execute_query(query=queries, params=params, fetch="all")

    return data


def update_department(department_id: str, name: str):
    """
    Updates the department's name in the database.

    Args:
    department_id (str): The ID of the department.
    name (str): The new department's name.

    Returns:
    None.
    """
    queries = "UPDATE departments SET name = %s WHERE id = %s"
    params = (name, department_id)
    execute_query(query=queries, params=params)

    return None


def get_department_by_id(department_id: str):
    """
    Retrieves the department details by ID from the database.

    Args:
    department_id (str): The ID of the department.

    Returns:
    DictRow.
    """
    query = "SELECT * FROM departments WHERE id = %s"
    data = execute_query(query, (department_id,), "one")

    return data
