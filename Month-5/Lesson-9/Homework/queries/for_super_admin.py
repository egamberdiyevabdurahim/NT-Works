from database_config.db_settings import execute_query


def total_number_of_employees_query():
    """
    Returns the total number of employees.
    """
    query = "SELECT COUNT(*) FROM users WHERE status = True;"
    return execute_query(query, fetch="one")


def number_of_employees_by_department_query():
    """
    Returns the number of employees by department.
    """
    query = """
        SELECT d.name, COUNT(*) AS employee_count
        FROM users
        JOIN departments d ON users.department_id = d.id
        WHERE users.status = TRUE
        GROUP BY d.name;
    """
    return execute_query(query, fetch="all")


def number_of_employees_by_company_query():
    """
    Returns the number of employees by company.
    """
    query = """
        SELECT c.name, COUNT(*) AS employee_count
        FROM users
        JOIN companies c ON users.company_id = c.id
        WHERE users.status = TRUE
        GROUP BY c.name;
    """
    return execute_query(query, fetch="all")


def number_of_users_by_role_query():
    """
    Returns the number of users by role.
    """
    query = """
        SELECT r.name, COUNT(*) AS user_count
        FROM users
        JOIN roles r ON users.role = r.id
        WHERE users.status = TRUE
        GROUP BY r.name;
    """
    return execute_query(query, fetch="all")


def number_of_employees_by_age_query():
    """
    Returns the number of employees by age.
    """
    query = """
        SELECT age, COUNT(*) AS employee_count
        FROM users
        WHERE users.status = TRUE
        GROUP BY age;
    """
    return execute_query(query, fetch="all")


def number_of_employees_by_gender_query():
    """
    Returns the number of employees by gender.
    """
    query = """
        SELECT gender, COUNT(*) AS employee_count
        FROM users
        WHERE users.status = TRUE
        GROUP BY gender;
    """
    return execute_query(query, fetch="all")


def number_of_employees_by_region_query():
    """
    Returns the number of employees by region.
    """
    query = """
        SELECT r.name, COUNT(*) AS employee_count
        FROM users
        JOIN regions r ON users.region_id = r.id
        WHERE users.status = TRUE
        GROUP BY r.name;
    """
    return execute_query(query, fetch="all")


def number_of_employees_by_birth_date_query():
    """
    Returns the number of employees by date_of_birth.
    """
    query = """
        SELECT date_of_birth, COUNT(*) AS employee_count
        FROM users
        WHERE users.status = TRUE
        GROUP BY date_of_birth
        ORDER BY date_of_birth DESC;
    """
    return execute_query(query, fetch="all")


def number_of_employees_by_salary_query():
    """
    Returns the number of employees by salary.
    """
    query = """
        SELECT salary, COUNT(*) AS employee_count
        FROM users
        WHERE users.status = TRUE
        GROUP BY salary
        ORDER BY salary DESC;
    """
    return execute_query(query, fetch="all")


def number_of_10_employees_by_highest_salary_query():
    """
    Returns the top 10 employees with the highest salary.
    """
    query = """
        SELECT id, first_name, last_name, salary
        FROM users
        WHERE users.status = TRUE
        ORDER BY salary DESC
        LIMIT 10;
    """
    return execute_query(query, fetch="all")


def number_of_10_employees_by_lowest_salary_query():
    """
    Returns the top 10 employees with the lowest salary.
    """
    query = """
        SELECT id, first_name, last_name, salary
        FROM users
        WHERE users.status = TRUE
        ORDER BY salary ASC
        LIMIT 10;
    """
    return execute_query(query, fetch="all")


def total_salary_for_all_employees_query():
    """
    Returns the total salary for all employees.
    """
    query = "SELECT SUM(salary) FROM users WHERE status = TRUE;"
    return execute_query(query, fetch="one")


