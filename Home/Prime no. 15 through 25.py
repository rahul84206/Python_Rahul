# Prime number from 15 through 25
print("Prime nos. range between 15 through 25 : ")
for num in range(15,25):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num,end=' ')

