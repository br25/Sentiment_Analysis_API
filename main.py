from fastapi import FastAPI, HTTPException
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.exceptions import HTTPException as MethodNotAllowedException
from starlette.responses import JSONResponse
from pydantic import BaseModel

# Connect FastAPI
app = FastAPI()

# Exception handler for StarletteHTTPException
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Go there: http://127.0.0.1:8000/docs#/"}
    )

# Exception handler for MethodNotAllowedException
@app.exception_handler(MethodNotAllowedException)
async def method_not_allowed_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Method Not Allowed"}
    )

# Exception handler for generic Exception
@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"}
    )

# Request body model
class AnalysisRequest(BaseModel):
    text: str

# Response model
class AnalysisResponse(BaseModel):
    sentiment: str

# Endpoint for sentiment analysis
@app.post("/analyze")
def analyze_sentiment(request: AnalysisRequest):
    # Input text
    text = request.text

    # If Not Text raise Error
    if not text:
        raise HTTPException(status_code=400, detail="Invalid request: Text is missing")


    # Prepare the response
    response = AnalysisResponse(sentiment="positive")
    return response

# Run the application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)