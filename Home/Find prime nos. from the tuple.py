# Find prime nos. from the tuple
T=eval(input("Enter a tuple : "))
ln=len(T)
prime=[]
for i in range (0,ln):
    p=T[i]
    c=0
    for j in range(1,p+1):
        if p%j==0:
            c+=1
    if c==2:
        prime.append(T[i])
prime_tup=tuple(prime)
print("Print nos. are : ",prime_tup)