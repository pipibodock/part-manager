from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.models.part import Part


def get_parts(db: Session):
    query = select(Part)
    return db.execute(query).scalars().all()
