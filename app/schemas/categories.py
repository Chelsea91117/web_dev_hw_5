from pydantic import BaseModel, Field

class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=30)

class CategoryResponse(BaseModel):
    name: str = Field(..., max_length=30)

    class Config:
        from_attributes = True
