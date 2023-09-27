class Employee:
    def __init__(self, new_id, new_name, new_salary):
        self._id = new_id
        self.set_name(new_name)
        self.set_salary(new_salary)

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        """Set the employee name after removing leading and trailing spaces, \
        which could be left by upstream system
        - new_name: the new name for the employee, possibly with leading and \
          trailing white space to be removed
        """
        self._name = new_name.replace(" ", "")

    def get_salary(self):
        return self._salary

    def set_salary(self, new_salary):
        self._salary = new_salary

    def is_intern(self):
        return self.get_salary() is None
