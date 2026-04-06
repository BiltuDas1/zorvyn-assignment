from fastapi import FastAPI
from core import lifespan
from routes import records, dashboard

app = FastAPI(title="Zorvyn API", lifespan=lifespan.APILifespan)

app.include_router(records.router)
app.include_router(dashboard.router)


@app.get("/")
def health_check():
  return {"status": "healthy"}

