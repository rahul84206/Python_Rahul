# Write a program to create a copy of a list, add 10 to its first and last elements and display the list.


ls=eval(input("Enter the list : "))
ls1=ls.copy()
ls1[0]+=10
ls1[-1]+=10
print("The list is : ",ls1)
