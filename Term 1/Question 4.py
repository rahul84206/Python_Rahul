# Write a program to input the value of x and n and print the sum of the following series: x-x**2/2+x**3/3-x**4/4+........x**n/n

x = int(input("Enter the value of x : "))
n = int(input("Enter the power (n) : "))
s = 0
for i in range(1, n+1):
    if i % 2 != 0:
        s = s+x**i/i
    else:
        s = s-x**i/i
print("The sum of the series is", s)
