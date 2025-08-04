from pydantic import BaseModel

class RequestCreate(BaseModel):
    guest_id: int
    type: str
    status: str
