// WebSocket Connection

const status = document.getElementById("status");
const messages = document.getElementById("messages");

// Connect to FastAPI WebSocket
const socket = new WebSocket("ws://127.0.0.1:8000/ws");

// Connection opened
socket.onopen = () => {
    console.log("Connected to WebSocket Server");
    status.innerText = "🟢 Connected";
    status.style.color = "green";

    // Send a test message
    socket.send("Hello from Client!");
};

// Message received
socket.onmessage = (event) => {
    console.log("Server:", event.data);

    const message = document.createElement("p");

const time = new Date().toLocaleTimeString();

message.textContent = `[${time}] ${event.data}`;

messages.appendChild(message);

    messages.scrollTop = messages.scrollHeight;
};

// Connection closed
socket.onclose = () => {
    console.log("Connection Closed");
    status.innerText = "🔴 Disconnected";
    status.style.color = "red";
};

// Error
socket.onerror = (error) => {
    console.log("WebSocket Error:", error);
};
// Send message when user presses Enter
document.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        const text = prompt("Enter a message:");

        if (text) {
            socket.send(text);
            console.log("Sent:", text);
        }
    }
});