from pydantic import BaseModel
from datetime import datetime

# What we return to the user
class DocumentResponse(BaseModel):
    id: int
    filename: str
    upload_date: datetime
    content_text: str

    class Config:
        from_attributes = True
