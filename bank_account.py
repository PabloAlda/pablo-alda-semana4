class BankAccount:
    def __init__(self,account_number,balance = 0):
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number
  
    def funds_add(self,funds):
        self.balance = self.balance + funds

    def get_balance(self):
        return self.balance

class SavingAccount(BankAccount)
    def __init__(self,account)


bank_account1 = BankAccount("ES12345678998765432")

#hago una transferencia
bank_account1.funds_add(456)

print(f"La cuenta con número: {bank_account1.get_account_number()} tiene {bank_account1.get_balance()}€ fondos disponibles.")

