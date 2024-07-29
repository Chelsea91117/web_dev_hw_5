from pydantic import BaseModel, Field

class CategoryCreate(BaseModel):
    name: str = Field(..., max_length=30)

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
