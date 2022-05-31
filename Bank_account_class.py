import csv


class Customer():
    accounts = []

    def __init__(self):
        pass

    def create_account(self):
        self.first_name = input('Please enter your first name: ')
        self.last_name = input('Please enter yor last name:')
        self.address = input('Enter your address: ')
        self.phone_number = int(input('Please enter your phone number: '))
        self.user_name = input('Please enter your username:')
        self.pass_word = input('Please enter your password:')
        self.initial_balance = int(input("Please enter initial balance"))
        with open('client_records.csv', 'a') as csv_files:
            csv_files.write(
                f'\n{self.first_name}, {self.last_name}, {self.address} ,{self.phone_number},{self.user_name},{self.pass_word},{self.initial_balance}')


class BankAccount(Customer):


    def __init__(self):

        self._acc_balance = int(input('Please enter your account balance:'))
        self.cust_acc_num = int(input('Please enter your account number:'))
        self.acc_username = input('Please enter your user name:')

        with open('Account_list.csv', 'w') as csv_file:
            csv_file.write(f'username,cust_acc_num,initial_balance')

        with open('Account_list.csv', 'a') as acc_list:
            acc_list.write(f'\n{self.acc_username},{self.cust_acc_num},{self._acc_balance}')

    def show_balance(self):
        print(f'Your Account No: {self.cust_acc_num}\t Balance: Euro {self._acc_balance}')

    def deposite(self):
        amount = int(input('Enter the deposite amount: '))
        if amount > 0:
            acc_balance = self._acc_balance + amount
            print(f'Transaction completed.Current Balance:Euro {acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self._acc_balance and amount > 0:
            acc_balance = self._acc_balance - amount
            print(f'Transaction completed.Current Balance:Euro {acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def payment(self):
        amount = int(input('Enter the payment amount:'))
        if amount <= self._acc_balance and amount > 0:
            acc_balance = self._acc_balance - amount
            # other.initial_balance = other.acc_balance + amount
            print(f'Transaction completed.Current Balance: Euro {self._acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def load_all_accounts(self) -> list:
        with open('Account_list.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if self.acc_username == row[0]:
                    List_bank_acc = [row[1], row[2]]
                    Customer.accounts.append(List_bank_acc)
                    print(Customer.accounts)



if __name__ == '__main__':
    '''cus_3 = BankAccount()
    # print(cus_3.crerate_account())
    print(cus_3.show_balance())
    print(cus_3.withdrawl())
    print(cus_3.deposite())
    print(cus_3.payment())
    print(cus_3.load_all_accounts())'''


