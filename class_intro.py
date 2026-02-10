class BankAccount:
    def __init__(self,b,n):
        self.name=n
        self.balance=b 
    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            return self.balance
        return "invalid input"
    def push(self,val):
        return self.items.pop()
    def pop(self): 
        return self.items.pop()           
n=input("enter the name of the account holder:")
b=int(input("enter the balance:"))
b1=BankAccount(n,b)
print(b1.name)
print(b1.balance)




    