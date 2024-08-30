from queries import auth


def match_password(username: str, password: str) -> bool:
    """
    Checks if the password matches the stored password for the given email address.

    Args:
    email (str): The user's email address.
    password (str): The user's password.

    Returns:
    bool: True if the password matches, False otherwise.
    """
    # Query to check if the password matches the stored password
    data = auth.get_password(username, password)

    # Compare the entered password with the stored password
    return data.get("password") == password


def is_username_taken(username: str) -> bool:
    """
    Checks if the email address is already taken in the database.

    Args:
    username (str): The user's username address.

    Returns:
    bool: True if the email address is taken, False otherwise.
    """
    # Query to check if the email address is already taken
    data = auth.get_username(username)

    return data is not None
