from pydantic import BaseModel


class ClientCreate(BaseModel):
    name: str
    email: str
    phone: str
    company: str = None
    address: str = None
