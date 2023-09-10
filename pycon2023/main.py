from pycon2023 import Company, Employee

class CompanyRunner:

    @classmethod
    def run(_cls):
        company = Company("Schnitzels and Bits")

        print("Welcome to our company, " + company.get_name())

        company.set_name("Bob's Bicycle Repair")

        print("Renamed the company to " + company.get_name())

        company.add_employee(Employee("001", " Alice", 100_000.00))
        company.add_employee(Employee("002", "Bob",    120_000.00))
        company.add_employee(Employee("003", "Carl",    80_000.00))
        company.add_employee(Employee("004", "Bob ",    90_000.00))

        print(f"There are {company.number_of_employees()} employees at the company")

        company.add_employee(Employee("005", "Billy Bob", 70_000.00))
        company.add_employee(Employee("006", "Anna Lee",  90_000.00))

        print("Welcome " + company.find_employee_by_id("005").get_name() + " and "
              + company.find_employee_by_id("006").get_name() + " to the company")

        print(f"Now there are {company.number_of_employees()} employees at the company")

        print("Time for a pay raise for everyone!")

        bob = company.find_employee_by_id("002")
        print(f"{bob.get_name()}'s salary before the raise is {bob.get_salary():.2f}\n")

        company.everybody_gets_raise_by(0.1)

        print(f"{bob.get_name()}'s salary before the raise is {bob.get_salary():.2f}\n")
    
if __name__ == "__main__":
    CompanyRunner.run()