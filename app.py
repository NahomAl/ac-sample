import os
import psycopg
from flask import Flask

app = Flask(__name__)

@app.get("/health")
def health():
    return "ok"

@app.get("/")
def index():
    # Properly indented block using 4 spaces
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        now = conn.execute("select now()").fetchone()[0]
    return f"Hello from ActiveCloud. Database time: {now}"

@app.get("/hog") # used only to test memory limits
def hog():
    data = bytearray(500 * 1024 * 1024)
    return f"allocated {len(data)} bytes"
