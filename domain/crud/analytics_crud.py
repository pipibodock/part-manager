from sqlalchemy import select
from sqlalchemy.orm import Session

from domain.models.part import Part

def get_parts_descriptions(db: Session) -> list[Part]:
    query = select(Part.description).where(Part.description.is_not(None))
    return db.execute(query).scalars().all()