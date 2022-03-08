import datetime
from pprint import pprint
from typing import List, Optional

from pydantic import BaseModel

order_json = {
    'item_id': '123',
    # 'created_date': '2002-11-24 12:22',
    'pages_visited': [1, 2, '3'],
    'price': 17.22,
    'other': 12
}


class Order(BaseModel):
    item_id: int
    created_date: Optional[datetime.datetime] = datetime.datetime.now()
    pages_visited: List[int] = [(int,str)]
    price: float


o = Order(**order_json)
pprint(o)


# Default for JSON post
# Can be done for others with mods.
# noinspection PyUnusedLocal
def order_api(order: Order):
    pass


order_api(Order(**order_json))
