from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator

app = FastAPI()


# We define a Pydantic model (User) with two fields: name & age. The class inherits from the BaseModel we imported from Pydantic.
class User(BaseModel):
    name: str
    age: int = Field(..., gt=0, le=120) # The age field must be greater than 0 but less than 120
    
    @field_validator("name") # Here we ensure the name field is not empty
    def name_must_not_be_empty(cls, v):
        if not v:
            raise ValueError("Name must not be empty")
        return v
    

# We then use the model in a post request model, to validate the incoming data.   
@app.post("/users/")
async def create_user(user: User):
    u = {"name": user.name, "age": user.age}
    return u


# In this example, we define a response body in a get request.
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    # example of user data
    return {"name": "adam", "age": 18}