from pydantic import BaseModel


class PartWordCountSerializer(BaseModel):
    word: str
    count: int
