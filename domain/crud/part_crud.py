from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.models.part import Part
from domain.serializers.v0.part_serializer import (
    PartCreateSerializer,
    PartUpdateSerializer,
)


def get_parts(db: Session) -> list[Part]:
    query = select(Part)
    return db.execute(query).scalars().all()

def get_part(db: Session, part_id: int) -> Part:
    query = select(Part).where(Part.id == part_id)
    return db.execute(query).scalars().first()

def create_part(db: Session, part: PartCreateSerializer) -> Part:
    db_part = Part(**part.model_dump())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

def update_part(db: Session, part_id: int, part: PartUpdateSerializer) -> Part:
    db_part = get_part(db, part_id)
    if db_part is None:
        return None
    for key, value in part.model_dump(exclude_unset=True).items():
        setattr(db_part, key, value)
    db.commit()
    db.refresh(db_part)
    return db_part

def delete_part(db: Session, db_part: Part) -> None:
    db.delete(db_part)
    db.commit()
