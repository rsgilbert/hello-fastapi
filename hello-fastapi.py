from fastapi import FastAPI
from enum import Enum

# start application using: uvicorn hello-fastapi:app --reload

app = FastAPI()


class RainbowName(str, Enum):
    red = 'red'
    orange = 'orange'
    yellow = 'yellow'
    green = 4


@app.get("/rainbow/{rainbow_name}")
def get_rainbow_color(rainbow_name: RainbowName):
    print(f"Name is {rainbow_name.name} , Value is {rainbow_name.value}. actual {str(rainbow_name)}")
    if rainbow_name == RainbowName.red:
        return "Kimyufu"
    if rainbow_name == "f":
        return "Kidugavu"
    if rainbow_name == RainbowName.green:
        return "Kilagala"
    return rainbow_name


@app.get("/files/{filepath:path}")
def read_file_from_filepath(filepath: str):
    # For urls like: http://localhost:8000/files//amo/root/det.txt
    print(f"File path is {filepath}")
    return {"fp": filepath}


@app.get("/")
async def root():
    return {"Message": "Hello World"}


@app.get("/items/{item_id:str}")
async def read_item(item_id, fr=8):
    return {"item_id": item_id}


@app.get("/users/me")
def read_user_me():
    return "I am me"


@app.get("/users/{user_id}")
def read_user_by_user_id(user_id: str):
    return f"User id is {user_id}"


@app.get("/users/me")
def read_user_me8():
    return "I am m ejj"


@app.get("/paginate/{count}")
def paginate(count: int, from_idx: int = None, to_idx: int = 0):
    return {'count': count, 'from_idx': from_idx, 'to_idx': to_idx}
