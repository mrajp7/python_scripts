'''

For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

'''


class Account():

    def __init__(self, name, initial_balance):
        '''
        Initiates an instance of Account.

        name: the owner of the Account holder.
        initial_balance: the initial balance for the account holder to have
        '''

        self.owner = name
        self.balance = initial_balance

    def deposit(self, amount):
        '''
        To deposit funds in to the bank account of the holder

        amount: value to add up to the account
        '''

        self.balance += amount
        return "Funds deposited successfully!"

    def withdraw(self, amount):
        '''
        To withdraw funds from the bank account of the holder
        withdraw will allowed only if the request funds are available in balance [i.e., withdraw_amount > balance]

        amount: value to withdraw from the account
        '''

        if(self.balance < amount):
            return "Insufficient funds!"

        self.balance -= amount
        return "Funds withdrawn successfully!"

    def __str__(self):
        '''
        When called it returns the account details
        '''
        return f"Account owner:{self.owner:>9}\nAccount balance:{self.balance:6}$"


# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
print(acct1.deposit(50))
print(acct1.withdraw(75))
print(acct1)

# 6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500))
