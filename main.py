import sqlite3
conn = sqlite3.connect('main.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS name(name TEXT)')
create_table()
def updating_table():
    while True:
        name1 = input("Enter one name:  ")
                    
        print("You entered: " + name1)
        continu_e = input("Do you want to enter another name? Kindly choose Yes(Y) or no(N)? ")
        if continu_e == "Y" or continu_e == "y":
            continue
        elif continu_e == "N" or continu_e == "n":
            print("Thank you.")
#            print("You did not chose an option above!")
            c.execute("INSERT INTO name(name) VALUES(?)",(name1,))
            conn.commit()
            print("Prossed nicely")
            break
updating_table()
def reading_table():
    c.execute('SELECT * FROM name')
    data = c.fetchall()
    for kol in data:
        print(kol)
reading_table()