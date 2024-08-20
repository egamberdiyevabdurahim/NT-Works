import psycopg2

from for_print import command, success, enter, error, re_enter, prints

from .classes import CursorContextManager

from .addition import email_details, developer_email, developer_password, admin_email, admin_password

conn = psycopg2.connect(
    database="lesson2", user="postgres", password="@12345aw", host="localhost", port="5432"
)


def check_table_exists(table_name: str) -> bool:
    with CursorContextManager(conn) as cursor:
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
        return cursor.fetchone()[0]


def check_column_exists(column_name: str, table_name: str) -> bool:
    with CursorContextManager(conn) as cursor:
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = '{table_name}' "
                       f"AND column_name = '{column_name}')")
        return cursor.fetchone()[0]


def add_column_to(from_important: str=None):
    while True:
        print(command+"\n1. Add Column\n"
                      "2. Stop\n")

        choice: str = input(enter+"Enter your choice: ")

        if choice == "1":
            if not from_important:
                table_name: str = input("Enter table name: ")
            else:
                table_name = from_important
            column_name: str = input("Enter column name: ")
            column_type: str = input("Enter column type: ")

            if not check_table_exists(table_name):
                print(error+"Table does not exist.")
                continue

            if check_column_exists(column_name, table_name):
                print(error+"Column already exists.")
                continue

            with CursorContextManager(conn) as cursor:
                cursor.execute(f"""ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type};""")
                conn.commit()
                print(success+"Column added successfully.")

        elif choice == "2":
            break

        else:
            print(error+"Invalid choice. Please try again.")


def rename_column():
    while True:
        print(prints + "stop for Exit\n")
        table_name: str = input("Enter table name: ")
        old_column_name: str = input("Enter old column name: ")
        new_column_name: str = input("Enter new column name: ")

        if table_name == "stop" or new_column_name == "stop" or old_column_name == "stop":
            break

        if not check_table_exists(table_name):
            print(error+"Table does not exist.")
            continue

        if not check_column_exists(old_column_name, table_name):
            print(error+"Column does not exist.")
            continue

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"""ALTER TABLE {table_name} RENAME COLUMN {old_column_name} TO {new_column_name};""")
            conn.commit()
            print(success+"Column renamed successfully.")
            return True


def change_datatype_column():
    while True:
        print(prints + "stop for Exit\n")
        table_name: str = input("Enter table name: ")
        column_name: str = input("Enter column name: ")
        new_type: str = input("Enter new type: ")

        if table_name == "stop" or new_type == "stop" or column_name == "stop":
            break

        if not check_table_exists(table_name):
            print(error+"Table does not exist.")
            continue

        if not check_column_exists(column_name, table_name):
            print(error+"Column does not exist.")
            continue

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"""ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {new_type};""")
            conn.commit()
            print(success+"Column data type changed successfully.")
            return True


def delete_column():
    while True:
        print(prints + "stop for Exit\n")
        table_name: str = input("Enter table name: ")
        column_name: str = input("Enter column name: ")

        if table_name == "stop" or column_name == "stop":
            break

        if not check_table_exists(table_name):
            print(error+"Table does not exist.")
            continue

        if not check_column_exists(column_name, table_name):
            print(error+"Column does not exist.")
            continue

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"""ALTER TABLE {table_name} DROP COLUMN {column_name};""")
            conn.commit()
            print(success+"Column deleted successfully.")
            return True


def create_table():
    name: str = input(enter+"Enter table name: ")
    if not check_table_exists(name):
        while True:
            mess: bool = False
            print(prints+"stop for Exit\n")
            type_of: str = input(enter + "Create table with id(y/n): ")

            if type_of == "stop":
                break

            if type_of == "y":
                mess = True
                with CursorContextManager(conn) as cursor:
                    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {name} (
                    id BIGSERIAL UNIQUE NOT NULL);""")

            elif type_of == "n":
                mess = True
                with CursorContextManager(conn) as cursor:
                    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {name} ();""")

            else:
                print(error+"Invalid input. Please enter 'y' or 'n'.")

            if mess:
                conn.commit()
                print(success+"Table created successfully.")
                add_column_to(from_important=name)
                break

    else:
        print(error+"Table already exists.")
        return None


