# Fibonacci Series
def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))

nterms = int(input("Enter the number of terms: "))

# check if the number of terms is valid or not
if nterms <= 0:
    print("Please enter a valid positive integer.")
else:
    print("Fibonacci Series:")
    for i in range(nterms):
        print(fibo(i))

