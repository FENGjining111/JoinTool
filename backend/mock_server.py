# backend/mock_server.py
from fastapi import FastAPI, Header, HTTPException
import time, random

app = FastAPI(title="Mock Meeting API")

@app.post("/api/login")
def login(payload: dict):
    user = payload.get("user")
    if not user:
        raise HTTPException(status_code=400, detail="Missing user")
    return {"token": f"token-{user}"}

@app.post("/api/meetings/{mid}/join")
def join(mid: str, payload: dict, authorization: str = Header(...)):
    if not authorization.startswith("Bearer"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    if random.random() < 0.95:
        time.sleep(random.uniform(0.1, 0.4))
        return {"status": "ok", "join_url": f"https://mock.meeting/{mid}/{payload.get('account_id')}"}
    else:
        raise HTTPException(status_code=500, detail="Mock failure")
