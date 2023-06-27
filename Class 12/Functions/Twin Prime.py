# Find twin prime
def prime(n):
    c=0
    for i in range(2,n+1):
        if n%i==0:
            c+=1
    if c==1:
        return True
    else:
        return False
def twinp(x,y):
    for i in range(x,y+1):
        if prime(i) and prime(i+2):
            print(i,',',i+2)
nlow=int(input('Enter the lower limit: '))
nup=int(input('Enter the upper limit: '))
print('The twin primes are: ')
twinp(nlow,nup)

