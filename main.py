from fastapi import FastAPI
from core import lifespan

app = FastAPI(title="Zorvyn API", lifespan=lifespan.APILifespan)
