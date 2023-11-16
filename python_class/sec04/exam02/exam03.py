class Account:
    def __init__(self,account,balance,interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate

    def setAccount(self,account):
        self.account = account
    def getAccount(self):
        return self.account

    def getBalance(self):
        return  self.balance

    def deposit(self,amt):
        self.balance += amt

    def calcculateInterst(self):
         interestAmt = self.getBalance() * self.interestRate
         return interestAmt

    def withdraw(self,money):
        if self.balance >= money:
            self.balance -= money
        else:
            print("Insufficient funds")

if __name__ == '__main__':
    account = Account('441-0290-1203',500000,0.073)
    print("초기 계좌 정보:" , account.getAccount() , "잔액:", account.getBalance())

    account.deposit(20000)
    print("입금 후:", account.getAccount(), "잔액:", account.getBalance())

    interest = account.calcculateInterst()
    print("이자:",interest)