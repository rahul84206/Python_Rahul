# Display first character of each word after changing the case
def case(x):
    for i in range(0,len(x)):
        if x[i]==' ':
            if x[i+1].upper():
                print(x[i+1].lower())
            else:
                print(x[i+1].upper())
st=input('Enter a string: ')
st_space=' '+st
case(st_space)
