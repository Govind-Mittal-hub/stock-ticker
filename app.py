"""
Photon - Real-Time WebSocket Stock Ticker

Week 1:
- FastAPI project setup
- Static files configuration
- HTML template configuration

"""
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio
from data_streamer import get_stock_data

app = FastAPI()
connected_clients = []

# Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
   return templates.TemplateResponse(
    request=request,
    name="index.html"
)
async def broadcast_stock_updates():
    while True:
        stock_data = get_stock_data()

        for client in connected_clients.copy():
            try:
                await client.send_json(stock_data)
            except:
                connected_clients.remove(client)

        await asyncio.sleep(1)
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    connected_clients.append(websocket)

    print(f"Clients connected: {len(connected_clients)}")

    # Start broadcaster when first client connects
    if len(connected_clients) == 1:
        asyncio.create_task(broadcast_stock_updates())

    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()

    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print(f"Client disconnected. Clients left: {len(connected_clients)}")

    except Exception as e:
        print("Error:", e)