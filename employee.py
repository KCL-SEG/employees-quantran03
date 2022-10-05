"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from enum import Enum

class Employee:
    def __init__(self, name, contract, commission, pay, commission_pay = 0, hours_worked = 0, contracts_secured = 0):
        self.name = name
        self.contract = contract
        self.commission = commission
        self.pay = pay
        self.commission_pay = commission_pay
        self.hours_worked = hours_worked
        self.contracts_secured = contracts_secured

    def get_pay(self):
        return self.calc_contract_pay() + self.calc_commission()

    def calc_contract_pay(self):
        if self.contract == Contract.SALARY:
            return self.pay
        elif self.contract == Contract.HOURLY:
            return self.pay * self.hours_worked

    def calc_commission(self):
        if self.commission == Commission.NONE:
            return 0
        elif self.commission == Commission.BONUS:
            return self.commission_pay
        elif self.commission == Commission.CONTRACT:
            return self.commission_pay * self.contracts_secured

    def __str__(self):
        string = self.name + " works on a "
        if self.contract == Contract.SALARY:
            string += "monthly salary of " + str(self.pay)
        elif self.contract == Contract.HOURLY:
            string += "contract of " + str(self.hours_worked) + " hours at "  + str(self.pay) + "/hour"
        
        if self.commission == Commission.BONUS:
            string += " and receives a bonus commission of " + str(self.commission_pay)
        elif self.commission == Commission.CONTRACT:
            string += " and receives a commission for " + str(self.contracts_secured) + " contract(s) at " + str(self.commission_pay) + "/contract"

        string += ". Their total pay is " + str(self.get_pay()) + "."

        return string

class Commission(Enum):
    NONE = 1
    BONUS = 2
    CONTRACT = 3

class Contract(Enum):
    SALARY = 1
    HOURLY = 2

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee("Billie", Contract.SALARY, Commission.NONE, 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Contract.HOURLY, Commission.NONE, 25, hours_worked = 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Contract.SALARY, Commission.CONTRACT, 3000, commission_pay=200, contracts_secured=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Contract.HOURLY, Commission.CONTRACT, 25, contracts_secured=3, commission_pay=220, hours_worked=150)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Contract.SALARY, Commission.BONUS, 2000, commission_pay=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Contract.HOURLY, Commission.BONUS, 30, hours_worked=120, commission_pay=600)

