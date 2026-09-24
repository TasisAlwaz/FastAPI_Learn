from fastapi import FastAPI, Depends 
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
     return "Welcome to the website"

products = [
    Product(id = 1,name = "phone",description = "budget phone",price = 99.99,quantity= 10),
    Product(id = 2,name = "laptop",description = "Macbook",price = 1999.99,quantity= 6),
    Product(id = 3,name = "pen",description = "A blue ink pen",price = 1.99,quantity= 100),
    Product(id = 4,name = "table",description = "A wooden table",price = 199.99,quantity= 20),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


def init_db(): 
    db = session() 

    count = db.query(database_models.Product).count()  

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump())) 
        db.commit()

init_db()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
     
    #db connection
    #  db = session()
    db_products = db.query(database_models.Product).all() 

    #query
    #  db.query()
    return db_products


# @app.get("/product")
# def get_product_by_id( ):
#      return products[0] #this will return first product


@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product not found"


@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    # products.append(product)
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product  

@app.put("/products/{id}")
def update_product(id: int , product: Product, db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i] = product
    #         return "Product added Successfully"

    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first() 

    if db_product:
         db_product.name = product.name
         db_product.description = product.description
         db_product.price = product.price
         db_product.quantity = product.quantity
         db.commit()  #this commit code is used to save the changes in database
         return "Product updated"
    else:
        return "No Product Found"
 
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         del products[i]
    #         return 'Product Deleted Successfully'

    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    #Fetching product from the database

    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return "Product Not Found"

    