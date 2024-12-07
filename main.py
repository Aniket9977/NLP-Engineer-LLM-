from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from utils.extract import extract_content
from utils.query_llm import query_llm

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf", "text/plain"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF or text files are allowed.")
    
    content = await file.read()
    extracted_data = extract_content(file.filename, content)
    return JSONResponse(content={"message": "File processed successfully", "data": extracted_data})

@app.post("/query")
async def query_extracted_content(query: str, file_data: dict):
    response = query_llm(query, file_data)
    return JSONResponse(content={"query": query, "response": response})
