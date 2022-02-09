# DB & user_info table creation

# Connecting to DB
import mysql.connector as connection

# Connecting to MYSQLdatabase
try:
    mydb = connection.connect(host='localhost',user='root',passwd='datascience',
    database = 'bank',use_pure=True)   
    cursor = mydb.cursor()

except Exception as e:
    mydb.close()
    print(str(e))

cursor.execute('create database if not exists Bank')
cursor.execute('use Bank')
# cursor.execute('drop table bank_user_info')
cursor.execute('''create table if not exists Bank_user_info(
    user_id varchar(50) primary key, 
    paswrd varchar(20) not null)''')

# Customer details Table
# cursor.execute('drop table if exists customer_details')
q1 = '''create table if not exists customer_details (
acc_no int primary key, 
acc_name varchar(50),
mob_no bigint(10) check(length(mob_no)=10) not null,
Gender varchar(1),
Cr_amt bigint(25)
)'''
cursor.execute(q1)

# Create Transaction table
q1 = '''create table if not exists transaction_details(
acc_no int primary key, 
Trans_description varchar(50), 
trans_date date, 
withdrawl_amt bigint(10), 
acc_balance bigint(10)
)'''
cursor.execute(q1)

# Creating function for trans_id generation
def Trans_ID():
    trans_id_lst = []
    q1= 'select Trans_ID from transaction_details'
    cursor.execute(q1)
    for i in cursor.fetchall():
        trans_id_lst.append(i[0])

    import random
    trans_id = random.randint(1111, 9999)
    while trans_id in trans_id_lst:
        trans_id = random.randint(1111, 9999)
    else: return trans_id

def update_acc_balance(new_bal,acc_number):
    q1 = '''
    update customer_details
    set acc_balance = %s
    where acc_no = %s
    '''
    val = (new_bal,acc_number)
    cursor.execute(q1,val)
    mydb.commit()

