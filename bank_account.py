class BankAccount:

    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate    
        self.balance = balance

    # Deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.amount= amount
        self.balance += amount
        return self

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not 
    # enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        self.amount = amount

        # conditional to check if the balance is greater than the amount requested, if so, continue, if not
        # print message
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Unable to proceed, The balance is lower than the requested withdrawal amount. ")
        return self
    
    #  display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"The current balance is ${self.balance}")
        return self
    
    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            # Using PEMDAS to prioritize floating pount number interest and multiply it by balance to output
            # total interest being collected per deposited funds. 
            self.int_rate = ( self.int_rate / 100) * self.balance
            self.balance += self.int_rate
            print(f"Your new balance is {self.balance} after a ${self.int_rate} interest rate applied. ")
        else:
            print("No interest can be applied to your account until new funds are deposited. ")
        return self
    
#Create 2 accounts
user1 = BankAccount(5, 30_000)
user2 = BankAccount(5, 10_000)

#To the first account, make 3 deposits and 1 withdrawal, then yield interest and display 
# the account's info all in one line of code (i.e. chaining)
user1.deposit(1000).deposit(5000).deposit(4000).withdraw(5000).yield_interest().display_account_info()
print("\n")

#To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's 
# info all in one line of code (i.e. chaining)
user2.deposit(10000).deposit(10000).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()
print("\n")
