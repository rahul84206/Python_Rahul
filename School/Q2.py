def PUSH(Arr):  
    s=[] 
    for i in range(0,len(Arr)):  
        if Arr[i]%5==0:  
            s.append(Arr[i])  
    if len(s)==0: 
        print("Stack is Empty.")
    else:  
        print(s)

Arr=[25,12,32,35,10,16]
PUSH(Arr)