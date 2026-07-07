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
    return {"message": "hello world i am changing the home message from feature branch"}

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