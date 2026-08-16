from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict, Field


class UserCreate(BaseModel):
    """Shape of the data required to register a new user."""
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserLogin(BaseModel):
    """Shape of the data required to log in."""
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """Shape of user data returned by the API. Never includes password_hash."""
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    """Shape of the response returned after a successful login."""
    access_token: str
    token_type: str = "bearer"