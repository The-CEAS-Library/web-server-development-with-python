from fastapi import FastAPI
from fastapi.responses import JSONResponse
import helpers
import models
import copy

app = FastAPI()

user_db = {}
todo_db = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello(name):
    return {"message": "Hello " + name}

@app.get("/fib")
async def fib(n):
    return helpers.fib(int(n))

@app.post("/user")
async def create_user(user: models.CreateUser):
    user_db[user.username] = {'password': user.password, 'interests': user.interests}

    return user_db[user.username]

@app.post("/todo")
async def create_todo(todo: models.CreateTodo):
    todo_db[todo.name] = {'priority': todo.priority, 'done': todo.done}

    return todo_db[todo.name]

@app.get("/user/{username}")
async def get_user(username):

    if username in user_db:
        user = copy.deepcopy(user_db[username])
        del user['password']
        return user
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})

@app.get("/todo/{name}")
async def get_todo(name):

    if name in todo_db:
        return name
    else:
        return JSONResponse(status_code=404, content={"message": "Item not found"})
