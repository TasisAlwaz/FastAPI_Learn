from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
     return "Welcome to the website"

products = [
    Product(id = 1,name = "phone",description = "budget phone",price = 99.99,quantity= 10),
    Product(id = 2,name = "laptop",description = "Macbook",price = 1999.99,quantity= 6),
    Product(id = 3,name = "pen",description = "A blue ink pen",price = 9.99,quantity= 100),



]

@app.get("/products")
def get_all_products():
     return products