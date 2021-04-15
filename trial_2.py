import random

database = {
    9945689832: ['olu', 'felix', 'olu@felix.com', 'passwordOlu', 1]
}
#tried adding more user to dict but won't login

def init():
    print("Welcome to BankLogic")
    a_user = int(input("Do you have an account with us: 1(yes) 2(no): "))
    if a_user == 1:
        login()
    elif a_user == 2:
        register()
    else:
        print("You selected an invalid option")
        init()

def login():
    print("************* LOGIN WITH YOUR ACCOUNT NUMBER AND PASSWORD *************")
    user_account = int(input("Enter your account number: \n"))
    user_password = input("Enter your password: \n")
    for acc_num, user_details in database.items():
        if acc_num == user_account and user_details[3] == user_password:
            bank_operation(acc_num, user_details)
        else:
            print("Invalid Account Number or Password")
            login()
    

def register():
    print("************* REGISTER TO HAVE AN ACCOUNT WITH BANKLOGIC ************* ")
    first_name = input("Please enter your first name: \n")
    last_name = input("Please enter your last name: \n")
    e_mail = input("Please enter your email address: \n")
    password = input("Create your password: \n")
    balance = 0

    print()

    account_number = generate_account()
    database = {
        account_number: [first_name, last_name, e_mail, password, balance], 
        account_number: [first_name, last_name, e_mail, password, balance]
    }
    
    print("Your Account has been created")
    print("=" * 30)
    print("Your Account Number is {}".format(account_number))
    print("=" * 30)
    print("Make sure you keep it safe.")

    print()

    login()

def generate_account():
    return random.randrange(1111111111, 9999999999)

def bank_operation(user_acc, user):
    print("Welcome {} {} to our banking service".format(user[0], user[1]))
    from datetime import datetime
    print(datetime.now())
    print('Please choose one of the option available')
    print('Option 1: Withdrawal')
    print('Option 2: Deposit')
    print('Option 3: Complaint')
    print("Option 4: Log out")
    print("Option 5: Exit")
    selectedOption = int(input('Select an Option \n'))
    if(selectedOption == 1):
        withdrawal_operation(user_acc, user)
        bank_operation(user_acc, user)
    elif(selectedOption == 2):
        deposit_operation(user_acc, user)
        bank_operation(user_acc, user)
    elif (selectedOption == 3):
        complaint_operation(user)
        bank_operation(user_acc, user)
    elif(selectedOption == 4):
        logout()
    elif(selectedOption == 5):
        exit()
    else:
        print('Invalid Option, please try again')
        bank_operation(user_acc ,user)

def withdrawal_operation(acc_num, name):
    print('Welcome {} please make your withdrawal' .format(name[0]))
    acc_bal = name[4]
    withdrawal = int(input('How much do you want withdraw \n'))
    if withdrawal < acc_bal:
        print('Withdrawal Successful')
        print('Take your cash')
        print("You made a withdrawal of {}".format(withdrawal))
        current_bal = acc_bal - withdrawal
        print('your current balance is {}'.format(current_bal))
        name[4] = current_bal
        database[acc_num] = name[4]
        print()
    else:
        print('Insuffient Funds')
        print('your current balance is {}'.format(acc_bal))
        print()
    # return bank_operation(user)

def deposit_operation(acc_num, name):
    print('Welcome{} please make your cash deposit'.format(name[0]))
    bal = name[4]
    deposit = int(input('How much do you want to deposit \n'))
    current_bal = bal + deposit
    print('your current balance is {0}'.format(current_bal))
    name[4] = current_bal
    database[acc_num] = name[4]
    print()

def complaint_operation(name):
    complaint = input('What issue will you like to report {}? \n'.format(name[0]))
    print()
    print(complaint)
    print('Thank you for contacting us')
    print()


def logout():
    login()



####  SYSTEM INITIALISATION #####
init()
