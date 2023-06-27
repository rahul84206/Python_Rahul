# Input a tuple having words of a string as its elements and translate each text element to Pig Latin
tup=eval(input("Enter a tuple : "))
index=0
while index < len(tup):
    new=tup[index][1:]+tup[index][0]+"ay"
    print(new,end=" ")
    index+=1
    
