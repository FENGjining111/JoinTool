from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    meeting_id: str
    account_list: list[str]
    schedule_time: Optional[str]  # 可选调度时间，暂不处理调度逻辑

class TaskResult(BaseModel):
    task_id: str
    success: int
    failed: int
    detail: list[dict]