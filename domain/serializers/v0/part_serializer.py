from pydantic import BaseModel

class PartSerializer(BaseModel):
    id: int
    name: str
    sku: str
    description: str | None = None
    weight_ounces: int | None = None
    is_active: bool = True

    class Config:
        orm_mode = True

class PartCreateSerializer(BaseModel):
    name: str
    sku: str
    description: str | None = None
    weight_ounces: int | None = None
    is_active: bool = True

    class Config:
        orm_mode = True

class PartUpdateSerializer(BaseModel):
    name: str | None = None
    description: str | None = None
    weight_ounces: int | None = None
    is_active: bool = True

    class Config:
        orm_mode = True