# Register / Login Page

import mysql.connector as connection
from bank_menu import Bank_Menu

# Connecting to MYSQLdatabase
try:
    mydb = connection.connect(host='localhost',user='root',passwd='datascience',
    database = 'bank',use_pure=True)   
    cursor = mydb.cursor()

except Exception as e:
    mydb.close()
    print(str(e))


def reg_login(n):
    if n == 1:
        try:
            user_id = input('Enter user ID--> ')
            paswrd = input('Enter Password--> ')
            q1 = "insert into bank_user_info values (%s, %s)"
            val = (user_id,paswrd)
            cursor.execute(q1,val)
            mydb.commit()
            print('User Created-', user_id)
        except:
            print('\nUser Already Registered, Please Login')
        import main
    elif n==2:
        user_id = input('Enter user ID--> ')
        q1 = 'select * from bank_user_info where user_id="'+ user_id +'" '
        cursor.execute(q1)
        if cursor.fetchone():
            paswrd = input('Enter Password--> ')
            q1 = 'select * from bank_user_info where user_id="'+ user_id +'" and paswrd = "'+ paswrd +'" '
            cursor.execute(q1)
            if cursor.fetchone() is None:
                print('\nInvalid userId or Password\nPlease Try Again')
            else:
                Bank_Menu(n,mydb)
        else: print('User do not Exist, please register')