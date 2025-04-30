from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies.database import get_db
from domain.crud.part_crud import get_parts
from domain.serializers.v0.part_serializer import PartSerializer


router = APIRouter(
    prefix="/parts",
    tags=["Parts"],
)


@router.get("/", response_model=list[PartSerializer], summary="List all Part on the database")
def read_parts(db: Session = Depends(get_db)):
    return get_parts(db)
