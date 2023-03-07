'''
Experiment No.7
Program to illustrate Python-MySQL database connectivity.
RollNo.:
Name:
'''
import mysql.connector

#Theory about MySQL and MySQL-Connector-Python

def insert(myc,r,n,a,m,p):
    query="insert into Student values('"+r+"','"+n+"','"+m+"','"+a+"',"+str(p)+")"
    print(query)
    try:
        myc.execute(query)
        myc.execute('commit')
        print('Record inserted successfully..')
    except Exception as e:
        print('Insertion failed..'+str(e))
    
def display(mycursor):
    query='select * from Student'
    mycursor.execute(query)
    for row in mycursor:
        print(row)
    
def update(mycursor,col,vals,r):
    try:
        query=f"update student set {col} = '{vals}' where RollNo = '{r}'"
        mycursor.execute(query)
        print('Record updated successfully..')
    except Exception as e:
        print("Update failed...",e)
def delete(mycursor,r):
    query=f"delete from student where RollNo = '{r}'"
    mycursor.execute(query)
    print('Record deleted successfully..')
    


def main():
    mydb = mysql.connector.connect(host="localhost",user="root",password="@rshadK786")
    mycursor=mydb.cursor()
    mycursor.execute('use stud_mgmt')
    while True:
        print('\t\t\tMENU\n1. Insert.\n2. Display.\n3. Update.')
        print('4. Delete. \n5. Exit.')
        ch=int(input('Enter your choice:: '))
        if ch==5:
            break
        elif ch==1:
            r=input('Enter the Roll No: ')
            n=input('Enter The Name: ')
            m=input('Enter Mobile No: ')
            a=input('Enter The Address: ')
            p=float(input('Enter The Pointer: '))
            insert(mycursor,r,n,a,m,p)
        elif ch==2:
            display(mycursor)
        elif ch==3:
            col=input("Enter column Name: ")
            vals=input("Enter value of Col: ")
            r=input('Enter the Roll No: ')
            update(mycursor,col,vals,r)
        elif ch==4:
            r=input('Enter the Roll No: ')
            delete(mycursor,r)
        else:
            print('Wrong choice...')

        
if __name__=='__main__':
    main()