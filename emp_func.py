import os

def add_employee():
    file = open('emp_data.txt','a')
    print("Add an Employee:")
    empid_list = [i for i in range(1000,2000)]
    file = open('emp_data.txt','r')
    lines = [i.split()[0] for i in file]
    for i in empid_list:
        if str(i) in lines:
            continue
        else: 
            empid = i
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

def del_employee(): 
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

def mod_employee(choice3):

    if choice3==1:
        newName = input("Enter new employee name: ")
        empid = input("Enter employee id: ")
        modification(1,empid,newName)
    elif choice3==2:
        newDept = input("Enter new Department name: ")
        empid = input("Enter employee id: ")
        modification(2,empid,newDept)

    elif choice3==3:
        newLoc = input("Enter new Location name: ")
        empid = input("Enter employee id: ")
        modification(3,empid,newLoc)

    elif choice3==4:
        newsal = input("Enter new Salary amount: ")
        empid = input("Enter employee id: ")
        modification(4,empid,newsal)

def modification(num,empid,typee):
    with open("emp_data.txt", 'r') as f:
        data = [line.split() for line in f]
        for i in data:
            if i[0]==empid:
                i[num]=typee
        for lo in data:
            with open('temp.txt', 'a') as outfile:
                outfile.write('\t'.join(str(i) for i in lo))
                outfile.write('\n')
    os.replace('temp.txt','emp_data.txt')
    print("Details modified.\n")

def view_employee():
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

def sort_employee(choice2):
    if choice2==1:
        sort(0)
    elif choice2==2:
        sort(1)
    elif choice2==3:
        sort(2)
    elif choice2==4:
        sort(3)
    elif choice2==5:
        sort(4)

def sort(num):
    with open("emp_data.txt", 'r') as f:
        data = [line.split() for line in f]
        data.sort(key = lambda x : x[num], reverse=False)
        for i in range(len(data)):
            print(*data[i], sep = '\t',end = '\n')