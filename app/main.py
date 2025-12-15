from fastapi import FastAPI
from pydantic import BaseModel
from summarizer import summarize_text

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(data: TextInput):
    summary = summarize_text(data.text)
    return {"summary": summary}

