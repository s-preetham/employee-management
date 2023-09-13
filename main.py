import emp_func

while(True):

    print("==============================")
    print("1: Add an Employee\n2: Delete an Employee\n3: Modify an Employee\n4: Search for an Employee\n5: Sort based on \n6: Exit")
    print("==============================")
    choice = int(input("Enter your choice: "))

    if choice==1:
        emp_func.add_employee()
        cont = input("Employee record added. Do you want to continue?  ")
        if cont == 'y':
            continue
        else:
            break

    elif choice==2:
        emp_func.del_employee()
        cont = input("Employee record deleted. Do you want to continue? ")
        if cont == 'y':
            continue
        else:
            break

    elif choice==3:
        while True:
            print("Modify Employee details: \n")
            print("1: Modify by Name:")
            print("2: Modify by Department:")
            print("3: Modify by Location:")
            print("4: Modify by Salary")
            print("5: Exit")
            choice3 = int(input("Enter option: "))
            if choice3 == 5:
                break
            if (choice3 > 5 or choice3 < 1 or type(choice3) != 'int'):
                print("Invalid choice")
            emp_func.mod_employee(choice3)
            
    elif choice==4:
        emp_func.view_employee()

    elif choice==5:
        while True:
            print("Sort employees\n")
            print("1: Sort by ID:")
            print("2: Sort by name:")
            print("3: Sort by department:")
            print("4: Sort by location:")
            print("5: Sort by salary:")
            print("6: Exit to main menu")
            choice2 = int(input("Enter choice: "))
            if choice2 == 6:
                break
            if (choice2 >= 6 or choice2 < 1 or type(choice2) != 'int'):
                print("Invalid choice")
            emp_func.sort_employee(choice2)

    elif choice==6:
        break
    
    else:
        print("Invalid choice!!\n")
        continue
    