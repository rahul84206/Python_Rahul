t= eval(input("enter the string tuple = "))

short = t [ 0 ]
for i in t :
    if len(i) < len( short ) :
        short = i
print("smllest string in tuple = ",short)

