# services/api/handlers/admin.py
from fastapi import APIRouter, Security
from fastapi_websocket_pubsub import PubSubEndpoint

router = APIRouter()
pubsub = PubSubEndpoint()

@router.websocket("/ws/admin")
async def admin_websocket(websocket: WebSocket):
    await pubsub(websocket)
    
@router.get("/system-metrics")
async def get_metrics(user=Security(admin_required)):
    return {
        "quantum": get_qpu_status(),
        "jobs": get_queue_stats(),
        "users": get_active_users()
    }