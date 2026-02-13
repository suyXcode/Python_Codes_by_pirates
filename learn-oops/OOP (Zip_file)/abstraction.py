from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def deposite(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def kyc(self):
        pass

class SBI(Bank):
    def deposite(self):
        print("This is deposite method")
    
    def withdraw(self):
        print("This is withdraw method")
        
    def kyc(self):
        print("This is kyc method")

c1 = SBI()
c1.deposite()
c1.withdraw()
c1.kyc()