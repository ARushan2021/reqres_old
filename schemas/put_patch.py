from datetime import datetime

from pydantic import BaseModel
from pydantic.class_validators import Optional

"""Валидация json-схем в response, какие должны быть поля и какие типы"""


class PutPatch(BaseModel):
    first_name: Optional[str]
    second_name: Optional[str]
    name: Optional[str]
    job: Optional[str]
    updatedAt: datetime
