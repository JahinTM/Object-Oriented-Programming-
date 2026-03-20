class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature = True

    def create_account(self, name, email, address, acc_type):
        for user in self.users.values():
            if user.email == email:
                print("An account with this email already exists.")
                return

        acc_no = len(self.users) + 1001
        user = User(name, email, address, acc_type, acc_no)
        self.users[acc_no] = user
        print(f"\n Welcome {name}. Your account has been created successfully.")
        print(f"Account Number: {acc_no}")
        print(f"Account Type: {acc_type}")

    def delete_account(self, acc_no):
        if acc_no in self.users:
            name = self.users[acc_no].name
            del self.users[acc_no]
            print(f"Account of {name} has been deleted successfully.")
        else:
            print("This account does not exist.")

    def show_all_accounts(self):
        if not self.users:
            print("No accounts found.")
            return
        print("\n All accounts:")
        for acc in self.users.values():
            print(acc)

    def bank_balance(self):
        print(f"Total bank balance is: {self.total_balance} BDT")

    def total_loans(self):
        print(f"Total loan amount is: {self.total_loan} BDT")

    def loan_toggle(self):
        self.loan_feature = not self.loan_feature
        status = "enabled" if self.loan_feature else "disabled"
        print(f"Loan feature is now {status}.")


class User:
    def __init__(self, name, email, address, acc_type, acc_no):
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type
        self.acc_no = acc_no
        self.balance = 0
        self.transactions = []
        self.loan_count = 0
        self.loan_balance = 0   # NEW

    def deposit(self, amount, bank):
        self.balance += amount
        bank.total_balance += amount
        self.transactions.append(f"Deposited {amount} BDT")
        print(f"{amount} BDT has been deposited successfully.")

    def withdraw(self, amount, bank):
        if amount > self.balance:
            print("You do not have enough balance.")
        elif amount > bank.total_balance:
            print("The bank does not have enough balance at the moment.")
        else:
            self.balance -= amount
            bank.total_balance -= amount
            self.transactions.append(f"Withdrawn {amount} BDT")
            print(f"{amount} BDT has been withdrawn successfully.")

    def check_balance(self):
        print(f"{self.name}, your current balance is: {self.balance} BDT")

    def transaction_history(self):
        print("\nTransaction history:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for t in self.transactions:
                print(t)

    def take_loan(self, amount, bank):
        if not bank.loan_feature:
            print("Loan service is currently unavailable.")
        elif self.loan_count >= 2:
            print("You have already taken the maximum number of loans.")
        else:
            self.balance += amount
            self.loan_balance += amount   
            bank.total_loan += amount
            self.loan_count += 1
            self.transactions.append(f"Loan taken: {amount} BDT")
            print(f"Loan of {amount} BDT has been approved.")

    def pay_loan(self, amount, bank):
        if self.loan_balance == 0:
            print("You have no loan to pay.")
        elif amount > self.balance:
            print("You do not have enough balance to pay loan.")
        else:
            if amount > self.loan_balance:
                amount = self.loan_balance

            self.balance -= amount
            self.loan_balance -= amount
            bank.total_loan -= amount
            bank.total_balance += amount

            self.transactions.append(f"Loan paid: {amount} BDT")
            print(f"{amount} BDT loan has been paid successfully.")

    def transfer(self, amount, acc_no, bank):
        if acc_no not in bank.users:
            print("The destination account does not exist.")
        elif amount > self.balance:
            print("You do not have enough balance for this transfer.")
        else:
            receiver = bank.users[acc_no]
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(f"Transferred {amount} BDT to {receiver.name}")
            receiver.transactions.append(f"Received {amount} BDT from {self.name}")
            print(f"{amount} BDT has been transferred successfully.")

    def __str__(self):
        return f"{self.name} | Acc: {self.acc_no} | Type: {self.acc_type} | Balance: {self.balance} BDT | Loan: {self.loan_balance} BDT"


def admin_login():
    for i in range(3):
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")

        if username == "admin" and password == "admin123":
            print("Login successful.")
            return True
        else:
            print(f"Invalid credentials ({i+1}/3)")
    print("Too many failed attempts.")
    return False


bank = Bank()

while True:
    print("\nBank Management System")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        if not admin_login():
            continue

        while True:
            print("\nAdmin Menu")
            print("1 Create Account")
            print("2 Delete Account")
            print("3 Show All Accounts")
            print("4 Bank Balance")
            print("5 Total Loan")
            print("6 Toggle Loan Feature")
            print("7 Logout")

            op = input("Select option: ")

            if op == "1":
                name = input("Name: ")
                email = input("Email: ")
                address = input("Address: ")
                acc_type = input("Account Type (Savings/Current): ")
                bank.create_account(name, email, address, acc_type)

            elif op == "2":
                acc = int(input("Account Number: "))
                bank.delete_account(acc)

            elif op == "3":
                bank.show_all_accounts()

            elif op == "4":
                bank.bank_balance()

            elif op == "5":
                bank.total_loans()

            elif op == "6":
                bank.loan_toggle()

            elif op == "7":
                break

    elif choice == "2":
        acc = int(input("Enter account number: "))

        if acc not in bank.users:
            print("Invalid account number.")
            continue

        user = bank.users[acc]

        while True:
            print(f"\nWelcome {user.name}")
            print("1 Deposit")
            print("2 Withdraw")
            print("3 Check Balance")
            print("4 Transaction History")
            print("5 Take Loan")
            print("6 Pay Loan")   # NEW
            print("7 Transfer Money")
            print("8 Logout")

            op = input("Select option: ")

            if op == "1":
                amount = int(input("Enter amount: "))
                user.deposit(amount, bank)

            elif op == "2":
                amount = int(input("Enter amount: "))
                user.withdraw(amount, bank)

            elif op == "3":
                user.check_balance()

            elif op == "4":
                user.transaction_history()

            elif op == "5":
                amount = int(input("Enter loan amount: "))
                user.take_loan(amount, bank)

            elif op == "6":
                amount = int(input("Enter amount to pay: "))
                user.pay_loan(amount, bank)

            elif op == "7":
                amount = int(input("Enter amount: "))
                to_acc = int(input("Enter receiver account number: "))
                user.transfer(amount, to_acc, bank)

            elif op == "8":
                break

    elif choice == "3":
        print("Exiting system. Thank you.")
        break

    else:
        print("Invalid option. Try again.")