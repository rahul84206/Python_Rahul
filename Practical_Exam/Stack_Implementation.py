# STACK IMPLEMENTATION

# Empty stack checking
def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False

# Push item into a stack
def push(stk, item):
    stk.append(item)
    top = len(stk)-1

# Pop item into a stack
def pop(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        item = stk.pop()
        if len(stk) == 0:
            top = None
        else:
            top = len(stk)-1
        return item

# Peek value of a Stack
def peek(stk):
    if isEmpty(stk):
        return "Underflow"
    else:
        top = len(stk)-1
        return stk[top]

# Display the stack
def display(stk):
    if isEmpty(stk):
        print("Stack Empty")
    else:
        top = len(stk)-1
        print(stk[top],"<-top")
        for i in range(top-1,-1,-1):
            print(stk[i])

# main
stk=[]
top=None

while True:
    print("Stack Operations")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("3. ")
    print("4. Display")
    print("5. Exit")
    ch=int(input("Enter your choice (1-5) : "))
    if ch==1:
        item=int(input("Enter item: "))
        push(stk,item)
    elif ch==2:
        item=pop(stk)
        if item =="Undeflow":
            print("Underflow! Stack is empty!")
        else:
            print("Popped item is",item)
    elif ch==3:
        item=peek(stk)
        if item == "Underflow":
            print("Underflow! Stack is empty!")
        else:
            print("Topmost item is",item)
    elif ch==4:
        display(stk)
    elif ch==5:
        break
    else:
        print("Invalid choice!")



