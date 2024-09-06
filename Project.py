class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary

    def display_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in self.employees:
            print("\nEmployee with this ID already exists.")
            return

        emp_name = input("Enter Employee Name: ")
        emp_salary = float(input("Enter Employee Salary: "))
        new_employee = Employee(emp_id, emp_name, emp_salary)
        self.employees[emp_id] = new_employee
        print("\nEmployee added successfully!")

    def delete_employee(self):
        emp_id = int(input("Enter Employee ID to delete: "))
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully!")
        else:
            print("Employee with this ID does not exist.")

    def display_all_employees(self):
        if not self.employees:
            print("No employees to display.")
        else:
            for emp in self.employees.values():
                emp.display_employee_details()
                print("-" * 30)

    def menu(self):
        while True:
            print("\n*** Employee Management System ***\n")
            print("1. Add Employee")
            print("2. Delete Employee")
            print("3. Display All Employees")
            print("4. Exit\n")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.delete_employee()
            elif choice == '3':
                print("\n*** Displaying all the Employee Records ***\n")
                self.display_all_employees()
            elif choice == '4':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.menu()
