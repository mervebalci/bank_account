# Transfering Money from One Bank Account to Another Bank Account
# To do that, I would have to add a Transfer Method.
# As far as I know you can transfer money from your checking account, but not from your saving account.
# So Transfer Method wouldn't make sense for checking account.
# There is a better solution which is INHERITANCE (deriving a class out of a base class)


class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
# In line 11, "filepath" is Instance Variable. These variables are defined inside the methods of the class.

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


# INHERITANCE: creating a subclass out of a base class
# This subclass shares the methods of the base class plus it has its own methods that are specific to that subclass.

# Creating a new class: Account is the BASE class and this new class Checking is the SUBCLASS.
# And then passing a doc string. doc string("""   """) is used to provide some information about that class
class Checking(Account):
    """This class generates checking account objects"""

# Creating a CLASS VARIABLE. This also is a DATA MEMBER
# Class variable is declared outside of the methods of that class.
# And class variables are shared by all the instances of a class. So instance variables are shared by only the object instance.
    type = "checking"


# Creating an init method which is the CONSTRUCTOR and then in this init method calling the init function of the Account class
# So, when I create an object instance of the Checking class, this method will be executed.
# This method executes the init function of the Account method (which I am calling the line 10).

# Let's say this tranfer also comes with some transfer fee. So this fee should be given as a parameter.
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee
# self.fee=fee is a DATA MEMBER


# Transfer Method is a class method. init method is also a class method but it is a special method. So it is called constructor
# CLASS METHODS that is applied to the OBJECT INSTANCE
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


# INSTANTIATION is the process of creating object instances
# Creating INSTANCE OBJECT which is line 61
# A Checking account object that stores data in this "karen.txt" file path and it also has an attribute which is fee (1).
karen_checking = Checking("karen.txt", 1)
karen_checking.deposit(10)
karen_checking.transfer(200)
print(karen_checking.balance)

# To SAVE/STORE the changes in bank account which is karen.txt
karen_checking.commit()

# The class variable (which is type="checking") is shared by all the instances of that class.
print(karen_checking.type)



# Creating another INSTANCE OBJECT which is line 75
marvin_checking = Checking("marvin.txt", 1)
marvin_checking.deposit(10)
marvin_checking.transfer(200)
print(marvin_checking.balance)
marvin_checking.commit()
print(marvin_checking.type)

# To see the info about the class
print(marvin_checking.__doc__)