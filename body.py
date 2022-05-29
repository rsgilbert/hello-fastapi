from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None]
    price: Union[float, None]
    tax: Union[float, None]


app = FastAPI()


@app.post("/items/")
def create_item(item: Item):
    print(item)
    return {'item': item.dict(include={'description', 'name'}, exclude={'tax', 'name'})}




