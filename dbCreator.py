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

#menuType = []

# ==================================================
#               Miscellanous functions
# ==================================================

# Iterates through an array of menu options
def menuIterator(menuOptions) :

    for i in range(len(menuOptions)) :

        print(i, menuOptions[i])

    return

# Simple but necessary for storing functions in array
def printExit() :

    print("Exit")

# ==================================================
#               Menu options
# ==================================================

def selectTestDB() :

    global mydb
    mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'HwangYeji72', database = 'ratedbV2')
    global mycursor
    mycursor = mydb.cursor(buffered = True)
    #print(mycursor)
    #print(type(mycursor))
    print("Test rate selected, choose action")
    #return mycursor

def deleteTestDB() :

    mycursor.execute("DROP DATABASE ratedbV2")
    print("Test database deleted")

def createTestDB() :

    mycursor.execute("CREATE DATABASE ratedbV2")
    print("New test database created")

# ==================================================
#               Tables Creator
# ==================================================

def createUsersTable() :

    # Table creation
    # CHANGE user type to ENUM
    mycursor.execute("CREATE TABLE users (username VARCHAR(255), password VARCHAR(255), email VARCHAR(255), user_type CHAR(5), registration_date DATE, uuid INT AUTO_INCREMENT PRIMARY KEY)")
    print("Users table created")

def createHostsTable() :
    mycursor.execute("CREATE TABLE hosts (uuid INT, rate_id INT, lead_host BOOL)")
    print("Hosts table created")

# DECIDE: song IDs with a table entry for every single song? or load it all into a JSON file
def createUserScoresTable() :
    # mycursor.execute("CREATE TABLE user_scores (rate_id INT PRIMARY KEY, uuid INT, scores JSON, comments JSON)")
    mycursor.execute("CREATE TABLE user_scores (song_id INT PRIMARY KEY, uuid INT, scores DECIMAL(3, 1), comments VARCHAR(255))")
    print("User scores table created")

def createRatesTable() :

    # change rateimage to some kind of binary type to internally store image rather than a varchar link
    # songlist JSON?
    mycursor.execute("CREATE TABLE rates (rate_id INT PRIMARY KEY, rate_name VARCHAR(510), rate_image VARCHAR(255), start_date DATE, reveal_date DATE)")
    print("Rates table created")

def createSongsTable() :

    # JSON file for artist features?
    mycursor.execute("CREATE TABLE songs (song_id INT AUTO_INCREMENT PRIMARY KEY, song_name VARCHAR(510), artist_id INT, rate_id INT, bonus BOOLEAN, placement INT(3), average DECIMAL (4, 3), controversy DECIMAL (4, 3))")
    print("Songs table created")

def createArtistsTable() :

    # company to ENUM?
    # gender to ENUM?
    mycursor.execute("CREATE TABLE artists (artist_id INT AUTO_INCREMENT PRIMARY KEY, artist_name VARCHAR(255), company VARCHAR(255), list_of_rates VARCHAR(255), soloist BOOLEAN, gender CHAR(1))")#, group BOOLEAN, gender CHAR(1))")
    print("Artists table created")

# ==================================================
#               Entry creators
# ==================================================

def insertUser() :

    username = str(input("Enter a username: "))
    password = str(input("Enter a password: "))
    email = str(input("Enter your email: "))
    userType = "rater" # use ENUM data type??
    registrationDate = datetest

    # Populate table with dummy entries
    #sql = f"INSERT INTO users (username, password, email, user_type, registration_date) VALUES ({username}, {password}, {email}, {userType}, {registrationDate})"

    sql = "INSERT INTO users (username, password, email, user_type, registration_date) VALUES (%s, %s, %s, %s, %s)"
    val = [
        (username, password, email, userType, registrationDate)
    ]

    mycursor.executemany(sql, val)
    mydb.commit()

    print("New user inserted")

    '''mycursor.execute(f"SELECT * FROM users")
    for x in mycursor :
        print(x)
        print(type(x[4]))'''
    
# ==================================================
#               Table Creation Menu
# ==================================================

createTablesList = ["Return", "Create users table", "Create hosts table", "Create user scores table", "Create rates table", "Create songs table", "Create artists table"]

#createTableFunctions = [manageFunction, createUsersTable, createHostsTable, createUserScoresTable, createRatesTable, createSongsTable, createArtistsTable]

def showTablesMenu() :

    manageFunction(createTablesList, createTableFunctions)


# ==================================================
#               Menu Options Loop
# ==================================================

# def tablesMenu() :

#menuOptionSelector = () # do I need this?
dbFunctions = ["Exit", "Create test DB", "Delete test DB", "Select test DB", "Open table creation menu", "Insert user"]

# DONE: Create a function that iterates through all the menu functions? i.e. instead of making new function for each menu, create array with functions list

def manageFunction(menuType, menuFunctionsArray) :

    menuOptionSelector = ()

    while menuOptionSelector != 0 :

        menuIterator(menuType) # menuType is the array containing the menu option strings
        menuOptionSelector = int(input(f"{30 * "-"}\nChoose option: "))

        if menuOptionSelector in range(len(menuType)) :

            #if menuOptionSelector == 0 :

                #menuFunctionsArray[menuOptionSelector]("Exit")

            #else :

                menuFunctionsArray[menuOptionSelector]()
        
        else :
            print("Error")

# ==================================================
#               Menus
# ==================================================

def mainMenu() :

    manageFunction(dbFunctions, initialMenuFunctions)

# ==================================================
#               Menu function arrays
# ==================================================

createTableFunctions = [mainMenu, createUsersTable, createHostsTable, createUserScoresTable, createRatesTable, createSongsTable, createArtistsTable]

initialMenuFunctions = [printExit, createTestDB, deleteTestDB, selectTestDB, showTablesMenu, insertUser]

# ==================================================
#               INITIAL MENU BOOTUP
# ==================================================

mainMenu()