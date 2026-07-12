// WebSocket Connection

const status = document.getElementById("status");
const messages = document.getElementById("messages");

// Connect to FastAPI WebSocket
const socket = new WebSocket("ws://127.0.0.1:8000/ws");

// Connection opened
socket.onopen = () => {
    console.log("Connected to WebSocket Server");
    status.innerText = "Connected";
    status.style.color = "green";

    // Send a test message
    socket.send("Hello from Client!");
};

// Message received
socket.onmessage = (event) => {
    console.log("Server:", event.data);

    const message = document.createElement("p");
    message.textContent = event.data;

    messages.appendChild(message);
};

// Connection closed
socket.onclose = () => {
    console.log("Connection Closed");
    status.innerText = "Disconnected";
    status.style.color = "red";
};

// Error
socket.onerror = (error) => {
    console.log("WebSocket Error:", error);
};