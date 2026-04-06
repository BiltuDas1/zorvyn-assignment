from . import environ

DATABASE_URL = environ.ENV.get("DATABASE_URL") or "sqlite://db.sqlite3"

TORTOISE_ORM = {
  "connections": {"default": DATABASE_URL},
  "apps": {
    "models": {
      "models": ["models.user", "models.record", "aerich.models"],
      "default_connection": "default",
    },
  },
}
