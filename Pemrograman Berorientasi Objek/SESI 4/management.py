class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def calculate_salary(self):
        return self.salary
    
    def show_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: ${self.calculate_salary()}")


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + (0.2 * self.salary)


class Engineer(Employee):
    def calculate_salary(self):
        return self.salary + (0.1 * self.salary)


class Intern(Employee):
    def __init__(self, name, emp_id, stipend):
        super().__init__(name, emp_id, stipend)
    
    def calculate_salary(self):
        return self.salary


employees = []

def add_employee():
    name = input("Enter employee name: ")
    emp_id = int(input("Enter employee ID: "))
    emp_type = input("Enter employee type (manager/engineer/intern): ").lower()
    salary = float(input("Enter salary (or stipend for intern): "))
    
    if emp_type == "manager":
        new_employee = Manager(name, emp_id, salary)
    elif emp_type == "engineer":
        new_employee = Engineer(name, emp_id, salary)
    elif emp_type == "intern":
        new_employee = Intern(name, emp_id, salary)
    else:
        print("Invalid employee type!")
        return
    
    employees.append(new_employee)
    print("Employee added successfully!")

def list_employees():
    if not employees:
        print("No employees found.")
    else:
        for emp in employees:
            emp.show_details()

while True:
    print("\n__Menu__")
    print("1. List employees")
    print("2. Add employee")
    print("3. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        list_employees()
    elif menu == "2":
        add_employee()
    elif menu == "3":
        break
    else:
        print("Invalid menu option. Please try again.")