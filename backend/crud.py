from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

def get_products(db: Session):
    """
    Retorna todos os produtos do banco de dados.
    """
    return db.query(ProductModel).all()
    

def get_product(db: Session, product_id: int):
    """
    Retorna um produto específico pelo ID.
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    """
    Cria um novo produto no banco de dados.
    """
    db_product = ProductModel(**product.model_dump()) # Cria uma instância do modelo com os dados do produto
    db.add(db_product) # Adiciona o produto ao banco de dados
    db.commit() # Confirma a transação no banco de dados
    db.refresh(db_product) # Atualiza o objeto do produto com os dados do banco de dados
    return db_product # Retorna o objeto do produto criado

def delete_product(db: Session, product_id: int):
    """
    Deleta um produto específico pelo ID.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product:
        db.delete(db_product) # Deleta o produto do banco de dados
        db.commit() # Confirma a transação no banco de dados
        return True # Retorna True se o produto foi deletado com sucesso
    return False # Retorna False se o produto não foi encontrado

def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Atualiza um produto específico pelo ID.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.category is not None:
        db_product.category = product.category

    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor  

    db.commit() # Confirma a transação no banco de dados
    db.refresh(db_product) # Atualiza o objeto do produto com os dados do banco de dados
    return db_product # Retorna o objeto do produto atualizado