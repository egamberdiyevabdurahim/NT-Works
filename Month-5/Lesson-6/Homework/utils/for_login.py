super_admin_username = "super"
super_admin_password = "super"


def is_super_admins_username(username: str):
    """
    Checks if the provided username is the super admin's username.

    Args:
    username: The username provided by the user.

    Returns:
    bool: True if the username matches, False otherwise.
    """
    return username == super_admin_username


def is_super_admin(username: str, password: str) -> bool:
    """
    Checks if the provided credentials match the super admin credentials.

    Args:
    username: The username provided by the user.
    password: The password provided by the user.

    Returns:
    bool: True if the credentials match, False otherwise.
    """
    return username == super_admin_username and password == super_admin_password


def authenticate(username: str, password: str) -> bool:
    """
    Authenticates the user by checking if the provided credentials match the super admin credentials.

    Args:
    username: The username provided by the user.
    password: The password provided by the user.

    Returns:
    bool: True if the credentials match, False otherwise.
    """
    return is_super_admin(username, password)


def update_super_admin_password() -> None:
    """
    Updates the super admin password.

    Returns:
    None: Prints a success message updating the super admin password.
    """
    global super_admin_password
    new_password: str = input("Enter Super Admin's new password")
    super_admin_password = new_password
    print("Super admin password updated successfully!")
    return None


def reset_super_admin_password() -> None:
    """
    Resets the super admin password to its default value.
    """
    global super_admin_password
    super_admin_password = "super"
    print("Super admin password reset successfully!")
    return None
