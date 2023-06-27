# Keep on accepting number until zero
sum = 0
n = float(input('Enter a number : '))
sum += n
c = 0
while n > 0:
    n = float(input('Enter a number : '))
    sum += n
    c += 1
avg = sum/c
print('Sum of all the numbers : ', sum)
print('Average of all the numbers : ', avg)
