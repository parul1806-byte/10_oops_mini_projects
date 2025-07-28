# BANK ACCOUNT SYSTEM WITH CONTEXT MANAGER
# creating a basic class that hold the basic methods of a bank account
import warnings
class Account():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        print(f"✅  created for {self.name} with initial balance: ₹{self.balance}")
        print("----------------------------------------------------------------------------")
# method to deposit an amount:
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"✅₹{amount}: Has been deposited\nnew Balance: ₹{self.balance}")
        else:
            print("Deposit Amount Must Positive.")
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"✅₹{amount}: Has been withdraw from {self.name}\nNew Balance: ₹{self.balance}")
            return True
        else:
            warnings.warn("❌ ERROR: INSUFFICIENT FUNDS")
            return False
    def transfer_to(self,other_account,amount):
        print("➡️ Starting secure transaction....")
        print("--------------------------------------------------------")
        if self.withdraw(amount):
            other_account.deposit(amount)
            print("_____________________________________________________________")
            print(f"💸 Transferring ₹{amount} from {self.name} to {other_account.name}....")
            print("----------------------------------------------------------------")
        else:
            print("❌:Transfer Failed Due To Insufficient Balance")
            raise Exception("Transfer Failed: Insufficient Balance")
        # adding context manager
# enter method
    def __enter__(self):
        self._original_balance = self.balance
        print(f"➡️ Transaction Started for {self.name} ")
        return self

#exit method
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.balance = self._original_balance
            print(f"❌ERROR! Rolling back:{self.name}'s balance to ₹{self.balance}")
        else:
            print(f"✅Transaction sucessful for {self.name}\nFinal balance:₹{self.balance}")

# creating objects
acc1 = Account("riya",8000)
acc2 = Account("raj",700)
try:
   with acc1:
       acc1.transfer_to(acc2,800)
   raise Exception("Simulated crash")
except Exception as e:
   print(f"⚠️ Exception caught:",{e})
print("=================================================================================")
acc3 = Account("parul",9000)
acc4 = Account("megha",1100)
try:
   with acc3:
       acc3.transfer_to(acc3,9500)
   raise Exception("Simulated crash")
except Exception as e:
   print(f"⚠️ Exception caught:",{e})

