import csv



def display_start_msg()->int:
    print('Welcome to Commerce Bank')
    print("Who are you? Please select one of the following options:\n 1. Customer\n 2. Admin \n 3. Exit\n Please select the option number:")
    ch = int(input('select the option number:'))
    return ch


def display_customer_welcome_msg() -> int:
    print('Welcome to customer Area: Choose from the below optios:\n1.Login\n2.signup\n3.Previous Menu\n4.exit.')
    ch = int(input('Please enter the number of your option:'))
    return ch


def display_loggedin_customer_msg() -> int:
    print('\n1.Create New Bank Account\n2.List Bank Accounts\n3.Show Balance\n4.Withdraw \n5. Deposit \n6. Exit')
    ch = int(input('Please enter the number of your option:'))
    return ch

def display_admin_welcome_msg() -> int:
    print('Welcome to Admin Area: Choose from the below optios:\n1.Login\n2.Previous Menu\n3.exit.')
    ch = int(input('Please enter the number of your option:'))
    return ch



def access_customer_account()->list:
    cus_first_name=input('Please enter the first name of the customer: ')
    cus_last_name=input('Please enter the last name of the customer:')
    cus_acc_num=input('Please enter customer account number:')
    cus_username=input('Please enter customer user name:')

    with open('client_records.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if cus_first_name==row[0] and cus_username==row[4] :
                print(row)

    ''' with open('Account_list.csv','r') as csv_file:
            csv_reader=csv.reader(csv_file)
            for row in csv_reader:
                if row[0]==cus_username and row[1]==cus_acc_num:
                 return row'''


def edit_customer_account():
        cus_first_name=input('Please enter the name of the customer: ')
        cus_username=input('Please enter the user name of the customer:')

        print(input('Please select the options number:\n1.Change phone number\n2.Change Address\n3.Change password'))
        opt=int(input('Please enter the number of your option'))



        with open('client_records.csv','r') as csv_file_1:
            csv_reader=csv.reader(csv_file_1)
            Found=False
            m1=[]
            for row in csv_reader:
                if row[0]==cus_first_name and row[4]==cus_username:
                #1.Change phone number:
                    if opt==1:
                      row[3]=int(input('Please enter new number'))
                      print(row)
                      Found==True
                    m1.append(row)


                    with open('client_records.csv','a') as csv_file_2:
                         writer=csv.writer(csv_file_2)
                         writer.writerow(m1)

                #2.Change Address
                    if opt==2:
                       row[2]=input('Please enter the new address:')
                       print(row)
                       Found=True
                       m1.append(row)
                       t=(','.join(m1))
                    '''if Found == True:
                      print('Data did not find')'''

                   # else:
                    with open('client_records.csv', 'a') as csv_file_3:
                               writer=csv.writer(csv_file_3)
                               writer.writerow(m1)

                #3.Change password

                    if opt==3:
                       row[5]=input('Please enter the new password:')
                       print(row)
                       Found=True
                       m1.append(row)


                    '''if Found == True:
                           print('Data did not find')

                    else:'''

                    with open('client_records.csv', 'a') as csv_file_4:
                              writer=csv.writer(csv_file_4)
                              writer.writerow(m1)


def delete_cus_account():
         cus_first_name=input("please enter customer first name:")
         cus_username=input('Please enter customer last name:')
         with open('client_records.csv','r') as csv_file_5:
             csv_reader=csv.reader(csv_file_5)
             m1=[]
             Found=False
             for row in csv_reader:
                  if row[0] != cus_first_name and row[4] != cus_username:
                     m1.append(row)


                  else:
                      Found==True

             '''if Found == True :
                   print('Data did not find')
             else:'''
             with open('client_records.csv', 'w') as csv_file_6:
                      writer=csv.writer(csv_file_6)
                      writer.writerow(m1)



print(access_customer_account())
print(edit_customer_account())
print(edit_customer_account())


