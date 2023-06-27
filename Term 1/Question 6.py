# Input a number and check if the number is a prime or composite number

n = int(input("Enter a number : "))
c = 0
for i in range(1, n+1):
    if n % i == 0:
        c += 1
if c == 2:
    print("The number", n, "is a prime number!")
else:
    print("The number", n, "is a composite number!")
