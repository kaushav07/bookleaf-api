from pydantic import BaseModel

class WithdrawalRequest(BaseModel):
    author_id: int
    amount: int
