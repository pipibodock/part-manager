from sqlalchemy import Column, Integer, String, Boolean

from dependencies.database import Base


class Part(Base):
    __tablename__ = "part"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    sku = Column(String(256), unique=True, nullable=False)
    description = Column(String(1024))
    weight_ounces = Column(Integer)
    is_active = Column(Boolean, default=True)
