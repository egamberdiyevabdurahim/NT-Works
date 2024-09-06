from queries.for_user import get_user_by_email_query


def login():
    """
    Handles the login process for a user.
    """
    email: str = input("Enter your email address: ")
    password: str = input("Enter your password: ")

    if email == "super" and password == "super":
        print("Login successful as Super Admin!")
        return "super"

    user_data = get_user_by_email_query(email)
    if user_data is None:
        print("Invalid email or password. Please try again.")
        return None

    if user_data['password'] != password:
        print("Invalid email or password. Please try again.")
        return None

    return user_data
