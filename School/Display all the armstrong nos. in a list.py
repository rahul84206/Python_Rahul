# Display all the armstrong nos. in a list

ls=eval(input("Enter a list : "))
for i in range (len(ls)):
    sum=0
    temp=ls[i]
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if (ls[i]==sum):
        print(ls[i],"is a Armstrong number.")
    else:
        print(ls[i],"is not an Armstrong number.")
