from enum import Enum
from tortoise.models import Model
from tortoise import fields


class TransactionType(str, Enum):
  INCOME = "income"
  EXPENSE = "expense"


class FinancialRecord(Model):
  id = fields.UUIDField(primary_key=True)
  amount = fields.DecimalField(max_digits=12, decimal_places=2)
  type = fields.CharEnumField(TransactionType)
  category = fields.CharField(max_length=100)
  date = fields.DateField()
  notes = fields.TextField(null=True)
  created_at = fields.DatetimeField(auto_now_add=True)
  created_by = fields.ForeignKeyField("models.User", related_name="records")

  class Meta:
    table = "financial_records"
