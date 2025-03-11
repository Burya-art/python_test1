class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, (int, float)):
            return self.name - other


account = BankAccount(50, 100)

new = account + 500

print(new)