def average_salary_for_all_employees_query():
    """
    Returns the average salary for all employees.
    """
    query = "SELECT AVG(salary) FROM users WHERE status = TRUE;"
    return execute_query(query, fetch="one")


def total_salary_in_each_company_query():
    """
    Returns the total salary for each company.
    """
    query = """
        SELECT c.name, SUM(u.salary) AS total_salary
        FROM users u
        JOIN companies c ON u.company_id = c.id
        WHERE u.status = TRUE
        GROUP BY c.name;
    """
    return execute_query(query, fetch="all")


def average_salary_in_each_company_query():
    """
    Returns the average salary for each company.
    """
    query = """
        SELECT c.name, AVG(u.salary) AS average_salary
        FROM users u
        JOIN companies c ON u.company_id = c.id
        WHERE u.status = TRUE
        GROUP BY c.name;
    """
    return execute_query(query, fetch="all")


def total_salary_in_each_department_query():
    """
    Returns the total salary for each department.
    """
    query = """
        SELECT d.name, SUM(u.salary) AS total_salary
        FROM users u
        JOIN departments d ON u.department_id = d.id
        WHERE u.status = TRUE
        GROUP BY d.name;
    """
    return execute_query(query, fetch="all")


def average_salary_in_each_department_query():
    """
    Returns the average salary for each department.
    """
    query = """
        SELECT d.name, AVG(u.salary) AS average_salary
        FROM users u
        JOIN departments d ON u.department_id = d.id
        WHERE u.status = TRUE
        GROUP BY d.name;
    """
    return execute_query(query, fetch="all")


def total_salary_in_each_region_query():
    """
    Returns the total salary for each region.
    """
    query = """
        SELECT r.name, SUM(u.salary) AS total_salary
        FROM users u
        JOIN regions r ON u.region_id = r.id
        WHERE u.status = TRUE
        GROUP BY r.name;
    """
    return execute_query(query, fetch="all")


def average_salary_in_each_region_query():
    """
    Returns the average salary for each region.
    """
    query = """
        SELECT r.name, AVG(u.salary) AS average_salary
        FROM users u
        JOIN regions r ON u.region_id = r.id
        WHERE u.status = TRUE
        GROUP BY r.name;
    """
    return execute_query(query, fetch="all")


def total_salary_in_each_role_query():
    """
    Returns the total salary for each role.
    """
    query = """
        SELECT r.name, SUM(u.salary) AS total_salary
        FROM users u
        JOIN roles r ON u.role = r.id
        WHERE u.status = TRUE
        GROUP BY r.name;
    """
    return execute_query(query, fetch="all")


def average_salary_in_each_role_query():
    """
    Returns the average salary for each role.
    """
    query = """
        SELECT r.name, AVG(u.salary) AS average_salary
        FROM users u
        JOIN roles r ON u.role = r.id
        WHERE u.status = TRUE
        GROUP BY r.name;
    """
    return execute_query(query, fetch="all")


def total_salary_in_each_age_query():
    """
    Returns the total salary for each age.
    """
    query = """
        SELECT age, SUM(salary) AS total_salary
        FROM users
        WHERE users.status = TRUE
        GROUP BY age;
    """
    return execute_query(query, fetch="all")


def average_salary_in_each_age_query():
    """
    Returns the average salary for each age.
    """
    query = """
        SELECT age, AVG(salary) AS average_salary
        FROM users
        WHERE users.status = TRUE
        GROUP BY age;
    """
    return execute_query(query, fetch="all")


def total_salary_in_each_gender_query():
    """
    Returns the total salary for each gender.
    """
    query = """
        SELECT gender, SUM(salary) AS total_salary
        FROM users
        WHERE users.status = TRUE
        GROUP BY gender;
    """
    return execute_query(query, fetch="all")


def average_salary_in_each_gender_query():
    """
    Returns the average salary for each gender.
    """
    query = """
        SELECT gender, AVG(salary) AS average_salary
        FROM users
        WHERE users.status = TRUE
        GROUP BY gender;
    """
    return execute_query(query, fetch="all")


