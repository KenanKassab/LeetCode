class Bank:

    def __init__(self, balance: List[int]):
        self.balance = [0] + balance
        self.max_id = len(balance)


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # print(self.balance)
        if account2 <= self.max_id and account1 <= self.max_id:
            if self.balance[account1] >= money:
                self.balance[account1] -= money
                self.balance[account2] += money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= self.max_id:
            self.balance[account] += money
            return True
        else:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.max_id:
            if self.balance[account] >= money:
                self.balance[account] -= money
                return True
            else:
                return False
        else:
            return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
