class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__account_balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew ₹{amount}. New balance: ₹{self.__account_balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: ₹{self.__account_balance}")

# Testing the BankAccount class
if __name__ == "__main__":
    # Creating an instance of BankAccount
    account = BankAccount("12345", "sharmila", 1000)

    # Displaying initial balance
    account.display_balance()

    # Depositing money
    account.deposit(500)

    # Withdrawing money
    account.withdraw(200)

    # Displaying updated balance
    account.display_balance()

