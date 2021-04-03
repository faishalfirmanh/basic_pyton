
# cust id
# name
# balance
#
# deposite

class Customer():
    def __init__(self,cussid, name, initial_bal=0): #mirip constructor
        self.id = cussid
        self.name = name
        self.balance = initial_bal

    def get_balance(self):
        return self

    def deposite(par, amount):
        par.balance = par.balance+amount
        return par.balance

    def withdraw(pp,amount): #balance - amount
        if  amount > pp.balance:
            return "tidak cukup"
        else:
            pp.balance -= amount
            return pp.balance

const = Customer("222","diki") #pembuatan objeknya
#print(const.id, const.name, const.balance)
cos2 = Customer("111","raya")
cus3 = Customer("83", "indah")

const.deposite(1000)
cus3.deposite(2000)
cos2.deposite(200)

l1 = [const,cos2, cus3]

for value in l1:
    if value.balance <  1000:
        print(value.id, value.name)
