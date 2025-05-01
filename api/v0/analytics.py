from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dependencies.database import get_db
from domain.serializers.v0.analytics_serializer import PartWordCountSerializer
from services.part_analytics_service import PartAnalyticsService


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

@router.get(
    "/parts/top-words",
    response_model=list[PartWordCountSerializer],
    summary="Top 5 most common words in Part descriptions"
)
def top_common_words(db: Session = Depends(get_db)):
    service = PartAnalyticsService(db)
    most_common_words = service.count_description_comon_words()
    return [PartWordCountSerializer(word=word, count=count) for word, count in most_common_words]
