# Tech Radar Backend

Tech Radar Backend is an application designed to manage a technology radar. It is developed in Python using FastAPI and is packaged into a Docker container for easy deployment and scaling.

## Requirements

To run this application, you need to have Docker installed and running on your machine.

## Installation and Setup

Follow these steps to get the application up and running:

### 1. Clone the Repository

```bash
git clone https://github.com/your-repository/tech_radar_backend.git
cd tech_radar_backend
```

### 2. Build the Docker Image

```bash
docker build -t tech_radar .
```

### 3. Run the Docker Container

```bash
docker run -d -p 8000:8000 tech_radar
```

### 4. Access the Application

Navigate to:

```
http://localhost:8000
```

### 5. View API Documentation

FastAPI provides interactive API documentation. Once the application is running, view the documentation at:

```
http://localhost:8000/docs
```