import re

from sqlalchemy.orm import Session
from collections import Counter

from domain.crud.analytics_crud import get_parts_descriptions


class PartAnalyticsService:
    def __init__(self, db: Session):
        self.db = db

    def count_description_comon_words(self, number_of_repetition: int = 5) -> list[tuple[str, int]]:
        parts_descriptions = get_parts_descriptions(self.db)
        text = " ".join(parts_descriptions)
        normalized_words = re.findall(r'\b\w+\b', text.lower())

        counter = Counter(normalized_words)
        return counter.most_common(number_of_repetition)