def rename_table():
    while True:
        print(prints+"stop for Exit\n")
        old_name: str = input("Enter old table name: ")
        new_name: str = input("Enter new table name: ")

        if new_name == "stop" or old_name == "stop":
            break

        if not check_table_exists(old_name):
            print(error + "Table does not exist.")
            continue

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"ALTER TABLE {old_name} RENAME TO {new_name};")
            conn.commit()
            print(success + "Table renamed successfully.")
            return True


def delete_table():
    while True:
        print(prints+"stop for Exit\n")
        table_name: str = input("Enter table name: ")

        if table_name == "stop":
            break

        if not check_table_exists(table_name):
            print(error + "Table does not exist.")
            continue

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"DROP TABLE {table_name};")
            conn.commit()
            print(success + "Table deleted successfully.")
            return True


def show_all_tables():
    with CursorContextManager(conn) as cursor:
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables
            WHERE table_schema = 'public';
        """)
        tables = cursor.fetchall()
        for table in tables:
            print(f"Table Name: {table[0]}")
        return True


def show_all_columns_from_table():
    while True:
        print(prints + "stop for Exit\n")
        table_name: str = input("Enter table name: ")

        if table_name == "stop":
            break

        if not check_table_exists(table_name):
            print(error + "Table does not exist.")
            continue

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"""
                SELECT *
                FROM information_schema.columns 
                WHERE table_name = '{table_name}';
                """)
            columns = cursor.fetchall()
            print("column | type | maximum_length | null | default")
            for column in columns:
                column = list(column)
                if column[8] is None:
                    column[8] = "I DON'T KNOW"

                if column[6] == "YES":
                    column[6] = "NULL TRUE"

                if column[5] is None:
                    column[5] = "I DON'T KNOW"
                print(f"{column[3]} | {column[7]} | {column[8]} | {column[6]} | {column[5]}")
            return True


def show_users(male: bool=False, female: bool=False):
    if male and female:
        print(error+"You can't select both male and female at the same time.")
        return False

    if male:
        with CursorContextManager(conn) as cursor:
            cursor.execute("SELECT * FROM users WHERE gender = 'Male'")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"First Name: {row[1]}\n"
                          f"Last Name: {row[2]}\n"
                          f"Email: {row[3]}\n"
                          f"Gender: {row[4]}\n"
                          f"Birthday: {row[5]}\n"
                          f"Password: {row[6]}\n"
                          f"Created At: {row[7]}\n")
                    print("----------------------------------------------------------------")
            else:
                print(error+"No users found.")

    elif female:
        with CursorContextManager(conn) as cursor:
            cursor.execute("SELECT * FROM users WHERE gender = 'Female'")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"First Name: {row[1]}\n"
                          f"Last Name: {row[2]}\n"
                          f"Email: {row[3]}\n"
                          f"Gender: {row[4]}\n"
                          f"Birthday: {row[5]}\n"
                          f"Password: {row[6]}\n"
                          f"Created At: {row[7]}\n")
                    print("----------------------------------------------------------------")
            else:
                print(error+"No users found.")

    else:
        with CursorContextManager(conn) as cursor:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(f"First Name: {row[1]}\n"
                          f"Last Name: {row[2]}\n"
                          f"Email: {row[3]}\n"
                          f"Gender: {row[4]}\n"
                          f"Birthday: {row[5]}\n"
                          f"Password: {row[6]}\n"
                          f"Created At: {row[7]}\n")
                    print("----------------------------------------------------------------")
            else:
                print(error+"No users found.")
    return True


def show_user(email):
    while True:
        with CursorContextManager(conn) as cursor:
            cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
            row = cursor.fetchone()
            if row:
                print(f"First Name: {row[1]}\n"
                      f"Last Name: {row[2]}\n"
                      f"Email: {row[3]}\n"
                      f"Gender: {row[4]}\n"
                      f"Birthday: {row[5]}\n"
                      f"Password: {row[6]}\n")
            else:
                print(error+"User not found.")
            return True


def create_user():
    """Create a new user"""
    while True:
        print(prints+"stop for Exit\n")
        first_name: str = input(enter+"Enter First Name: ")

        if first_name == "stop":
            break

        while not first_name.isalpha():
            print(error+"Invalid First Name\n"
                        "stop for Exit")
            first_name = input(re_enter+'Re-Enter First Name: ')

            if first_name == "stop":
                break

        last_name: str = input(enter+"Enter Last Name: ")
        while not last_name.isalpha():
            print(error+"Invalid Last Name\n"
                        "stop for Exit")
            last_name = input(re_enter+'Re-Enter Last Name: ')

            if last_name == "stop":
                break

        email: str = input(enter+"Enter Email: ")
        while not email.endswith(email_details):
            print(error+"Invalid Email\n"
                        "stop for Exit")
            email = input(re_enter+'Re-Enter Email: ')

            if email == "stop":
                break

        gender: str = input(enter+"Enter Gender(m/f): ")
        while gender.lower() not in ['m', 'f']:
            print(error+"Invalid Gender\n"
                        "stop for Exit")
            gender = input(re_enter+'Re-Enter Gender(m/f): ')

            if gender == "stop":
                break

        if gender == "m":
            gender = "Male"

        elif gender == "f":
            gender = "Female"

        birthday: str = input(enter+"Enter Birthday(YYYY.MM.DD): ")
        while not birthday[4:5] == "." and not birthday[7:8] == ".":
            print(error+"Invalid Birthday. Use format YYYY.MM.DD\n"
                        "stop for Exit")
            birthday = input(re_enter+'Re-Enter Birthday(YYYY.MM.DD): ')

            if birthday == "stop":
                break

        password: str = input(enter+"Enter Password: ")
        while len(password) < 8:
            print(error+"Password should be at least 8 characters long\n"
                        "stop for Exit")
            password = input(re_enter+'Re-Enter Password: ')

            if password == "stop":
                break

        confirm_password: str = input(enter+"Confirm Password: ")
        while confirm_password != password:
            print(error+"Passwords do not match\n"
                        "stop for Exit")
            confirm_password = input(re_enter+'Re-Enter Confirm Password: ')

            if confirm_password == "stop":
                break

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"SELECT EXISTS (SELECT * FROM users WHERE email = '{email}')")
            row = cursor.fetchone()
            if row:
                if row[0]:
                    print(error+"Email already exists.")
                    continue

            cursor.execute(f"INSERT INTO users (first_name, last_name, email, gender, birthday, password)"
                           f"VALUES ('{first_name}', '{last_name}', '{email}', '{gender}', '{birthday}', '{password}')")

            conn.commit()
            print(success+"User created successfully.")
            return email, password, "User"


def delete_user():
    """Delete a user from the database"""
    while True:
        print(prints + "stop for Exit\n")
        email: str = input("Enter Email: ")

        if email == "stop":
            break

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")
            row = cursor.fetchone()

            if row:
                if row[0]:
                    cursor.execute(f"DELETE FROM users WHERE email = '{email}'")
                    conn.commit()
                    print(success+"User deleted successfully.")

            else:
                print(error+"User not found.")
            return True


def login():
    """
    Login to the database with the given email and password and return the
    result as a string with the email, password and status"""
    while True:
        print(prints + "stop for Exit\n")
        email: str = input("Enter Email: ")
        password: str = input("Enter Password: ")

        if email == "stop" or password == "stop":
            break

        if email == developer_email and password == developer_password:
            print(success+"Logged in successfully as Developer.")
            return email, password, "Developer"

        elif email == admin_email and password == admin_password:
            print(success+"Logged in successfully as Admin.")
            return email, password, "Admin"

        with CursorContextManager(conn) as cursor:
            cursor.execute(f"SELECT EXISTS (SELECT * FROM users WHERE email = '{email}' AND password = '{password}')")
            row = cursor.fetchone()

            if row[0]:
                print(success+"Logged in successfully.")
                return email, password, "User"

            else:
                print(error+"Invalid email or password.")

            return False
