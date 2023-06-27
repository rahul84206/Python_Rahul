def monotonic(xlist):
    for i in range (len(xlist)-1):
        if xlist[i]<xlist[i+1]:
            return False
    return True
data1=[5,3,2,2,0]
data2=[5,2,3,2,0]
print(monotonic(data1),monotonic(data2))

                          