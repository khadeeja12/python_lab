class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance is ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance is ${self.balance}")
        else:
            print("Insufficient amount")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = 0.05  

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added. Current balance is ${self.balance}")


class CurrentAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=1000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance is ${self.balance}")
        else:
            print("Withdrawal amount exceeds overdraft limit")



    
savings = SavingsAccount(1000)
savings.display_balance()
savings.deposit(500)
savings.add_interest()
savings.withdraw(2000)
savings.withdraw(1500)
savings.display_balance()

print("\n")

   
current = CurrentAccount(500, 1000)
current.display_balance()
current.withdraw(700)
current.withdraw(800)
current.display_balance()
