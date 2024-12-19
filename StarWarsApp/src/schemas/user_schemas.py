from pydantic import BaseModel, EmailStr


class SafeUser(BaseModel):
    email: EmailStr

    class Config:
        extra = "forbid"
