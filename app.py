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
            now = cur.fetchone()
    return f"Hello from ActiveCloud. Database time: {now}"

@app.get("/hog") 
def hog():
    # Force an aggressive memory leak loop that pierces cgroups v2 instantly
    leak = []
    while True:
        # Continuously dump massive data frames until the kernel triggers OOM
        leak.append(bytearray(50 * 1024 * 1024)) 
    return f"allocated {len(leak)} chunks"
