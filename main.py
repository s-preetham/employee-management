import random
import os
while(True):
    print("==============================")
    print("1: Add an Employee\n2: Delete an Employee\n3: Modify an Employee\n4: Search for an Employee\n5: Sort based on \n6: Exit")
    print("==============================")
    choice = int(input("Enter your choice: "))
    if choice==1:
        file = open('emp_data.txt','a')
        print("Add an Employee:")
        while(True):
            empid = random.randrange(1000,1999) 
            file = open('emp_data.txt','r')
            if empid in file:
                continue
            else: 
                break
        print(f"Employee ID assigned: {empid}")
        empName = input("Enter the Name: ")
        while(True):
            deptName = input("Enter the dept name (sales, accounts, finance only): ")
            if deptName == "sales" or deptName == "accounts" or deptName == "finance":
                break
            else: 
                print("Enter only from sales/accounts/finance!")
        empLoc = input("Enter the employee location: ")
        empSalary = int(input("Enter the employee salary: "))
        print(empid,empName,deptName,empLoc,empSalary)
        
        with open("emp_data.txt", 'a') as file1:
            file1.write(f"{empid}\t{empName}\t{deptName}\t{empLoc}\t{empSalary}\n")
        file.close()
        cont = input("Employee record added. Do you want to continue?  ")
        if cont == 'y':
            continue
        else:
            break
    elif choice==2:
        print("Delete an Employee:")
        while True:
            empid = input("Enter the employee ID: ")
            with open("emp_data.txt", 'r') as file:
                content = file.read()
                lines = file.readlines()
                if empid in content:
                    print('ID exists')
                    break
                else:
                    print('Employee does not exist')
                    continue
        with open("emp_data.txt", "r") as input1:
            with open("temp.txt", "w") as output:
                for line in input1:
                    if not line.strip("\n").startswith(empid):
                        output.write(line)
        os.replace('temp.txt', 'emp_data.txt')
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
            if choice3==1:
                newName = input("Enter new employee name: ")
                empid = input("Enter employee id: ")
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    for i in data:
                        if i[0]==empid:
                            i[1]=newName
                    for lo in data:
                        with open('temp.txt', 'a') as outfile:
                            outfile.write('\t'.join(str(i) for i in lo))
                            outfile.write('\n')
                os.replace('temp.txt','emp_data.txt')
                print("Details modified.\n")
            elif choice3==2:
                newDept = input("Enter new Department name: ")
                empid = input("Enter employee id: ")
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    for i in data:
                        if i[0]==empid:
                            i[2]=newDept
                    for lo in data:
                        with open('temp.txt', 'a') as outfile:
                            outfile.write('\t'.join(str(i) for i in lo))
                            outfile.write('\n')
                os.replace('temp.txt','emp_data.txt')
                print("Details modified.\n")
            elif choice3==3:
                newLoc = input("Enter new Location name: ")
                empid = input("Enter employee id: ")
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    for i in data:
                        if i[0]==empid:
                            i[3]=newLoc
                    for lo in data:
                        with open('temp.txt', 'a') as outfile:
                            outfile.write('\t'.join(str(i) for i in lo))
                            outfile.write('\n')
                os.replace('temp.txt','emp_data.txt')
                print("Details modified.\n")
            elif choice3==4:
                newsal = input("Enter new Salary amount: ")
                empid = input("Enter employee id: ")
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    for i in data:
                        if i[0]==empid:
                            i[4]=newsal
                    for lo in data:
                        with open('temp.txt', 'a') as outfile:
                            outfile.write('\t'.join(str(i) for i in lo))
                            outfile.write('\n')
                os.replace('temp.txt','emp_data.txt')
                print("Details modified.\n")
            else:
                break
    elif choice==4:
        print("View employee details: ")
        empid = input("Enter ID: ")
        print("Details for {}:\n".format(empid))
        flag = 0
        with open('emp_data.txt', 'r+', encoding='utf-8') as file:
            data = file.readlines()
        for line in data:
            if line.startswith(empid):
                deet = ['Id', 'Employee name', 'Department name','Location', 'Salary']
                new = line.split('\t')
                for x in zip(deet, new):   
                    print(": ".join(map(str, x)))
                flag = 1
                break
        if flag != 1:
            print("Employee not found!\n")
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
            if choice2==1:
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    data.sort(key = lambda x : x[0], reverse=False)
                    for i in range(len(data)):
                        print(*data[i], sep = '\t',end = '\n')       
            elif choice2==2:
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    data.sort(key = lambda x : x[1], reverse=False)
                    for i in range(len(data)):
                        print(*data[i], sep = '\t',end = '\n')
            elif choice2==3:
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    data.sort(key = lambda x : x[2], reverse=False)
                    for i in range(len(data)):
                        print(*data[i], sep = '\t',end = '\n')
            elif choice2==4:
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    data.sort(key = lambda x : x[3], reverse=False)
                    for i in range(len(data)):
                        print(*data[i], sep = '\t',end = '\n')
            elif choice2==5:
                with open("emp_data.txt", 'r') as f:
                    data = [line.split() for line in f]
                    data.sort(key = lambda x : x[4], reverse=False)
                    for i in range(len(data)):
                        print(*data[i], sep = '\t',end = '\n')
            elif choice2==6:
                break
    elif choice==6:
        break
    else:
        break
    