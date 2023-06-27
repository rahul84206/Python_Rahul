# Write a program to input names of n students and store them in a tuple. Also input a name from the user and finds if this student is present in the tuple or not.

#Program to input names of n students and store them in a tuple.
#Input a name from the user and find if this student is present in the tuple or not.


name = tuple()
#Create empty tuple 'name' to store the values
n = int(input("How many names do you want to enter? "))
for i in range(0, n):
    num = input("> ")
    #it will assign emailid entered by user to tuple 'name'
    name = name + (num,)
print("\nThe names entered in the tuple are:")
print(name)
search=input("\nEnter the name of the student you want to search? ")
#Using membership function to check if name is present or not
if search in name:
    print("The name",search,"is present in the tuple")
else:
    print("The name",search,"is not found in the tuple")