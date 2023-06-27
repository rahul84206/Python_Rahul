# Compute the greatest common divisor and least common multiple of two integers

x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller + 1):
    if ((x % i == 0) and (y % i == 0)):
        hcf = i
lcm = (x*y)//hcf
print("The H.C.F. of", x, "and", y, "is", hcf)
print("The L.C.M. of", x, "and", y, "is", lcm)
