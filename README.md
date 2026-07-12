# Photon - Real-Time WebSocket Stock Ticker

## Project Overview

Photon is a real-time stock ticker web application built using **FastAPI** and **WebSockets**. It allows users to view live stock price updates without refreshing the webpage. The backend broadcasts stock data to all connected clients through WebSockets, while the frontend updates the interface instantly.

---

## Week 1 Objectives

* Set up the FastAPI project.
* Create the basic project structure.
* Configure static files and HTML templates.
* Create the frontend page.
* Prepare the project for WebSocket integration.
* Establish the foundation for real-time communication.

---

## Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn
* Jinja2
* WebSockets (Week 2 implementation)

### Frontend

* HTML5
* CSS3
* JavaScript

### Version Control

* Git
* GitHub

---

## Project Structure

```text
stock-ticker/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── venv/
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Govind-Mittal-hub/stock-ticker.git
```

### 2. Navigate to the Project

```bash
cd stock-ticker
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

The application will be available at:

* Home Page: http://127.0.0.1:8000
* API Documentation: http://127.0.0.1:8000/docs

---

## Features Completed in Week 1

* FastAPI project initialized.
* Virtual environment configured.
* Project directory structure created.
* HTML template added.
* CSS styling added.
* JavaScript file added.
* Static files configured.
* Template rendering configured.
* Backend ready for WebSocket integration.
* GitHub repository initialized with version control.

---

## Upcoming Features

### Week 2

* Implement WebSocket endpoint (`/ws`).
* Enable client-server communication.
* Echo messages between client and server.

### Week 3

* Simulate live stock price updates.
* Broadcast stock prices to multiple connected clients.

### Week 4

* Improve user interface.
* Display stock cards with live price changes.
* Final testing, bug fixes, and deployment.

---

## Team Members

* Member 1 – Backend Setup (FastAPI Project Structure)
* Member 2 – WebSocket Server Development
* Member 3 – Frontend Development (HTML & CSS)
* Member 4 – Frontend JavaScript & WebSocket Integration

---

## Future Scope

* Integration with real-time stock market APIs.
* User authentication.
* Personalized watchlists.
* Interactive stock charts.
* Responsive mobile interface.
* Deployment to a cloud platform.

---

## License

This project is developed for academic purposes as part of a collaborative software development project.
