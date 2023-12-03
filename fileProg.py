#28
import mysql.connector as conn

C=conn.connect(host='localhost',
               user='root',
               password='tiger',
               database='Dbase')



c1=C.cursor()
c1.execute('''
    CREATE TABLE IF NOT EXISTS BankDetails
        (ACCOUNT_ID CHAR(5) PRIMARY KEY,
        NAME char(15) NOT NULL,
        EMAIL char(35) NOT NULL,
        AMOUNT INT);
    ''')

def add():
    X=input('Enter Account ID: ')
    Y=input('Enter Account name: ')
    Z=input('Enter email linked: ')
    K=int(input('Enter amount in the account: '))
    c1.execute("INSERT INTO BankDetails VALUES('{}', '{}', '{}', {})".format(X,Y,Z,K))
    C.commit()
        
    
def display():
    c1.execute('SELECT * FROM BankDetails;')
    D=c1.fetchall()
    for i in D:
        print(i)
    
print("MENU DRIVEN - bank details\n")
print("1. Add")
print("2. Display")
print('3. Exit')

while True:
    print()
    ch=int(input('Enter your choice: '))
    if ch==1:
        add()
    elif ch==2:
        display()
    elif ch==3:
        print("Thank you!")
        break
    else:
        print("!!ERROR!!")






#29
import mysql.connector
F=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="test")
M=F.cursor()

def add_rec():
    a=int(input("Enter the Flight Number: "))
    b=input("Enter the Airline: ")
    c=int(input("Enter the Flight Time: "))
    d=input("Enter the Origin: ")
    e=input("Enter the Destination: ")
    qry="INSERT INTO FLIGHT VALUES({},'{}',{},'{}','{}')".format(a,b,c,d,e)
    M.execute(qry)
    F.commit()

def disp():
    qry="SELECT * FROM FLIGHT"
    M.execute(qry)
    data=M.fetchall()
    for i in data:
        print(i)

def modify():
    a = int(input("Enter the Flight Number to modify: "))
    b = input("Enter the new Airline: ")
    c = int(input("Enter the new Flight Time: "))
    d = input("Enter the new Origin: ")
    e = input("Enter the new Destination: ")
    qry = "UPDATE FLIGHT SET Airline = '{}', FlightTime = {}, Origin = '{}', Destination = '{}' WHERE FlightNumber = {}".format(b,c,d,e, a)
    M.execute(qry)
    F.commit()

def delete():
    flight_number = int(input("Enter the Flight Number to delete: "))
    qry = "DELETE FROM FLIGHT WHERE FlightNumber = {}".format(flight_number)
    M.execute(qry)
    F.commit()


while True:
    print("Flight Management System")
    print("1. Add Record")
    print("2. Display Records")
    print("3. Modify Record")
    print("4. Delete Record")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_rec()
    elif ch == 2:
        disp()
    elif ch == 3:
        modify()
    elif ch == 4:
        delete()
    elif ch == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")








#30
import mysql.connector
F = mysql.connector.connect(host="localhost", user="root", passwd="tiger", database="Dbase")
M = F.cursor()

def add_t():
    a = int(input("Enter the Train Number: "))
    b = input("Enter the Train Name: ")
    c = input("Enter the Source: ")
    d = input("Enter the Destination: ")
    qry = "INSERT INTO TRAIN VALUES({},'{}','{}','{}')".format(a,b,c,d)
    M.execute(qry)
    F.commit()


def disp():
    qry = "SELECT * FROM TRAIN"
    M.execute(qry)
    data = M.fetchall()
    if not data:
        print("No train records found.")
    else:
        for train in data:
            print(train)

def search():
    n = input("Enter a keyword to search for in Train Name: ")
    qry = "SELECT * FROM TRAIN WHERE TrainName LIKE '{}'".format(n)
    M.execute(qry)
    data = M.fetchall()
    if not data:
        print("No matching train records found.")
    else:
        for train in data:
            print(train)
print("MENU DRIVEN - train details\n")
print("1. Add Train Record")
print("2. Display Train Records")
print("3. Search for a Train")
print("4. Exit")


while True:
    print()

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_t()
    elif choice == 2:
        disp()
    elif choice == 3:
        search()
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")