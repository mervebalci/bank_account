# Creating a Bank Account
# I will create .py and .txt files for the Bank Account App.
# I will be saving the current balance of the user's bank account in this text file.


# Creating the Class
class Account:

# To create an object instance, I need to grab the "balance.txt" value and pass it to __init__ function. So I construct this minimal object.
# Because I have a txt file, I need to READ the number (the initial balance - "1000") from balance.txt file.
# And I will OPEN a filepath as txt file in READ mode.

# In this particular case, I will create an integer. So a number out of the balance.txt file.
# I will be doing file handling as using WITH method. And this is a txt file. So I will go with 'r' mode, which means READ.
# To store the value in the txt file => self.balance = file.read()
# Here, balance is the instance variable and self is account object.
# I also need to add integer function, because the balance (1000) will be read as a string by default. So I need to convert that value (1000) to an integer.
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

# Without line 19, filepath is a LOCAL variable in this __init__ function. 
# So if you comment out line 19  and run the program, it will give you an error for line 44 and 64.
# AttributeError: 'Account' object has no attribute 'filepath.
# With line 19, this local variable will become an INSTANCE variable !!!
# Here, self.filepath is instance variable and filepath is the parameter of the __init__ function which balance.txt will go to this parameter.


# WITHDRAW - DEPOSIT METHOD
# There is an initial balance that is being from txt file.
# And I want to allow the user to withdraw money from this balance.
# Once the user executes the witdrawal method, I want to update balance number inside the object instance. 
# amount is a LOCAL VARIABLE. They have the same name, but they don't have to do much with each other.
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount


# After the user withdraws or deposits money, the changes need to be written in the txt file. To do that:
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
# 'w' (WRITE) ARGUMENT MUST BE STRING, NOT INTEGER !!! Because txt file is made by string values. If it was database file, integer would be ok


# Calling an Instance (Object) of this class...
# Let's say store that in the "account" variable. So this will be the object which will be created out of the account blueprints.
# And I need to pass the parameter (balance.txt) for the "filepath" argument.
# For "self" argument, python will automatically pass the account object instance.
account = Account("balance.txt")
print(account.balance)


# Let's withdraw some money.
# Witdraw takes 2 arguments (self, amount). The object instance (self) is passed automatically and let's say, amount is 100.
account.withdraw(100)
print(account.balance)


# Let's say the user wants to add some money to the account:
account.deposit(200)
print(account.balance)


# Let's call the commit method to update and store the balance after the user witdraw or deposit some money
account.commit()