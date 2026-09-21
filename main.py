from fastapi import FastAPI
from models import Product
from database import session

app = FastAPI()

@app.get("/")
def greet():
     return "Welcome to the website"

products = [
    Product(id = 1,name = "phone",description = "budget phone",price = 99.99,quantity= 10),
    Product(id = 2,name = "laptop",description = "Macbook",price = 1999.99,quantity= 6),
    Product(id = 3,name = "pen",description = "A blue ink pen",price = 1.99,quantity= 100),
    Product(id = 4,name = "table",description = "A wooden table",price = 199.99,quantity= 20),
]

@app.get("/products")
def get_all_products():
     
     #db connection
     db = session()

     #query
     db.query()
     return products


# @app.get("/product")
# def get_product_by_id( ):
#      return products[0] #this will return first product


@app.get("/product/{id}")
def get_product_by_id(id: int):
     for product in products:
           if product.id == id :
            return product
     return "Product not found"


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product  

@app.put("/product")
def update_product(id: int , product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added Successfully"
    return "No Product Found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return 'Product Deleted Successfully'
    return "Product Not Found"