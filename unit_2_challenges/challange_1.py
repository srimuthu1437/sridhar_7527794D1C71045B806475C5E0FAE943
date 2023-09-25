class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount}. New balance: {self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__account_balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print("Account balance for ",self.__account_holder_name,":",self.__account_balance)

# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    my_account = BankAccount("1234567890", "sridhar", 1000)
    
    my_account.display_balance()
    # Make a deposit
    my_account.deposit(500)

    # Make a withdrawal
    my_account.withdraw(200)

    # Attempt to withdraw more than the balance
    my_account.withdraw(10)

 
