from queries import for_department


def get_department_id_from_name(name: str, company_id: str):
    """
    Retrieves the ID of a department from the database.

    Args:
    name (str): The department's name.

    Returns:
    int: The ID of the department if found, None otherwise.
    """
    data = for_department.get_id_department_from_name_query(name, company_id)

    if data:
        return data["id"]
    else:
        return None


def is_department_name_taken(name: str, company_id: str):
    """
    Checks if the department name is already taken in the database for the given company.

    Args:
    name (str): The department's name.
    company_id (str): The ID of the company.

    Returns:
    bool: True if the department name is taken, False otherwise.
    """
    data = for_department.get_department_name(name, company_id)

    return data is not None
