import random
string = 'CBSEONLINE'
num = random.randint(0, 3)
n = 9
while string[n] != 'L':
    print(string[n]+string[num]+'#', end='')
    num = num+1
    n = n-1
