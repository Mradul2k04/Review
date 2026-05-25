from fastapi import APIRouter,Path
import crud
from fastapi.responses import JSONResponse
from schema import CreatProduct,UpdateProduct

router = APIRouter()

@router.get('/')
def home():
    return {'message':'E-Commerce API'}

# GET : Fetch all tasks
@router.get('/Product')
def view_Product():
    return crud.get_all_product_data()

# GET : Fetch task by ID
@router.get('/Product/{id}')
def Product_by_id(id: str = Path(..., description='Product ID', example='1')):
    return crud.get_product_by_id(id)   

# POST : Create new task
@router.post('/Product')
def create_Product(Product: CreatProduct):
    crud.add_product(Product)
    return JSONResponse(status_code=201, content={'message':'Product Added successfully'})

# PUT : Update task
@router.put('/edit_Product/{id}')
def update_Product(id: str, Product_Update:UpdateProduct):
    crud.update_product(id,Product_Update)
    return JSONResponse(status_code=200, content={'message':'Product updated successfully'})

# DELETE : Delete task
@router.delete('/del_Product/{id}')
def delete_extisting_Product(id: str):
    crud.delete_Product(id)
    return JSONResponse(status_code=200, content={'message':'Product deleted successfully'})
