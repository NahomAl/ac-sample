import os
import psycopg
from flask import Flask

app = Flask(__name__)

@app.get("/health")
def health():
    return "ok"

@app.get("/")
def index():
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT NOW();")
            now = cur.fetchone()[0]
    return f"Hello from ActiveCloud. Database time: {now}"

@app.get("/hog") # Force a massive allocation that ignores cgroup slack
def hog():
    data = bytearray(600 * 1024 * 1024)
    return f"allocated {len(data)} bytes"
