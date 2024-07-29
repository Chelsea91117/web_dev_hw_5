from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., max_length=30)

    class Config:
        orm_mode = True
        from_attributes = True

class QuestionCreate(BaseModel):
    id: int
    text: str = Field(..., min_length=12)
    category_id: int = Field(..., gt=0)

    class Config:
        orm_mode = True
        from_attributes = True

class QuestionResponse(BaseModel):
    id: int
    text: str
    category: CategoryBase

    class Config:
        # Указываем Pydantic использовать эти параметры чтобы можно было переносить данные прямо с объекта
        orm_mode = True
        from_attributes = True



class MessageResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True
        from_attributes = True