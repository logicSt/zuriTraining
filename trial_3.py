class Budget:

    Budget_bal = [0,0,0]
    # food = 0
    # clothing = 1
    # entertainment = 2
    Budgets = ["food", "clothing", "entertainment"]

    def __init__(self, category ):
        # self.food = food
        # self.clothing = clothing
        # self.entertainment = entertainment
        self.category = category - 1

    def activity(self):
        print("What would you like to do?: ")
        print(f"1. Deposit to {self.Budgets[self.category]} Budget")
        print(f"2. Witdraw from {self.Budgets[self.category]} Budget")
        print(f"3. Check balance of {self.Budgets[self.category]} Budget")
        print("4. Transfer to another Budget")

        options = int(input("Please select from the options above: \n"))

        if options == 1:
            self.deposit()
        
        elif options == 2:
            self.withdraw()

        elif options == 3:
            self.balance()

        elif options == 4:
            self.transfer() 

        else:
            print("Invalid options selected")

    def deposit(self):
        amount = int(input('How much do you want to deposit: \n'))
        self.Budget_bal[self.category] += amount
        print("Transaction Completed!")
        pass
    
    def withdraw(self):
        amount = int(input("How much do you want withdraw:\n"))
        if self.Budget_bal[self.category] != 0 or amount < self.Budget_bal[self.category]:
            self.Budget_bal[self.category] -= amount
            print('Withdrawal Successful')

        else:
            print("Insufficient funds")

    def balance(self):
        print(f"You have {self.Budget_bal[self.category]} in your {self.Budgets[self.category]} Budget")

    def transfer(self):
        print("1: Food")
        print("2: Clothing")
        print("3: Entertainment")

        choice = int(input("Please choose a budget to transfer to: \n"))

        if choice <= 3:
            choice -= 1

            amount = int(input("How much do you want to transfer: \n"))

            if choice == self.category:
                print("Same category selected")
            
            elif self.Budget_bal[choice] != 0 or amount < self.Budget_bal[choice]:
                print(f"The amount of {amount} has been transferred from your {self.Budgets[choice]} to {self.Budgets[self.category - 1]}")
                self.Budget_bal[choice] -= amount
                self.Budget_bal[self.category -1] += amount
            
            else:
                print("Insufficient Funds")
        
        else:
            print("Invalid Selection")
        
def init():
    print("Welcome to the Budget App") 
    print("Please select from the categories below")
    print("1: Food")
    print("2: Clothing")
    print("3: Entertainment")

    choice = int(input("Please choose a budget to transfer to: \n"))

    if choice == 1:
        food = Budget(1)
        food.activity()

    elif choice == 2:
        clothing = Budget(2)
        clothing.activity()
    
    elif choice == 3:
        entertainment = Budget(3)
        entertainment.activity()

    else:
        print("Invalid option choosen")


init()

