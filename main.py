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

#gx1: fibonacci endpoint

#ex1: compound interest endpoint

#gx2: create user

#gx3: get user
