import csv
import os
def create():
    f=open("emp.csv","a",newline="")
    cw=csv.writer(f)
    eid=input("Enter New Employee Id: ")
    ename=input("Enter Employee Name: ")
    sal=input("Enter Employee Salary: ")
    rec=[eid,ename,sal]
    cw.writerow(rec)
    print("Record successfully added in csv file")
    f.close()
def read():
    f=open("emp.csv","r")
    cr=csv.reader(f)
    for x in cr:
        print(x)
    f.close()
def update():
    f1=open("emp.csv","r")
    f2=open("temp.csv","w",newline="")
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    neid=input("Enter Employee id to update : ")
    found=0
    for r in cr:
        if r[0]==neid:
            nename=input("Enter new name of the Employee: ")
            nsal=input("Enter new Salary of the Employee: ")
            t=[neid,nename,nsal]
            cw.writerow(t)
            found=1
        else:
            cw.writerow(r)
    f1.close()
    f2.close()
    os.remove("emp.csv")
    os.rename("temp.csv","emp.csv")
    if found==1:
        print("Record successfully Updated")
    else:
        print("Sorry, Record of Employee not found")
def delete():
    f1=open("emp.csv","r")
    f2=open("temp.csv","w",newline="")
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    neid=input("Enter Employee for delete in csv")
    found=0
    for r in cr:
        if r[0]==neid:
            found=1
        else:
            cw.writerow(r)
    f1.close()
    f2.close()
    os.remove("emp.csv")
    os.rename("temp.csv","emp.csv")
    if found==1:
        print("Record successfully Deleted")
    else:
        print("Sorry, Record of Employee not found")
def search():
    f1=open("emp.csv","r")
    cr=csv.reader(f1)
    neid=input("Enter Employee ID for SEARCH : ")
    found=0
    for r in cr:
        if r[0]==neid:
            found=1
            print(r)
        if found==0:
            print("Sorry, Record of Employee not found")

print("EMPLOYEE MANAGEMENT SYSTEM")
while True:
    print("1. to Add Employee details\n2. to Display all Employee details\n3. to Update an Employee's details\n4.to Delete Employee details\n5 to Search an Employee details\n6. to Exit\nEnter your choice: ")
    ch=input()
    if ch=="1":
        print("You selected to CREATE New Employee details:")
        create()
    elif ch=="2":
        print("You selected to READ Employee details: ")
        read()
    elif ch=="3":
        print("You selected to UPDATE Employee details: ")
        update()
    elif ch=="4":
        print("You selected to DELETE Employee details: ")
        delete()
    elif ch=="5":
        print("You selected to SEARCH Employee details: ")
        search()
    elif ch=="6":
        print("---Closing---")
        break
    else:
        print("Invalid Choice")
