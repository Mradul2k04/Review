from fastapi import HTTPException
from database import load_data, save_data
from schema import  CreatProduct,UpdateProduct

def get_all_product_data():
    return load_data()

def get_product_by_id(id: str):
    data = load_data()
    if id not in data:
        raise HTTPException(status_code='404', detail='Product not found')
    
    return data[id]


def add_product(Product:CreatProduct):
    data = load_data()
    if Product.id in data:
        raise HTTPException(status_code=400, detail='Product already exists')
    
    data[Product.id] = Product.model_dump(exclude={'id'},mode = 'json')
    save_data(data)
    
    
def update_product(id:str , product_update: UpdateProduct):
    data = load_data()
    if id not in data:
        raise HTTPException(status_code=404, detail="Product not found")
    
    existing_product_info = data[id]
    updated_product_info = product_update.model_dump(exclude_unset=True)

    for key, value in updated_product_info.items():
        existing_product_info[key] = value

    existing_product_info["id"] = id
    product_obj = CreatProduct(**existing_product_info)

    data[id] = product_obj.model_dump(exclude={"id"})
    save_data(data)    
    
def delete_Product(id: str):
    data = load_data()
    if id not in data:
        raise HTTPException(status_code=404, detail='Product not found')
    
    del data[id]
    save_data(data)    
    

