print("👨‍💼 Employee Management System")

employees = []

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))

        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary
        }

        employees.append(employee)

        print("✅ Employee added successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("❌ No employees found.")
        else:
            print("\nEmployee Details:")

            for employee in employees:
                print("--------------------")
                print("ID:", employee["id"])
                print("Name:", employee["name"])
                print("Department:", employee["department"])
                print("Salary:", employee["salary"])

    elif choice == "3":
        search_id = input("Enter employee ID to search: ")

        found = False

        for employee in employees:
            if employee["id"] == search_id:
                print("\n✅ Employee Found")
                print("ID:", employee["id"])
                print("Name:", employee["name"])
                print("Department:", employee["department"])
                print("Salary:", employee["salary"])
                found = True
                break

        if not found:
            print("❌ Employee not found.")

    elif choice == "4":
        update_id = input("Enter employee ID to update: ")

        found = False

        for employee in employees:
            if employee["id"] == update_id:
                employee["name"] = input("Enter new name: ")
                employee["department"] = input("Enter new department: ")
                employee["salary"] = float(input("Enter new salary: "))

                print("✅ Employee updated successfully!")
                found = True
                break

        if not found:
            print("❌ Employee not found.")

    elif choice == "5":
        delete_id = input("Enter employee ID to delete: ")

        found = False

        for employee in employees:
            if employee["id"] == delete_id:
                employees.remove(employee)
                print("✅ Employee deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Employee not found.")

    elif choice == "6":
        print("Thank you for using Employee Management System! 👋")
        break

    else:
        print("❌ Invalid choice!")
