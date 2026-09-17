
from pydantic import BaseModel 


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

'''
#We are using imported 'BaseModel' to replace these:

def __init__(self, id: int,name: str,description: str,price: float,quantity: int):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
'''
    