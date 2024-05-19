import employee_info

def test_get_employees_by_age_range():
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert employee_info.get_employees_by_age_range(24, 34) == expected_result


def test_calculate_average_salary():
    expected_average_salary = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    assert employee_info.calculate_average_salary() == expected_average_salary

def test_get_employees_by_dept():
    expected_result = [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    assert employee_info.get_employees_by_dept("Engineering") == expected_result