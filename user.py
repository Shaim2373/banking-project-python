class Bank:
    def __init__(self):
        self.users = []

    def create_account(self, name, initial_balance):
        user = User(name, initial_balance)
        self.users.append(user)
        print(f"Account created successfully for {name}.")

    def get_user(self, name):
        for user in self.users:
            if user.name == name:
                return user
        return None

    def check_balance(self, name):
        user = self.get_user(name)
        if user:
            print(f"Available balance for {name}: {user.balance}")
        else:
            print(f"No user found with name {name}.")

    def deposit(self, name, amount):
        user = self.get_user(name)
        if user:
            user.deposit(amount)
            print(f"Amount {amount} deposited successfully for {name}.")
        else:
            print(f"No user found with name {name}.")

    def withdraw(self, name, amount):
        user = self.get_user(name)
        if user:
            if user.balance >= amount:
                user.withdraw(amount)
                print(f"Amount {amount} withdrawn successfully for {name}.")
            else:
                print("Bank is bankrupt. Unable to withdraw amount.")
        else:
            print(f"No user found with name {name}.")

    def transfer(self, sender_name, receiver_name, amount):
        sender = self.get_user(sender_name)
        receiver = self.get_user(receiver_name)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(f"Amount {amount} transferred from {sender_name} to {receiver_name} successfully.")
            else:
                print(f"Insufficient balance in {sender_name}'s account.")
        else:
            print("Invalid sender or receiver name.")

    def loan(self, name):
        user = self.get_user(name)
        if user:
            loan_amount = user.balance * 2
            user.deposit(loan_amount)
            print(f"Loan of {loan_amount} granted to {name}.")
        else:
            print(f"No user found with name {name}.")


class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_history.append(f"Withdrawn: {amount}")

    def display_transaction_history(self):
        print(f"Transaction history for {self.name}:")
        for transaction in self.transaction_history:
            print(transaction)


# Usage example:
bank = Bank()

# Create accounts
bank.create_account("Alice", 1000)
bank.create_account("Bob", 500)
bank.create_account("Charlie", 2000)

# Deposit money
bank.deposit("Alice", 500)
bank.deposit("Bob", 1000)

# Withdraw money
bank.withdraw("Alice", 300)
bank.withdraw("Bob", 800)

# Transfer money
bank.transfer("Alice", "Bob", 200)
bank.transfer("Charlie", "Alice", 500)

# Check balance
bank.check_balance("Alice")
bank.check_balance("Bob")
bank.check_balance("Charlie")

# Check transaction history
user = bank.get_user("Alice")
user.display_transaction_history()

# Take a loan
bank.loan("Charlie")
bank.check_balance("Charlie")
