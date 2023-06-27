# Determine whether a number is a perfect number, palindrome or an armstrong number
n = int(input("Enter a number : "))
# Perfect number
sum1 = 0
for i in range(1, n):
    if (n % i == 0):
        sum1 += i
if (sum1 == n):
    print("The number", n, "is a perfect number!")
else:
    print("The number", n, "is not a perfect number!")

# Armstrong number
sum2 = 0
temp = n
while (temp > 0):
    digit = temp % 10
    sum2 += digit**3
    temp //= 10
if (n == sum2):
    print("The number", n, "is an Armstrong number!")
else:
    print("The number", n, "is not an Armstrong number!")

# Palindrome number
temp2 = n
rev = 0
while (temp2 > 0):
    dig = temp2 % 10
    rev = rev*10 + dig
    temp2 //= 10
if (n == rev):
    print("The number", n, "is a Palindrome!")
else:
    print("The number", n, "is not a Palindrome!")