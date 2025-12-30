from fastapi import FastAPI
from payments.debit_card import DebitCard
from payments.credit_card import CreditCard
from payments.payment_service import PaymentService

fast_api: FastAPI = FastAPI()

@fast_api.post("/payment/debit")
def debit_card(pay_details: str, amount: float) -> str:
    debit_card: DebitCard = DebitCard(pay_details)
    payment_service: PaymentService = PaymentService(debit_card)
    response: str = payment_service.make_payment(amount)
    return response

@fast_api.post("/payment/credit")
def credit_card(pay_details: str, amount: float) -> str:
    credit_card: CreditCard = CreditCard(pay_details)
    payment_service: PaymentService = PaymentService(credit_card)
    response: str = payment_service.make_payment(amount)
    return response
