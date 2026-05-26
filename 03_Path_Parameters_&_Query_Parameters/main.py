from fastapi import FastAPI

app = FastAPI()


# Example of route that uses {user_id} as a path parameter in the path "/users/{user_id}"
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user": {user_id}}


# Example of route that uses user_id (required) and name (optional since it's None) as query parameters
@app.get("/users/")
def read_user(user_id: int, name: str = None):
    return {"user_id": {user_id}, "name": {name}}


# Example of route that uses both path and query parameters. include_email is optional and defaults to False
@app.get("/users/{user_id}/details")
def read_user_details(user_id: int, include_email: bool = False):
    if include_email:
        return {"user_id": user_id, "include_email": "email included"}
    else:
        return {"user_id": user_id, "include_email": "email not included"}
