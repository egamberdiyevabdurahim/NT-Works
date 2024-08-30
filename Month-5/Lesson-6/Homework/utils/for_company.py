from queries.for_company import get_id_from_username_query, get_company_username, get_company_password


def get_id_from_username(username: str):
    """
    Retrieves the ID of a user from the database based on their username.

    Args:
    username (str): The user's username.

    Returns:
    int: The ID of the user if found, None otherwise.
    """
    # Query to retrieve the ID of a user from the database based on their username
    data = get_id_from_username_query(username)
    print("data:", data)
    if data:
        return data["id"]
    return list()


def is_company_username_taken(username: str):
    """
    Checks if the company username is already taken in the database.

    Args:
    username (str): The user's company username address.

    Returns:
    bool: True if the company username is taken, False otherwise.
    """
    # Query to check if the company username is already taken
    data = get_company_username(username)

    return data is not None


def match_company_password(username: str, password: str) -> bool:
    """
    Checks if the password matches the stored password for the given email address.

    Args:
    email (str): The user's email address.
    password (str): The user's password.

    Returns:
    bool: True if the password matches, False otherwise.
    """
    # Query to check if the password matches the stored password
    data = get_company_password(username, password)

    # Compare the entered password with the stored password
    return data.get("password") == password
