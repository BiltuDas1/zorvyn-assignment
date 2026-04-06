from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.records import FinancialRecord
from models.user import User, RoleEnum
from schemas.record import RecordCreate, RecordResponse
from core.dependencies import get_current_user, require_roles

router = APIRouter(prefix="/records", tags=["Records"])


# Analysts and Admins can view records
@router.get("/", response_model=List[RecordResponse])
async def get_records(
  user: User = Depends(require_roles([RoleEnum.ADMIN, RoleEnum.ANALYST])),
):
  return await FinancialRecord.all()


# Only Admins can create records
@router.post("/", response_model=RecordResponse)
async def create_record(
  record_data: RecordCreate, user: User = Depends(require_roles([RoleEnum.ADMIN]))
):
  record = await FinancialRecord.create(**record_data.dict(), created_by=user)
  return record


# Only Admins can delete
@router.delete("/{record_id}")
async def delete_record(
  record_id: str, user: User = Depends(require_roles([RoleEnum.ADMIN]))
):
  deleted_count = await FinancialRecord.filter(id=record_id).delete()
  if not deleted_count:
    raise HTTPException(status_code=404, detail="Record not found")
  return {"message": "Deleted successfully"}
