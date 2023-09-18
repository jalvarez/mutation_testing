class Company:

    def __init__(self, new_name):
        self._name = new_name
        self._employees = []

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

    def add_employee(self, new_employee):
        self._employees.append(new_employee)

    def everybody_gets_raise_by(self, increment_as_fraction):
        """Increase every employee's salary by the specified fraction
            - increment_as_fraction: salary increase as a fraction of the original salary. \
              e.g. if the value of the parameter is 0.1, everyone at the company gets \
              a 10% raise
        """
        for e in self._employees:
            e.set_salary(e.get_salary() * increment_as_fraction)

    def find_employee_by_id(self, id):
        """Finds an employee by their id
           - id: the id of the employee to be found
     
        Return the employee with the id passed as the parameter 
        or null if no such employee exists
        """
        found_index = 0
        for i in range(0, len(self._employees)):
            if self._employees[i].get_id() == id:
                found_index = i
                break
        return self._employees[found_index]
    
    def number_of_employees(self):
        return len(self._employees)
    
    def employee_with_largest_salary(self):
        found = self._employees[0]

        for i in range(0, len(self._employees)):
            employee = self._employees[i]
            if not employee.is_intern() and employee.get_salary() > found.get_salary():
                found = employee
        return found
    
    def employee_with_lowest_salary(self):
        found = self._employees[0]

        for i in range(0, len(self._employees)):
            employee = self._employees[i]
            if employee.get_salary() is not None and employee.get_salary() > found.get_salary():
                employee = found
        return found