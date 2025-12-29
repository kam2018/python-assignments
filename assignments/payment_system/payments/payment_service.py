from payments.payment_startegy import PaymentStrategy

class PaymentService:
    def __init__(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy = payment_strategy
        

    def make_payment(self, amount: float) -> None:
        if self.payment_strategy.validate_details():
            self.payment_strategy.pay(amount);
        