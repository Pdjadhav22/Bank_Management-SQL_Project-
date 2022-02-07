# Front page of Bank
import datetime
from bank_reg_login import reg_login

print('\n====Welcome to Bank====')
print(datetime.datetime.now().strftime("%A, %d %B %Y  ( %I:%M:%S %p %Z)"))


print('''
1. Register
2. Login
3. Exit''')
n =int(input('Enter your choice--> '))
if n in (1,2):
    reg_login(n)
 
elif n==3:
        print("Thank you!, Visit Again")
else:
    print('Please select valid option')
    import main
# import Bank_main