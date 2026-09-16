from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product
)

router = APIRouter()

#Rota para buscar todos os itens:
@router.get("/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

#Rota para buscar um item:
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_products(db=db, product_id=product_id)

    if db_product is None:
        raise HTTPException(status_code=404, detail = "O produto buscado não existe" )
    return db_product

#Rota para adicionar um item:
@router.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(product= product, db=db)

#Rota para deletar um item:
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_db =  delete_product(product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail = "O produto buscado não existe" )
    return product_db

#Rota para fazer update:
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail = "O produto buscado não existe" )
    return product_db