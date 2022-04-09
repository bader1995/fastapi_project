from fastapi import FastAPI
from classes.User import User
from models.User import UserModel

app = FastAPI()


@app.get("/api/v1/users/list")
def root():
    return User.getAllUsers()

@app.post("/api/v1/users/add")
def root(user: UserModel):
    return User.addUser(user)

@app.delete("/api/v1/users/delete")
def root(id):
    return User.deleteUser(id)