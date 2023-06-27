from random import randint
def random_ndigits(n):
    range_start=10**(n-1)
    range_end=(10**n)-1
    return randint(range_start,range_end)
n=int(input('Enter the number of terms: '))
print(random_ndigits(n))
