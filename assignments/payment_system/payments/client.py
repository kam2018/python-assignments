from payments.debit_card import DebitCard
from payments.credit_card import CreditCard
from payments.payment_service import PaymentService

class Client:
    def debit_card_payment() -> None:
        debit_card: DebitCard = DebitCard("1234567891012345")
        payment_service: PaymentService = PaymentService(debit_card)
        payment_service.make_payment(100)
        
    def credit_card_payment() -> None:
        credit_card: CreditCard = CreditCard("1234567891055555")
        payment_service: PaymentService = PaymentService(credit_card)
        payment_service.make_payment(200)      

    debit_card_payment() 
    credit_card_payment()   