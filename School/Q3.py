import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='84206', database="test", charset='utf8')
if mydb.is_connected():
    print ('Succesfully connected to MySql database')
else:
    print('Not Connected')
'''
cur=mydb.cursor()
for i in range(5):
    id=int(input("Enter Employee Number: "))
    name=input("Enter Employee Name: ")
    job = input("Enter Employee's Job: ")
    salary = int(input("Enter Employee's Salary: "))


    query=("Insert into Employee Values({},'{}','{}',{})".format(id,name,job,salary))
    cur.execute(query)
    mydb.commit()

cur.execute("select * from Employee")
data = cur.fetchmany(4)
for i in data :
    print(i)'''

















