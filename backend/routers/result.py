# backend/routers/result.py
from fastapi import APIRouter
from backend.models.models import TaskResult
from backend.routers.task import TASK_RESULTS

router = APIRouter()

@router.get("/{task_id}")
def get_result(task_id: str):
    if task_id not in TASK_RESULTS:
        return {"error": "task not found"}
    return {"task_id": task_id, "results": TASK_RESULTS[task_id]}
