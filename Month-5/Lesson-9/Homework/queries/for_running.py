import os

from database_config.db_settings import execute_query


def create_company_table_query() -> None:
    """
    Creates a new table for companies.
    """
    query = """
        CREATE TABLE IF NOT EXISTS companies (
            id BIGINT PRIMARY KEY,
            name VARCHAR(64) UNIQUE NOT NULL,
            status BOOLEAN DEFAULT True,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
    execute_query(query)
    return None


def create_roles_table_query() -> None:
    query = """
        CREATE TABLE IF NOT EXISTS roles (
            id BIGSERIAL PRIMARY KEY,
            name VARCHAR(64) UNIQUE NOT NULL,
            status BOOLEAN DEFAULT True
        );
    """
    execute_query(query)
    return None


def create_regions_table_query() -> None:
    query = """
        CREATE TABLE IF NOT EXISTS regions (
            id BIGSERIAL PRIMARY KEY,
            name VARCHAR(64) UNIQUE NOT NULL,
            status BOOLEAN DEFAULT True
        );
    """
    execute_query(query)
    return None


def create_departments_table_query() -> None:
    """
    Creates a new table for departments.
    """
    query = """
        CREATE TABLE IF NOT EXISTS departments (
            id BIGINT PRIMARY KEY,
            name VARCHAR(64) UNIQUE NOT NULL,
            company_id BIGINT NOT NULL,
            status BOOLEAN DEFAULT True,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
    execute_query(query)
    return None


def create_users_table_query() -> None:
    """
    Creates a new table for users.
    """
    query = """
        CREATE TABLE IF NOT EXISTS users (
            id BIGINT PRIMARY KEY,
            email VARCHAR(64) UNIQUE NOT NULL,
            first_name VARCHAR(64) NOT NULL,
            last_name VARCHAR(64) NOT NULL,
            password VARCHAR(64) NOT NULL,
            gender VARCHAR(64) NOT NULL,
            age INTEGER NOT NULL,
            salary DECIMAL(10, 2) NOT NULL,
            date_of_birth DATE NOT NULL,
            region_id BIGINT,
            role BIGINT NOT NULL,
            company_id BIGINT,
            department_id BIGINT,
            status BOOLEAN DEFAULT True,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
    execute_query(query)
    return None


def add_manager_id_to_companies_query() -> None:
    """
    Adds manager_id column to the companies table.
    """
    query = """
        ALTER TABLE companies
        ADD COLUMN manager_id BIGINT;
    """
    execute_query(query)
    return None


def create_is_used_table_query() -> None:
    """
    Creates a new table for tracking whether the application is already run.
    """
    query = """
        CREATE TABLE IF NOT EXISTS is_used (
            id BIGSERIAL PRIMARY KEY,
            is_used BOOLEAN DEFAULT FALSE
        );
    """
    execute_query(query)
    return None


def insert_is_used_query():
    """
    Inserts a new record into the is_used table.
    """
    query = """
        SELECT * FROM is_used
        ORDER BY id DESC
        LIMIT 1;
        """
    data = execute_query(query, fetch="one")
    if data is None:
        query = "INSERT INTO is_used (is_used) VALUES (False);"
        execute_query(query)
    return None


def update_is_used_query():
    """
    Updates the is_used column in the is_used table.
    """
    query = "UPDATE is_used SET is_used = TRUE;"
    execute_query(query)
    return None


def is_used():
    query = """
    SELECT * FROM is_used
    ORDER BY id DESC
    LIMIT 1;
    """
    data = execute_query(query, fetch="one")
    return data['is_used'] is True


def before_run() -> None:
    """
    Creates all required tables before running the application.
    """
    create_company_table_query()
    create_roles_table_query()
    create_regions_table_query()
    create_departments_table_query()
    create_users_table_query()
    add_manager_id_to_companies_query()
    return None


def if_not_used():
    path = os.path.join(os.path.dirname(__file__),)
    create_is_used_table_query()
    insert_is_used_query()
    if not is_used():
        before_run()

        with open(f"{path}/inserter_for_company.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)

        with open(f"{path}/inserter_for_department.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)

        with open(f"{path}/inserter_for_roles.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)

        with open(f"{path}/inserter_for_region.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)

        with open(f"{path}/inserter_for_user.sql", 'r') as insert_file:
            lines = insert_file.readlines()
            for line in lines:
                query = line.strip()
                execute_query(query)


        update_is_used_query()

    return None
