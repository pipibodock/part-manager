from pydantic import BaseModel, ConfigDict


class PartSerializer(BaseModel):
    id: int
    name: str
    sku: str
    description: str | None = None
    weight_ounces: int | None = None
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)

class PartCreateSerializer(BaseModel):
    name: str
    sku: str
    description: str | None = None
    weight_ounces: int | None = None
    is_active: bool = True
    model_config = ConfigDict(from_attributes=True)

class PartUpdateSerializer(BaseModel):
    name: str | None = None
    description: str | None = None
    weight_ounces: int | None = None
    is_active: bool = True
    model_config = ConfigDict(from_attributes=True)