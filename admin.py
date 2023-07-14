class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, initial_balance):
        user = User(name, initial_balance)
        self.users.append(user)
        self.total_balance += initial_balance
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
            self.total_balance += amount
            print(f"Amount {amount} deposited successfully for {name}.")
        else:
            print(f"No user found with name {name}.")

    def withdraw(self, name, amount):
        user = self.get_user(name)
        if user:
            if user.balance >= amount:
                user.withdraw(amount)
                self.total_balance -= amount
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
        if self.loan_feature_enabled:
            user = self.get_user(name)
            if user:
                loan_amount = user.balance * 2
                user.deposit(loan_amount)
                self.total_loan_amount += loan_amount
                print(f"Loan of {loan_amount} granted to {name}.")
            else:
                print(f"No user found with name {name}.")
        else:
            print("Loan feature is currently disabled.")

    def check_total_balance(self):
        print(f"Total available balance in the bank: {self.total_balance}")

    def check_total_loan_amount(self):
        print(f"Total loan amount in the bank: {self.total_loan_amount}")

    def enable_loan_feature(self):
        self.loan_feature_enabled = True
        print("Loan feature enabled.")

    def disable_loan_feature(self):
        self.loan_feature_enabled = False
        print("Loan feature disabled.")


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


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, initial_balance):
        self.bank.create_account(name, initial_balance)

    def check_total_balance(self):
        self.bank.check_total_balance()

    def check_total_loan_amount(self):
        self.bank.check_total_loan_amount()

    def enable_loan_feature(self):
        self.bank.enable_loan_feature()

    def disable_loan_feature(self):
        self.bank.disable_loan_feature()


# Usage example:
bank = Bank()
admin = Admin(bank)

# Admin creates accounts
admin.create_account("Alice", 1000)
admin.create_account("Bob", 500)
admin.create_account("Charlie", 2000)

# Admin checks total balance and loan amount
admin.check_total_balance()
admin.check_total_loan_amount()

# Admin enables/disables loan feature
admin.enable_loan_feature()
admin.disable_loan_feature()

# Admin checks total balance and loan amount again
admin.check_total_balance()
admin.check_total_loan_amount()
