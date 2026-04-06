from fastapi import APIRouter, Depends
from tortoise.functions import Sum
from models.records import FinancialRecord, TransactionType
from models.user import User, RoleEnum
from core.dependencies import require_roles

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
async def get_dashboard_summary(
  user: User = Depends(
    require_roles([RoleEnum.VIEWER, RoleEnum.ANALYST, RoleEnum.ADMIN])
  ),
):
  records = await FinancialRecord.all()

  total_income = sum(
    float(r.amount) for r in records if r.type == TransactionType.INCOME
  )
  total_expense = sum(
    float(r.amount) for r in records if r.type == TransactionType.EXPENSE
  )
  net_balance = total_income - total_expense

  # Category wise totals
  categories = {}
  for r in records:
    categories[r.category] = categories.get(r.category, 0) + float(r.amount)

  return {
    "total_income": total_income,
    "total_expenses": total_expense,
    "net_balance": net_balance,
    "category_totals": categories,
    "recent_activity": await FinancialRecord.all().order_by("-date").limit(5).values(),
  }
