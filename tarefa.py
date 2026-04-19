import csv

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

def register_new_employee():
  dict_employee = {
        "id": "1234",
        "name": "",
        "position": "",
        "department": "",
        "salary": "",
        "hire_date": ""
    }
    
  for key in dict_employee:

      
    name = input("Enter the employee's name: ")
    department = input("Enter the employee's department: ")
    position = input("Enter the  employee's position: ")
      
    while True:
      try:
        salary = float(input("Enter the employee's salary: "))
        break
      except ValueError:
        print("Invalid salary. Please enter a numeric value.")
      
    while True:
      try:
        hire_date = input("Enter the employee's hire date (YYYY-MM-DD): ")
        break
      except:
        print("Invalid salary. Please enter a numeric value.")

    employee = {
        "id": id,
        "name": name,  
        "position": position,
        "department": department,
        "salary": salary,
        "hire_date": hire_date
    }

    employees.append(employee)
    
    print(
        f"\nEmployee successfully registered!\n"
        f"ID: {id}\n"
        f"Name: {name}\n"
        f"Department: {department}\n"
        f"Role: {position}\n"
        f"Salary: ${salary:.2f}\n"
        f"Hire Date: {hire_date}\n"
    )

def list_employees():
  for employee in employees:
    print(employee)

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
            register_new_employee()
            print("Employee registered.")
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
