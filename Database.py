import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate
# from datetime import datetime
import datetime

def addplayers():
    global cur
    row = {}
    print("Enter the new player's details: ")

    row["ID"] = input("Player ID: ")
    row["PlayerType"] = input("Player Type: ")
    row["PlayerName"] = input("Player Name: ")
    row["Age"] = int(input("Age: "))
    row["DOB"] = input("DOB (YYYY-MM-DD): ")
    row["Country"] = input("Country: ")
    row["Experience"] = int(input("Experience: "))
    row["Achievements"] = input("Achievements: ")
    
    try:
        query = "INSERT INTO Players(ID, PlayerType,PlayerName,Age, DOB,Country,Experience,Achievements) VALUES('%s', '%s', '%s', '%d','%s', '%s', '%s', '%s')" % (
            row["ID"], row["PlayerType"],row["PlayerName"],  row["Age"], row["DOB"],row["Country"],row["Experience"],row["Achievements"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return


def addmatches():
    global cur
    row = {}
    print("Enter the new matches's details: ")

    row["match_number"] = int(input("match number: "))
    row["teamname"] = input("team name: ")
    row["match_time"] = input("match time: ")
    row["Venue"] = (input("venue: "))
    row["DateofMatch"] = input("Date of match: ")
    
    
    try:
        query = "INSERT INTO MATCHES(Match_number, team_name,Match_Time,Venue,date_of_match) VALUES('%d', '%s', '%s', '%s','%s')" % (
            row["match_number"],row["teamname"],row["match_time"],  row["Venue"],row["DateofMatch"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return

def addcommentators():
    global cur
    row = {}
    print("Enter the new cheer girl's details: ")

    row["ID"] = int(input("ID: "))
    row["name"] = input("name: ")
    row["Language"] = input("Language: ")
    row["Country"] = input("Country: ")
    row["Experience"] = input("Experience: ")
    row["Qualification"] = input("Qualification: ")
    
    try:
        query = "INSERT INTO Commentators(ID, name,Language,Country,Experience,Qualification) VALUES('%d', '%s', '%s', '%s','%s','%s')" % (
            row["ID"],row["name"],row["Language"],row["Country"] ,row["Experience"],row["Qualification"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    return
def updateplayer():
    global cur
    row = {}
    print("Enter the Player's new details: ")
    row["ID"] = int(input("ID: "))
    row["playerName"] = input("Playername: ")

    try:
        query = "UPDATE Players SET PlayerName='%s' WHERE ID=%d" % (
            row["playerName"], row["ID"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("Please try with different data")
        return
    return

def updatematches():
    global cur
    row = {}
    print("Enter the match's new details: ")
    row["ID"] = int(input("match number: "))
    row["teamName"] = input("team name: ")

    try:
        query = "UPDATE MATCHES SET team_name='%s' WHERE Match_number=%d" % (
            row["teamName"], row["ID"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("Please try with different data")
        return
    return

def updateCommentators():
    global cur
    row = {}
    print("Enter the Commentators's new details: ")
    row["ID"] = int(input("ID: "))
    row["CommentatorsName"] = input("Commentators name: ")

    try:
        query = "UPDATE Players SET PlayerName='%s' WHERE ID=%d" % (
            row["CommentatorsName"], row["ID"])
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("Please try with different data")
        return
    return

def options():
    print("Choose an option\n")
    print("1. Players")
    print("2. MATCHES")
    print("3. Commentators")
    print("\n")
    print("Please enter your choice: ")

def viewTable(rows):

    a = []
    try:
        a.append(list(rows[0].keys()))
    except:
        print("\n-----------------\nEMPTY TABLE\n-----------------\n")   
        return
    for row in rows:
        b = []
        for k in row.keys():
            b.append(row[k])
        a.append(b)
    print(tabulate(a, tablefmt="psql", headers="firstrow"))
    print()
    return

def Queriesoptions():
    options()
    n=input()
    if n == '1':
        query = "SELECT * FROM Players;"
    elif n == '2':
        query = "SELECT * FROM MATCHES;"
    elif n == '3':
        query = "SELECT * FROM Commentators;"
    try:
        no_of_rows = cur.execute(query)
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return
    rows = cur.fetchall()
    viewTable(rows)
    con.commit()


def Deleteoptions():
    options()
    n = input()
    if(n=='1'):
        a=input("Enter player ID")
        query = "DELETE FROM Players WHERE ID='%s';" % (a)
    elif(n=='2'):
        a=input("Enter Match number")
        query = "DELETE FROM MATCHES WHERE match_number='%s';" % (a)
    elif(n=='3'):
        a=input("Enter commentators ID")
        query = "DELETE FROM Commentators WHERE ID='%s';" % (a)
    try:
        cur.execute(query)
        con.commit()
    except Exception as e:
        print(e)
        print("\n\nError: PLEASE TRY AGAIN WITH DIFFERENT DATA!\n")
        return

def Updateoptions():
    options()
    n = input()
    if(n=='1'):
        updateplayer()
    elif(n=='2'):
        updatematches()
    elif(n=='3'):
        updateCommentators()


def addOptions():
    
    options()
    n = input()
    if n == '1':
        addplayers()
    elif n=='2':
        addmatches()
    elif n=='3':
        addcommentators()

while(1):
    tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")
    # username="tanvi"
    # password="password"

    try:
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='SPL',
                              cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        print(e)
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
        continue

    with con:
        cur = con.cursor()
        exitflag = 0
        while(1):
            tmp = sp.call('clear', shell=True)

            print("1.Update")
           
            print("2.Insert")
           
            print("3.Delete")

            print("4.Queries")

            print("5.exit")

            print("CHOOSE AN OPTION: ")
            inp = input(" ")
            print("\n")
            if(inp=='1'):
                Updateoptions()
            elif(inp == '2'):
                addOptions()
            elif(inp=='3'):
                Deleteoptions()
            elif(inp == '4'):
                Queriesoptions()
            elif(inp == '5'):
                    exitflag = 1
                    print("Bye")
                    break
            print("Press enter to continue ... ")
            x=input()

    if exitflag == 1:
        break
