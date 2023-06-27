# Sum values of odd nos. and prime nos. separately from a list of elements 

ls=eval(input("Enter a list : "))
osum=0
psum=0
for i in ls:
    if i%2 != 0:
        sum+=i
