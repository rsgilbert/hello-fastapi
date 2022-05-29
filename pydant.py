import datetime
from typing import List, Union

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name = "James"
    signup_ts: Union[datetime.datetime, None] = None
    friends: List[int] = []
    paid: bool


external_data = {
    "id": 100,
    "signup_ts": "2022-04-30 20:12:59",
    "friends": [1, "2", b"523"],
    "paid": "0"
}

user = User(**external_data)
print(user)
print(user.id)




