from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from models.records import TransactionType


class RecordCreate(BaseModel):
  amount: float = Field(..., gt=0, description="Amount must be strictly positive")
  type: TransactionType
  category: str
  date: date
  notes: Optional[str] = None


class RecordResponse(RecordCreate):
  id: str
  created_at: date

  class Config:
    orm_mode = True
