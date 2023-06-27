# Largest no. of a list of numbers entered through keyboard
a=[]
n=int(input('Size of list : '))
for i in range(0,n):
    b=int(input('Enter a no. : '))
    a.append(b) 
max=a[0]
for i in range(1,n):
    if a[i]>max:
        max=a[i]
print('The largest no. is : ',max)
