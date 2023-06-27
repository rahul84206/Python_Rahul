# Product of the digits of a number
num = int(input('Enter a number : '))
p = 1
while num > 0:
    dig = num % 10
    p = p*dig
    num = num//10
print('Product of the digits of a number : ', p)
