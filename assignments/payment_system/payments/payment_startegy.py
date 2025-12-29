from abc import ABC, abstractmethod

class PaymentStrategy(ABC):

    def __init__(self, pay_details: str) -> None:
        super().__init__()
        self.pay_details = pay_details
    
    @abstractmethod
    def validate_details(self) -> bool:
        pass

    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

    