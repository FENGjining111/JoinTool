
from fastapi import FastAPI
from backend.routers import task, result

app = FastAPI(title="Meeting Scheduler Platform")

app.include_router(task.router, prefix="/task", tags=["Task"])
app.include_router(result.router, prefix="/result", tags=["Result"])