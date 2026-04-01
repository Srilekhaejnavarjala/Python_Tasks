#Payment system (Runtime Polymorphism)
'''
An online store supports multiple payment methods: CreditCard, UPI, and
NetBanking. Create a base class Payment with a method process_payment() and
override it in each payment type.

'''
class Payment:
    def process_payment(self):
        print("Payment Loading...")
        
class CreditCard(Payment):
    def process_payment(self):
        print("Payment done using credit card")

class UPI(Payment):
    def process_payment(self):
        print("Payment done using UPI ")

class NetBanking(Payment):
    def process_payment(self):
        print("Payment done using Net Banking")

#creating objects
credit = CreditCard()
upi = UPI()
net = NetBanking()

#printing statements
credit.process_payment()
upi.process_payment()
net.process_payment()

    
        
