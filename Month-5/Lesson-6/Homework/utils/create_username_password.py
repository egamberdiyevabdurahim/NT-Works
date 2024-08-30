import random

from .auth import is_username_taken


def random_username() -> str:
    """Create random username"""

    username = random.randint(1000, 9999)
    username = str(username)
    if is_username_taken(username):
        return random_username()

    return username


def random_password() -> str:
    """Create random password"""

    password = random.randint(1000, 9999)
    return str(password)


def create_user() -> tuple:
    """Create new username and password with random"""
    username = random_username()
    password = random_password()
    return username, password
