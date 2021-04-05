print('Welcome to Logic ATM services')
condition = 'Yes'
while(condition == 'Yes'):
    name = input('What is your name \n')
    allowedUser =['Olu', 'Gemma', 'Damo']
    allowedPassword = ['passwordOlu', 'passwordGemma', 'passwordDamo']
    if (name in allowedUser):
        password = input('Enter your password \n')
        userID = allowedUser.index(name)
        if(password == allowedPassword[userID]):
            from datetime import datetime
            print(datetime.now())
            print('Welcome ' + name +' to our ATM service')
            print('Please choose one of the option available')
            print('Option 1: Withdrawal')
            print('Option 2: Deposit')
            print('Option 3: Complaint')
            print('Option 4: Balance Enquiry')
            currentBal = [200, 450, 50]
            selectedOption = int(input('Select an Option \n'))
            if(selectedOption == 1):
                print('Welcome {0} please make your withdrawal' .format(name))
                withdrawal = int(input('How much do you want withdraw \n'))
                if(withdrawal <= currentBal[userID]):
                    print('Withdrawal Successful')
                    print('Take your cash')
                    currentBal[userID] -= withdrawal
                    print('your current balance is {0}'.format(currentBal[userID]))
                    condition = input('Do you want to continue? Yes/No \n')
                else:
                    print('Insuffient Funds')
                    condition = input('Do you want to continue? Yes/No \n')
            elif(selectedOption == 2):
                print('Welcome {0} please make your cash deposit' .format(name))
                deposit = int(input('How much do you want to deposit \n'))
                currentBal[userID] += deposit
                print('your current balance is {0}'.format(currentBal[userID]))
                condition = input('Do you want to continue? Yes/No \n')
            elif (selectedOption == 3):
                complaint = input('What issue will you like to report? \n')
                print('Thank you for contacting us')
                condition = input('Do you want to continue? Yes/No \n')
            elif(selectedOption == 4):
                print('Welcome {0}' .format(name))
                print('your current balance is {0}'.format(currentBal[userID]))
                condition = input('Do you want to continue? Yes/No \n')
             
                condition = input('Do you want to continue? Yes/No \n')
        else:
            print('Incorrect Password, please try again')
            condition = input('Do you want to continue? Yes/No \n')
    else:
        print('Name not register, please try again')
        condition = input('Do you want to continue? Yes/No \n')
print('Thank You for Banking with us')

