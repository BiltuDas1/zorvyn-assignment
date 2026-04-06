from fastapi import FastAPI
from contextlib import asynccontextmanager
from tortoise import Tortoise
from . import logger
from .settings import TORTOISE_ORM

@asynccontextmanager
async def APILifespan(app: FastAPI):
  logger.LOGGER.debug("Connecting to Database Server...")
  
  await Tortoise.init(config=TORTOISE_ORM)
  await Tortoise.generate_schemas()
  logger.LOGGER.debug("Database connected and schemas generated.")

  yield

  await Tortoise.close_connections()
  logger.LOGGER.debug("Closed connection of Database Server")
