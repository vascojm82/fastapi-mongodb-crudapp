from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.student import student_router

client_apps= ['http://localhost:3000']  # Our React app will be running on this IP and port
app = FastAPI()
app.include_router(student_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[client_apps],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
