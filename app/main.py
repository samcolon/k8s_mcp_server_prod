from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="K8s MCP Server")

# Serve static schema
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
app.mount("/", StaticFiles(directory=parent_dir), name="static")
