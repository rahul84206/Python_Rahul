def fib(n):
    ls=[0,1]
    for i in range(0,7):
        c=ls[i]+ls[i+1]
        ls.append(c)
    return ls
n=9
print('Fibonacci Series',tuple(fib(n)))
