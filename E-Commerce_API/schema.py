from pydantic import BaseModel,Field
from typing import Optional,Literal,Annotated

class CreatProduct(BaseModel):
    id:int
    name:str=Field(...,min_length=1)
    description:Optional[str]=None
    price:float=Field(...,gt=0)
    stock:int=Field(...,ge=0)
    category:Annotated[Literal["electronics", "clothing"], Field(default= "clothing")]
    
class UpdateProduct(BaseModel):
    name:Optional[str]=None
    description:Optional[str]=None
    price:Optional[float]=None
    stock:Optional[int]=None
    
        
    