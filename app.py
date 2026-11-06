from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from markitdown import MarkItDown
import os

app = FastAPI()
md = MarkItDown()

class ConvertRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {"status": "MarkItDown MCP Service is running"}

@app.post("/convert")
def convert_file(request: ConvertRequest):
    try:
        result = md.convert(request.url)
        return {"markdown": result.text_content}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
