"""

Pydantic is a Python library for data parsing
and validation using Python type annotations.

"""

from typing import Annotated
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field, field_validator


# Advanced Validation with Pydantic
# Regex expressions
# Custom Validators using '@'


class User(BaseModel):
    username: Annotated[str, Field(pattern=r'^[a-zA-Z0-9_.\-]+$')]
    email: EmailStr
    age: Annotated[int, Field(gt=0)]

    @field_validator("username")
    @classmethod
    def username_must_not_contain_spaces(cls, v):
        if ' ' in v:
            raise ValueError("username must not contain spaces")
        return v


app = FastAPI()


# We define a post request that takes in user data and validates it against our pydantic model
@app.post("/register/")
async def register_user(user: User):
    return user