# Input three numbers and display the largest/smallest number

# Display the Largest number.
a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))
max = 0
if a > b:
    max = a
else:
    max = b
if c > max:
    max = c
print("The largest number is :", max)

# OR

# Display the Smallest number.
min = 0
if a < b:
    min = a
else:
    min = b
if c < min:
    min = c
print("The Smallest number is :", min)
