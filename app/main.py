from fastapi import FastAPI
import redis

app = FastAPI()
r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

@app.get("/")
def home():
    return {"message": "hello world welcome to fastapi cicd pipeline hello"}

@app.get("/health")
def health():
    try:
        r.ping()
        return {
            "status": "healthy",
            "redis": "connected and everything is working fine"
        }
    except Exception :
        return {
            "status": "unhealthy",
            "redis": "disconnected"
        }