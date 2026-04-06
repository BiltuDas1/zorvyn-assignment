from enum import Enum
from tortoise.models import Model
from tortoise import fields
from typing import cast
from utils import security


class RoleEnum(str, Enum):
  VIEWER = "viewer"
  ANALYST = "analyst"
  ADMIN = "admin"


class User(Model):
  id = fields.UUIDField(primary_key=True)
  firstname = fields.CharField(max_length=50)
  lastname = fields.CharField(max_length=50)
  email = fields.CharField(max_length=255, unique=True)
  password = fields.CharField(max_length=60)
  role = fields.CharEnumField(RoleEnum, default=RoleEnum.VIEWER)
  created_at = fields.DatetimeField(auto_now_add=True)
  is_active = fields.BooleanField(default=True)

  @classmethod
  async def create(cls, **kwargs):
    if "email" in kwargs:
      kwargs["email"] = cast(str, kwargs["email"]).lower()
    if "password" in kwargs:
      kwargs["password"] = security.hash_password(cast(str, kwargs["password"]))
    return await super().create(**kwargs)
