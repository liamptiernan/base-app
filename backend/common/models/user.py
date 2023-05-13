from pydantic import BaseModel


class User(BaseModel):
    id: int
    full_name: str
    email: str
    client_id: int
    roles: list[str] = []

    class Config:
        orm_mode = True
