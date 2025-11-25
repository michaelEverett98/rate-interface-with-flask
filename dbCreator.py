import mysql.connector

# mycursor.execute("DROP DATABASE ratedbV2")

# mycursor.execute("CREATE DATABASE ratedbV2")

# So I can select/delete DB immediately

# mysql.connector.cursor_cext.CMySQLCursorBuffered

mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '')
#mycursor = mysql.connector.cursor_cext.CMySQLCursorBuffered
mycursor = mydb.cursor(buffered = True)

from datetime import date
datetest = date.today()#.strftime('%Y-%m-%d')
print(datetest)
print(type(datetest))
# %H:%M:%S


# ==================================================
#               Menu options
# ==================================================

def selectTestDB() :

    global mydb
    mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = '', database = 'ratedbV2')
    global mycursor
    mycursor = mydb.cursor(buffered = True)
    print(mycursor)
    print(type(mycursor))
    #return mycursor

def deleteTestDB() :

    mycursor.execute("DROP DATABASE ratedbV2")

def createTestDB() :

    mycursor.execute("CREATE DATABASE ratedbV2")

# ==================================================
#               Tables Creator
# ==================================================

def createUsersTable() :

    # Table creation
    mycursor.execute("CREATE TABLE users (username VARCHAR(255), password VARCHAR(255), email VARCHAR(255), user_type CHAR(5), registration_date DATE, uuid INT AUTO_INCREMENT PRIMARY KEY)")

# ==================================================
#               Entry creators
# ==================================================

def insertUser() :

    username = str(input("Enter a username: "))
    password = str(input("Enter a password: "))
    email = str(input("Enter your email: "))
    userType = "rater"
    registrationDate = datetest

    # Populate table with dummy entries
    #sql = f"INSERT INTO users (username, password, email, user_type, registration_date) VALUES ({username}, {password}, {email}, {userType}, {registrationDate})"

    sql = "INSERT INTO users (username, password, email, user_type, registration_date) VALUES (%s, %s, %s, %s, %s)"
    val = [
        (username, password, email, userType, registrationDate)
    ]

    mycursor.executemany(sql, val)
    mydb.commit()

    print("User inserted")
    mycursor.execute(f"SELECT * FROM users")
    for x in mycursor :
        print(x)
        print(type(x[4]))


# ==================================================
#               Menu Options Loop
# ==================================================

# def tablesMenu() :

dbOptions = ()
dbFunctions = ["Exit", "Create test DB", "Delete test DB", "Select test DB", "Create users table", "Insert user"]

def dbManage() :
    for i in range(len(dbFunctions)) :
        print(i, dbFunctions[i])
    return

def manageFunction() :

    dbOptions = ()

    while dbOptions != 0 :

        dbManage()
        dbOptions = int(input(f"{30 * "-"}\nChoose option: "))
        #print(mycursor)

        if dbOptions == 0 :
            print("Exit")

        elif dbOptions == 1 :
            createTestDB()

        elif dbOptions == 2 :
            deleteTestDB()

        elif dbOptions == 3 :
            selectTestDB()

        elif dbOptions == 4 :
         #   tablesMenu()
            createUsersTable()

        elif dbOptions == 5 :
            insertUser()

        else :
            dbOptions = int(input(f"{30 * "-"}\nPlease select a valid option: "))

    dbOptions = ()

manageFunction()