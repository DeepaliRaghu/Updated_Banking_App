import csv
import input_utility
from Bank_account_class import Customer
from Bank_account_class import BankAccount

existing_cus=Customer()


def signup_customer()->bool:
    print('Please enter the following details')
    first_name = input('Please enter your first name: ')
    last_name = input('Please enter yor last name:')
    address = input('Enter your address: ')
    try:
        phone_number = int(input('Please enter your phone number: '))
    except:
        phone_number = int(input('Please enter valid phone number, it should be only numbers: '))

    try:
        i=0
        while(i<3):
            user_name = input('Please enter your username:')
            if user_exists(user_name)==False:
                pass_word = input('Please enter your password:')
                initial_balance = int(input("Please enter initial balance"))
                with open('client_records.csv', 'a') as record:
                    record.write(f'\n{first_name}, {last_name}, {address} ,{phone_number},{user_name},{pass_word},{initial_balance}')

                print('**** Congratulations you have successfully signed up...proceed with login..**** \n')
                return True
            else:
                print('!!!! User already exists..... please select diffrant user  \n')
                i+=1
        print('!!!! 3 attempts are failed.... please be sure about your option..  \n')
        return False

    except:
        return False


def login_customer()->bool:
    print('For login please enter the following:')
    uname = input('Please enter your user name: ')
    pwd = input('Please Enter your pass word: ')
    with open('client_records.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if uname == row[-3] and pwd == row[-2]:
                print(f"Welcome {row[0]} {row[1]}")
                print('Your stored details are :', row)
                existing_cus.first_name=row[0]
                existing_cus.last_name=row[1]
                existing_cus.username=uname
                existing_cus.password=pwd
                return True
            else:
                print("Either username or password is wrong. Please enter the correct username and password\n")
        return False

def user_exists(username:str)->bool:
    try:
        with open('client_records.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[4] == username:
                    return True
        return False
    except:
        print("Error...in user exists function..")
        return True



ch=input_utility.display_start_msg()

if ch<3:
    loop = True


while loop:
    # Customer section
    if ch==1:
        ch=input_utility.display_customer_welcome_msg()
        # 1. Login
        if ch==1:
            if login_customer() == True:
                opt = input_utility.display_loggedin_customer_msg()
                existing_cus=BankAccount()
                BankAccount.load_all_accounts(existing_cus)

                # Opt 1.Create New Bank Account
                if opt == 1 :
                    #existing_cus.create_account()
                    num=int(input('Number of customers accounts:'))
                    i=0
                    while i<=num:
                        cust_acc_num = int(input('Please enter your bank account number:'))
                        acc_username = input('Please enter your username: ')
                        acc_balance = int(input('Please Enter your initial balance: '))
                        with open('Account_list.csv', 'a') as acc_list:
                            acc_list.write(f'\n{acc_username},{cust_acc_num},{acc_balance}')
                        i+=1



                # Opt 2.List Bank Accounts
                if opt == 2:
                    existing_cus=BankAccount()
                    print(BankAccount.load_all_accounts(existing_cus))


                    #existing_cus=BankAccount()


                # Opt 3.Show Balance
                if opt == 3:
                    if len(existing_cus.accounts) == 1:
                        print(existing_cus.accounts[0])

                    elif len(existing_cus.accounts) > 1:
                        acc_no = input('Please Enter your account number: ')
                        for obj in existing_cus.accounts:
                            if obj[0] == acc_no:
                                BankAccount.show_balance(obj)
                                break
                    else:
                        print("No accounts find for this user.")




                #Opt 4.Withdraw

                if opt == 4:
                    if len(existing_cus.accounts) == 1:
                        print(existing_cus.accounts[0][1])

                    elif len(existing_cus.accounts) > 1:
                        acc_no = input('Please Enter your account number: ')
                        for obj in existing_cus.accounts:
                            if obj[0] == acc_no:
                                BankAccount.withdrawl(existing_cus)
                                break
                    else:
                        print("No accounts find for this user.")



                 # Opt 5. Deposit
                if opt == 5:
                     if len(existing_cus.accounts) == 1:
                         print(existing_cus.accounts[0][1])

                     elif len(existing_cus.accounts) > 1:
                         acc_no = input('Please Enter your account number: ')
                         for obj in existing_cus.accounts:
                            if obj[0] == acc_no:
                                BankAccount.deposite(existing_cus)
                                break
                     else:
                         print("No accounts find for this user.")


                # Opt 6. Exit
                if opt == 6:
                    loop=False
                    break
            else:
                loop=False
                break

        # 2. Sign up
        if ch == 2:
            if signup_customer() == True:
                ch = input_utility.display_customer_welcome_msg()
            else:
                ch = input_utility.display_start_msg()


        # 3. Previous Menu
        if ch==3:
            ch = input_utility.display_start_msg()
            if ch==3:
                loop=False
                break

        # 4. exit
        if ch==4:
            break


    # admin section
    if ch==2:
        #existing_admin=Admin()
        ch=input_utility.display_admin_welcome_msg()

        #2.Admin Login
        if ch==1:
            User_Name=input('Please enter your username:')
            Pass_Word=input('Please enter your password: ')
            input_utility.access_customer_account()
            input_utility.edit_customer_account()
            input_utility.delete_cus_account()


    # anything greater than 2 is exit
    if ch>=3:
        break




    