def total_salary_in_each_birth_date_query():
    """
    Returns the total salary for each birth date.
    """
    query = """
        SELECT date_of_birth, SUM(salary) AS total_salary
        FROM users
        WHERE users.status = TRUE
        GROUP BY date_of_birth;
    """
    return execute_query(query, fetch="all")


def average_salary_in_each_birth_date_query():
    """
    Returns the average salary for each birth date.
    """
    query = """
        SELECT date_of_birth, AVG(salary) AS average_salary
        FROM users
        WHERE users.status = TRUE
        GROUP BY date_of_birth;
    """
    return execute_query(query, fetch="all")


def total_salary_in_same_salary_query():
    """
    Returns the total salary for employees with the same salary.
    """
    query = """
        SELECT salary, SUM(salary) AS total_salary
        FROM users
        WHERE users.status = TRUE
        GROUP BY salary;
    """
    return execute_query(query, fetch="all")


def average_salary_in_same_salary_query():
    """
    Returns the average salary for employees with the same salary.
    """
    query = """
        SELECT salary, AVG(salary) AS average_salary
        FROM users
        WHERE users.status = TRUE
        GROUP BY salary;
    """
    return execute_query(query, fetch="all")


def show_all_users_query():
    """
    Returns all users.
    """
    query = "SELECT * FROM users WHERE status = TRUE;"
    return execute_query(query, fetch="all")


def show_all_companies_query():
    """
    Returns all companies.
    """
    query = "SELECT * FROM companies WHERE status = TRUE;"
    return execute_query(query, fetch="all")


def show_all_departments_query():
    """
    Returns all departments.
    """
    query = "SELECT * FROM departments WHERE status = TRUE;"
    return execute_query(query, fetch="all")


def show_all_regions_query():
    """
    Returns all regions.
    """
    query = "SELECT * FROM regions WHERE status = TRUE;"
    return execute_query(query, fetch="all")


def show_all_roles_query():
    """
    Returns all roles.
    """
    query = "SELECT * FROM roles WHERE status = TRUE;"
    return execute_query(query, fetch="all")


def sum_of_all_ages_query():
    """
    Returns the sum of all ages.
    """
    query = "SELECT SUM(age) FROM users WHERE status = TRUE;"
    return execute_query(query, fetch="one")


def all_users_by_older_to_younger_query():
    """
    Returns all users sorted by age from older to younger.
    """
    query = "SELECT * FROM users WHERE status = TRUE ORDER BY age ASC;"
    return execute_query(query, fetch="all")


def all_users_by_younger_to_older_query():
    """
    Returns all users sorted by age from younger to older.
    """
    query = "SELECT * FROM users WHERE status = TRUE ORDER BY age DESC;"
    return execute_query(query, fetch="all")


def all_users_by_new_hired_to_old_hired_query():
    """
    Returns all users sorted by hire_date from new hired to old hired.
    """
    query = "SELECT * FROM users WHERE status = TRUE ORDER BY hire_date ASC;"
    return execute_query(query, fetch="all")


def all_users_by_old_hired_to_new_hired_query():
    """
    Returns all users sorted by hire_date from old hired to new hired.
    """
    query = "SELECT * FROM users WHERE status = TRUE ORDER BY hire_date DESC;"
    return execute_query(query, fetch="all")


def all_users_by_starts_with_letter_query(first: str, second: str, third:str):
    """
    Returns all users sorted alphabetically by name.
    """
    query = f"""
        SELECT * FROM users
        WHERE status = TRUE
        AND name LIKE 's%' OR name LIKE 's%' OR name LIKE 's%'
        ORDER BY name ASC;
    """
    return execute_query(query, (first, second, third), fetch="all")


