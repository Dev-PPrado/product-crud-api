from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from schemas import (
    ProductResponse,
    ProductUpdate,
    ProductCreate
)

from crud import (
    create_product as crud_create_product,
    get_products as crud_get_products,
    get_product as crud_get_product,
    delete_product as crud_delete_product,
    update_product as crud_update_product
)


router = APIRouter()


# Rota para buscar todos os produtos
@router.get("/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = crud_get_products(db)
    return products


# Rota para buscar um produto
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    db_product = crud_get_product(db, product_id)

    if db_product is None:
        raise HTTPException(
            status_code=404,
            detail="O produto buscado não existe"
        )

    return db_product


# Rota para adicionar um produto
@router.post("/products/", response_model=ProductResponse)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db)
):
    return crud_create_product(
        db=db,
        product=product
    )


# Rota para deletar um produto
@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product_deleted = crud_delete_product(
        db=db,
        product_id=product_id
    )

    if not product_deleted:
        raise HTTPException(
            status_code=404,
            detail="O produto buscado não existe"
        )

    return {
        "message": "Produto deletado com sucesso"
    }


# Rota para atualizar um produto
@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db)
):
    product_db = crud_update_product(
        db=db,
        product_id=product_id,
        product=product
    )

    if product_db is None:
        raise HTTPException(
            status_code=404,
            detail="O produto buscado não existe"
        )

    return product_db