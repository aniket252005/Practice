class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Please Deposit more than 0 Rupees")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Please Withdraw more than 0 Rupees")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def show_balance(self):
        print(f"Current Balance: ₹{self.balance}")


# Create an object
account = BankAccount()

# Call methods
account.deposit(1000)
account.withdraw(250)
account.show_balance()