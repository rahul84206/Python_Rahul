# Input a list of numbers and find the smallest and largest number from the list.
#create empty list
mylist = []
number = int(input('How many elements to put in the List? '))
for n in range(number):
    element = int(input('Enter element : '))
    mylist.append(element)
print("Maximum element in the list is : ", max(mylist))
print("Minimum element in the list is : ", min(mylist))
