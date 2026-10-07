import os
import psycopg
from flask import Flask

app = Flask(__name__)

@app.get("/health")
def health():
    return "ok"

@app.get("/")
def index():
    # Use the context manager to open the connection and cursor cleanly
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT NOW();")
            now = cur.fetchone()[0] # Safely extract the raw timestamp element
    return f"Hello from ActiveCloud. Database time: {now}"

@app.get("/hog") # used only to test memory limits
def hog():
    data = bytearray(500 * 1024 * 1024)
    return f"allocated {len(data)} bytes"
