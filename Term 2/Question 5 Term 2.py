# Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have scored marks above 75.

no_of_std = int(input("Enter number of students : "))
result = {}
for i in range(no_of_std):
    print("Enter details of student no.", i+1)
    roll_no = int(input("Roll No : "))
    std_name = input("Student Name : ")
    marks = int(input("Marks : "))
    result[roll_no] = [std_name, marks]
print("Result : ",result)
print("Student's name who have scored more than 75 marks is/are : ")
for student in result:
    if result[student][1] > 75:
        print(result[student][0],end=', ')

