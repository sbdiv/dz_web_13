from pydantic import BaseModel


class EmailVerification(BaseModel):
    email: str
    verification_token: str