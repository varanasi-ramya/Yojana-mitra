from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.main import app as fastapi_app

# Create a wrapper app that Vercel can use
app = fastapi_app

# Make sure CORS is enabled
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)