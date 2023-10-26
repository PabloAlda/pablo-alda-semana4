from bank_account import BankAccount

#Crear cuenta de banco
account1 = BankAccount("00001")
account2 = BankAccount("00002")
#Depostar dinero y retirar
account1.deposit(1000)
account1.withdraw(300)

#Crear un chat para preguntar
account_number = input("¿Cuál es tu número de cuenta?")

account = BankAccount(account_number)
pritn(f"Dispone de {account.get_balance()}€ en su eucnta.")

funds = float(input("¿Cuánto dinero desea añadir a su cuenta?"))

account.funds_add(funds)
if funds != '0':
    print(f"Depósito realizado con éxito. Ahora dispone de {account.get_balance()}€ en su cuenta.")

withdrawal = float(input("¿Cuánto dinero desea retirar de su cuenta?"))

print(f"Perfecto. Ahora dispone de {account.get_balance()}€ en su cuenta.")

