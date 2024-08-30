from utils import additions, create_username_password, auth, for_company, for_login


def login():
    """
    Handles the login process for a user.
    """
    username: str = input("Enter your email: ")
    password: str = input("Enter your password: ")

    # Check if the username and password match the stored ones
    if for_login.authenticate(username, password):
        print("SuperAdmin Logged In successful!")
        return username

    # Check if the username exists in the database
    elif for_company.is_company_username_taken(username):
        # Check if the password matches
        if for_company.match_company_password(username, password):
            print("Company Logged In successful!")
            return username
        else:
            print("Wrong password!")

    # Check the username address exists in the database
    elif auth.is_username_taken(username):
        # Check if the password matches
        if auth.match_password(username, password):
            print("User Logged In successful!")
            return username
        else:
            print("Wrong password!")

    else:
        print("Invalid email or password")

    return None
