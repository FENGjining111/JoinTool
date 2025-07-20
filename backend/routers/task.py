# backend/routers/task.py
from fastapi import APIRouter
from backend.models.models import TaskCreate
import uuid
import asyncio
from backend.services.scheduler import simulate_accounts

router = APIRouter()
TASK_RESULTS = {}  # 简化：存内存

@router.post("/create")
async def create_task(task: TaskCreate):
    task_id = str(uuid.uuid4())
    results = await simulate_accounts(task.account_list, task.meeting_id)
    TASK_RESULTS[task_id] = results
    return {"task_id": task_id, "summary": results}