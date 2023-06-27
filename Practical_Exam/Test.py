import  pickle
def write():
    f=open("Student.dat","wb")
    while True:
        r=int(input("Enter Roll No.: "))
        n=input("Enter Name: ")
        data=[r,n]
        pickle.dump(data, f)
        ch=input("More? (Y/N)")
        if ch in 'Nn':
            break
    f.close()
def search():
    found=0
    r = int(input("Enter Roll No. whose name you want: "))
    f=open("Student.dat","rb")
    try:
        while True:
            rec=pickle.load(f)
            if rec[0]==r:
                print(rec[1])
                found=1
                break
    except EOFError:
        f.close()
    if found==0:
        print("Sorry, no record found")
write()
search()





