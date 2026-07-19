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

app = FastAPI()

# Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")

    try:
        while True:
            message = await websocket.receive_text()
            print("Received:", message)

            # Echo the same message back
            await websocket.send_text(message)

    except WebSocketDisconnect:
        print("Client disconnected")

    except Exception as e:
        print("Error:", e)