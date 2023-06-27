# Display the Fibonacci series upto nth term

n = int(input("Enter the value of nth terms : "))
first = 0
second = 1
print("\nFibonacci series is : ")
print(first, end=", ")
print(second, end=", ")
for i in range(2, n):
    third = first + second
    if i != n-1:
        print(third, end=", ")
    else:
        print(third, end="")
    first = second
    second = third
