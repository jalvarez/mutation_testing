import pytest
from unittest.mock import patch

from pycon2023 import Company, Employee

@pytest.fixture(name="company")
def _company_fixture():
    return Company("Megadyne, Inc.")

def test_company_renamed(company):
    proposed_name = "Cybertron Unlimited, Ltd."

    with patch.object(company, 'set_name', wraps=company.set_name) as wrapped_set_name:
        company.set_name(proposed_name)

        wrapped_set_name.assert_called_with(proposed_name)
        assert company.get_name() is not None

def test_leading_trailing_spaces_removed_from_employee_name():
    employee_1 = Employee("001", " Bob", 100_000.00)
    assert "Bob" == employee_1.get_name()

    employee_2 = Employee("002", "Alice  ", 100_000.00)
    assert "Alice", employee_2.get_name()

def test_employee_with_largest_salary(company):
    company.add_employee(Employee("002", "Bob",   115_000.00))
    company.add_employee(Employee("003", "Carl",  110_000.00))
    company.add_employee(Employee("001", "Alice", 120_000.00))

    highest_earner = company.employee_with_largest_salary()
    
    assert "Alice" == highest_earner.get_name()

def test_employee_added(company):
    previous_employee_num = company.number_of_employees()

    company.add_employee(Employee("123", "Dave", 100_000.00))
    assert previous_employee_num + 1 == company.number_of_employees()

    company.add_employee(Employee("456", "Bob", 50_000.00))
    assert previous_employee_num + 2 == company.number_of_employees()

def test_everybody_gets_raise(company):
    increase_by = 0.1   # everybody's salary should go up by this fraction
    daves_original_salary = 100_000.00
    daves_new_salary = 110_000.00

    company.add_employee(Employee("123", "Dave",  daves_original_salary))
    company.add_employee(Employee("456", "Alice", 120_000.00))
    company.add_employee(Employee("789", "Bob",   110_000.00))

    company.everybody_gets_raise_by(increase_by)

    dave = company.find_employee_by_id("123")
    assert daves_new_salary == pytest.approx(dave.get_salary(), 0.001)

def test_default_raise(company):
    original_salary = 100_000.00
    new_salary = 101_000.00
    company.add_employee(Employee("101", "Tom", original_salary))

    company.everybody_gets_raise_by()

    employee = company.find_employee_by_id("101")
    assert new_salary == pytest.approx(employee.get_salary(), 0.001)

def test_find_employee_by_id(company):
    company.add_employee(Employee("123", "Dave",  100_000.00))
    company.add_employee(Employee("456", "Alice", 100_000.00))
    company.add_employee(Employee("789", "Bob",   100_000.00))

    hopefully_dave = company.find_employee_by_id("123")
    hopefully_no_one = company.find_employee_by_id("999")

    assert hopefully_no_one is None

def test_employee_name_changed(company):
    company.add_employee(Employee("123", "Dave",  100_000.00))
    company.add_employee(Employee("456", "Alice", 100_000.00))
    company.add_employee(Employee("789", "Bob",   100_000.00))

    employee = company.find_employee_by_id("123")
    employee.set_name("Tommy Lee")
    employee = company.find_employee_by_id("123")
    print("PASSED" if employee.get_name() == "Tommy Lee" else "FAILED")

def test_employee_with_lowest_salary(company):
    company.add_employee(Employee("001", "Bob", 110_000.00))
    company.add_employee(Employee("002", "Alice", 115_000.00))
    company.add_employee(Employee("003", "Carl",  120_000.00))

    lowest_earner = company.employee_with_lowest_salary()
    
    assert "Bob" == lowest_earner.get_name()