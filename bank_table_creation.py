# DB & user_info table creation
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
acc_name varchar(50), 
trans_date date, 
withdrawl_amt bigint(10), 
deposit_amt bigint(10)
)'''
cursor.execute(q1)