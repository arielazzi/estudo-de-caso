import csv
from datetime import datetime

employees = []

employee_file = "employees.csv"

def load_employees():
  global employee_file, employees
  try:
    with open(employee_file, "r") as file:
      leitor = csv.reader(file)
      employees = [linha[0] for linha in leitor if linha]
      print(f"Loaded {len(employees)} employees from {employee_file}.")
  except FileNotFoundError:
    # create file if it doesn't exist
    with open(employee_file, "w") as file:
      csv.writer(file).writerows([["id", "name", "salary", "department", "job_description", "hire_date"]])
      pass
    employees.clear()
    print(f"No existing employee file found. Starting with an empty employee list.")

def generate_employee_id():
  new_id = len(employees) + 1
  return f"{new_id:06d}"

def register_new_employee():
  dict_employee = {
        "name": "",
        "department": "",
        "position": "",   
        "salary": "",
        "hire_date": ""
    }
    
  for key in dict_employee:

    if key == "salary":
      while True:
        try:
          value = float(input(f"Enter the employee's {key}: "))
          dict_employee[key] = value
          break
        except ValueError:
          print(f"Invalid {key}. Please enter a numeric value.")

    elif key == "hire_date":
      while True:
        value = input("Enter the employee's hire date (YYYY-MM-DD): ")
        try:
          datetime.strptime(value, "%Y-%m-%d")
          dict_employee[key] = value
          break
        except ValueError:
          print("Invalid date format. Use YYYY-MM-DD.")

    else:
      dict_employee[key] = input(f"Enter the employee's {key}: ").strip()

  employee = {
    "id": generate_employee_id(),
    **dict_employee 
  }

  employees.append(employee)

  print(
    f"\nEmployee successfully registered!\n"
    f"ID: {employee['id']}\n"
    f"Name: {employee['name']}\n"
    f"Position: {employee['position']}\n"
    f"Department: {employee['department']}\n"
    f"Salary: ${employee['salary']:.2f}\n"
    f"Hire Date: {employee['hire_date']}\n"
  )

def print_employee(employee):
    print(
        f"\nID: {employee['id']}\n"
        f"Name: {employee['name']}\n"
        f"Position: {employee['position']}\n"
        f"Department: {employee['department']}\n"
        f"Salary: ${employee['salary']:.2f}\n"
        f"Hire Date: {employee['hire_date']}\n"
    )

def list_employees():
  for employee in employees:
    print(employee)

def get_employee_by_id(employee_id):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    return None

def get_employees():
  if not employees:
    print("No employees registered.")
    return

  while True:
    print("\n====== Get Employees ======")
    print("1. Show all employees")
    print("2. Search employee by ID")
    print("3. Search employee by name")
    print("4. Show total payroll")
    print("5. Back to main menu")

    option = input("Choose an option: ").strip()

    match option:
      case "1":
        list_employees()

      case "2":
        employee_id = input("Enter the employee ID: ").strip()
        employee = get_employee_by_id(employee_id)

        if employee:
          print_employee(employee)
        else:
          print(f"Employee with ID {employee_id} not found.")

      case "3":
        name = input("Enter the employee name: ").strip().lower()
        found_employees = [
          employee for employee in employees
          if name in employee["name"].lower()
          ]

        if found_employees:
          for employee in found_employees:
            print_employee(employee)
        else:
          print(f"No employees found with name containing '{name}'.")

      case "4":
        
      case "5":
        break

      case _:
        print("Invalid option! Please try again.")

def update_employee_salary():
  list_employees()

  employee_id = input("Enter the employee ID to update salary: ")
  new_salary = input("Enter the new salary: ")

  for employee in employees:
    if employee["id"] == employee_id:
      employee["salary"] = new_salary
      print(f"Employee {employee_id} salary updated to {new_salary}.")
      return

  print(f"Employee with ID {employee_id} not found.")

def terminate_employee():
    list_employees()

    employee_id = input("Enter the employee ID to terminate: ")

    for employee in employees:
        if employee["id"] == employee_id:
            employees.remove(employee)
            print(f"Employee {employee_id} has been terminated.")
        return

    print(f"Employee with ID {employee_id} not found.")


def menu():
  while True:
    print("\n====== Payroll management ======")
    print("1. Register new employee")
    print("2. Get employees")
    print("3. Update employee salary")
    print("4. Terminate employee")
    print("5. Exit")

    option = input("Choose an option: ")

    match option:
        case "1":
          while True:
            register_new_employee()
            
            while True:
              choice = input("Do you want to register another employee? (y/n): ").lower()
              if choice in ["y", "n"]:
                break
              else:
                print("Invalid option. Please enter 'y' or 'n'.")

            if choice == "n":
              break
        case "2":
            get_employees()
            print("Employees retrieved.")
            break
        case "3":
            update_employee_salary()
            break
        case "4":
            terminate_employee()
            # save_employees()
            print("Employees saved. Exiting the program...")
            break
        case "5":
            print("Exiting the program...")
            exit()
        case _:
            print("Invalid option! Please try again.")

load_employees()
menu()
# print("User login:")

# user = input("Type username: ").strip().lower()
# password = input("Type password: ").strip()


# if user == "admin" and password == "admin123":
#   menu()
# else:
#   print("Invalid credentials! Exiting the program...")
#   exit()
