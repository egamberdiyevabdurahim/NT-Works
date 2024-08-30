def employee_printer(data):
    """
    Print employee data in a formatted manner.
    """
    print(f"ID: {data['id']}\n"
          f"First Name: {data['first_name']}\n"
          f"Last Name: {data['last_name']}\n"
          f"Username: {data['username']}\n"
          f"Password: {data['password']}\n"
          f"Created At: {data['created_at']}\n"
          f"Company ID: {data['department_id']}\n")
    return None


def company_printer(data):
    """
    Print company data in a formatted manner.
    """
    print(f"ID: {data['id']}\n"
          f"Name: {data['name']}\n"
          f"Username: {data['username']}\n"
          f"Password: {data['password']}\n")
    return None


def department_printer(data):
    """
    Print department data in a formatted manner.
    """
    print(f"ID: {data['id']}\n"
          f"Name: {data['name']}\n")
    return None
