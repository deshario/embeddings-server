from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone

from FlagEmbedding import BGEM3FlagModel

import uvicorn

app = FastAPI(
  title="Embeddings service",
)

model = BGEM3FlagModel('BAAI/bge-m3',  use_fp16=True) # Setting use_fp16 to True speeds up computation with a slight performance degradation

@app.get("/")
def root():
    return datetime.now(timezone.utc).isoformat()

@app.get("/convert-to-vector")
def convert_to_vector(text: str):
    if len(text) > 30:
        raise HTTPException(status_code=400, detail="Text length exceeds 30 characters")

    # Encode the input text to a vector (dense representation)
    output = model.encode([text], return_dense=True) # return_sparse=False, return_colbert_vecs=False

    # Safely get the dense_vecs from the output dictionary
    dense_vecs = output.get('dense_vecs')[0]

    if dense_vecs is None:
        raise HTTPException(status_code=500, detail="Encoding failed")

    return {
        "text": text,
        "vector": dense_vecs.tolist()
    }

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
