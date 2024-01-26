class BankAccount():

    def __init__(self, balance=0):
        self._balance = balance

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 0:
            raise ValueError('На счете недостаточно средств')
        else:
            self._balance -= amount

    def transfer(self, account, amount):
        if self._balance - amount < 0:
            raise ValueError ('На счете недостаточно средств')
        else:
            self._balance -= amount
            account._balance += amount


account = BankAccount()

print(account.get_balance())
account.deposit(100)
print(account.get_balance())
account.withdraw(50)
print(account.get_balance())