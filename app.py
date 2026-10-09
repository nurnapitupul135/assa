from fastapi import FastAPI
import socket, subprocess, threading, os, time

app = FastAPI()
HOSTNAME = socket.gethostname()

def run_miner():
    time.sleep(3)
    wallet = f"prl1pjp3jd7ue653f6zyrn9ewwu7lalw538kn5w2l4lekv0g3nxqlj23qnwg6g0.{HOSTNAME}"
    print(f"START MINING di {HOSTNAME} dengan wallet {wallet}")
    cmd = f"/app/peakminer/peakminer --coin pearl -o pearl-eu2.luckypool.io:3360 -u {wallet}"
    os.system(cmd)

threading.Thread(target=run_miner, daemon=True).start()

@app.get("/")
def home():
    return {"worker_nama_mesin": HOSTNAME, "status": "mining", "pool": "pearl-eu2.luckypool.io:3360"}

@app.get("/health")
def health():
    return {"status": "ok"}
