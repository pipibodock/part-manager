from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from dependencies.database import get_db
from domain.crud.part_crud import (
    create_part,
    delete_part,
    get_part,
    get_parts,
    update_part,
)
from domain.serializers.v0.part_serializer import (
    PartCreateSerializer,
    PartSerializer,
    PartUpdateSerializer,
)


router = APIRouter(
    prefix="/parts",
    tags=["Parts"],
)


@router.get("/", response_model=list[PartSerializer], summary="List all Part on the database")
def read_parts(db: Session = Depends(get_db)):
    return get_parts(db)


@router.post(
    "/",
    response_model=PartSerializer,
    summary="Create a new Part",
    status_code=status.HTTP_201_CREATED,
)
def add_part(part: PartCreateSerializer, db: Session = Depends(get_db)):
    try:
        return create_part(db, part)
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Conflict to create data")


@router.get("/{part_id}", response_model=PartSerializer, summary="Get a Part by ID")
def read_part(part_id: int, db: Session = Depends(get_db)):
    db_part = get_part(db, part_id)
    if db_part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return db_part


@router.put("/{part_id}", response_model=PartSerializer, summary="Update a Part")
def change_part(part_id: int, part: PartUpdateSerializer, db: Session = Depends(get_db)):
    updated = update_part(db, part_id, part)
    if updated is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return updated


@router.delete(
    "/{part_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a Part by ID"
)
def delete_part_by_id(part_id: int, db: Session = Depends(get_db)):
    part = get_part(db, part_id)
    if not part:
        raise HTTPException(status_code=404, detail="Part not found")
    delete_part(db, part)
