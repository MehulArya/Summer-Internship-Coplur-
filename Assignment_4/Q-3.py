import sqlite3 as sql

conn = sql.connect("db1.db")  # 1. Create Database

def createTable(table_name):  # 2. Create 2-3 tables
    conn.execute(f'''
    Create table {table_name}(
    userid INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(100),
    password VARCHAR(50),
    mobile_number VARCHAR(50)
    )
    ''')
    conn.commit()

def insertData(table_name):  # 3. Insert some Records
    username = input("Enter User Name: ")
    password = input("Enter Your Password: ")
    mobile_number = input("Enter Your Mobile Number: ")
    conn.execute(f'''
    INSERT INTO {table_name}("username", "password", "mobile_number") VALUES("{username}", "{password}", "{mobile_number}")
    ''')
    conn.commit()

def showData(table_name):  # 4. Perform Different Select Operations
    ch = input('''
    Enter Your choice:
    1. Show All Columns
    2. Show Specefic Columns
    choice =   
    ''')
    if ch == "1":
        data = conn.execute(f'''
        SELECT * FROM {table_name}
        ''')
        for i in data:
            print(i)
    elif ch == "2":
        specify = input("Enter the specefic column name to find in this table: ")
        data = conn.execute(f'''
        SELECT {specify} FROM {table_name}
        ''')
        for i in data:
            print(i)
    else:
        print("Wrong Choice")

def updateData(table_name):  # 5. Update Some Data
    col_to_upd = input("Enter the column to Update: ")
    val_to_upd = input("Enter the value to Update: ")
    upd_at_id = input("Enter ID to update the value at: ")
    conn.execute(f"UPDATE {table_name} set {col_to_upd} = '{val_to_upd}' where userid = {upd_at_id}")
    conn.commit()

def deleteData(table_name):  # 6. Delete Some Data
    id = input("ID to delete: ")
    conn.execute(f"DELETE FROM {table_name} WHERE userid = {id}")
    conn.commit()

table_name = input("Enter the Table name to perform operations or name a table you would create: ")
ch = input('''
     Enter Your Choice of Operation:
     1. Create Table
     2. Insert Data
     3. Show Data
     4. Update Data
     5. Delete Data
     Enter Choice = 
     ''')

if ch == "1":
    createTable(table_name)
elif ch == "2":
    insertData(table_name)
elif ch == "3":
    showData(table_name)
elif ch == "4":
    updateData(table_name)
elif ch == "5":
    deleteData(table_name)
else:
    print("Invalid Choice")

conn.close()