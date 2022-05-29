from typing import Union

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items")
def get_items(q: Union[str, None] = Query(default="Pycharm", min_length=3)):
    return q



