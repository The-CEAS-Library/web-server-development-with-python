# Import pydantic's BaseModel that's used for object validation
from pydantic import BaseModel

# We create our own class that inherits 
class CreateUser(BaseModel):

    # we add fields and their datatype
    username: str
    password: str
    interests: list[str]

class CreateTodo(BaseModel):

    name: str
    priority: int
    done: bool

# when we get a request that's supposed to be have a JSON that looks like this,
# FastAPI will compare the input to this class to enforce the structture