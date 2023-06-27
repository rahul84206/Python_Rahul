# Write a program to enter names of employees and their salaries as input and store them in a dictionary.

emp_dic = {}
while True:
    name = input("Enter employee name : ")
    sal = int(input("Enter employee salary : "))
    emp_dic[name] = sal
    choice = input("Do you want to enter another record press 'y' if yes : ")
    if choice != "y":
        break
print(emp_dic)
