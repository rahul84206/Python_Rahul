# Write a program to search for an element in a given list of numbers.

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Enter the element you want to search for : "))
if x in l:
 print(x, "is in position", l.index(x), "in the list.")
else:
 print("Element not found.")