def all_users_by_starts_with_letter2_query(first: str, second: str):
    """
    Returns all users sorted alphabetically by name.
    """
    query = f"""
        SELECT * FROM users
        WHERE status = TRUE
        AND name LIKE 's%' OR name LIKE 's%'
        ORDER BY name ASC;
    """
    return execute_query(query, (first, second), fetch="all")


def all_users_by_starts_with_letter_endswith_letter_query(first: str, second: str):
    """
    Returns all users sorted alphabetically by name, where the first letter starts with the given letter and the last letter ends with the given letter.
    """
    query = f"""
        SELECT * FROM users
        WHERE status = TRUE
        AND name LIKE '{first}%' AND name LIKE '%{second}';
        ORDER BY name ASC;
    """
    return execute_query(query, (first, second), fetch="all")


def all_users_by_ends_with_letter_query(first: str, second: str, third:str):
    """
    Returns all users sorted alphabetically by name.
    """
    query = f"""
        SELECT * FROM users
        WHERE status = TRUE
        AND name LIKE '%s' OR name LIKE '%s' OR name LIKE '%s'
        ORDER BY name ASC;
    """
    return execute_query(query, (first, second, third), fetch="all")


def all_users_by_ends_with_letter2_query(first: str, second: str):
    """
    Returns all users sorted alphabetically by name.
    """
    query = f"""
        SELECT * FROM users
        WHERE status = TRUE
        AND name LIKE '%s' OR name LIKE '%s'
        ORDER BY name ASC;
    """
    return execute_query(query, (first, second), fetch="all")


def all_users_by_born_after_2020_query():
    """
    Returns all users born after 2020 sorted alphabetically by name.
    """
    query = """
        SELECT * FROM users
        WHERE status = TRUE
        AND birth_date > '2020-12-31'
        ORDER BY name ASC;
    """
    return execute_query(query, fetch="all")


def all_users_by_born_before_2020_query():
    """
    Returns all users born before 2020 sorted alphabetically by name.
    """
    query = """
        SELECT * FROM users
        WHERE status = TRUE
        AND birth_date < '2020-01-01'
        ORDER BY name ASC;
    """
    return execute_query(query, fetch="all")


def all_users_by_hired_after_2020_query():
    """
    Returns all users hired after 2020 sorted alphabetically by name.
    """
    query = """
        SELECT * FROM users
        WHERE status = TRUE
        AND created_at > '2020-12-31'
        ORDER BY name ASC;
    """
    return execute_query(query, fetch="all")


def all_users_by_hired_before_2020_query():
    """
    Returns all users hired before 2020 sorted alphabetically by name.
    """
    query = """
        SELECT * FROM users
        WHERE status = TRUE
        AND created_at < '2020-01-01'
        ORDER BY name ASC;
    """
    return execute_query(query, fetch="all")


def all_companies_created_before_2020_query():
    """
    Returns all companies created before 2020 sorted alphabetically by name.
    """
    query = """
        SELECT * FROM companies
        WHERE status = TRUE
        AND created_at < '2020-01-01'
        ORDER BY name ASC;
    """
    return execute_query(query, fetch="all")


def all_companies_created_after_2020_query():
    """
    Returns all companies created after 2020 sorted alphabetically by name.
    """
    query = """
        SELECT * FROM companies
        WHERE status = TRUE
        AND created_at > '2020-12-31'
        ORDER BY name ASC;
    """
    return execute_query(query, fetch="all")


def all_departments_created_before_2020_query():
    """
    Returns all departments created before 2020 sorted alphabetically by name.
    """
    query = """
        SELECT * FROM departments
        WHERE status = TRUE
        AND created_at < '2020-01-01'
        ORDER BY name ASC;
    """
    return execute_query(query, fetch="all")


def all_departments_created_after_2020_query():
    """
    Returns all departments created after 2020 sorted alphabetically by name.
    """
    query = """
        SELECT * FROM departments
        WHERE status = TRUE
        AND created_at > '2020-12-31'
        ORDER BY name ASC;
    """
    return execute_query(query, fetch="all")
