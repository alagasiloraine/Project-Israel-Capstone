# from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# from typing import List
# import asyncio
# import serial_asyncio
# import json

# router = APIRouter()

# # Active WebSocket clients
# connections: List[WebSocket] = []

# # Async Serial Reader
# import random

# async def read_serial_forever():
#     while True:
#         # Simulated NPK data
#         data = {
#             "nitrogen": random.randint(0, 100),
#             "phosphorus": random.randint(0, 100),
#             "potassium": random.randint(0, 100)
#         }

#         print("📦 Simulated Arduino Data:", data)

#         for ws in connections.copy():
#             try:
#                 await ws.send_json(data)
#             except Exception as e:
#                 print("⚠️ Failed to send:", e)
#                 connections.remove(ws)

#         await asyncio.sleep(2)  # simulate delay


# # WebSocket route
# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     connections.append(websocket)
#     print("🔌 WebSocket connected")

#     try:
#         while True:
#             await asyncio.sleep(1)  # Keep alive
#     except WebSocketDisconnect:
#         print("❌ WebSocket disconnected")
#     finally:
#         if websocket in connections:
#             connections.remove(websocket)

# # Run serial reader in background
# @router.on_event("startup")
# async def on_startup():
#     asyncio.create_task(read_serial_forever())
