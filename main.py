from config.app import app
from config.config import Config

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=int(Config.APP_PORTS), reload=True)
