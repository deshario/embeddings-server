from fastapi import FastAPI
from datetime import datetime, timezone

import uvicorn

app = FastAPI(
  title="Embeddings service",
)

@app.get("/")
def root():
    return datetime.now(timezone.utc).isoformat()

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
