from fastapi import Header, HTTPException, status, Depends
from models.user import User, RoleEnum


async def get_current_user(
  x_user_email: str = Header(..., description="Mock Auth: Enter user email"),
):
  user = await User.get_or_none(email=x_user_email)
  if not user:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user email"
    )
  if not user.is_active:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Inactive user")
  return user


def require_roles(allowed_roles: list[RoleEnum]):
  async def role_checker(user: User = Depends(get_current_user)):
    if user.role not in allowed_roles:
      raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=f"Operation not permitted for role: {user.role}",
      )
    return user

  return role_checker
