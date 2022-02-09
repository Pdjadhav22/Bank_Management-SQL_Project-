# Bank Menu
import pandas as pd
import datetime as dt
from bank_table_creation import Trans_ID, update_acc_balance
def Bank_Menu(n,mydb):
    cursor = mydb.cursor()
    go_on = 'y'
    while go_on == 'y':
        print('')
        print ('===Welcome to Bank Menu===')
        print ('1. Create a Bank Account--> ')
        print ('2. Withdrawl / Deposit--> ')
        print ('3. customer Details--> ')
        print ('4. Transaction Details-->  ')
        print ('5. Delete Account-->  ')
        print ('6. Quit--> ')
        n= int(input('Please Enter your choice from above Menu--> '))
        if n==1:
            acc_number = input('Please Enter your Account Number- ')
            acc_name = input('Please enter your Full Name- ')
            mob_no = input('Please enter your Mobile number- ')
            gender = input('Please enter your Gender M/F/O- ')
            cr_amt = input('Please enter your Credit amount- ')
            Trans_description = 'Account opening credit'
            trans_date = dt.datetime.now().date()
            q1 = 'insert into transaction_details values (%s,%s,%s,%s,%s,%s)'
            val= (acc_number,Trans_description,trans_date,0,cr_amt,Trans_ID())
            cursor.execute(q1,val)
            mydb.commit()
            q1 = 'insert into customer_details values (%s,%s,%s,%s,%s)'
            val= (acc_number,acc_name,mob_no,gender,cr_amt)
            cursor.execute(q1,val)
            mydb.commit()
            print('Bank account created succesfully!')
        
        elif n==2:
            print ('\n1.Withdrawl\n2.Deposit')
            sel = int(input('Please choose from above options--> '))
            acc_number = input('Please Enter your Account Number- ')
            if sel== 1:
                amt =int(input('Please enter amount to Withdrawl- '))
                # check acc_bal
                
                q1 = '''select acc_balance from customer_details
                        where acc_no = %s'''
                val = (acc_number,)
                cur = mydb.cursor()
                cur.execute(q1,val)
                curr_acc_bal = cur.fetchone()[0]
                if amt <= curr_acc_bal:
                    # record transaction in Transaction_details
                    Trans_description = input('Enter Transaction Description: ')
                    trans_date = dt.datetime.now().date()
                    q1 = 'insert into transaction_details values (%s,%s,%s,%s,%s,%s)'
                    val= (acc_number,Trans_description,trans_date,amt,0,Trans_ID())
                    cursor.execute(q1,val)
                    mydb.commit()
                    new_bal = curr_acc_bal-amt
                    update_acc_balance(new_bal,acc_number)
                    print('Withdrawl Completed')
                    print('Balance availabe = Rs.',new_bal) 
                else:
                    print('Insufficient Amount, Please try again')
            else:
                amt =int(input('Please enter amount to Deposit- '))              
                q1 = '''select acc_balance from customer_details
                        where acc_no = %s'''
                val = (acc_number,)
                cur = mydb.cursor()
                cur.execute(q1,val)
                curr_acc_bal = cur.fetchone()[0]
                # record transaction in Transaction_details
                Trans_description = input('Enter Transaction Description: ')
                trans_date = dt.datetime.now().date()
                q1 = 'insert into transaction_details values (%s,%s,%s,%s,%s,%s)'
                val= (acc_number,Trans_description,trans_date,0,amt,Trans_ID())
                cursor.execute(q1,val)
                mydb.commit()
                new_bal = curr_acc_bal+amt
                update_acc_balance(new_bal,acc_number)
                print('Deposit Completed')
                print('Balance availabe = Rs.',new_bal) 
        
        elif n==3:
            acc_number = int(input('Please Enter your Account Number- '))
            q1 = "select * from customer_details where acc_no = %s"
            val = (acc_number,)
            cursor.execute(q1,val)
            if cursor.fetchall():
                df = pd.read_sql("select * from customer_details",mydb)
                print('\n',df[df.acc_no==acc_number])
            else: 
                print()
                print('No Customer Details available, Please create Account')

        elif n==4:
            acc_number = int(input('Please Enter your Account Number- '))
            q1 = "select * from transaction_details where acc_no = %s"
            val= (acc_number,)
            cursor.execute(q1,val)
            if not cursor.fetchall():
                print('No transaction to show')
            else:
                df = pd.read_sql("select * from transaction_details",mydb)
                print('\n',df[df.acc_no==acc_number])
        
        elif n==5:
            acc_number = int(input('Please Enter your Account Number- '))
            q1 = "delete from customer_details where acc_no = %s"
            val= (acc_number,)
            cursor.execute(q1,val)
            print('Account Deleted succesfully')
        
        print ('\nDo you want to Continue?')
        go_on = input('Please enter your choice-->y/n ')
    else:
        print('Thank you Have a nice day, Visit again')
#         quit()