from payments.payment_startegy import PaymentStrategy

class CreditCard(PaymentStrategy):
    def __init__(self, pay_details: str):
        super().__init__(pay_details)
        

    def validate_details(self) -> bool:
        if len(self.pay_details) == 16:
            print(f"Credit Card (***********{self.pay_details[-5:]}) validate successfully!!")
            return True
        else:
            print(f"Credit Card ({self.pay_details[-5:]}) validation failed!! as length is ({len(self.pay_details)})")
            return False
        
    def pay(self, amount: float) -> None:
        return f"Payment of ({amount}) completed!!"