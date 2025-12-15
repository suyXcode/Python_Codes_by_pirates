class Bank:
    bname = "SBI"
    loc = 'Noida'
    Ifsc = 'SBIN0011'
    bmanager = 'Mr.Nitish'

    def __init__(self,name,addr,bal):
        self.name = name
        self.addr = addr
        self.bal = bal
        

    @classmethod
    def bank_details(cls):
        print(f"Bank name : {cls.bname}")
        print(f"Location : {cls.loc}")
        print(f"IFSC code : {cls.Ifsc}")
        print(f"Bank manager : {cls.bmanager}")

    @classmethod
    def change_location(cls):
        cls.loc =input("Enteer the new address : ")
        print("Location is changed successfully.")
        cls.bank_details()
    
    def customer_details(self):
        print(self.name)
        print(self.addr)
        print(self.bal)

    def change_address(self):
        self.addr = input("Enter the new address of the customer : ")
        print("Addesss is changed successfully.")

    def deposite(self):
        amount = self.get_amount()
        self.bal +=amount
        print("Deposited successfully.")
        print(f"Availbale balance : {self.bal}")


    def withdraw(self):
        amount = self.get_amount()
        if self.bal >=amount:
            self.bal -= amount
            print("Withdrawed successfully.")
            print(f"Availbale balance : {self.bal}")
        else:
            print("Insufficient balance")
        

    @staticmethod
    def get_amount():
        amount = int(input("Enter the amount : "))
        return amount
    

c1 = Bank('Divya','Noida',10000)
c2 = Bank('Nitu','Noida',20000)


while True:
    print("Enter---\n1 for customer details\n2 for change the address\n3 for deposite\n4 for withdraw\n5 for exit")
    choice = int(input("Enter your choice--"))
    
    if choice == 1:
        c1.customer_details()
        print("="*40)
    elif choice == 2:
        c1.change_address()
        print("="*15)
    elif choice == 3:
        c1.deposite()
        print("="*15)
    elif choice == 4:
        c1.withdraw()
        print("="*15)
    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Invalid choice")
        print("="*15)