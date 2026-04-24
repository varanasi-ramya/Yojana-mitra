from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.main import app

# Export for Vercel
handler = app