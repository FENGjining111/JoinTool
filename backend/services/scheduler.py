# backend/services/scheduler.py
import httpx
import asyncio
import random

API = "http://127.0.0.1:8001/api"  # mock_server 服务地址

async def simulate_account(account: str, meeting_id: str):
    async with httpx.AsyncClient() as client:
        try:
            login = await client.post(f"{API}/login", json={"user": account, "pass": "123456"})
            token = login.json().get("token")
            headers = {"Authorization": f"Bearer {token}"}
            join = await client.post(f"{API}/meetings/{meeting_id}/join", headers=headers, json={"account_id": account})
            return {"account": account, "status": join.status_code, "join_url": join.json().get("join_url", None)}
        except Exception as e:
            return {"account": account, "status": 500, "error": str(e)}

async def simulate_accounts(accounts: list[str], meeting_id: str):
    tasks = [simulate_account(a, meeting_id) for a in accounts]
    results = await asyncio.gather(*tasks)
    success = sum(1 for r in results if r.get("status") == 200)
    failed = len(results) - success
    return {"success": success, "failed": failed, "detail": results}