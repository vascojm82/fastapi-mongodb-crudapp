from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.student import student_router

client_apps = [
    'http://localhost:5173',  # Our React app (Vite) will be running on this IP and port
    'http://127.0.0.1:5173',
]
app = FastAPI()
app.include_router(student_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=client_apps,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
