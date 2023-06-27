# Check whether Perfect number or not
n = int(input('Enter a number : '))
sum = 0
for i in range (1, n):
    if (n%i==0):
        sum+=i
if (sum==n):
    print('The number',n,'is a Perfect Number!')
else:
    print('The number', n, 'is not a Perfect Number!')
